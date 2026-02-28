"""
WSGI config for gestao_pessoas project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_pessoas.settings')
application = get_wsgi_application()
