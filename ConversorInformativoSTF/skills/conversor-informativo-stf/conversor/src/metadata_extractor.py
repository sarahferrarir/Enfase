from __future__ import annotations

import re

from .schemas import InformativoMetadata, Paragraph
from .utils import parse_pt_date


def extract_metadata(paragraphs: list[Paragraph]) -> InformativoMetadata:
    text = "\n".join(p.text for p in paragraphs[:20])

    numero = None
    ano = None
    numero_match = re.search(r"N[ºo]\s*(\d{1,4})/(\d{4})", text, flags=re.IGNORECASE)
    if numero_match:
        numero, ano = numero_match.groups()

    data_line_match = re.search(
        r"Data de divulga[cç][aã]o:\s*(.+)",
        text,
        flags=re.IGNORECASE,
    )
    data = parse_pt_date(data_line_match.group(1)) if data_line_match else None
    if not data:
        data = parse_pt_date(text)

    return InformativoMetadata(
        numero_informativo=numero,
        ano_informativo=ano,
        data_informativo=data,
    )
