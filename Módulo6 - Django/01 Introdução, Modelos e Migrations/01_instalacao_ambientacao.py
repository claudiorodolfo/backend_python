"""
01 - Instalação e Ambientação do Django
========================================

Este arquivo demonstra como instalar e configurar o Django em um ambiente Python.
"""

# ============================================================================
# INSTALAÇÃO DO DJANGO
# ============================================================================

# 1. Criar ambiente virtual (recomendado)
# python -m venv .venv
# source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate      # Windows

# 2. Instalar Django
# pip3 install django

# 3. Verificar instalação
# django-admin --version

# 4. Criar projeto Django
# django-admin startproject meu_projeto .

# 5. Criar app dentro do projeto
# cd meu_projeto
# python manage.py startapp minha_app

# ============================================================================
# ESTRUTURA DE UM PROJETO DJANGO
# ============================================================================

"""
Estrutura típica de um projeto Django:

meu_projeto/
├── manage.py              # Script de gerenciamento do projeto
├── meu_projeto/           # Diretório de configuração do projeto
│   ├── __init__.py
│   ├── settings.py        # Configurações do projeto
│   ├── urls.py            # URLs principais (URLConf)
│   ├── wsgi.py            # Interface WSGI para servidor
│   └── asgi.py            # Interface ASGI para servidor assíncrono
└── minha_app/             # App da aplicação
    ├── migrations/        # Migrations do banco de dados
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py           # Configuração do admin
    ├── apps.py            # Configuração do app
    ├── models.py          # Models (camada de dados)
    ├── views.py           # Views (lógica de negócio)
    ├── urls.py            # URLs do app
    ├── forms.py           # Formulários (geralmente criado manualmente)
    └── tests.py           # Testes
"""

# ============================================================================
# CONCEITO MTV (MODEL-TEMPLATE-VIEW)
# ============================================================================

"""
Django usa o padrão MVT (Model-View-Template), similar ao MVC:

1. MODEL (Model):
   - Camada de dados
   - Define estrutura do banco de dados
   - Contém lógica de acesso aos dados
   - Exemplo: models.py

2. VIEW (View):
   - Camada de lógica de negócio
   - Processa requisições HTTP
   - Retorna respostas HTTP
   - Exemplo: views.py

3. TEMPLATE (Template):
   - Camada de apresentação
   - Define como os dados são exibidos
   - Usa Django Template Language (DTL)
   - Exemplo: templates/*.html

FLUXO MTV:
1. Usuário acessa URL
2. URLConf roteia para uma View
3. View consulta/atualiza Model se necessário
4. View passa dados para Template via Context
5. Template renderiza HTML
6. View retorna HttpResponse ao usuário
"""

# ============================================================================
# SETTINGS.PY - CONFIGURAÇÕES IMPORTANTES
# ============================================================================

"""
# settings.py - Exemplo de configurações importantes

INSTALLED_APPS = [
    'django.contrib.admin',      # Interface administrativa
    'django.contrib.auth',       # Sistema de autenticação
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'minha_app',                 # Seu app
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Para PostgreSQL:
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'nome_banco',
#         'USER': 'usuario',
#         'PASSWORD': 'senha',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Segurança (IMPORTANTE EM PRODUÇÃO)
DEBUG = True  # False em produção
SECRET_KEY = 'sua-chave-secreta-aqui'  # Use variável de ambiente em produção
ALLOWED_HOSTS = []  # ['seu-dominio.com'] em produção
"""

# ============================================================================
# COMANDOS ÚTEIS DO DJANGO
# ============================================================================

"""
# Rodar servidor de desenvolvimento
python manage.py runserver
python manage.py runserver 8000  # Porta específica
python manage.py runserver 0.0.0.0:8000  # Acessível na rede

# Criar migrations (antes de qualquer mudança em models)
python manage.py makemigrations
python manage.py makemigrations minha_app  # App específico

# Aplicar migrations
python manage.py migrate
python manage.py migrate minha_app  # App específico

# Ver SQL das migrations (sem aplicar)
python manage.py sqlmigrate minha_app 0001

# Criar superusuário (para acessar admin)
python manage.py createsuperuser

# Shell interativo do Django
python manage.py shell

# Coletar arquivos estáticos (produção)
python manage.py collectstatic

# Executar testes
python manage.py test
python manage.py test minha_app  # App específico
"""

# ============================================================================
# EXEMPLO DE USO DO SHELL DO DJANGO
# ============================================================================

"""
# No shell do Django (python manage.py shell)

from minha_app.models import MinhaModel
from django.utils import timezone

# Criar objeto
obj = MinhaModel.objects.create(nome="Teste", data=timezone.now())

# Consultar
MinhaModel.objects.all()
MinhaModel.objects.get(id=1)
MinhaModel.objects.filter(nome__contains="Teste")

# Atualizar
obj.nome = "Novo Nome"
obj.save()

# Deletar
obj.delete()
"""

print("Arquivo de exemplo: Instalação e Ambientação do Django")
print("Execute os comandos comentados acima para configurar seu projeto Django")

