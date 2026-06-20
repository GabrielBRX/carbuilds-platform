from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class Build(Base):
    __tablename__ = "builds"

    id = Column(Integer, primary_key=True, index=True)

    slug = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    titulo = Column(String, nullable=False)

    descricao = Column(Text, nullable=True)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    carro_id = Column(
        Integer,
        ForeignKey("carros.id"),
        nullable=False
    )

    data_criacao = Column(
        DateTime,
        default=datetime.utcnow
    )

    usuario = relationship("Usuario")

    carro = relationship("Carro")

    imagens = relationship(
        "Imagem",
        back_populates="build",
        cascade="all, delete",
        order_by="Imagem.ordem"
    )

    likes = relationship(
        "Like",
        back_populates="build",
        cascade="all, delete"
    )

    comentarios = relationship(
        "Comentario",
        back_populates="build",
        cascade="all, delete"
    )