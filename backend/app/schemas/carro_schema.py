from pydantic import BaseModel, ConfigDict


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
