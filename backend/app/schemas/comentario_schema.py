from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ComentarioCreate(BaseModel):
    conteudo: str


class ComentarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    conteudo: str
    usuario_id: int
    build_id: int
    data_criacao: datetime