# 04 - Testes, Segurança e Deploy

## Objetivo

Garantir qualidade e preparar a API para produção.

## Conteúdo

- Testes de endpoints com `pytest`.
- CORS e variáveis de ambiente.
- Introdução a autenticação JWT.
- Deploy com Docker e servidor ASGI.

## Arquivos

- `01_pytest_e_testclient.py` — `TestClient` e uso típico nos projetos.
- `02_cors_e_configuracao.py` — `CORSMiddleware` e boas práticas.
- `03_autenticacao_jwt_visao_geral.py` — conceitos e links para o tutorial oficial.
- `04_deploy_docker_uvicorn.py` — Dockerfile resumido e checklist de produção.
- `tests/test_exemplo_cliente.py` — exemplo executável com `pytest`.

## Resultado esperado

Projeto pronto para validação contínua e publicação.

## Testes nesta pasta

```bash
pip install fastapi pytest httpx
pytest -q
```
