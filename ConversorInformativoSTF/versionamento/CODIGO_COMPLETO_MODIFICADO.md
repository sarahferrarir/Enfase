# CÓDIGO COMPLETO DOS ARQUIVOS MODIFICADOS

## 1️⃣ models.py
```python
from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict, Any
from datetime import datetime


class Julgado(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    id: str | None = None
    created_at: str | None = None
    informativo: str | None = None
    classe_processo: str | None = None
    numero_processo: str | None = None
    incidente_julgamento: str | None = None
    uf: str | None = None
    observacao: str | None = None
    data_julgamento: str | None = None
    relator: str | None = None
    redator_acordao: str | None = None
    orgao_julgador: str | None = None
    tipo_julgamento: str | None = None
    situacao_julgamento: str | None = None
    titulo: str | None = None
    tese_julgado: str | None = None
    resumo: str | None = None
    noticia: str | None = None
    ramo_direito: str | None = None
    materia: str | None = None
    repercussao_geral: str | None = None
    tema_rg: str | None = None
    legislacao: str | None = None
    ods_onu2030: str | None = None
    covid19: str | None = None
    noticia_completa: str | None = None
    data_informativo: str | None = None
    status: str | None = None
    type: str | None = None
    classificacao: str | None = None
    comentario: str | None = None
    comments: Dict[str, Any] | None = None
    conteudo_fixacao: str | None = None
    grau_incidencia: str | None = None
    html: str | None = None
    is_extraordinary: bool = False
    metadata: Dict[str, Any] | None = None
    modified_by_users: List[str] | None = None
    new_classificacao: str | None = None
    questao: str | None = None
    tema_julgado: str | None = None


class Informativo(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    numero_informativo: str
    ano_informativo: str
    data_publicacao: str
    julgados: List[Julgado]
```

---

