from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.database.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.utils.security import hash_senha

from app.schemas.usuario_schema import UsuarioLogin
from app.utils.security import verificar_senha
from app.core.jwt import criar_token

from app.core.deps import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UsuarioResponse)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email já registrado")

    senha_hash = hash_senha(usuario.senha)

    novo_usuario = Usuario(
        email=usuario.email,
        senha_hash=senha_hash
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    usuario = db.query(Usuario).filter(
        Usuario.email == form_data.username
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )

    if not verificar_senha(
        form_data.password,
        usuario.senha_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha inválida"
        )

    token = criar_token({"sub": usuario.email})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def perfil(usuario = Depends(get_current_user)):

    return {
        "id": usuario.id,
        "email": usuario.email,
        "criado_em": usuario.data_criacao
    }