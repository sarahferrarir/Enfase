from __future__ import annotations

from .schemas import Paragraph
from .utils import normalize_heading


def _is_plenario_heading(text: str) -> bool:
    return normalize_heading(text).replace(" ", "") == "1PLENARIO"


def _is_turmas_heading(text: str) -> bool:
    return normalize_heading(text).replace(" ", "") == "2TURMAS"


def extract_plenario_section(paragraphs: list[Paragraph]) -> list[Paragraph]:
    """Retorna somente os paragrafos do conteudo real de 1 PLENARIO."""

    plenario_indexes = [i for i, paragraph in enumerate(paragraphs) if _is_plenario_heading(paragraph.text)]
    if not plenario_indexes:
        return []

    # O primeiro 1 Plenario costuma pertencer ao sumario inicial.
    start_index = plenario_indexes[1] if len(plenario_indexes) > 1 else plenario_indexes[0]
    start_index += 1

    end_index = len(paragraphs)
    for i in range(start_index, len(paragraphs)):
        if _is_turmas_heading(paragraphs[i].text):
            end_index = i
            break

    return paragraphs[start_index:end_index]

