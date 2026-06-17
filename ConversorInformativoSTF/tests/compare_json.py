from __future__ import annotations

import argparse
import difflib
import html
import json
import re
import sys
import unicodedata
from collections import defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RELEVANT_FIELDS = (
    "informativo",
    "classe_processo",
    "numero_processo",
    "uf",
    "data_julgamento",
    "relator",
    "redator_acordao",
    "orgao_julgador",
    "situacao_julgamento",
    "titulo",
    "resumo",
    "noticia",
    "ramo_direito",
    "materia",
    "ods_onu2030",
    "legislacao",
    "tema_rg",
    "repercussao_geral",
    "data_informativo",
    "type",
)

MATCH_FIELDS = ("classe_processo", "numero_processo", "uf")
SEPARATOR_NORMALIZED_FIELDS = {
    "ramo_direito",
    "materia",
    "classe_processo",
    "numero_processo",
    "uf",
    "ods_onu2030",
    "situacao_julgamento",
}
MISSING = object()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compara JSON gerado pelo conversor com um JSON esperado."
    )
    parser.add_argument("--generated", required=True, help="Caminho do JSON gerado.")
    parser.add_argument("--expected", required=True, help="Caminho do JSON esperado.")
    parser.add_argument(
        "--informativo",
        required=True,
        help="Número do informativo a comparar.",
    )
    parser.add_argument(
        "--ignore-fields",
        default="",
        help=(
            "Campos adicionais a ignorar na comparação, separados por vírgula. "
            "Exemplo: legislacao,situacao_julgamento"
        ),
    )
    parser.add_argument(
        "--report-json",
        help=(
            "Caminho customizado para salvar o relatório completo da comparação "
            "em JSON. Por padrão, salva em reports/compare_<informativo>.json."
        ),
    )
    return parser.parse_args()


def load_julgados(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict) and isinstance(data.get("julgado_stf"), list):
        items = data["julgado_stf"]
    elif isinstance(data, list):
        items = data
    else:
        raise ValueError(
            f"{path}: formato inválido. Esperado objeto com chave 'julgado_stf'."
        )

    invalid_items = [index for index, item in enumerate(items) if not isinstance(item, dict)]
    if invalid_items:
        raise ValueError(f"{path}: itens não-objeto encontrados: {invalid_items}")

    return items


