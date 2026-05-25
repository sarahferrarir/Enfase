import re


def extract_metadata(text: str) -> dict:
    metadata = {
        "numero_informativo": "",
        "ano_informativo": "",
        "data_publicacao": ""
    }

    numero_match = re.search(r"n[ºo]\s*(\d+)/(\d{4})", text, re.IGNORECASE)
    if numero_match:
        metadata["numero_informativo"] = numero_match.group(1)
        metadata["ano_informativo"] = numero_match.group(2)

    data_match = re.search(
        r"(\d{1,2}\s+de\s+\w+\s+de\s+\d{4})",
        text,
        re.IGNORECASE
    )
    if data_match:
        metadata["data_publicacao"] = data_match.group(1)

    return metadata


def _normalize_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^[#>\-\s_*\[\]\(\)]+", "", line)
    line = line.replace("__", "")
    line = line.replace("**", "")
    line = line.replace("*", "")
    return line.strip()


def _is_header_line(line: str) -> bool:
    normalized = _normalize_line(line)
    return normalized.upper().startswith("DIREITO ")


def split_julgados(text: str) -> list[str]:
    inicio_plenario = re.search(r"1\s+PLENÁRIO|__1\s+PLENÁRIO__", text, re.IGNORECASE)

    if inicio_plenario:
        text = text[inicio_plenario.end():]
        
    lines = text.splitlines()
    blocks = []
    current_block = []

    for line in lines:
        if _is_header_line(line):
            if current_block:
                block_text = "\n".join(current_block).strip()
                if _is_valid_julgado_block(block_text):
                    blocks.append(block_text)

            current_block = [line]

        elif current_block:
            current_block.append(line)

    if current_block:
        block_text = "\n".join(current_block).strip()
        if _is_valid_julgado_block(block_text):
            blocks.append(block_text)

    return blocks


def _is_valid_julgado_block(block: str) -> bool:
    if not block or len(block) < 100:
        return False

    if "Resumo:" not in block:
        return False

    processo_pattern = r"\b(ADI|ADPF|ADO|ADC|RE|ARE|HC|MS|Rcl|RCL|ACO)\s*[\d\.\-]+"
    if not re.search(processo_pattern, block):
        return False

    invalid_sections = [
        "__SUMÁRIO__",
        "SUMÁRIO",
        "INOVAÇÕES NORMATIVAS",
        "CALENDÁRIO",
        "EDIÇÕES ANTERIORES"
    ]

    first_part = block[:500].upper()
    if any(section in first_part for section in invalid_sections):
        return False

    return True