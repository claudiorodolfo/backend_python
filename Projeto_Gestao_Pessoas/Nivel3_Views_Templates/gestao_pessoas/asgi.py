"""
ASGI config for gestao_pessoas project.
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_pessoas.settings')
application = get_asgi_application()
