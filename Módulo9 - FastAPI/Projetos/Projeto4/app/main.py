from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routers.categorias import router as categorias_router
from app.routers.produtos import router as produtos_router

app = FastAPI(title='Projeto4 - Catálogo')
app.include_router(categorias_router)
app.include_router(produtos_router)

@app.on_event('startup')
def startup() -> None:
    create_db_and_tables()

@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}
