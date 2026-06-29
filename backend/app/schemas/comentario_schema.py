from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.usuario_schema import UsuarioResponse


class ComentarioCreate(BaseModel):
    conteudo: str


class ComentarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    conteudo: str
    data_criacao: datetime

    usuario: UsuarioResponse