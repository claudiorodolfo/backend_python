"""
03 - Preparação para Produção
===============================

Este arquivo demonstra como preparar uma aplicação Django para produção.
"""

# ============================================================================
# SETTINGS PARA PRODUÇÃO
# ============================================================================

"""
# Criar estrutura de settings

projeto/
├── settings/
│   ├── __init__.py
│   ├── base.py        # Configurações comuns
│   ├── development.py # Configurações de desenvolvimento
│   └── production.py   # Configurações de produção

# settings/__init__.py
import os

ENV = os.environ.get('DJANGO_ENV', 'development')

if ENV == 'production':
    from .production import *
else:
    from .development import *


# settings/base.py - Configurações comuns
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Para servir arquivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'projeto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# settings/development.py
from .base import *

DEBUG = True
SECRET_KEY = 'dev-secret-key-change-in-production'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# settings/production.py
from .base import *
import os
import dj_database_url

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Banco de dados
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Segurança
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'django.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
"""

# ============================================================================
# REQUIREMENTS.TXT
# ============================================================================

"""
# requirements.txt

# Core Django
Django==4.2.0

# Banco de dados
psycopg2-binary==2.9.6  # PostgreSQL

# Arquivos estáticos
whitenoise==6.5.0

# Servidor WSGI
gunicorn==21.2.0

# Variáveis de ambiente
python-decouple==3.8

# Outras dependências
# django-cors-headers==4.0.0
# pillow==10.0.0

# requirements-dev.txt (desenvolvimento)
-r requirements.txt

pytest==7.4.0
pytest-django==4.5.2
pytest-cov==4.1.0
django-debug-toolbar==4.2.0
"""

# ============================================================================
# VARIÁVEIS DE AMBIENTE
# ============================================================================

"""
# .env (desenvolvimento)
DEBUG=True
SECRET_KEY=dev-secret-key-change-in-production
DATABASE_URL=sqlite:///db.sqlite3

# .env.production (nunca commitar!)
DEBUG=False
SECRET_KEY=seu-secret-key-super-seguro-aqui
DATABASE_URL=postgresql://user:password@host:port/dbname
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
"""

# ============================================================================
# .GITIGNORE
# ============================================================================

"""
# .gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
/staticfiles/
/media/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Ambiente
.env
.env.production
*.env

# OS
.DS_Store
Thumbs.db
"""

# ============================================================================
# COLECTSTATIC
# ============================================================================

"""
# Coletar arquivos estáticos para produção
python manage.py collectstatic --noinput

# Isso coleta todos os arquivos estáticos para STATIC_ROOT
"""

# ============================================================================
# SEGURANÇA
# ============================================================================

"""
# Checklist de segurança para produção:

1. DEBUG = False
2. SECRET_KEY seguro (use variável de ambiente)
3. ALLOWED_HOSTS configurado
4. HTTPS habilitado
5. SECURE_SSL_REDIRECT = True
6. SESSION_COOKIE_SECURE = True
7. CSRF_COOKIE_SECURE = True
8. Senhas de banco de dados em variáveis de ambiente
9. Não commitar .env ou secrets
10. Usar migrações
11. Validar entrada de dados
12. Proteção CSRF habilitada
13. Headers de segurança configurados
"""

print("Arquivo de referência: Preparação para Produção")
print("Configure DEBUG=False, SECRET_KEY seguro e variáveis de ambiente em produção")

