from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class Imagem(Base):
    __tablename__ = "imagens"

    id = Column(Integer, primary_key=True, index=True)

    url = Column(String, nullable=False)

    ordem = Column(Integer, default=0)

    principal = Column(Boolean, default=False)

    build_id = Column(
        Integer,
        ForeignKey("builds.id"),
        nullable=False
    )

    build = relationship(
        "Build",
        back_populates="imagens"
    )