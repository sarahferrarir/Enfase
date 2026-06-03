from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from uuid import uuid4


MONTHS_PT = {
    "janeiro": "01",
    "fevereiro": "02",
    "marco": "03",
    "março": "03",
    "abril": "04",
    "maio": "05",
    "junho": "06",
    "julho": "07",
    "agosto": "08",
    "setembro": "09",
    "outubro": "10",
    "novembro": "11",
    "dezembro": "12",
}


def generate_id() -> str:
    return str(uuid4())


def generate_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def normalize_spaces(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_heading(text: str) -> str:
    clean = strip_accents(normalize_spaces(text)).upper()
    clean = clean.replace("—", "-").replace("–", "-")
    return clean


def parse_pt_date(text: str) -> str | None:
    match = re.search(
        r"(\d{1,2})\s+de\s+([a-zçãéíóúâêô]+)\s+de\s+(\d{4})",
        text,
        flags=re.IGNORECASE,
    )
    if not match:
        return None

    day, month_name, year = match.groups()
    month = MONTHS_PT.get(month_name.lower())
    if not month:
        return None
    return f"{year}-{month}-{int(day):02d}"


def parse_numeric_date(text: str) -> str | None:
    match = re.search(r"\b(\d{1,2})[./](\d{1,2})[./](\d{4})\b", text)
    if not match:
        return None
    day, month, year = match.groups()
    return f"{year}-{int(month):02d}-{int(day):02d}"


def unique_or_join(values: list[str], separator: str = "; ") -> str | None:
    cleaned = [normalize_spaces(v) for v in values if v and normalize_spaces(v)]
    if not cleaned:
        return None

    unique: list[str] = []
    for value in cleaned:
        if value not in unique:
            unique.append(value)

    if len(unique) == 1:
        return unique[0]
    return separator.join(unique)

