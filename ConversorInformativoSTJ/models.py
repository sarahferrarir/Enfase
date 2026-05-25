from pydantic import BaseModel, Field, field_validator
from typing import Optional

class JulgadoItem(BaseModel):
    processo: Optional[str] = None
    ramo_direito: Optional[str] = None
    tema: Optional[str] = None
    destaque: Optional[str] = None
    informacoes_inteiro_teor: Optional[str] = None
    relator: Optional[str] = None
    orgao_julgador: Optional[str] = None
    data_julgamento: Optional[str] = None
    legislacao_aplicada: list[str] = Field(default_factory=list)

    @field_validator('destaque', 'tema', 'informacoes_inteiro_teor', 'processo', 'relator', mode='before')
    @classmethod
    def converter_lista_para_string(cls, v):
        """Converte arrays em strings (concatena com quebra de linha)."""
        if isinstance(v, list):
            return '\n'.join(str(item) for item in v) if v else None
        return v

    @field_validator('legislacao_aplicada', mode='before')
    @classmethod
    def garantir_lista(cls, v):
        """Garante que legislacao_aplicada é sempre uma lista."""
        if isinstance(v, str):
            return [v]
        if v is None:
            return []
        return v if isinstance(v, list) else []


class InformativoResponse(BaseModel):
    numero_informativo: Optional[str] = None
    data_publicacao: Optional[str] = None
    julgados: list[JulgadoItem] = Field(default_factory=list)

