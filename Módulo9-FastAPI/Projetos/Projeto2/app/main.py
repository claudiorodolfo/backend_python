from fastapi import FastAPI
from .routers.pessoas import router as pessoas_router

app = FastAPI(title='Projeto2 - Pessoas com Filtros')
app.include_router(pessoas_router)

@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}
