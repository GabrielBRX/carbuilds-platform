from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    senha_hash = Column(String)
    data_criacao = Column(DateTime, default=datetime.utcnow)