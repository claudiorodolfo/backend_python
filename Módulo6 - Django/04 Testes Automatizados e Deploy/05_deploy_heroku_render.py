"""
05 - Deploy em Heroku e Render
================================

Este arquivo demonstra como fazer deploy do Django em plataformas gratuitas.
"""

# ============================================================================
# DEPLOY NO HEROKU
# ============================================================================

"""
# 1. Instalar Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login no Heroku
heroku login

# 3. Criar app
heroku create meu-projeto-django

# 4. Configurar Procfile
# Criar arquivo Procfile na raiz:
web: gunicorn projeto.wsgi --log-file -

# 5. Configurar runtime.txt (opcional)
# Criar arquivo runtime.txt:
python-3.11.5

# 6. Configurar settings para Heroku
# settings/production.py

import django_heroku
import os

# Configurações básicas
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = ['meu-projeto-django.herokuapp.com']

# Banco de dados (PostgreSQL no Heroku)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise para servir arquivos estáticos
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... outros middlewares
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Aplicar configurações do Heroku
django_heroku.settings(locals())


# 7. requirements.txt (adicionar)
django-heroku==0.3.1
gunicorn==21.2.0
whitenoise==6.5.0
psycopg2-binary==2.9.6


# 8. Configurar variáveis de ambiente
heroku config:set SECRET_KEY='sua-secret-key-aqui'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='meu-projeto-django.herokuapp.com'


# 9. Adicionar addon PostgreSQL
heroku addons:create heroku-postgresql:mini


# 10. Deploy
git init
git add .
git commit -m "Initial commit"
heroku git:remote -a meu-projeto-django
git push heroku main


# 11. Executar migrations
heroku run python manage.py migrate


# 12. Criar superusuário
heroku run python manage.py createsuperuser


# 13. Coletar arquivos estáticos
heroku run python manage.py collectstatic --noinput


# Comandos úteis:
heroku logs --tail                    # Ver logs
heroku ps                             # Ver processos
heroku restart                        # Reiniciar app
heroku run python manage.py shell     # Shell do Django
heroku config                         # Ver variáveis de ambiente
heroku config:unset VARIAVEL         # Remover variável
"""

# ============================================================================
# DEPLOY NO RENDER
# ============================================================================

"""
Render é uma alternativa moderna ao Heroku, com plano gratuito.

# 1. Criar conta no Render.com

# 2. Criar arquivo render.yaml (opcional, para deploy via YAML)

services:
  - type: web
    name: meu-projeto-django
    runtime: python
    buildCommand: pip install -r requirements.txt && python manage.py collectstatic --noinput
    startCommand: gunicorn projeto.wsgi
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: projeto.settings.production
      - key: SECRET_KEY
        sync: false
      - key: DATABASE_URL
        fromDatabase:
          name: meu-projeto-db
          property: connectionString

databases:
  - name: meu-projeto-db
    plan: free


# 3. Configurar settings para Render
# settings/production.py

import os
import dj_database_url

DEBUG = os.environ.get('DEBUG', 'False') == 'True'
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [
    'meu-projeto.onrender.com',
    # Adicionar outros domínios se necessário
]

# Banco de dados
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... outros middlewares
]

# Segurança (se usar HTTPS)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# 4. Criar build script (build.sh)
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput


# 5. Criar start script (start.sh)
#!/usr/bin/env bash
set -o errexit

python manage.py migrate --noinput
gunicorn projeto.wsgi


# 6. No dashboard do Render:
# - Conectar repositório GitHub/GitLab
# - Configurar build command: pip install -r requirements.txt && python manage.py collectstatic --noinput
# - Configurar start command: gunicorn projeto.wsgi
# - Adicionar variáveis de ambiente:
#   * DJANGO_SETTINGS_MODULE: projeto.settings.production
#   * SECRET_KEY: (gerar chave segura)
#   * DATABASE_URL: (automático se criar PostgreSQL)
#   * DEBUG: False


# 7. Criar PostgreSQL database no Render (se necessário)
# - Adicionar como serviço separado
# - Render automaticamente fornece DATABASE_URL
"""

# ============================================================================
# REQUIREMENTS.TXT PARA DEPLOY
# ============================================================================

"""
# requirements.txt

Django==4.2.0
gunicorn==21.2.0
whitenoise==6.5.0
psycopg2-binary==2.9.6
python-decouple==3.8

# Para Heroku (opcional):
# django-heroku==0.3.1

# Para Render (opcional):
# dj-database-url==2.1.0
"""

# ============================================================================
# PROCFILE (HEROKU)
# ============================================================================

"""
# Procfile na raiz do projeto

web: gunicorn projeto.wsgi --log-file -
release: python manage.py migrate --noinput
"""

# ============================================================================
# .ENV PARA DEPLOY
# ============================================================================

"""
# Nunca commitar .env!

# .env.example (commitar este)
DEBUG=False
SECRET_KEY=generate-secret-key-here
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DATABASE_URL=postgresql://user:pass@host:port/dbname

# Gerar SECRET_KEY:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
"""

# ============================================================================
# CHECKLIST DE DEPLOY
# ============================================================================

"""
Antes de fazer deploy:

☐ DEBUG = False
☐ SECRET_KEY seguro em variáveis de ambiente
☐ ALLOWED_HOSTS configurado
☐ Banco de dados PostgreSQL configurado
☐ Migrations aplicadas
☐ Arquivos estáticos coletados (collectstatic)
☐ Whitenoise configurado
☐ HTTPS configurado (se aplicável)
☐ Logs configurados
☐ Backups configurados
☐ Monitoramento configurado
☐ Testes passando
☐ Documentação atualizada
"""

# ============================================================================
# COMANDOS ÚTEIS PARA DEPLOY
# ============================================================================

"""
# Heroku
heroku logs --tail                    # Ver logs em tempo real
heroku run python manage.py shell     # Abrir shell Django
heroku run python manage.py migrate   # Executar migrations
heroku restart                        # Reiniciar app
heroku ps:scale web=2                 # Escalar workers
heroku config:set VAR=value           # Definir variável

# Render (via dashboard)
- Ver logs na interface
- Executar shell via interface
- Configurar variáveis de ambiente na interface
"""

# ============================================================================
# TROUBLESHOOTING COMUM
# ============================================================================

"""
# Problema: App não inicia
- Verificar logs: heroku logs --tail
- Verificar Procfile está correto
- Verificar variáveis de ambiente

# Problema: Erro 500
- Verificar DEBUG=False em produção
- Verificar logs de erro
- Verificar ALLOWED_HOSTS
- Verificar SECRET_KEY configurado

# Problema: Arquivos estáticos não carregam
- Executar collectstatic
- Verificar STATIC_ROOT configurado
- Verificar WhiteNoise configurado

# Problema: Migrations não aplicadas
- heroku run python manage.py migrate
- Verificar se banco de dados está conectado

# Problema: Timeout
- Aumentar timeout no gunicorn
- Verificar queries lentas
- Usar cache quando apropriado
"""

print("Arquivo de referência: Deploy em Heroku e Render")
print("Ambas as plataformas oferecem planos gratuitos para começar")

