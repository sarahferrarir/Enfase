import argparse
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from document_converter import docx_to_markdown
from text_cleaner import clean_markdown
from text_splitter import extract_metadata, split_julgados
from llm_processor import extract_julgado_data


def _is_julgado_valid(julgado, bloco_original: str) -> bool:
    if not julgado.classe_processo or not julgado.classe_processo.strip():
        return False

    if not julgado.numero_processo or not julgado.numero_processo.strip():
        return False

    if not julgado.titulo or not julgado.titulo.strip():
        return False

    if not julgado.resumo or not julgado.resumo.strip():
        return False

    bloco_upper = bloco_original.upper()

    classes = [
        item.strip().upper()
        for item in julgado.classe_processo.split(";")
        if item.strip()
    ]

    numeros = [
        item.strip()
        for item in julgado.numero_processo.split(";")
        if item.strip()
    ]

    # Pelo menos uma classe deve aparecer no bloco
    if classes and not any(classe in bloco_upper for classe in classes):
        return False

    # Pelo menos um número de processo deve aparecer no bloco
    if numeros and not any(numero in bloco_original for numero in numeros):
        return False

    return True


def _generate_iso_timestamp() -> str:
    now = datetime.now(timezone.utc)
    return now.isoformat(timespec='milliseconds').replace('+00:00', 'Z')


def _generate_uuid() -> str:
    return str(uuid.uuid4())


def main():
    parser = argparse.ArgumentParser(
        description="Conversor de Informativos do STF de DOCX para JSON"
    )
    parser.add_argument(
        "docx_file",
        help="Caminho do arquivo DOCX a ser convertido"
    )

    args = parser.parse_args()
    input_path = Path(args.docx_file)

    if not input_path.exists():
        print(f"Erro: Arquivo '{input_path}' não encontrado.")
        return

    if input_path.suffix.lower() != ".docx":
        print(f"Erro: O arquivo deve ser um DOCX. Recebido: {input_path.suffix}")
        return

    try:
        print(f"Convertendo {input_path.name} para Markdown...")
        markdown = docx_to_markdown(str(input_path))

        print("Limpando Markdown...")
        cleaned = clean_markdown(markdown)

        print("Extraindo metadados do informativo...")
        metadata = extract_metadata(cleaned)
        numero_informativo = metadata.get("numero_informativo", "")
        data_publicacao = metadata.get("data_publicacao", "")

        print("Separando blocos de julgados...")
        blocos_julgados = split_julgados(cleaned)
        print(f"Total de blocos encontrados: {len(blocos_julgados)}")

        for i, bloco in enumerate(blocos_julgados, start=1):
            print(f"\n========== DEBUG BLOCO {i} ==========")
            print(bloco[:2000])
            print("========== FIM DEBUG ==========\n")

        julgados_stf = []
        blocos_descartados = 0

        for idx, bloco in enumerate(blocos_julgados, 1):
            print(f"\nProcessando bloco {idx}/{len(blocos_julgados)}...")

            try:
                julgado = extract_julgado_data(bloco)

                if julgado.informativo is None:
                    julgado.informativo = numero_informativo

                if julgado.data_informativo is None:
                    julgado.data_informativo = data_publicacao

                if _is_julgado_valid(julgado, bloco):
                    julgado.id = _generate_uuid()
                    julgado.created_at = _generate_iso_timestamp()
                    julgados_stf.append(julgado)
                    print(f"✅ Julgado válido: {julgado.numero_processo}")

                else:
                    print(f"❌ Julgado descartado (incompleto ou inválido):")
                    print(f"   - classe_processo: {julgado.classe_processo}")
                    print(f"   - numero_processo: {julgado.numero_processo}")
                    print(f"   - titulo: {julgado.titulo}")
                    print(f"   - resumo: {julgado.resumo[:50] if julgado.resumo else 'vazio'}...")
                    blocos_descartados += 1

            except Exception as e:
                print(f"⚠️ Erro ao processar bloco {idx}: {str(e)}")
                blocos_descartados += 1
                continue

        print(f"\n{'='*60}")
        print(f"Resumo do processamento:")
        print(f"  - Blocos encontrados: {len(blocos_julgados)}")
        print(f"  - Julgados válidos: {len(julgados_stf)}")
        print(f"  - Blocos descartados: {blocos_descartados}")
        print(f"{'='*60}")

        if not julgados_stf:
            print("Erro: Nenhum julgado válido foi processado.")
            return

        output_path = input_path.with_suffix(".json")

        resultado = {"julgado_stf": [julgado.model_dump() for julgado in julgados_stf]}

        print(f"\nSalvando em {output_path.name}...")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                resultado,
                f,
                indent=2,
                ensure_ascii=False
            )

        print(f"Conversão concluída com sucesso!")
        print(f"Arquivo: {output_path}")

    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")


if __name__ == "__main__":
    main()

