from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict

from app.schemas.build_schema import BuildResponseComplete


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

class UsuarioPublicResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    data_criacao: datetime

class UsuarioProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    data_criacao: datetime
    builds: list[BuildResponseComplete]
