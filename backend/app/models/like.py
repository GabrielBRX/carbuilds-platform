from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)

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