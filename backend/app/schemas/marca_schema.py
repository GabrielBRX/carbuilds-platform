from pydantic import BaseModel, ConfigDict

class MarcaCreate(BaseModel):
    nome: str
    pais: str

class MarcaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str
    pais: str

class MarcaSimple(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome: str