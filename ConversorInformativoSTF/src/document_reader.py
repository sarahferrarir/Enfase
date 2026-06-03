from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from .schemas import Paragraph


NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W_VAL = f"{{{NS['w']}}}val"


def read_docx_paragraphs(docx_path: str | Path) -> list[Paragraph]:
    """Le um DOCX como sequencia de paragrafos textuais."""

    path = Path(docx_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    if path.suffix.lower() != ".docx":
        raise ValueError(f"Arquivo deve ser DOCX, recebido: {path.suffix}")

    with ZipFile(path) as docx:
        document_xml = docx.read("word/document.xml")

    root = ET.fromstring(document_xml)
    paragraphs: list[Paragraph] = []

    for raw_index, para in enumerate(root.findall(".//w:p", NS)):
        text = "".join(node.text or "" for node in para.findall(".//w:t", NS)).strip()
        if not text:
            continue

        style_node = para.find("./w:pPr/w:pStyle", NS)
        style = style_node.attrib.get(W_VAL) if style_node is not None else None
        paragraphs.append(Paragraph(index=raw_index, text=text, style=style))

    return paragraphs

