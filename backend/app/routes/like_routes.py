from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.like import Like
from app.models.build import Build
from app.models.usuario import Usuario

from app.core.deps import get_current_user


router = APIRouter(
    prefix="/likes",
    tags=["likes"]
)

@router.post(
    "/{build_id}",
    status_code=status.HTTP_201_CREATED
)

def like_build(
    build_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):

    build = db.query(Build).filter(
        Build.id == build_id
    ).first()

    if not build:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Build não encontrada."
        )
    
    existing_like = db.query(Like).filter(
        Like.usuario_id == usuario.id,
        Like.build_id == build_id
    ).first()
    

    if existing_like:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você já curtiu esta build."
        )
    
    like = Like(
        usuario_id=usuario.id,
        build_id=build_id

    )

    db.add(like)
    db.commit()

    return {
        "message": "Build curtida com sucesso."
    }
    
