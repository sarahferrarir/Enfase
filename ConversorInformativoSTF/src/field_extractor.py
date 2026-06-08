from __future__ import annotations

import re

from .editorial_item_splitter import is_legal_area_line
from .html_formatter import paragraph_to_html, paragraphs_to_html, paragraphs_to_list_html
from .schemas import EditorialItem, InformativoMetadata, JulgadoSTF, Paragraph
from .utils import generate_id, generate_timestamp, normalize_spaces, parse_numeric_date, unique_or_join


PROCESS_CLASSES = r"ADI|ADPF|ADO|ADC|RE|ARE|HC|MS|Rcl|RCL|ACO|RMS|PET|SL"
PROCESS_RE = re.compile(
    rf"\b(?P<class>{PROCESS_CLASSES})\s+"
    r"(?P<number>\d[\d.]*(?:\s+[A-Za-z][A-Za-z.-]*)?)"
    r"(?:/(?P<uf>[A-Z]{2}))?",
    flags=re.IGNORECASE,
)
MAIN_TITLE_THEME_RG_RE = re.compile(
    r"\(\s*Tema\s+(?P<theme>\d+\s*RG)\s*\)",
    flags=re.IGNORECASE,
)


def _split_area_line(text: str) -> tuple[str, str | None]:
    parts = re.split(r"\s+[–—-]\s+", text, maxsplit=1)
    ramo = normalize_spaces(parts[0]).upper()
    materia = normalize_spaces(parts[1]).upper() if len(parts) > 1 else None
    return ramo, materia


def _extract_area(paragraphs: list[Paragraph]) -> tuple[str | None, str | None, int]:
    ramos: list[str] = []
    materias: list[str] = []
    consumed = 0

    for paragraph in paragraphs:
        if not is_legal_area_line(paragraph.text):
            break
        ramo, materia = _split_area_line(paragraph.text)
        ramos.append(ramo)
        if materia:
            materias.append(materia)
        consumed += 1

    return unique_or_join(ramos, "; "), " | ".join(materias) if materias else None, consumed


def _split_title_and_processes(text: str) -> tuple[str, str]:
    matches = list(re.finditer(r"\s+[–—-]\s+", text))
    for match in reversed(matches):
        suffix = text[match.end():]
        if PROCESS_RE.search(suffix):
            return normalize_spaces(text[: match.start()]), normalize_spaces(suffix)
    return normalize_spaces(text), ""


def _clean_title(text: str) -> str:
    text = MAIN_TITLE_THEME_RG_RE.sub("", text)
    return normalize_spaces(text).strip(" -–—")


def _extract_main_theme_rg(process_text: str) -> tuple[str | None, str | None]:
    """Extrai Tema RG somente do trecho do processo principal no titulo."""

    match = MAIN_TITLE_THEME_RG_RE.search(process_text)
    if not match:
        return None, None

    theme = normalize_spaces(match.group("theme")).upper()
    return theme, "sim"


def _normalize_process_number(number: str) -> str:
    number = normalize_spaces(number)
    parts = number.split(" ", 1)
    base = parts[0].replace(".", "")
    if len(parts) == 1:
        return base
    return f"{base} {parts[1]}"


def _extract_processes(text: str) -> tuple[str | None, str | None, str | None]:
    classes: list[str] = []
    numbers: list[str] = []
    ufs: list[str] = []

    for match in PROCESS_RE.finditer(text):
        cls = match.group("class")
        number = match.group("number")
        uf = match.group("uf")
        classes.append("Rcl" if cls.lower() == "rcl" else cls.upper())
        numbers.append(_normalize_process_number(number))
        if uf:
            ufs.append(uf.upper())

    return (
        ";".join(classes) if classes else None,
        ";".join(numbers) if numbers else None,
        ";".join(ufs) if ufs else None,
    )


def _extract_ods(text: str) -> str | None:
    match = re.search(r"^ODS:\s*(.+)$", text, flags=re.IGNORECASE)
    if not match:
        return None
    numbers = re.findall(r"\d+", match.group(1))
    return ", ".join(numbers) if numbers else None


def _is_process_footer(text: str) -> bool:
    return bool(PROCESS_RE.match(text)) and (
        "relator" in text.lower() or "julgamento" in text.lower()
    )


def _find_footer_start(lines: list[str]) -> int:
    for index, line in enumerate(lines):
        if _is_process_footer(line):
            return index
    return len(lines)


def _footer_paragraphs(paragraphs: list[Paragraph], lines: list[str], footer_start: int) -> list[Paragraph]:
    return [
        paragraphs[index]
        for index in range(footer_start, len(lines))
        if _is_process_footer(lines[index])
    ]


def _extract_person(text: str, marker: str, stop_markers: list[str]) -> str | None:
    lower = text.lower()
    start = lower.find(marker.lower())
    if start < 0:
        return None

    start += len(marker)
    end = len(text)
    for stop in stop_markers:
        stop_index = lower.find(stop.lower(), start)
        if stop_index >= 0:
            end = min(end, stop_index)

    return normalize_spaces(text[start:end].strip(" ,.")) or None


