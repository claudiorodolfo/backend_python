# Nível 6 - API REST com Django REST Framework

Este nível adiciona uma API REST completa usando Django REST Framework.

## 📦 Dependências

```bash
pip install djangorestframework
```

## 🎯 Funcionalidades

- API REST completa
- Serializers para o modelo Pessoa
- ViewSets ou APIViews
- Documentação automática (Swagger/OpenAPI)
- Autenticação de API

## 📝 Implementação

1. Adicionar `rest_framework` em `INSTALLED_APPS`
2. Criar `pessoas/serializers.py`
3. Criar `pessoas/views_api.py`
4. Configurar URLs da API
5. Adicionar autenticação (opcional)

## 🔗 Endpoints da API

- `GET /api/pessoas/` - Listar pessoas
- `POST /api/pessoas/` - Criar pessoa
- `GET /api/pessoas/<id>/` - Detalhes
- `PUT /api/pessoas/<id>/` - Atualizar
- `DELETE /api/pessoas/<id>/` - Excluir
