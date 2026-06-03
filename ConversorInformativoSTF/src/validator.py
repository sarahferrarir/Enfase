from __future__ import annotations

from .schemas import JulgadoSTF


def validate_julgados(julgados: list[JulgadoSTF]) -> list[str]:
    issues: list[str] = []

    for index, julgado in enumerate(julgados, start=1):
        prefix = f"Item {index}"
        if not julgado.titulo:
            issues.append(f"{prefix}: titulo ausente")
        if not julgado.resumo:
            issues.append(f"{prefix}: resumo ausente")
        if not julgado.classe_processo or not julgado.numero_processo:
            issues.append(f"{prefix}: processo principal ausente")

    return issues