def normalize_text(value: str) -> str:
    value = html.unescape(value).replace("\xa0", " ")
    value = re.sub(
        r"(?is)<\s*/?\s*(br|p|li|ul|ol|div|section|article|h[1-6])[^>]*>",
        " ",
        value,
    )
    value = re.sub(r"(?is)<[^>]+>", "", value)
    value = html.unescape(value).replace("\xa0", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_value(value: Any) -> Any:
    if isinstance(value, str):
        return normalize_text(value)
    if isinstance(value, list):
        return [normalize_value(item) for item in value]
    if isinstance(value, dict):
        return {key: normalize_value(item) for key, item in value.items()}
    return value


def normalize_separators(value: str) -> str:
    value = re.sub(r"\s*;\s*", "; ", value)
    value = re.sub(r"\s*\|\s*", " | ", value)
    value = re.sub(r"\s*,\s*", ", ", value)
    value = re.sub(r"\s*/\s*", "/", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def normalize_value_for_field(field: str, value: Any) -> Any:
    normalized = normalize_value(value)
    if field in SEPARATOR_NORMALIZED_FIELDS and isinstance(normalized, str):
        return normalize_separators(normalized)
    return normalized


def normalize_for_title_match(value: Any) -> str:
    normalized = normalize_text(str(value or "")).casefold()
    normalized = unicodedata.normalize("NFKD", normalized)
    normalized = "".join(char for char in normalized if not unicodedata.combining(char))
    return normalized


def filter_by_informativo(
    items: list[dict[str, Any]], informativo: str
) -> list[dict[str, Any]]:
    return [
        item
        for item in items
        if normalize_text(str(item.get("informativo", ""))) == informativo
    ]


def make_match_key(item: dict[str, Any]) -> tuple[str, str, str]:
    return tuple(
        normalize_value_for_field(field, str(item.get(field) or ""))
        for field in MATCH_FIELDS
    )


def key_label(item: dict[str, Any]) -> str:
    classe, numero, uf = make_match_key(item)
    titulo = normalize_text(str(item.get("titulo") or ""))
    label = f"{classe} {numero}/{uf}".strip()
    return f"{label} | {titulo}" if titulo else label


def match_items(
    expected_items: list[dict[str, Any]], generated_items: list[dict[str, Any]]
) -> tuple[
    list[tuple[dict[str, Any], dict[str, Any]]],
    list[dict[str, Any]],
    list[dict[str, Any]],
]:
    generated_by_key: dict[tuple[str, str, str], deque[dict[str, Any]]] = defaultdict(deque)
    for item in generated_items:
        generated_by_key[make_match_key(item)].append(item)

    matched: list[tuple[dict[str, Any], dict[str, Any]]] = []
    missing: list[dict[str, Any]] = []

    for expected in expected_items:
        key = make_match_key(expected)
        if generated_by_key[key]:
            matched.append((expected, generated_by_key[key].popleft()))
        else:
            missing.append(expected)

    extra = [
        item
        for remaining_items in generated_by_key.values()
        for item in remaining_items
    ]
    return matched, missing, extra


def field_value(item: dict[str, Any], field: str) -> Any:
    if field not in item:
        return MISSING
    return normalize_value_for_field(field, item[field])


def find_field_differences(
    matched_items: list[tuple[dict[str, Any], dict[str, Any]]],
    compared_fields: tuple[str, ...],
) -> list[tuple[dict[str, Any], str, Any, Any]]:
    differences: list[tuple[dict[str, Any], str, Any, Any]] = []
    for expected, generated in matched_items:
        for field in compared_fields:
            expected_value = field_value(expected, field)
            generated_value = field_value(generated, field)
            if expected_value != generated_value:
                differences.append((expected, field, expected_value, generated_value))
    return differences


def parse_ignore_fields(value: str) -> set[str]:
    if not value:
        return set()
    return {field.strip() for field in value.split(",") if field.strip()}


def shorten(value: str, limit: int = 240) -> str:
    if len(value) <= limit:
        return value
    return f"{value[: limit - 3]}..."


def render_value(value: Any) -> str:
    if value is MISSING:
        return "<campo ausente>"
    if isinstance(value, str):
        return f'"{shorten(value)}"'
    return shorten(json.dumps(value, ensure_ascii=False, sort_keys=True))


def serialize_value(value: Any) -> Any:
    if value is MISSING:
        return "<campo ausente>"
    return value


def first_difference_index(left: Any, right: Any) -> int | None:
    if not isinstance(left, str) or not isinstance(right, str):
        return None

    for index, (left_char, right_char) in enumerate(zip(left, right)):
        if left_char != right_char:
            return index
    if len(left) != len(right):
        return min(len(left), len(right))
    return None


def best_title_suggestion(
    item: dict[str, Any], candidates: list[dict[str, Any]]
) -> tuple[float, dict[str, Any] | None]:
    title = normalize_for_title_match(item.get("titulo"))
    if not title:
        return 0.0, None

    best_score = 0.0
    best_candidate = None
    for candidate in candidates:
        candidate_title = normalize_for_title_match(candidate.get("titulo"))
        if not candidate_title:
            continue
        score = difflib.SequenceMatcher(None, title, candidate_title).ratio()
        if score > best_score:
            best_score = score
            best_candidate = candidate
    return best_score, best_candidate


def print_item_list(
    title: str,
    items: list[dict[str, Any]],
    suggestion_candidates: list[dict[str, Any]],
) -> None:
    print(f"\n{title}: {len(items)}")
    if not items:
        print("  Nenhum.")
        return

    for item in items:
        print(f"  - {key_label(item)}")
        score, suggestion = best_title_suggestion(item, suggestion_candidates)
        if suggestion is not None:
            print(
                "    Possível correspondência por título "
                f"({score:.0%}): {key_label(suggestion)}"
            )


def print_field_differences(
    differences: list[tuple[dict[str, Any], str, Any, Any]]
) -> None:
    print(f"\nDiferenças por campo: {len(differences)}")
    if not differences:
        print("  Nenhuma.")
        return

    current_item: dict[str, Any] | None = None
    for item, field, expected_value, generated_value in differences:
        if item is not current_item:
            current_item = item
            print(f"  - {key_label(item)}")

        print(f"    Campo: {field}")
        first_diff = first_difference_index(expected_value, generated_value)
        if first_diff is not None:
            print(f"      Primeira diferença no caractere: {first_diff}")
        print(f"      Esperado: {render_value(expected_value)}")
        print(f"      Gerado:   {render_value(generated_value)}")


def item_report_entry(
    item: dict[str, Any], suggestion_candidates: list[dict[str, Any]]
) -> dict[str, Any]:
    score, suggestion = best_title_suggestion(item, suggestion_candidates)
    entry: dict[str, Any] = {"item": key_label(item)}
    if suggestion is not None:
        entry["possible_title_match"] = {
            "score": round(score, 4),
            "item": key_label(suggestion),
        }
    return entry


def build_report(
    *,
    informativo: str,
    expected_path: Path,
    generated_path: Path,
    expected_items: list[dict[str, Any]],
    generated_items: list[dict[str, Any]],
    matched_items: list[tuple[dict[str, Any], dict[str, Any]]],
    missing_items: list[dict[str, Any]],
    extra_items: list[dict[str, Any]],
    field_differences: list[tuple[dict[str, Any], str, Any, Any]],
    ignored_fields: set[str],
) -> dict[str, Any]:
    passed = not (missing_items or extra_items or field_differences)
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "expected_path": str(expected_path),
        "generated_path": str(generated_path),
        "informativo": informativo,
        "expected_items": len(expected_items),
        "generated_items": len(generated_items),
        "matched_items": len(matched_items),
        "missing_items": len(missing_items),
        "extra_items": len(extra_items),
        "field_differences": len(field_differences),
        "passed": passed,
        "ignored_fields": sorted(ignored_fields),
        "missing": [
            item_report_entry(item, generated_items) for item in missing_items
        ],
        "extra": [
            item_report_entry(item, expected_items) for item in extra_items
        ],
        "differences": [
            {
                "item": key_label(item),
                "field": field,
                "expected": serialize_value(expected_value),
                "generated": serialize_value(generated_value),
            }
            for item, field, expected_value, generated_value in field_differences
        ],
    }


def write_report_json(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=2)
        file.write("\n")


def main() -> int:
    args = parse_args()
    informativo = normalize_text(str(args.informativo))
    ignored_fields = parse_ignore_fields(args.ignore_fields)
    compared_fields = tuple(
        field for field in RELEVANT_FIELDS if field not in ignored_fields
    )

    expected_path = Path(args.expected)
    generated_path = Path(args.generated)

    expected_items = filter_by_informativo(load_julgados(expected_path), informativo)
    generated_items = filter_by_informativo(load_julgados(generated_path), informativo)

    matched_items, missing_items, extra_items = match_items(
        expected_items, generated_items
    )
    field_differences = find_field_differences(matched_items, compared_fields)
    report = build_report(
        informativo=informativo,
        expected_path=expected_path,
        generated_path=generated_path,
        expected_items=expected_items,
        generated_items=generated_items,
        matched_items=matched_items,
        missing_items=missing_items,
        extra_items=extra_items,
        field_differences=field_differences,
        ignored_fields=ignored_fields,
    )

    report_json_path = (
        Path(args.report_json)
        if args.report_json
        else Path("reports") / f"compare_{informativo}.json"
    )
    write_report_json(report_json_path, report)

    print("Relatório de comparação de acurácia")
    print(f"Informativo comparado: {informativo}")
    print(f"Itens esperados: {len(expected_items)}")
    print(f"Itens gerados: {len(generated_items)}")
    print(f"Itens casados: {len(matched_items)}")
    if ignored_fields:
        print(f"Campos ignorados adicionalmente: {', '.join(sorted(ignored_fields))}")

    print_item_list("Itens faltando", missing_items, generated_items)
    print_item_list("Itens extras", extra_items, expected_items)
    print_field_differences(field_differences)

    print(f"\nResumo final: {'PASSOU' if report['passed'] else 'FALHOU'}")
    print(f"Relatório JSON salvo em: {report_json_path}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
