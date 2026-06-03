from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any


class Paragraph(BaseModel):
    """Paragrafo extraido do DOCX mantendo metadados minimos."""

    index: int
    text: str
    style: str | None = None


class InformativoMetadata(BaseModel):
    numero_informativo: str | None = None
    ano_informativo: str | None = None
    data_informativo: str | None = None
    type: str = "STF"


class EditorialItem(BaseModel):
    paragraphs: list[Paragraph] = Field(default_factory=list)

    @property
    def text(self) -> str:
        return "\n".join(p.text for p in self.paragraphs if p.text.strip())


class JulgadoSTF(BaseModel):
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
    orgao_julgador: str | None = "PLENARIO"
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
    status: str | None = "APROVADO"
    type: str | None = "STF"
    classificacao: str | None = None
    comentario: str | None = None
    comments: dict[str, Any] = Field(default_factory=dict)
    conteudo_fixacao: str | None = None
    grau_incidencia: str | None = "PENDENTE"
    html: str | None = None
    is_extraordinary: bool = False
    metadata: dict[str, Any] = Field(default_factory=dict)
    modified_by_users: list[str] | None = None
    new_classificacao: str | None = None
    questao: str | None = None
    tema_julgado: str | None = None


class InformativoOutput(BaseModel):
    julgado_stf: list[JulgadoSTF] = Field(default_factory=list)

