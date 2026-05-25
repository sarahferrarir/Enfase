import uuid
from datetime import datetime, timezone
from typing import Optional


def generate_id() -> str:
    """Gera UUID para julgado."""
    return str(uuid.uuid4())


def generate_timestamp() -> str:
    """Gera timestamp ISO 8601 em UTC."""
    now = datetime.now(timezone.utc)
    return now.isoformat(timespec='milliseconds').replace('+00:00', 'Z')


def wrap_html(text: Optional[str]) -> Optional[str]:
    """
    Envolve texto em tags <p> se não tiver HTML.

    Args:
        text: texto plano ou HTML

    Returns:
        Texto envolvido em <p> tags ou None
    """
    if not text:
        return None

    text = str(text).strip()

    if not text:
        return None

    if text.startswith("<"):
        return text

    # Divide por parágrafo e envolve cada um
    paragraphs = text.split("\n\n")
    wrapped = "".join(
        f"<p>{p.strip()}</p>"
        for p in paragraphs
        if p.strip()
    )

    return wrapped if wrapped else None


def format_ods(ods_str: Optional[str]) -> Optional[str]:
    """
    Formata string de ODS em formato padrão.
    Entrada: "1;2;3" ou "[1][2]" ou "1, 2, 3"
    Saída: "1, 2, 3"

    Args:
        ods_str: string com ODS

    Returns:
        Formato normalizado ou None
    """
    if not ods_str:
        return None

    # Remove caracteres não-numéricos exceto separadores
    import re
    numeros_str = re.sub(r"[^\d,;]", ",", str(ods_str))

    # Extrai números
    numeros = set()
    for num in re.findall(r"\d+", numeros_str):
        try:
            n = int(num)
            if 1 <= n <= 17:  # ODS vão de 1 a 17
                numeros.add(n)
        except ValueError:
            pass

    if not numeros:
        return None

    # Retorna formatado
    return ", ".join(str(n) for n in sorted(numeros))
