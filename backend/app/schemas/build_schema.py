from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


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