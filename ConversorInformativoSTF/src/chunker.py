import re
from typing import List


def chunk_text(text: str, chunk_size: int = 3000, overlap: int = 300) -> List[str]:
    """
    Divide texto em chunks de forma inteligente:
    1. Primeiro tenta detectar blocos por cabeçalhos de área jurídica
    2. Se bloco for muito grande, divide com overlap
    3. Preserva contexto de julgados

    Args:
        text: texto para dividir
        chunk_size: tamanho máximo de cada chunk (em caracteres)
        overlap: sobreposição entre chunks

    Returns:
        Lista de chunks
    """
    if not text or len(text) < chunk_size:
        return [text]

    # Padrões de cabeçalho de área jurídica
    header_pattern = r"(?:^|\n)((?:DIREITO\s+[A-Z\s]+?|[A-Z\s]+?:)(?=\n|$))"

    # Primeiro, tenta dividir por headers
    blocks = re.split(header_pattern, text, flags=re.MULTILINE | re.IGNORECASE)

    chunks = []
    for block in blocks:
        if not block or len(block.strip()) < 50:
            continue

        block = block.strip()

        # Se bloco cabe em um chunk, adicionar
        if len(block) <= chunk_size:
            chunks.append(block)
        else:
            # Senão, subdividir com overlap
            sub_chunks = _split_large_block(block, chunk_size, overlap)
            chunks.extend(sub_chunks)

    return chunks if chunks else [text]


def _split_large_block(text: str, chunk_size: int, overlap: int) -> List[str]:
    """
    Subdivide um bloco grande tentando não quebrar no meio de parágrafos.

    Args:
        text: bloco de texto
        chunk_size: tamanho máximo
        overlap: sobreposição

    Returns:
        Lista de chunks
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size

        # Se não é o último, tenta quebrar em parágrafo (não meio de linha)
        if end < len(text):
            # Procura por "\n\n" próximo ao final
            last_para_break = text.rfind("\n\n", start + chunk_size - 500, end)
            if last_para_break > start + 200:
                end = last_para_break
            else:
                # Fallback: quebrar em nova linha
                last_line_break = text.rfind("\n", start + chunk_size - 200, end)
                if last_line_break > start + 200:
                    end = last_line_break

        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        # Se é o último chunk, sair
        if end >= len(text):
            break

        # Avança com overlap
        start = end - overlap

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
