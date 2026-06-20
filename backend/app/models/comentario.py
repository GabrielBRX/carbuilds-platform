from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Comentario(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True)

    conteudo = Column(Text, nullable=False)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    build_id = Column(
        Integer,
        ForeignKey("builds.id"),
        nullable=False
    )

    data_criacao = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    build = relationship(
        "Build",
        back_populates="comentarios"
    )