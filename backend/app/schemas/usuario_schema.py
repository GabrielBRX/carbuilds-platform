from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str = Field(min_length=8)


class UsuarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    data_criacao: datetime


class UsuarioLogin(BaseModel):
    email: EmailStr
    senha: str
