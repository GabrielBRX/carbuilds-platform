from pydantic import BaseModel, ConfigDict
from app.schemas.marca_schema import MarcaSimple

class CarroCreate(BaseModel):
    marca_id: int
    modelo: str
    geracao: str
    ano_inicio: int
    ano_fim: int


class CarroResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    marca_id: int
    modelo: str
    geracao: str
    ano_inicio: int
    ano_fim: int

class CarroResponseComplete(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    modelo: str
    geracao: str
    ano_inicio: int
    ano_fim: int

    marca: MarcaSimple
