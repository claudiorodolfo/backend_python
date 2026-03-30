"""
01 - Instalação e ambientação do FastAPI
========================================

Este arquivo descreve como preparar o ambiente para desenvolvimento com FastAPI.
"""

# ============================================================================
# AMBIENTE VIRTUAL
# ============================================================================

# python -m venv .venv
# source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate      # Windows

# ============================================================================
# INSTALAÇÃO DAS DEPENDÊNCIAS PRINCIPAIS
# ============================================================================

# pip install fastapi uvicorn[standard]

# ============================================================================
# VERIFICAR VERSÕES
# ============================================================================

# python -c "import fastapi; print(fastapi.__version__)"
# uvicorn --version

# ============================================================================
# O QUE É FASTAPI (RESUMO)
# ============================================================================

"""
FastAPI é um framework para construir APIs web (REST) com Python.

- Baseado em padrões abertos (OpenAPI e JSON Schema).
- Tipagem com anotações Python: validação automática com Pydantic.
- Gera documentação interativa (Swagger UI) e ReDoc.
- Servidor ASGI típico: Uvicorn (também funciona com Hypercorn, Daphne, etc.).

Diferença em relação a Django (visão geral):
- Django: framework completo (templates, admin, ORM, etc.) — frequentemente usado
  com sites admin e aplicações web tradicionais.
- FastAPI: foco em APIs modernas de alto desempenho e contratos tipados.

Referência oficial: https://fastapi.tiangolo.com/
"""

# ============================================================================
# ESTRUTURA MÍNIMA SUGERIDA PARA ESTUDAR
# ============================================================================

"""
projeto/
├── main.py           # app = FastAPI() e rotas
├── requirements.txt
└── .venv/
"""
