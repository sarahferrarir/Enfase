import json
from typing import List, Optional, Dict, Any
from .ollama_client import OllamaClient
from .schemas import Julgado


SYSTEM_PROMPT = """Você é um especialista em jurisprudência do STF (Superior Tribunal Federal).
Sua tarefa é identificar e extrair APENAS julgados principais do informativo.

REGRAS CRÍTICAS:
1. Retorne APENAS JSON válido. Nenhum texto adicional antes/depois.
2. Um julgado PRINCIPAL tem: classe + número + título + resumo (todos obrigatórios)
3. DECISÕES CONJUNTAS: Se vários processos foram julgados JUNTOS, combine em UM item separando com ";"
   - Exemplo: "Rcl 77.893 e Rcl 78.401 julgados juntos" → numero_processo: "77893;78401"
4. Dados INCOMPLETOS não devem ser retornados como julgado
5. Se um número de processo aparece APENAS dentro do resumo de outro caso (como precedente/citação), NÃO extraia como julgado separado
6. Se o "resumo" é apenas "[Rcl 77.893 AgR/GO, relator...]" (dado referencial), NÃO é um julgado, descarte
7. Preserve o texto original, não resuma nem abrevie
8. Um resumo deve ser o texto substancial da decisão, não uma data ou referência processual
9. Para decisões conjuntas, o resumo é compartilhado entre todos os processos
10. Extraia TODAS as informações disponíveis: relator, data, legislação, incidente_julgamento, etc"""


JULGADO_EXTRACTION_PROMPT = """Analise o seguinte texto de um informativo do STF e identifique APENAS os julgados PRINCIPAIS.

CRITÉRIOS DE INCLUSÃO DE JULGADO (todos os 4 campos obrigatórios):
✓ classe_processo: ADI, ADPF, RE, ARE, HC, MS, Rcl, ACO, SL, etc (uma OU múltiplas classes separadas por ";")
✓ numero_processo: número completo (ex: "1.234/SP" ÚNICO ou "1005;1006;1097" se JULGADOS CONJUNTOS)
✓ titulo: título SUBSTANTIVO do caso (não vazio, não apenas "*itálicos*")
✓ resumo: parágrafo COMPLETO com a essência da decisão (mínimo 50 caracteres, NOT referências como "[Rcl 77.893 AgR/GO, relator...]")

DECISÕES CONJUNTAS (MUITO IMPORTANTE):
Se múltiplos processos foram julgados JUNTOS na MESMA DECISÃO:
- COMBINE em UM ÚNICO julgado com campos separados por ";"
- Exemplo: "ADPF 1.005, 1.006 e 1.097" julgados juntos →
  {{
    "classe_processo": "ADPF;ADPF;ADPF",
    "numero_processo": "1005;1006;1097",
    "incidente_julgamento": "6468508; 6468597; 6792100"
  }}
- O RESUMO é compartilhado (UM ÚNICO resumo para todos os processos da decisão conjunta)
- SE há informações diferentes por processo, use FOOTNOTES no resumo

CRITÉRIOS DE EXCLUSÃO:
✗ Números de processo citados apenas como precedentes/referências dentro outro resumo
✗ Entradas com dados incompletos ou fragmentados
✗ Resumos que são apenas dados processuais (datas, relatores, links)
✗ Processos que aparecem em listas como "ADI 7.490" mencionadas comparativamente

CAMPOS ADICIONAIS (preencer se disponível, senão null):
- uf: estado (ex: "SP", "GO", "DF"). Se múltiplos: "SP;MG;DF"
- ramo_direito: área jurídica (ex: "DIREITO CONSTITUCIONAL")
- materia: tema específico do caso
- relator: nome do Ministro relator (pode ser um para decisão conjunta)
- legislacao: leis/artigos mencionados
- ods_onu2030: objetivos ONU (ex: "1, 2, 5")
- data_julgamento: data do julgamento (em formato YYYY-MM-DD)
- observacao: qualquer observação relevante
- incidente_julgamento: números de incidente do STF (se múltiplos: separar com ";")
- situacao_julgamento: estado do julgamento (finalizado, etc)
- redator_acordao: nome do ministro redator, se diferente do relator

RETORNE JSON COM ESTRUTURA:
{{
  "julgados": [
    {{
      "classe_processo": "string (obrigatório, pode ter ;)",
      "numero_processo": "string (obrigatório, pode ter ;)",
      "uf": "string ou null (pode ter ;)",
      "titulo": "string (obrigatório)",
      "resumo": "string (obrigatório, mínimo 50 chars)",
      "ramo_direito": "string ou null",
      "materia": "string ou null",
      "relator": "string ou null",
      "legislacao": "string ou null",
      "ods_onu2030": "string ou null",
      "data_julgamento": "string ou null (YYYY-MM-DD format)",
      "observacao": "string ou null",
      "incidente_julgamento": "string ou null (pode ter ;)",
      "situacao_julgamento": "string ou null",
      "redator_acordao": "string ou null"
    }}
  ]
}}

TEXTO:
{text}"""


