from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.database.database import get_db

from app.models.build import Build
from app.models.usuario import Usuario
from app.models.carro import Carro

from app.schemas.build_schema import (
    BuildCreate,
    BuildResponse,
    BuildResponseComplete
)

from app.core.deps import get_current_user


router = APIRouter(prefix="/builds", tags=["builds"])


@router.get("/", response_model=list[BuildResponseComplete])
def list_builds(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    builds = (
        db.query(Build)
        .options(
            joinedload(Build.carro).joinedload(Carro.marca),
            joinedload(Build.imagens),
            joinedload(Build.likes)
        )
        .order_by(Build.id.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

    for build in builds:
        build.likes_count = len(build.likes)

    return builds


@router.post(
    "/",
    response_model=BuildResponse,
    status_code=status.HTTP_201_CREATED
)
def create_build(
    payload: BuildCreate,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
):

    existing_build = db.query(Build).filter(
        Build.slug == payload.slug
    ).first()

    if existing_build:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A build with this slug already exists.",
        )

    carro = db.query(Carro).filter(
        Carro.id == payload.carro_id
    ).first()

    if not carro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Carro não encontrado."
        )

    build = Build(
        slug=payload.slug.strip().lower(),
        titulo=payload.titulo.strip(),
        descricao=payload.descricao,
        usuario_id=usuario.id,
        carro_id=payload.carro_id
    )

    db.add(build)
    db.commit()
    db.refresh(build)

    build.likes_count = 0

    return build


@router.get(
    "/marca/{marca_nome}",
    response_model=list[BuildResponseComplete]
)
def get_builds_by_marca(
    marca_nome: str,
    db: Session = Depends(get_db)
):

    builds = (
        db.query(Build)
        .join(Build.carro)
        .join(Carro.marca)
        .options(
            joinedload(Build.carro).joinedload(Carro.marca),
            joinedload(Build.imagens),
            joinedload(Build.likes)
        )
        .filter(Carro.marca.has(nome=marca_nome.capitalize()))
        .all()
    )

    for build in builds:
        build.likes_count = len(build.likes)

    return builds


@router.get("/{slug}", response_model=BuildResponseComplete)
def get_build(slug: str, db: Session = Depends(get_db)):

    build = (
        db.query(Build)
        .options(
            joinedload(Build.carro).joinedload(Carro.marca),
            joinedload(Build.imagens),
            joinedload(Build.likes)
        )
        .filter(Build.slug == slug)
        .first()
    )

    if not build:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Build not found."
        )

    build.likes_count = len(build.likes)

    return build