def _extract_footer_fields(footer_lines: list[str]) -> dict[str, str | None]:
    relatores: list[str] = []
    redatores: list[str] = []
    datas: list[str] = []
    situacoes: list[str] = []

    for line in footer_lines:
        relator = _extract_person(
            line,
            "relator",
            ["redator do acórdão", "redatora do acórdão", "julgamento"],
        )
        if relator:
            relatores.append(relator)

        redator = None
        for marker in ["redator do acórdão", "redatora do acórdão"]:
            redator = _extract_person(line, marker, ["julgamento"])
            if redator:
                break
        if redator:
            redatores.append(redator)

        date = parse_numeric_date(line)
        if date:
            datas.append(date)

        situation_match = re.search(r"julgamento\s+(virtual\s+)?([a-zçãéíóúâêô]+)", line, flags=re.IGNORECASE)
        if situation_match:
            situacoes.append(normalize_spaces(situation_match.group(2).lower()))

    return {
        "relator": unique_or_join(relatores, "; "),
        "redator_acordao": unique_or_join(redatores, "; "),
        "data_julgamento": unique_or_join(datas, "; "),
        "situacao_julgamento": unique_or_join(situacoes, "; "),
    }


def _extract_tese(lines: list[str]) -> tuple[str | None, set[int]]:
    consumed: set[int] = set()
    for index, line in enumerate(lines):
        if line.lower().startswith("tese fixada"):
            consumed.add(index)
            if index + 1 < len(lines):
                consumed.add(index + 1)
                return lines[index + 1], consumed
            return None, consumed
    return None, consumed


def _extract_resumo_noticia_indexes(lines: list[str], ignored_indexes: set[int], footer_start: int) -> tuple[int | None, list[int]]:
    try:
        resumo_marker_index = next(i for i, line in enumerate(lines) if line.lower().startswith("resumo:"))
    except StopIteration:
        return None, []

    body_indexes = [
        i for i in range(resumo_marker_index + 1, footer_start)
        if i not in ignored_indexes and lines[i].strip()
    ]
    if not body_indexes:
        return None, []

    return body_indexes[0], body_indexes[1:]


def _join_html(*parts: str | None) -> str | None:
    html_parts = [part for part in parts if part]
    return "\n".join(html_parts) if html_parts else None


def _build_textual_html(
    paragraphs: list[Paragraph],
    lines: list[str],
    ignored_indexes: set[int],
    footer_start: int,
) -> tuple[str | None, str | None, str | None]:
    resumo_index, noticia_indexes = _extract_resumo_noticia_indexes(lines, ignored_indexes, footer_start)
    resumo = paragraph_to_html(paragraphs[resumo_index]) if resumo_index is not None else None
    noticia_html = paragraphs_to_html([paragraphs[index] for index in noticia_indexes])
    footer_html = paragraphs_to_list_html(_footer_paragraphs(paragraphs, lines, footer_start))

    noticia = _join_html(noticia_html, footer_html)
    noticia_completa = _join_html(
        paragraphs_to_html(paragraphs[1:footer_start]),
        footer_html,
    )
    return resumo, noticia, noticia_completa


def _extract_legislacao(text: str) -> str | None:
    patterns = [
        r"\bCF/1988\b(?:,\s*art\.?\s*[\wº°., §-]+)?",
        r"\bConstitui[cç][aã]o Federal\b",
        r"\bLei\s+n[ºo]\s*[\d.]+/\d{4}",
        r"\bLei Complementar\s+n[ºo]\s*[\d.]+/\d{4}",
        r"\bDecreto(?:-Lei)?\s+n[ºo]\s*[\d.]+/\d{4}",
        r"\bADCT\b",
        r"\bCPC/2015\b",
        r"\bCDC\b",
    ]
    found: list[str] = []
    for pattern in patterns:
        found.extend(match.group(0) for match in re.finditer(pattern, text, flags=re.IGNORECASE))
    return unique_or_join(found, "; ")


def extract_fields(item: EditorialItem, metadata: InformativoMetadata) -> JulgadoSTF:
    paragraphs = item.paragraphs
    ramo_direito, materia, consumed_area = _extract_area(paragraphs)
    remaining_paragraphs = paragraphs[consumed_area:]
    remaining = [p.text for p in remaining_paragraphs]

    title_line = remaining[0] if remaining else ""
    title, process_text = _split_title_and_processes(title_line)
    title = _clean_title(title)
    classe, numero, uf = _extract_processes(process_text)
    tema_rg, repercussao_geral = _extract_main_theme_rg(process_text)

    footer_start = _find_footer_start(remaining)
    footer_lines = [line for line in remaining[footer_start:] if _is_process_footer(line)]
    footer_fields = _extract_footer_fields(footer_lines)

    if footer_lines and not classe:
        classe, numero, uf = _extract_processes(" ".join(footer_lines))

    ods_values = [_extract_ods(line) for line in remaining]
    ods_onu2030 = next((value for value in ods_values if value), None)

    tese, tese_indexes = _extract_tese(remaining)
    ignored_indexes = set(tese_indexes)
    ignored_indexes.update(i for i, line in enumerate(remaining) if line.lower().startswith("ods:"))

    resumo, noticia, noticia_completa = _build_textual_html(
        remaining_paragraphs,
        remaining,
        ignored_indexes,
        footer_start,
    )

    return JulgadoSTF(
        id=generate_id(),
        created_at=generate_timestamp(),
        informativo=metadata.numero_informativo,
        data_informativo=metadata.data_informativo,
        type=metadata.type,
        classe_processo=classe,
        numero_processo=numero,
        uf=uf,
        titulo=title,
        ramo_direito=ramo_direito,
        materia=materia,
        repercussao_geral=repercussao_geral,
        tema_rg=tema_rg,
        ods_onu2030=ods_onu2030,
        resumo=resumo,
        noticia=noticia,
        noticia_completa=noticia_completa,
        html=noticia_completa,
        tese_julgado=tese,
        legislacao=_extract_legislacao(item.text),
        orgao_julgador="PLENÁRIO",
        relator=footer_fields["relator"],
        redator_acordao=footer_fields["redator_acordao"],
        data_julgamento=footer_fields["data_julgamento"],
        situacao_julgamento=footer_fields["situacao_julgamento"],
    )
