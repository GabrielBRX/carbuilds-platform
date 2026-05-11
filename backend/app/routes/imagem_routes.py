import os
import shutil

from uuid import uuid4

from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.imagem import Imagem
from app.models.build import Build

from app.schemas.imagem_schema import ImagemResponde

router = APIRouter(
    prefix="/imagens",
    tags=["imagens"]
)


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


ALLOWED_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
    "webp"
}


MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


@router.post(
    "/{build_id}",
    response_model=ImagemResponse,
    status_code=status.HTTP_201_CREATED
)
def upload_imagem(
    build_id: int,
    arquivo: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    build = db.query(Build).filter(
        Build.id == build_id
    ).first()

    if not build:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Build não encontrada."
        )

    # 🔒 limite máximo de imagens
    total_imagens = db.query(Imagem).filter(
        Imagem.build_id == build_id
    ).count()

    if total_imagens >= 25:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Limite máximo de 25 imagens atingido."
        )

    # 🔒 valida extensão
    extensao = arquivo.filename.split(".")[-1].lower()

    if extensao not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Formato de imagem inválido."
        )

    # 🔒 valida tamanho
    conteudo = arquivo.file.read()

    if len(conteudo) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Imagem muito grande. Máximo permitido: 10MB."
        )

    arquivo.file.seek(0)

    nome_arquivo = f"{uuid4()}.{extensao}"

    caminho_arquivo = os.path.join(
        UPLOAD_DIR,
        nome_arquivo
    )

    with open(caminho_arquivo, "wb") as buffer:
        shutil.copyfileobj(arquivo.file, buffer)

    imagem = Imagem(
        url=f"/uploads/{nome_arquivo}",
        build_id=build.id
    )

    db.add(imagem)
    db.commit()
    db.refresh(imagem)

    return imagem
