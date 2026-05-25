import re
from models import Julgado


def extract_julgado_data(bloco: str) -> Julgado:
    julgado = Julgado()

    julgado.noticia_completa = bloco.strip()

    classe_processo, numero_processo, uf = _extract_processo(bloco)
    julgado.classe_processo = classe_processo
    julgado.numero_processo = numero_processo
    julgado.uf = uf

    julgado.ramo_direito = _extract_ramo_direito(bloco)

    julgado.materia = _extract_materia(bloco)

    julgado.titulo = _extract_titulo(bloco)

    resumo_text = _extract_resumo(bloco)
    julgado.resumo = _wrap_html(resumo_text) if resumo_text else None

    ods_raw = _extract_ods(bloco)
    julgado.ods_onu2030 = _format_ods(ods_raw) if ods_raw else None

    julgado.legislacao = _extract_legislacao(bloco)

    julgado.noticia = _extract_noticia(bloco)

    julgado.type = "STF"
    julgado.status = "APROVADO"
    julgado.is_extraordinary = False
    julgado.grau_incidencia = "PENDENTE"
    julgado.metadata = {}
    julgado.comments = {}
    julgado.new_classificacao = "{}"
    julgado.modified_by_users = []

    return julgado


def _extract_processo(bloco: str) -> tuple:
    pattern = r"\b(ADI|ADPF|ADO|ADC|RE|ARE|HC|MS|Rcl|ACO)\s+(\d+\.?\d*(?:\s*AgR)?)\s*/\s*([A-Z]{2})"

    match = re.search(pattern, bloco)
    if match:
        classe = match.group(1)
        numero = f"{match.group(2)}/{match.group(3)}"
        uf = match.group(3)
        return classe, numero, uf

    return None, None, None


def _extract_ramo_direito(bloco: str) -> str:
    primeira_linha = bloco.split("\n")[0].strip()

    if primeira_linha.startswith("DIREITO "):
        ramo = primeira_linha.replace("DIREITO ", "").strip()
        ramo = ramo.split("–")[0].strip()
        if ramo:
            return f"DIREITO {ramo}"

    return None


def _extract_materia(bloco: str) -> str:
    primeira_linha = bloco.split("\n")[0].strip()

    if "–" in primeira_linha:
        partes = primeira_linha.split("–")
        if len(partes) > 1:
            materias = [p.strip() for p in partes[1:]]
            materia_str = ";".join(materias)
            if materia_str:
                return materia_str

    return None


def _extract_titulo(bloco: str) -> str:
    padroes = [
        r"__\*([^*]+)\*__",
        r"\*\*([^*]+)\*\*",
        r"__(.*?)__",
        r"\*\*(.*?)\*\*"
    ]

    for padrao in padroes:
        match = re.search(padrao, bloco)
        if match:
            titulo = match.group(1).strip()
            if titulo and len(titulo) > 5:
                return titulo

    linhas = bloco.split("\n")
    for i, linha in enumerate(linhas):
        linha_stripped = linha.strip()
        if (i > 0 and
            linha_stripped and
            not linha_stripped.startswith("DIREITO") and
            not linha_stripped.startswith("ADI") and
            not linha_stripped.startswith("ADPF") and
            not linha_stripped.startswith("RE ") and
            len(linha_stripped) > 10 and
            len(linha_stripped) < 300 and
            "Resumo:" not in linha_stripped):
            return linha_stripped

    return None


def _extract_resumo(bloco: str) -> str:
    padrao = r"Resumo:\s*(.*?)(?=\n\n|\n(?:Conforme|Com base|Precedentes|Sumário|ADI|ADPF|RE |$))"

    match = re.search(padrao, bloco, re.DOTALL | re.IGNORECASE)
    if match:
        resumo_raw = match.group(1).strip()
        resumo_clean = re.sub(r"__\*|\*__|\*\*|__", "", resumo_raw)
        resumo_clean = re.sub(r"\s+", " ", resumo_clean).strip()

        if resumo_clean:
            return resumo_clean

    return None


def _extract_ods(bloco: str) -> str:
    padroes = [
        r"__ODS:?__\s*([\d\,;]+)",
        r"ODS:\s*(\[[0-9]+\][,\s]*)+",
        r"ODS:\s*([\d,;]+)",
        r"\[([0-9]+)\]\s*e\s*\[([0-9]+)\]",
        r"ODS\s+([0-9]+)"
    ]

    encontrados = set()

    # Extração específica de links markdown
    link_pattern = r"\[([0-9]+)\]"
    link_matches = re.findall(link_pattern, bloco)
    encontrados.update(link_matches)

    # Extração por padrões adicionais
    for padrao in padroes:
        matches = re.findall(padrao, bloco, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                for item in match:
                    if item.isdigit():
                        encontrados.add(item)
            else:
                numeros = re.findall(r"\d+", str(match))
                encontrados.update(numeros)

    if encontrados:
        return ";".join(sorted(encontrados))

    return None


def _extract_legislacao(bloco: str) -> str:
    padroes = [
        r"(?:Lei|Decreto|Emenda|CF|Constituição|Código|Súmula|Resolução)\s+(?:n[oº]\.?\s*)?([^\n,;]+?)(?=[,;.\n])",
        r"(?:Art|artigo)\s+(\d+(?:\s*,\s*\d+)*)",
        r"(?:Lei|Lei Complementar|Lei Federal)\s+([^\n,;]+?)(?=[,;.\n])",
    ]

    encontradas = []

    for padrao in padroes:
        matches = re.findall(padrao, bloco, re.IGNORECASE)
        encontradas.extend([m.strip() for m in matches if m.strip()])

    encontradas = list(dict.fromkeys(encontradas))
    encontradas = [l for l in encontradas if len(l) > 2 and len(l) < 200]

    if encontradas:
        return ";".join(encontradas[:10])

    return None


def _wrap_html(text: str) -> str:
    if not text:
        return None
    if text.startswith("<"):
        return text
    paragraphs = text.split("\n\n")
    wrapped = "".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())
    return wrapped


def _format_ods(ods_str: str) -> str:
    if not ods_str:
        return None
    numeros = [n.strip() for n in ods_str.replace(";", ",").split(",") if n.strip()]
    numeros = sorted(set(numeros), key=int)
    return ", ".join(numeros)


def _extract_noticia(bloco: str) -> str:
    resumo_text = _extract_resumo(bloco)
    if resumo_text:
        return _wrap_html(resumo_text)
    return None