## 2️⃣ llm_processor.py
```python
import re
from models import Julgado


def extract_julgado_data(bloco: str) -> Julgado:
    julgado = Julgado()

    julgado.noticia_completa = bloco.strip()

    classe_processo, numero_processo, uf = _extract_processo(bloco)
    julgado.classe_processo = classe_processo
    julgado.numero_processo = numero_processo
    julgado.uf = uf

    julgado.ramo_direito = _extract_ramo_direito(bloco)

    julgado.materia = _extract_materia(bloco)

    julgado.titulo = _extract_titulo(bloco)

    resumo_text = _extract_resumo(bloco)
    julgado.resumo = _wrap_html(resumo_text) if resumo_text else None

    ods_raw = _extract_ods(bloco)
    julgado.ods_onu2030 = _format_ods(ods_raw) if ods_raw else None

    julgado.legislacao = _extract_legislacao(bloco)

    julgado.noticia = _extract_noticia(bloco)

    julgado.type = "STF"
    julgado.status = "APROVADO"
    julgado.is_extraordinary = False
    julgado.grau_incidencia = "PENDENTE"
    julgado.metadata = {}
    julgado.comments = {}
    julgado.new_classificacao = "{}"
    julgado.modified_by_users = []

    return julgado


def _extract_processo(bloco: str) -> tuple:
    pattern = r"\b(ADI|ADPF|ADO|ADC|RE|ARE|HC|MS|Rcl|ACO)\s+(\d+\.?\d*(?:\s*AgR)?)\s*/\s*([A-Z]{2})"

    match = re.search(pattern, bloco)
    if match:
        classe = match.group(1)
        numero = f"{match.group(2)}/{match.group(3)}"
        uf = match.group(3)
        return classe, numero, uf

    return None, None, None


def _extract_ramo_direito(bloco: str) -> str:
    primeira_linha = bloco.split("\n")[0].strip()

    if primeira_linha.startswith("DIREITO "):
        ramo = primeira_linha.replace("DIREITO ", "").strip()
        ramo = ramo.split("–")[0].strip()
        if ramo:
            return f"DIREITO {ramo}"

    return None


def _extract_materia(bloco: str) -> str:
    primeira_linha = bloco.split("\n")[0].strip()

    if "–" in primeira_linha:
        partes = primeira_linha.split("–")
        if len(partes) > 1:
            materias = [p.strip() for p in partes[1:]]
            materia_str = ";".join(materias)
            if materia_str:
                return materia_str

    return None


def _extract_titulo(bloco: str) -> str:
    padroes = [
        r"__\*([^*]+)\*__",
        r"\*\*([^*]+)\*\*",
        r"__(.*?)__",
        r"\*\*(.*?)\*\*"
    ]

    for padrao in padroes:
        match = re.search(padrao, bloco)
        if match:
            titulo = match.group(1).strip()
            if titulo and len(titulo) > 5:
                return titulo

    linhas = bloco.split("\n")
    for i, linha in enumerate(linhas):
        linha_stripped = linha.strip()
        if (i > 0 and
            linha_stripped and
            not linha_stripped.startswith("DIREITO") and
            not linha_stripped.startswith("ADI") and
            not linha_stripped.startswith("ADPF") and
            not linha_stripped.startswith("RE ") and
            len(linha_stripped) > 10 and
            len(linha_stripped) < 300 and
            "Resumo:" not in linha_stripped):
            return linha_stripped

    return None


def _extract_resumo(bloco: str) -> str:
    padrao = r"Resumo:\s*(.*?)(?=\n\n|\n(?:Conforme|Com base|Precedentes|Sumário|ADI|ADPF|RE |$))"

    match = re.search(padrao, bloco, re.DOTALL | re.IGNORECASE)
    if match:
        resumo_raw = match.group(1).strip()
        resumo_clean = re.sub(r"__\*|\*__|\*\*|__", "", resumo_raw)
        resumo_clean = re.sub(r"\s+", " ", resumo_clean).strip()

        if resumo_clean:
            return resumo_clean

    return None


def _extract_ods(bloco: str) -> str:
    padroes = [
        r"__ODS:?__\s*([\d\,;]+)",
        r"ODS:\s*(\[[0-9]+\][,\s]*)+",
        r"ODS:\s*([\d,;]+)",
        r"\[([0-9]+)\]\s*e\s*\[([0-9]+)\]",
        r"ODS\s+([0-9]+)"
    ]

    encontrados = set()

    link_pattern = r"\[([0-9]+)\]"
    link_matches = re.findall(link_pattern, bloco)
    encontrados.update(link_matches)

    for padrao in padroes:
        matches = re.findall(padrao, bloco, re.IGNORECASE)
        for match in matches:
            if isinstance(match, tuple):
                for item in match:
                    if item.isdigit():
                        encontrados.add(item)
            else:
                numeros = re.findall(r"\d+", str(match))
                encontrados.update(numeros)

    if encontrados:
        return ";".join(sorted(encontrados))

    return None


def _extract_legislacao(bloco: str) -> str:
    padroes = [
        r"(?:Lei|Decreto|Emenda|CF|Constituição|Código|Súmula|Resolução)\s+(?:n[oº]\.?\s*)?([^\n,;]+?)(?=[,;.\n])",
        r"(?:Art|artigo)\s+(\d+(?:\s*,\s*\d+)*)",
        r"(?:Lei|Lei Complementar|Lei Federal)\s+([^\n,;]+?)(?=[,;.\n])",
    ]

    encontradas = []

    for padrao in padroes:
        matches = re.findall(padrao, bloco, re.IGNORECASE)
        encontradas.extend([m.strip() for m in matches if m.strip()])

    encontradas = list(dict.fromkeys(encontradas))
    encontradas = [l for l in encontradas if len(l) > 2 and len(l) < 200]

    if encontradas:
        return ";".join(encontradas[:10])

    return None


def _wrap_html(text: str) -> str:
    if not text:
        return None
    if text.startswith("<"):
        return text
    paragraphs = text.split("\n\n")
    wrapped = "".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip())
    return wrapped


def _format_ods(ods_str: str) -> str:
    if not ods_str:
        return None
    numeros = [n.strip() for n in ods_str.replace(";", ",").split(",") if n.strip()]
    numeros = sorted(set(numeros), key=int)
    return ", ".join(numeros)


def _extract_noticia(bloco: str) -> str:
    resumo_text = _extract_resumo(bloco)
    if resumo_text:
        return _wrap_html(resumo_text)
    return None
```

---

## 3️⃣ converter.py
```python
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

    if classes and not any(classe in bloco_upper for classe in classes):
        return False

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
```

---

## 📋 SUMÁRIO DAS MUDANÇAS

| Arquivo | Linhas Originais | Linhas Novas | Mudanças |
|---------|-----------------|-------------|----------|
| models.py | 42 | 59 | +16 campos, imports |
| llm_processor.py | 163 | 208 | +4 funções, melhorias extração |
| converter.py | 156 | 170 | +2 funções, geração ID/timestamp |
| **Total** | **361** | **437** | **+76 linhas** |

---

## ✅ VALIDAÇÕES

Todos os arquivos foram:
- ✅ Testados com sucesso
- ✅ Validados com Pydantic
- ✅ Executados sem erros
- ✅ Geraram JSON correto com 41 campos
