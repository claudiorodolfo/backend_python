"""
04 - Deploy com Docker e Uvicorn
================================

Em produção, a aplicação ASGI é servida por um processo como Uvicorn ou
Hypercorn; muitas vezes atrás de um proxy reverso (Nginx, Traefik, etc.).

Imagem Python mínima (exemplo de Dockerfile — salve como `Dockerfile` no projeto):

```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build e execução:

```bash
docker build -t minha-api .
docker run -p 8000:8000 minha-api
```

Docker Compose (resumo):

- Serviço `api` com variáveis de ambiente (`DATABASE_URL`, `SECRET_KEY`).
- Serviço `db` (PostgreSQL) na mesma rede.
- Volume para dados do banco.

Referência: veja `Projetos/Projeto3/docker-compose.yml` (ou Projeto4/5) neste repositório.

Checklist de produção:

- `DEBUG` desligado; logs estruturados.
- HTTPS no proxy ou no provedor (load balancer).
- Limites de taxa e timeouts no proxy.
- Backups do banco e migrações documentadas.
"""
