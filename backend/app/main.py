from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.database.database import Base, engine

from app.routes import (
    auth_routes,
    marca_routes,
    carro_routes,
    build_routes,
    imagem_routes,
    usuario_routes
)

# cria tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BuildHub API",
    version="1.0.0"
)

# rotas
app.include_router(auth_routes.router)
app.include_router(marca_routes.router)
app.include_router(carro_routes.router)
app.include_router(build_routes.router)
app.include_router(imagem_routes.router)
app.include_router(usuario_routes.router)
# uploads
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)