from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.database import Base, engine
from app.models.like import Like
from app.models.comentario import Comentario

from app.routes import (
    auth_routes,
    marca_routes,
    carro_routes,
    build_routes,
    imagem_routes,
    usuario_routes,
    like_routes,
    comentario_routes
)


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BuildHub API",
    version="1.0.0"
)


app.include_router(auth_routes.router)
app.include_router(marca_routes.router)
app.include_router(carro_routes.router)
app.include_router(build_routes.router)
app.include_router(imagem_routes.router)
app.include_router(usuario_routes.router)
app.include_router(like_routes.router)
app.include_router(comentario_routes.router)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)