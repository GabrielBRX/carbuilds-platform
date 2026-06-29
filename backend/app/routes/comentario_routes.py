from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.database.database import get_db

from app.models.comentario import Comentario
from app.models.build import Build
from app.models.usuario import Usuario

from app.schemas.comentario_schema import (
    ComentarioCreate,
    ComentarioResponse
)

from app.core.deps import get_current_user


router = APIRouter(
    prefix="/comentarios",
    tags=["comentarios"]
)

@router.post(
    "/{build_id}",
    response_model=ComentarioResponse,
    status_code=status.HTTP_201_CREATED
)
def criar_comentario(
    build_id: int,
    payload: ComentarioCreate,
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

    comentario = Comentario(
        conteudo=payload.conteudo,
        usuario_id=usuario.id,
        build_id=build_id
    )

    db.add(comentario)
    db.commit()
    db.refresh(comentario)

    return comentario


@router.get(
    "/build/{build_id}",
    response_model=list[ComentarioResponse]
)
def listar_comentarios_build(
    build_id: int,
    db: Session = Depends(get_db)
):

    comentarios = (
        db.query(Comentario)
        .options(
            joinedload(Comentario.usuario)
        )
        .filter(Comentario.build_id == build_id)
        .order_by(Comentario.id.desc())
        .all()
    )

    return comentarios


@router.delete(
    "/{comentario_id}",
    status_code=status.HTTP_200_OK
)
def deletar_comentario(
    comentario_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):

    comentario = db.query(Comentario).filter(
        Comentario.id == comentario_id
    ).first()

    if not comentario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comentário não encontrado."
        )

    if comentario.usuario_id != usuario.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para deletar este comentário."
        )

    db.delete(comentario)
    db.commit()

    return {
        "message": "Comentário deletado com sucesso."
    }