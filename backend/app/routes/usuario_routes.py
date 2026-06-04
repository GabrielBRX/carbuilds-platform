from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.database.database import get_db
from app.models.usuario import Usuario
from app.models.build import Build
from app.models.carro import Carro

from app.schemas.usuario_schema import UsuarioProfileResponse


router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.get(
    "/{usuario_id}/perfil",
    response_model=UsuarioProfileResponse
)
def get_usuario_profile(
        usuario_id: int,
        db: Session = Depends(get_db)
):
    
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario não encontrado."
        )
    
    builds = (
        db.query(Build)
        .options(
            joinedload(Build.carro).joinedload(Carro.marca),
            joinedload(Build.imagens)
        )
        .filter(Build.usuario_id == usuario_id)
        .order_by(Build.id.desc())
        .all()
    )

    usuario.builds = builds

    return usuario