import re
from typing import List


def chunk_text(text: str, chunk_size: int = 3000, overlap: int = 300) -> List[str]:
    """
    Divide texto em chunks sobrepostos sem assumir limites de julgados.
    Estratégia: baseada em tamanho + tentativa de não quebrar no meio de parágrafos.

    Args:
        text: texto para dividir
        chunk_size: tamanho aproximado de cada chunk (em caracteres)
        overlap: sobreposição entre chunks para não perder contexto

    Returns:
        Lista de chunks
    """
    if not text or len(text) < chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        # Se não é o último chunk, tenta não quebrar no meio de parágrafo
        if end < len(text):
            # Procura por quebra de parágrafo (\n\n) próxima ao final
            last_break = text.rfind("\n\n", start + chunk_size - 500, end)
            if last_break > start + chunk_size - 800:
                end = last_break

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        # Avança com overlap
        start = end - overlap

        if start >= len(text):
            break

    return chunks


def extract_julgados_rough(text: str) -> List[dict]:
    """
    Extração MUITO simples e rápida de blocos que parecem ser julgados.
    Usado para debug/logging, não para extração final.

    Args:
        text: texto completo

    Returns:
        Lista com dict {"start": int, "end": int, "preview": str}
    """
    blocks = []

    # Padrão muito básico: procura por "ADI", "RE", etc. seguido de número
    processo_pattern = r"\b(ADI|ADPF|ADO|ADC|RE|ARE|HC|MS|Rcl|RCL|ACO)\s+[\d\.\-/]+"

    for match in re.finditer(processo_pattern, text):
        start = max(0, match.start() - 200)
        end = min(len(text), match.end() + 2000)

        blocks.append({
            "start": start,
            "end": end,
            "preview": text[start:start + 100] + "..."
        })

    # Remove duplicatas
    unique_blocks = []
    for block in blocks:
        is_duplicate = False
        for unique_block in unique_blocks:
            if abs(block["start"] - unique_block["start"]) < 100:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_blocks.append(block)

    return unique_blocks