class LLMProcessor:
    """Processa chunks de texto usando LLM para extrair julgados."""

    def __init__(self, client: OllamaClient):
        """
        Args:
            client: instância do OllamaClient
        """
        self.client = client

    def process_chunk(self, chunk: str) -> List[Dict[str, Any]]:
        """
        Processa um chunk de texto e extrai julgados via LLM.

        Args:
            chunk: texto para processar

        Returns:
            Lista de dicts com dados de julgados extraídos
        """
        if not chunk or len(chunk.strip()) < 100:
            return []

        prompt = JULGADO_EXTRACTION_PROMPT.format(text=chunk)

        try:
            response = self.client.generate_json(
                prompt=prompt,
                system=SYSTEM_PROMPT,
            )

            data = response["data"]
            julgados = data.get("julgados", [])

            # Filtra julgados vazios
            julgados = [j for j in julgados if self._is_julgado_candidate(j)]

            return julgados

        except ValueError as e:
            print(f"⚠️ Erro ao extrair JSON do chunk: {str(e)}")
            return []
        except Exception as e:
            print(f"❌ Erro ao processar chunk: {str(e)}")
            return []

    def _is_julgado_candidate(self, data: Dict[str, Any]) -> bool:
        """
        Verifica se dict tem pelo menos os campos mínimos para ser um julgado.

        Args:
            data: dict com dados

        Returns:
            True se parece ser um julgado legítimo
        """
        # Precisa ter classe ou número ou título
        has_classe = data.get("classe_processo") and str(data.get("classe_processo")).strip()
        has_numero = data.get("numero_processo") and str(data.get("numero_processo")).strip()
        has_titulo = data.get("titulo") and str(data.get("titulo")).strip()

        return has_classe or has_numero or has_titulo

    def convert_to_julgado(self, data: Dict[str, Any]) -> Julgado:
        """
        Converte dict da LLM para modelo Pydantic Julgado.

        Args:
            data: dados extraídos pela LLM

        Returns:
            Instância de Julgado
        """
        julgado = Julgado(
            classe_processo=data.get("classe_processo"),
            numero_processo=data.get("numero_processo"),
            incidente_julgamento=data.get("incidente_julgamento"),
            uf=data.get("uf"),
            ramo_direito=data.get("ramo_direito"),
            materia=data.get("materia"),
            titulo=data.get("titulo"),
            resumo=data.get("resumo"),
            relator=data.get("relator"),
            legislacao=data.get("legislacao"),
            ods_onu2030=data.get("ods_onu2030"),
            data_julgamento=data.get("data_julgamento"),
            observacao=data.get("observacao"),
            noticia_completa=data.get("noticia_completa"),
            situacao_julgamento=data.get("situacao_julgamento"),
            redator_acordao=data.get("redator_acordao"),
            type="STF",
            status="APROVADO",
            is_extraordinary=False,
            grau_incidencia="PENDENTE",
            metadata={},
            comments={},
        )
        return julgado
