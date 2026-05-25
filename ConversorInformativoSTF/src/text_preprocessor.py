import re


def clean_text(text: str) -> str:
    """
    Limpeza básica do texto/markdown.
    Remove artefatos do DOCX, normaliza espaços.
    NÃO tenta extrair julgados aqui.

    Args:
        text: markdown bruto do DOCX

    Returns:
        Texto limpo
    """
    # Remove anchors HTML
    text = re.sub(r"<a[^>]*></a>", "", text)

    # Remove imagens base64
    text = re.sub(r"!\[\]\(data:image[^)]*\)", "", text)

    # Remove barras de escape
    text = text.replace("\\.", ".")
    text = text.replace("\\-", "-")
    text = text.replace("\\(", "(")
    text = text.replace("\\)", ")")

    # Normaliza múltiplas quebras de linha (máximo 2)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove espaços em branco extras no final/início
    text = text.strip()

    return text


def extract_metadata(text: str) -> dict:
    """
    Extrai metadados básicos do informativo.

    Args:
        text: conteúdo do informativo

    Returns:
        Dict com número, ano e data de publicação
    """
    metadata = {
        "numero_informativo": None,
        "ano_informativo": None,
        "data_publicacao": None
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
