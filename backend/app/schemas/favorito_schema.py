from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.build_schema import BuildResponseComplete


class FavoritoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    data_criacao: datetime
    build: BuildResponseComplete