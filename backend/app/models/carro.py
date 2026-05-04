from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, nullable=False)
    geracao = Column(String, nullable=False)
    ano_inicio = Column(Integer, nullable=False)
    ano_fim = Column(Integer, nullable=True)

    marca_id = Column(Integer, ForeignKey("marcas.id"), nullable=False)

    marca = relationship("Marca", back_populates="carros")