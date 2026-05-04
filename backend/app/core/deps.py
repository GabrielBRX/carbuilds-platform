from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.core.jwt import verificar_token
from app.models.usuario import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    
    email = verificar_token(token)

    if email is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    usuario = db.query(Usuario).filter(Usuario.email == email).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return usuario