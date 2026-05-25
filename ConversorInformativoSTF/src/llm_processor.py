import json
from typing import List, Optional, Dict, Any
from .ollama_client import OllamaClient
from .schemas import Julgado


SYSTEM_PROMPT = """Você é um especialista em jurisprudência do STF (Superior Tribunal Federal).
Sua tarefa é identificar e extrair julgados do texto fornecido.

Regras importantes:
- Retorne APENAS JSON válido
- NÃO invente dados
- NÃO resuma campos, preserve o texto original
- Um julgado típico tem: classe (ADI, RE, etc), número, título, resumo
- Se algum campo estiver ausente, use null
- Sempre validate o JSON antes de retornar"""


JULGADO_EXTRACTION_PROMPT = """Analise o seguinte texto de um informativo do STF e identifique TODOS os julgados presentes.

Para cada julgado encontrado, extraia (se disponível):
- classe_processo: ADI, ADPF, RE, ARE, HC, MS, Rcl, ACO, etc
- numero_processo: número completo do processo
- uf: estado da unidade de origem
- ramo_direito: DIREITO CONSTITUCIONAL, DIREITO CIVIL, etc
- materia: tema específico
- titulo: título do julgado (geralmente em negrito ou itálico)
- resumo: resumo executivo da decisão
- relator: nome do relator
- legislacao: leis, artigos ou normas mencionadas
- ods_onu2030: objetivos de desenvolvimento sustentável (números)
- data_julgamento: data do julgamento se informada
- observacao: qualquer observação relevante

Retorne um JSON com a seguinte estrutura:
{{
  "julgados": [
    {{
      "classe_processo": "string ou null",
      "numero_processo": "string ou null",
      "uf": "string ou null",
      "ramo_direito": "string ou null",
      "materia": "string ou null",
      "titulo": "string ou null",
      "resumo": "string ou null",
      "relator": "string ou null",
      "legislacao": "string ou null",
      "ods_onu2030": "string ou null",
      "data_julgamento": "string ou null",
      "observacao": "string ou null"
    }}
  ]
}}

Aqui está o texto:

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
            type="STF",
            status="APROVADO",
            is_extraordinary=False,
            grau_incidencia="PENDENTE",
            metadata={},
            comments={},
        )
        return julgado
