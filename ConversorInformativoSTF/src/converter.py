import json
from pathlib import Path
from typing import Optional, List
import argparse

from .document_reader import read_docx
from .text_preprocessor import clean_text, extract_metadata
from .chunker import chunk_text
from .ollama_client import OllamaClient
from .llm_processor import LLMProcessor
from .validator import JulgadoValidator
from .schemas import Julgado, Informativo
from .utils import generate_id, generate_timestamp


class InformativoConverter:
    """Orquestrador do pipeline de conversão de informativos STF."""

    def __init__(
        self,
        ollama_base_url: str = "http://localhost:11434",
        ollama_model: str = "qwen2.5:14b",
        ollama_temperature: float = 0.1,
        chunk_size: int = 3000,
        chunk_overlap: int = 300,
    ):
        """
        Args:
            ollama_base_url: URL do Ollama
            ollama_model: modelo a usar
            ollama_temperature: temperatura do modelo
            chunk_size: tamanho de cada chunk
            chunk_overlap: sobreposição entre chunks
        """
        self.ollama_client = OllamaClient(
            base_url=ollama_base_url,
            model=ollama_model,
            temperature=ollama_temperature,
        )
        self.llm_processor = LLMProcessor(self.ollama_client)
        self.validator = JulgadoValidator()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def convert(self, docx_path: str, output_path: Optional[str] = None) -> Path:
        """
        Converte DOCX em JSON de julgados.

        Args:
            docx_path: caminho do DOCX
            output_path: caminho de saída (opcional, auto-gera se não informado)

        Returns:
            Path do arquivo JSON gerado

        Raises:
            FileNotFoundError: se DOCX não existir
            RuntimeError: se Ollama não estiver disponível
        """
        input_path = Path(docx_path)

        if not input_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {docx_path}")

        if input_path.suffix.lower() != ".docx":
            raise ValueError(f"Arquivo deve ser DOCX, recebido: {input_path.suffix}")

        print(f"📄 Lendo DOCX: {input_path.name}")
        markdown = read_docx(str(input_path))

        print("🧹 Limpando texto...")
        cleaned_text = clean_text(markdown)

        print("📊 Extraindo metadados...")
        metadata = extract_metadata(cleaned_text)
        numero_informativo = metadata.get("numero_informativo")
        data_publicacao = metadata.get("data_publicacao")

        print(f"   - Informativo: {numero_informativo}")
        print(f"   - Data: {data_publicacao}")

        print(f"✂️  Dividindo em chunks ({self.chunk_size} chars)...")
        chunks = chunk_text(cleaned_text, self.chunk_size, self.chunk_overlap)
        print(f"   - Total de chunks: {len(chunks)}")

        print("\n🤖 Processando chunks com Ollama...")
        all_julgados_data = []

        for i, chunk in enumerate(chunks, 1):
            print(f"\n   Chunk {i}/{len(chunks)} ({len(chunk)} chars)...")
            try:
                julgados_data = self.llm_processor.process_chunk(chunk)
                all_julgados_data.extend(julgados_data)
                print(f"   ✅ Encontrados {len(julgados_data)} julgados")
            except Exception as e:
                print(f"   ❌ Erro: {str(e)}")
                continue

        print(f"\n📋 Convertendo para modelos Pydantic...")
        julgados = []
        for data in all_julgados_data:
            try:
                julgado = self.llm_processor.convert_to_julgado(data)
                julgado.informativo = numero_informativo
                julgado.data_informativo = data_publicacao
                julgado.id = generate_id()
                julgado.created_at = generate_timestamp()

                julgados.append(julgado)
            except Exception as e:
                print(f"   ⚠️  Erro ao converter: {str(e)}")
                continue

        print(f"\n✔️  Validando julgados...")
        valid_julgados = []
        for julgado in julgados:
            is_valid, issues = self.validator.is_valid(julgado)
            if is_valid:
                valid_julgados.append(julgado)
                print(f"   ✅ {julgado.numero_processo or julgado.classe_processo}")
            else:
                print(f"   ❌ Descartado: {', '.join(issues)}")

        # Remove duplicatas
        valid_julgados = self.validator.merge_julgados(valid_julgados)

        print(f"\n{'='*60}")
        print(f"📊 RESUMO:")
        print(f"   - Chunks processados: {len(chunks)}")
        print(f"   - Julgados extraídos: {len(all_julgados_data)}")
        print(f"   - Julgados válidos: {len(valid_julgados)}")
        print(f"{'='*60}")

        # Monta JSON final
        informativo = Informativo(
            numero_informativo=numero_informativo,
            data_publicacao=data_publicacao,
            julgados=valid_julgados,
        )

        # Determina caminho de saída
        if output_path is None:
            output_path = input_path.with_suffix(".json")
        else:
            output_path = Path(output_path)

        print(f"\n💾 Salvando em {output_path.name}...")
        with open(output_path, "w", encoding="utf-8") as f:
            resultado = {"julgado_stf": [j.model_dump() for j in valid_julgados]}
            json.dump(resultado, f, indent=2, ensure_ascii=False)

        print(f"✨ Conversão concluída com sucesso!")
        print(f"   Arquivo: {output_path.absolute()}")

        return output_path


def main():
    """CLI para converter informativos STF."""
    parser = argparse.ArgumentParser(
        description="Conversor de Informativos STF (DOCX → JSON) com Ollama"
    )
    parser.add_argument(
        "docx_file",
        help="Caminho do arquivo DOCX a converter"
    )
    parser.add_argument(
        "-o", "--output",
        help="Caminho do arquivo JSON de saída (opcional)",
        default=None
    )
    parser.add_argument(
        "--model",
        help="Modelo Ollama a usar (default: qwen2.5:14b)",
        default="qwen2.5:14b"
    )
    parser.add_argument(
        "--url",
        help="URL do Ollama (default: http://localhost:11434)",
        default="http://localhost:11434"
    )
    parser.add_argument(
        "--chunk-size",
        type=int,
        help="Tamanho de cada chunk em caracteres (default: 3000)",
        default=3000
    )
    parser.add_argument(
        "--temperature",
        type=float,
        help="Temperatura do modelo (0.0-1.0, default: 0.1)",
        default=0.1
    )

    args = parser.parse_args()

    try:
        converter = InformativoConverter(
            ollama_base_url=args.url,
            ollama_model=args.model,
            ollama_temperature=args.temperature,
            chunk_size=args.chunk_size,
        )
        converter.convert(args.docx_file, args.output)
    except Exception as e:
        print(f"\n❌ Erro fatal: {str(e)}")
        exit(1)


if __name__ == "__main__":
    main()
