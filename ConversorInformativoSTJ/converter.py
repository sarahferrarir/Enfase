import json
import argparse
import time
from pathlib import Path
from bs4 import BeautifulSoup

from html_parser import (
    read_html_file,
    extract_informativo_metadata,
    extract_julgados_html,
    clean_html_block,
    validate_html_structure,
)
from llm_processor import process_single_julgado
from models import InformativoResponse, JulgadoItem

def save_json(data: InformativoResponse, input_file: str) -> Path:
    """Salva resposta validada em arquivo JSON."""
    input_path = Path(input_file)
    output_path = input_path.with_suffix(".json")

    output_path.write_text(
        json.dumps(data.model_dump(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return output_path

def convert_informativo(html_file: str) -> InformativoResponse:
    """Converte arquivo HTML em InformativoResponse estruturado."""

    tempo_inicio = time.time()

    # Lê arquivo HTML
    html_content = read_html_file(html_file)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Valida estrutura HTML
    validate_html_structure(soup)

    # Extrai metadados do informativo
    metadata = extract_informativo_metadata(soup)
    informativo = InformativoResponse(
        numero_informativo=metadata["numero_informativo"],
        data_publicacao=metadata["data_publicacao"],
    )

    # Extrai blocos HTML de julgados
    julgados_html = extract_julgados_html(soup)
    print(f"Encontrados {len(julgados_html)} julgados para processar.\n")

    # Processa cada julgado individualmente
    for i, julgado_html in enumerate(julgados_html, 1):
        print(f"Processando julgado {i}/{len(julgados_html)}...")

        cleaned_text = clean_html_block(julgado_html)

        julgado = process_single_julgado(cleaned_text)

        if julgado:
            informativo.julgados.append(julgado)
            print(f"✓ Julgado {i} processado com sucesso")
        else:
            print(f"✗ Falha ao processar julgado {i}")

    tempo_fim = time.time()
    tempo_decorrido = tempo_fim - tempo_inicio

    print(f"\nTotal de julgados processados: {len(informativo.julgados)}")
    print(f"Tempo de processamento: {tempo_decorrido:.2f}s")

    return informativo

def main():
    parser = argparse.ArgumentParser(
        description="Converte HTML de informativo STJ para JSON estruturado."
    )

    parser.add_argument(
        "html_file",
        help="Caminho do arquivo HTML do informativo."
    )

    args = parser.parse_args()

    try:
        informativo = convert_informativo(args.html_file)

        output_path = save_json(informativo, args.html_file)

        print(f"\n✓ JSON salvo em: {output_path}")

    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
