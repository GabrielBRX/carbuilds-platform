from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload

from app.database.database import get_db

from app.models.favorito import Favorito
from app.models.build import Build
from app.models.usuario import Usuario

from app.schemas.favorito_schema import FavoritoResponse

from app.core.deps import get_current_user


router = APIRouter(
    prefix="/favoritos",
    tags=["favoritos"]
)


@router.post(
    "/{build_id}",
    status_code=status.HTTP_201_CREATED
)
def favoritar_build(
    build_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):

    build = db.query(Build).filter(Build.id == build_id).first()

    if not build:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Build não encontrada."
        )

    favorito_existente = (
        db.query(Favorito)
        .filter(
            Favorito.usuario_id == usuario.id,
            Favorito.build_id == build_id
        )
        .first()
    )

    if favorito_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Esta build já está nos favoritos."
        )

    favorito = Favorito(
        usuario_id=usuario.id,
        build_id=build_id
    )

    db.add(favorito)
    db.commit()

    return {
        "message": "Build adicionada aos favoritos."
    }


@router.delete("/{build_id}")
def remover_favorito(
    build_id: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):

    favorito = (
        db.query(Favorito)
        .filter(
            Favorito.usuario_id == usuario.id,
            Favorito.build_id == build_id
        )
        .first()
    )

    if not favorito:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Favorito não encontrado."
        )

    db.delete(favorito)
    db.commit()

    return {
        "message": "Favorito removido com sucesso."
    }


@router.get(
    "/",
    response_model=list[FavoritoResponse]
)
def listar_favoritos(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):

    favoritos = (
        db.query(Favorito)
        .options(
            joinedload(Favorito.build)
            .joinedload(Build.carro)
        )
        .options(
            joinedload(Favorito.build)
            .joinedload(Build.imagens)
        )
        .filter(Favorito.usuario_id == usuario.id)
        .order_by(Favorito.id.desc())
        .all()
    )

    return favoritos