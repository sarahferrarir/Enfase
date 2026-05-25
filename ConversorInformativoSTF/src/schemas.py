from pydantic import BaseModel, ConfigDict, Field
from typing import List, Dict, Any, Optional
from datetime import datetime


class Julgado(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    id: Optional[str] = None
    created_at: Optional[str] = None
    informativo: Optional[str] = None
    classe_processo: Optional[str] = None
    numero_processo: Optional[str] = None
    incidente_julgamento: Optional[str] = None
    uf: Optional[str] = None
    observacao: Optional[str] = None
    data_julgamento: Optional[str] = None
    relator: Optional[str] = None
    redator_acordao: Optional[str] = None
    orgao_julgador: Optional[str] = None
    tipo_julgamento: Optional[str] = None
    situacao_julgamento: Optional[str] = None
    titulo: Optional[str] = None
    tese_julgado: Optional[str] = None
    resumo: Optional[str] = None
    noticia: Optional[str] = None
    ramo_direito: Optional[str] = None
    materia: Optional[str] = None
    repercussao_geral: Optional[str] = None
    tema_rg: Optional[str] = None
    legislacao: Optional[str] = None
    ods_onu2030: Optional[str] = None
    covid19: Optional[str] = None
    noticia_completa: Optional[str] = None
    data_informativo: Optional[str] = None
    status: Optional[str] = Field(default="APROVADO")
    type: Optional[str] = Field(default="STF")
    classificacao: Optional[str] = None
    comentario: Optional[str] = None
    comments: Optional[Dict[str, Any]] = None
    conteudo_fixacao: Optional[str] = None
    grau_incidencia: Optional[str] = Field(default="PENDENTE")
    html: Optional[str] = None
    is_extraordinary: bool = False
    metadata: Optional[Dict[str, Any]] = None
    modified_by_users: Optional[List[str]] = None
    new_classificacao: Optional[str] = None
    questao: Optional[str] = None
    tema_julgado: Optional[str] = None


class Informativo(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True)

    numero_informativo: Optional[str] = None
    ano_informativo: Optional[str] = None
    data_publicacao: Optional[str] = None
    julgados: List[Julgado] = Field(default_factory=list)


class LLMResponse(BaseModel):
    julgados: List[Julgado]
