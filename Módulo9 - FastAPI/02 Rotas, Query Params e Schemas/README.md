# 02 - Rotas, Query Params e Schemas

## Objetivo

Aprender a validar dados de entrada e saída usando tipagem e Pydantic.

## Conteúdo

- `path params`, `query params` e `request body`.
- Schemas com Pydantic.
- `response_model` para padronização de retorno.
- Erros com `HTTPException`.

## Arquivos

- `01_path_e_query.py` — combinação de path e query com validação.
- `02_schemas_pydantic.py` — modelos de entrada (`POST`) e corpo JSON.
- `03_response_model.py` — contrato de saída e omissão de campos sensíveis.
- `04_http_exception.py` — status codes e `detail` padronizado.

## Resultado esperado

Uma API com contratos claros de entrada/saída e mensagens de erro consistentes.

## Execução

```bash
pip install fastapi uvicorn
uvicorn 02_schemas_pydantic:app --reload
```

(Use o nome do arquivo desejado no lugar de `02_schemas_pydantic`.)
