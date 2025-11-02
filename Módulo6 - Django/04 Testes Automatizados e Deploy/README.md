# 04 - Testes Automatizados e Deploy

Este módulo aborda a importância dos testes, frameworks de teste (incluindo Pytest), e como preparar e fazer deploy de aplicações Django em produção.

## 📚 Conteúdo

1. **Importância dos Testes**
2. **Testes Unitários, de Integração e Funcionais**
3. **Frameworks de Teste no Django (Pytest)**
4. **Criar Testes Simples**
5. **Executar Testes e Interpretar Resultados**
6. **Preparação para Produção**
7. **Configuração de Servidor (Gunicorn, Nginx)**
8. **Plataformas de Deploy Gratuito (Heroku, Render)**

## 🎯 Objetivos de Aprendizado

Ao final desta unidade, você será capaz de:
- Escrever testes automatizados para aplicações Django
- Usar Pytest para testes mais avançados
- Preparar aplicações Django para produção
- Configurar servidores com Gunicorn e Nginx
- Fazer deploy em plataformas gratuitas como Heroku e Render
- Interpretar resultados de testes e logs

## 📁 Arquivos

- `01_testes_django.py` - Framework de testes do Django
- `02_pytest.py` - Testes com Pytest
- `03_preparacao_producao.py` - Configurações para produção
- `04_gunicorn_nginx.py` - Configuração de servidores
- `05_deploy_heroku_render.py` - Deploy em plataformas gratuitas

## 🧪 Testes no Django

### Teste Básico

```python
from django.test import TestCase
from .models import Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome='Teste',
            preco=100.00
        )
    
    def test_produto_criacao(self):
        self.assertEqual(self.produto.nome, 'Teste')
```

### Teste de View

```python
from django.test import Client
from django.urls import reverse

def test_lista_produtos(self):
    client = Client()
    response = client.get(reverse('produtos:lista'))
    self.assertEqual(response.status_code, 200)
```

### Teste com Autenticação

```python
def setUp(self):
    self.client = Client()
    self.user = User.objects.create_user(
        username='test',
        password='pass123'
    )
    self.client.login(username='test', password='pass123')
```

### Executar Testes

```bash
# Todos os testes
python manage.py test

# App específico
python manage.py test produtos

# Teste específico
python manage.py test produtos.tests.ProdutoTestCase.test_criar_produto
```

## 🔬 Pytest

### Instalação

```bash
pip install pytest pytest-django pytest-cov
```

### Teste com Pytest

```python
import pytest
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_criar_usuario():
    User = get_user_model()
    user = User.objects.create_user(
        username='test',
        password='pass123'
    )
    assert user.username == 'test'
```

### Fixtures

```python
@pytest.fixture
def usuario():
    User = get_user_model()
    return User.objects.create_user(
        username='test',
        password='pass123'
    )

@pytest.mark.django_db
def test_com_fixture(usuario):
    assert usuario.username == 'test'
```

### Executar com Pytest

```bash
# Todos os testes
pytest

# Com cobertura
pytest --cov=app --cov-report=html

# Verbose
pytest -v
```

## 🚀 Preparação para Produção

### Settings Separadas

```python
# settings/production.py
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['seu-dominio.com']

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}
```

### Variáveis de Ambiente

```bash
# .env (nunca commitar!)
DEBUG=False
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=postgresql://user:pass@host/db
```

### Coletar Arquivos Estáticos

```bash
python manage.py collectstatic --noinput
```

### Checklist de Segurança

- ✅ `DEBUG = False`
- ✅ `SECRET_KEY` em variável de ambiente
- ✅ `ALLOWED_HOSTS` configurado
- ✅ HTTPS habilitado
- ✅ Cookies seguros (`SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`)
- ✅ Headers de segurança configurados

## 🔧 Gunicorn

### Instalação

```bash
pip install gunicorn
```

### Executar

```bash
gunicorn projeto.wsgi:application

# Com opções
gunicorn projeto.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120
```

### Procfile (Heroku)

```
web: gunicorn projeto.wsgi --log-file -
```

## 🌐 Nginx

### Configuração Básica

```nginx
upstream django {
    server unix:/run/gunicorn.sock;
}

server {
    listen 80;
    server_name seu-dominio.com;
    
    location /static/ {
        alias /path/to/staticfiles/;
    }
    
    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## ☁️ Deploy em Heroku

### Passos

1. Instalar Heroku CLI
2. Login: `heroku login`
3. Criar app: `heroku create meu-app`
4. Configurar Procfile
5. Deploy: `git push heroku main`
6. Migrations: `heroku run python manage.py migrate`
7. Criar superusuário: `heroku run python manage.py createsuperuser`

### Variáveis de Ambiente

```bash
heroku config:set SECRET_KEY='sua-chave'
heroku config:set DEBUG=False
```

## 🎨 Deploy no Render

### Configuração

1. Conectar repositório GitHub
2. Configurar build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
3. Configurar start command: `gunicorn projeto.wsgi`
4. Adicionar variáveis de ambiente no dashboard
5. Criar PostgreSQL database (se necessário)

### Build Script

```bash
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
```

## 📊 Cobertura de Testes

### Com Pytest

```bash
pytest --cov=app --cov-report=html
```

### Com Coverage.py

```bash
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 💡 Boas Práticas

1. **Escreva testes antes de refatorar**
2. **Mantenha cobertura acima de 70%**
3. **Teste casos de sucesso e erro**
4. **Use fixtures para dados de teste**
5. **Separe testes unitários, integração e funcionais**
6. **Configure CI/CD para rodar testes automaticamente**

## 📖 Tipos de Teste

### Testes Unitários
Testam componentes isolados (models, forms, funções)

### Testes de Integração
Testam interação entre componentes (view + model + template)

### Testes Funcionais
Testam fluxos completos de usuário (end-to-end)

## 🔍 Debugging em Produção

### Logs no Heroku

```bash
heroku logs --tail
```

### Logs no Render
Via interface web do dashboard

### Logs do Gunicorn

```bash
sudo journalctl -u gunicorn -f
```

### Logs do Nginx

```bash
sudo tail -f /var/log/nginx/error.log
```

## 📚 Recursos Adicionais

- [Django Testing](https://docs.djangoproject.com/en/stable/topics/testing/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Gunicorn Documentation](https://docs.gunicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Heroku Django Guide](https://devcenter.heroku.com/articles/django-app-configuration)
- [Render Django Guide](https://render.com/docs/deploy-django)

