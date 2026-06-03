import mammoth
from pathlib import Path


def read_docx(docx_path: str) -> str:
    """
    Lê arquivo DOCX e converte para markdown/texto.

    Args:
        docx_path: caminho do arquivo DOCX

    Returns:
        Conteúdo do DOCX em formato markdown

    Raises:
        FileNotFoundError: se arquivo não existir
        ValueError: se arquivo não for DOCX válido
    """
    path = Path(docx_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {docx_path}")

    if path.suffix.lower() != ".docx":
        raise ValueError(f"Arquivo deve ser DOCX, recebido: {path.suffix}")

    try:
        with open(path, "rb") as f:
            result = mammoth.convert_to_markdown(f)
            markdown = result.value
            return markdown
    except Exception as e:
        raise ValueError(f"Erro ao ler DOCX: {str(e)}")
