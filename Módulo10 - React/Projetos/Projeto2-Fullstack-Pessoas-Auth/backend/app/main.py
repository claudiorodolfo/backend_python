from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, pessoas

app = FastAPI(title="Projeto2 — Pessoas + Auth")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(pessoas.router, prefix="/pessoas", tags=["pessoas"])


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
