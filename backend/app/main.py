from fastapi import FastAPI

from app.database.database import engine, Base
from app.routes.auth_routes import router as auth_router
from app.routes.build_routes import router as build_router
from app.routes.marca_routes import router as marca_routes
from app.routes.carro_routes import router as carro_router
from app.routes import imagem_routes

from fastapi.staticfiles import StaticFiles

from app.models.usuario import Usuario
from app.models.marca import Marca
from app.models.carro import Carro
from app.models.build import Build
from app.models.imagem import Imagem

app = FastAPI()

app.include_router(imagem_routes.router)
app.include_router(marca_routes)
app.include_router(carro_router)
app.include_router(auth_router)
app.include_router(build_router)
Base.metadata.create_all(bind=engine)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.get("/")
def home():
    return {"message": "Car Builds API running"}
