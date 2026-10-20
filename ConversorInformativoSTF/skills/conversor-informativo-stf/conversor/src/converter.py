from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from xml.etree.ElementTree import ParseError
from zipfile import BadZipFile

from .document_reader import read_docx_paragraphs
from .editorial_item_splitter import split_editorial_items
from .field_extractor import extract_fields
from .metadata_extractor import extract_metadata
from .schemas import InformativoOutput
from .section_extractor import extract_plenario_section
from .validator import validate_julgados


def convert_docx(docx_path: str | Path) -> InformativoOutput:
    paragraphs = read_docx_paragraphs(docx_path)
    metadata = extract_metadata(paragraphs)
    plenario = extract_plenario_section(paragraphs)
    items = split_editorial_items(plenario)
    julgados = [extract_fields(item, metadata) for item in items]
    return InformativoOutput(julgado_stf=julgados)


def save_json(output: InformativoOutput, output_path: str | Path) -> Path:
    path = Path(output_path)
    path.write_text(
        json.dumps(output.model_dump(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def convert_file(docx_path: str | Path, output_path: str | Path | None = None) -> Path:
    input_path = Path(docx_path)
    output = convert_docx(input_path)
    issues = validate_julgados(output.julgado_stf)
    if issues:
        print("Avisos de validação:")
        for issue in issues:
            print(f"- {issue}")

    target = Path(output_path) if output_path else input_path.with_suffix(".json")
    return save_json(output, target)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Converte Informativo STF em DOCX para JSON base determinístico."
    )
    parser.add_argument("docx_file", help="Caminho do DOCX do Informativo STF.")
    parser.add_argument("-o", "--output", help="Caminho do JSON de saída.")
    args = parser.parse_args()

    input_path = Path(args.docx_file)
    if not input_path.exists():
        print(f"Erro: arquivo não encontrado: {input_path}", file=sys.stderr)
        sys.exit(1)
    if input_path.suffix.lower() != ".docx":
        print(f"Erro: o arquivo de entrada deve ser .docx: {input_path}", file=sys.stderr)
        sys.exit(1)

    try:
        output_path = convert_file(input_path, args.output)
    except (BadZipFile, KeyError, ParseError):
        print(
            f"Erro: não foi possível ler o DOCX. O arquivo pode estar inválido ou corrompido: {input_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"JSON salvo em: {output_path}")


if __name__ == "__main__":
    main()
