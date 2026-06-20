from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from app.schemas.carro_schema import CarroResponseComplete
from app.schemas.imagem_schema import ImagemResponse


class BuildCreate(BaseModel):
    slug: str
    titulo: str
    descricao: Optional[str] = None
    carro_id: int


class BuildResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    titulo: str
    descricao: Optional[str]
    usuario_id: int
    carro_id: int
    data_criacao: datetime

    likes_count: int = 0
    comentarios_count: int = 0


class BuildResponseComplete(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    slug: str
    titulo: str
    descricao: str | None
    data_criacao: datetime

    carro: CarroResponseComplete
    imagens: list[ImagemResponse]

    likes_count: int = 0
    comentarios_count: int = 0