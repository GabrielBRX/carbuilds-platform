from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    pais = Column(String, nullable=False)

    carros = relationship(
        "Carro",
        back_populates="marca",
        cascade="all, delete"
    )