from __future__ import annotations

import re

from .schemas import EditorialItem, Paragraph
from .utils import normalize_heading


def is_summary_marker(text: str) -> bool:
    return normalize_heading(text) == "SUMARIO"


def is_legal_area_line(text: str) -> bool:
    heading = normalize_heading(text)
    if not heading.startswith("DIREITO "):
        return False
    if len(heading) < 12:
        return False
    return bool(re.search(r"\s[-–—]\s| - |;|:", text)) or heading.count("DIREITO ") >= 1


def _looks_like_valid_item(paragraphs: list[Paragraph]) -> bool:
    if not paragraphs:
        return False
    text = "\n".join(p.text for p in paragraphs)
    return "Resumo:" in text and bool(re.search(r"\b(ADI|ADPF|ADO|ADC|RE|ARE|HC|MS|MI|Rcl|RCL|ACO)\b", text))


def split_editorial_items(plenario_paragraphs: list[Paragraph]) -> list[EditorialItem]:
    """Separa itens editoriais reais do Plenario sem chunking por tamanho."""

    items: list[EditorialItem] = []
    current: list[Paragraph] = []

    for paragraph in plenario_paragraphs:
        text = paragraph.text.strip()
        if not text:
            continue

        if is_summary_marker(text):
            if _looks_like_valid_item(current):
                items.append(EditorialItem(paragraphs=current))
            current = []
            continue

        if is_legal_area_line(text) and current and _looks_like_valid_item(current):
            items.append(EditorialItem(paragraphs=current))
            current = [paragraph]
            continue

        if is_legal_area_line(text) and not current:
            current = [paragraph]
            continue

        if current:
            current.append(paragraph)

    if _looks_like_valid_item(current):
        items.append(EditorialItem(paragraphs=current))

    return items

