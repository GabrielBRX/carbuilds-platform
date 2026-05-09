from pydantic import BaseModel, ConfigDict


class ImagemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    url: str
    principal: bool
    ordem: int