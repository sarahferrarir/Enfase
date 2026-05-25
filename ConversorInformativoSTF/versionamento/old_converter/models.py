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
