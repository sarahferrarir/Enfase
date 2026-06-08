from __future__ import annotations

from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from .schemas import Paragraph, TextRun


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
W_VAL = f"{{{NS['w']}}}val"
R_ID = f"{{{NS['r']}}}id"


def _read_relationships(docx: ZipFile) -> dict[str, str]:
    try:
        rels_xml = docx.read("word/_rels/document.xml.rels")
    except KeyError:
        return {}

    root = ET.fromstring(rels_xml)
    relationships: dict[str, str] = {}
    for rel in root.findall("rel:Relationship", NS):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rel_id and target:
            relationships[rel_id] = target
    return relationships


def _has_run_flag(run: ET.Element, tag: str) -> bool:
    node = run.find(f"./w:rPr/w:{tag}", NS)
    if node is None:
        return False

    value = node.attrib.get(W_VAL)
    return value is None or value not in {"0", "false", "False"}


def _run_text(run: ET.Element) -> str:
    fragments: list[str] = []
    for child in run:
        if child.tag == f"{{{NS['w']}}}t":
            fragments.append(child.text or "")
        elif child.tag == f"{{{NS['w']}}}tab":
            fragments.append("\t")
        elif child.tag == f"{{{NS['w']}}}br":
            fragments.append("\n")
    return "".join(fragments)


def _extract_runs_from_run(run: ET.Element, href: str | None = None) -> list[TextRun]:
    text = _run_text(run)
    if not text:
        return []

    return [
        TextRun(
            text=text,
            bold=_has_run_flag(run, "b"),
            italic=_has_run_flag(run, "i"),
            underline=_has_run_flag(run, "u"),
            href=href,
        )
    ]


def _extract_runs(node: ET.Element, relationships: dict[str, str], href: str | None = None) -> list[TextRun]:
    runs: list[TextRun] = []

    if node.tag == f"{{{NS['w']}}}r":
        return _extract_runs_from_run(node, href)

    if node.tag == f"{{{NS['w']}}}hyperlink":
        rel_id = node.attrib.get(R_ID)
        href = relationships.get(rel_id) if rel_id else href

    for child in node:
        runs.extend(_extract_runs(child, relationships, href))

    return runs


def _merge_adjacent_runs(runs: list[TextRun]) -> list[TextRun]:
    merged: list[TextRun] = []
    for run in runs:
        if not run.text:
            continue

        if merged:
            previous = merged[-1]
            if (
                previous.bold == run.bold
                and previous.italic == run.italic
                and previous.underline == run.underline
                and previous.href == run.href
            ):
                previous.text += run.text
                continue

        merged.append(run)
    return merged


def read_docx_paragraphs(docx_path: str | Path) -> list[Paragraph]:
    """Le um DOCX como sequencia de paragrafos textuais."""

    path = Path(docx_path)
    if not path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {path}")
    if path.suffix.lower() != ".docx":
        raise ValueError(f"Arquivo deve ser DOCX, recebido: {path.suffix}")

    with ZipFile(path) as docx:
        document_xml = docx.read("word/document.xml")
        relationships = _read_relationships(docx)

    root = ET.fromstring(document_xml)
    paragraphs: list[Paragraph] = []

    for raw_index, para in enumerate(root.findall(".//w:p", NS)):
        runs = _merge_adjacent_runs(_extract_runs(para, relationships))
        text = "".join(run.text for run in runs).strip()
        if not text:
            continue

        style_node = para.find("./w:pPr/w:pStyle", NS)
        style = style_node.attrib.get(W_VAL) if style_node is not None else None
        is_list_item = para.find("./w:pPr/w:numPr", NS) is not None
        paragraphs.append(
            Paragraph(
                index=raw_index,
                text=text,
                style=style,
                runs=runs,
                is_list_item=is_list_item,
            )
        )

    return paragraphs
