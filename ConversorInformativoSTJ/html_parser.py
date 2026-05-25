from pathlib import Path
from bs4 import BeautifulSoup
import re

def read_html_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

    encodings = ["utf-8", "latin-1", "iso-8859-1", "windows-1252"]
    for encoding in encodings:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError(
        "Não foi possível ler o arquivo com as codificações testadas."
    )

def validate_html_structure(soup: BeautifulSoup) -> bool:
    """Valida se HTML contém pelo menos uma div.clsInformativoBlocoItem."""
    items = soup.find_all('div', class_='clsInformativoBlocoItem')
    if not items:
        raise ValueError(
            "HTML inválido: nenhuma div com classe 'clsInformativoBlocoItem' encontrada. "
            "Verifique se o arquivo é um Informativo de Jurisprudência do STJ válido."
        )
    return True

def extract_informativo_metadata(soup: BeautifulSoup) -> dict:
    """Extrai número e data de publicação do primeiro clsInformativoBlocoItem."""
    first_item = soup.find('div', class_='clsInformativoBlocoItem')
    if not first_item:
        return {"numero_informativo": None, "data_publicacao": None}

    titulo = first_item.find('span', class_='clsInformativoTitulo')
    if not titulo:
        return {"numero_informativo": None, "data_publicacao": None}

    text = titulo.get_text(" ", strip=True)

    numero = None
    data = None

    numero_match = re.search(
        r'(?:nº|n°|n\.|numero|número)\s*(\d{1,4})(?=\s|$)',
        text,
        re.IGNORECASE
    )
    if numero_match:
        numero = numero_match.group(1)

    data_match = re.search(
        r'(\d{1,2}\s+de\s+[a-zçãéíóúâêô]+\s+de\s+\d{4})',
        text,
        re.IGNORECASE
    )
    if data_match:
        data = data_match.group(1)

    return {
        "numero_informativo": numero,
        "data_publicacao": data
    }

def extract_julgados_html(soup: BeautifulSoup) -> list[str]:
    """Extrai blocos HTML individuais de julgados, ignorando o primeiro (cabeçalho)."""
    items = soup.find_all('div', class_='clsInformativoBlocoItem')
    return [str(item) for item in items[1:]]

def clean_html_block(html_block: str) -> str:
    """Extrai o texto de um bloco HTML de julgado preservando o conteúdo o máximo possível."""
    soup = BeautifulSoup(html_block, 'html.parser')

    for tag in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    # Remove apenas linhas completamente vazias, sem alterar espaços internos do texto.
    lines = text.splitlines()
    lines = [line for line in lines if line.strip()]

    return "\n".join(lines)