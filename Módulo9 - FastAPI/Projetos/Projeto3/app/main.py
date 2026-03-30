from fastapi import FastAPI
from app.db import create_db_and_tables
from app.routers.pessoas import router as pessoas_router

app = FastAPI(title='Projeto3 - Pessoas com Banco')
app.include_router(pessoas_router)

@app.on_event('startup')
def startup() -> None:
    create_db_and_tables()

@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}
