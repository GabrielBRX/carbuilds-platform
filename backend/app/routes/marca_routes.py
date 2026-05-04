from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.marca import Marca
from app.schemas.marca_schema import MarcaCreate, MarcaResponse

router = APIRouter(prefix="/marcas", tags=["marcas"])

@router.post("/", response_model=MarcaResponse)
def criar_marca(payload: MarcaCreate, db: Session = Depends(get_db)):

    # 🔒 verifica duplicidade
    marca_existente = db.query(Marca).filter(Marca.nome == payload.nome).first()

    if marca_existente:
        raise HTTPException(status_code=400, detail="Marca já existe")

    marca = Marca(
        nome=payload.nome,
        pais=payload.pais
    )

    db.add(marca)
    db.commit()
    db.refresh(marca)

    return marca


@router.get("/", response_model=list[MarcaResponse])
def listar_marcas(db: Session = Depends(get_db)):
    return db.query(Marca).all()