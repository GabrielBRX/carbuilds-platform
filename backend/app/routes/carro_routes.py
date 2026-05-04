from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.carro import Carro
from app.models.marca import Marca
from app.schemas.carro_schema import CarroCreate, CarroResponse

router = APIRouter(prefix="/carros", tags=["carros"])

@router.post("/", response_model=CarroResponse)
def criar_carro(payload: CarroCreate, db: Session = Depends(get_db)):
    marca = db.query(Marca).filter(Marca.id == payload.marca_id).first()
    if not marca:
        raise HTTPException(status_code=404, detail="Marca não encontrada")

    carro = Carro(
        marca_id=payload.marca_id,
        modelo=payload.modelo,
        geracao=payload.geracao,
        ano_inicio=payload.ano_inicio,
        ano_fim=payload.ano_fim,
    )

    db.add(carro)
    db.commit()
    db.refresh(carro)

    return carro

@router.get("/", response_model=list[CarroResponse])
def listar_carros(db: Session = Depends(get_db)):
    
    return db.query(Carro).all()
