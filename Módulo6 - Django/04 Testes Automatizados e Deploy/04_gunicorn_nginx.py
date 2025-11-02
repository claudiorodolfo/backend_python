"""
04 - Configuração de Gunicorn e Nginx
======================================

Este arquivo demonstra como configurar Gunicorn e Nginx para produção.
"""

# ============================================================================
# GUNICORN
# ============================================================================

"""
Gunicorn é um servidor WSGI HTTP para Python.
É usado para servir aplicações Django em produção.

# Instalação
pip install gunicorn

# Executar localmente (teste)
gunicorn projeto.wsgi:application

# Com configurações
gunicorn projeto.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -

# Opções comuns:
--bind ADDRESS    # IP:porta (ex: 0.0.0.0:8000)
--workers N       # Número de workers (2-4 por CPU)
--timeout SECONDS # Timeout para requests
--access-logfile  # Arquivo de log de acesso
--error-logfile   # Arquivo de log de erros
--daemon          # Executar em background
--pid PIDFILE     # Arquivo PID
--user USER       # Usuário para executar
--group GROUP     # Grupo para executar
"""

# ============================================================================
# CONFIGURAÇÃO DO GUNICORN (gunicorn_config.py)
# ============================================================================

"""
# gunicorn_config.py

import multiprocessing

# Configurações de servidor
bind = "0.0.0.0:8000"
backlog = 2048

# Workers
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Processo
daemon = False
pidfile = "/var/run/gunicorn/pid"
umask = 0
user = None
group = None
tmp_upload_dir = None

# Executar com configuração:
# gunicorn projeto.wsgi:application -c gunicorn_config.py
"""

# ============================================================================
# SYSTEMD SERVICE (GUNICORN)
# ============================================================================

"""
# Criar arquivo: /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/projeto
ExecStart=/path/to/venv/bin/gunicorn \
    --access-logfile - \
    --error-logfile - \
    --workers 3 \
    --bind unix:/run/gunicorn.sock \
    projeto.wsgi:application

Restart=always

[Install]
WantedBy=multi-user.target


# Comandos:
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
"""

# ============================================================================
# NGINX
# ============================================================================

"""
Nginx é um servidor web que atua como reverse proxy para Gunicorn.

# Instalação (Ubuntu/Debian)
sudo apt update
sudo apt install nginx

# Instalação (CentOS/RHEL)
sudo yum install nginx
"""

# ============================================================================
# CONFIGURAÇÃO DO NGINX
# ============================================================================

"""
# /etc/nginx/sites-available/projeto

upstream django {
    server unix:/run/gunicorn.sock;
    # Ou usar TCP:
    # server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name seu-dominio.com www.seu-dominio.com;
    
    # Redirecionar para HTTPS (recomendado)
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name seu-dominio.com www.seu-dominio.com;
    
    # Certificados SSL (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/seu-dominio.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/seu-dominio.com/privkey.pem;
    
    # SSL Configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    # Logs
    access_log /var/log/nginx/projeto_access.log;
    error_log /var/log/nginx/projeto_error.log;
    
    # Tamanho máximo de upload
    client_max_body_size 100M;
    
    # Arquivos estáticos
    location /static/ {
        alias /path/to/projeto/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
    
    # Arquivos de mídia
    location /media/ {
        alias /path/to/projeto/media/;
        expires 7d;
    }
    
    # Proxy para Django/Gunicorn
    location / {
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Favicon
    location = /favicon.ico {
        access_log off;
        log_not_found off;
    }
    
    # Denegar acesso a arquivos ocultos
    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }
}
"""

# ============================================================================
# ATIVAR SITE NO NGINX
# ============================================================================

"""
# Criar link simbólico
sudo ln -s /etc/nginx/sites-available/projeto /etc/nginx/sites-enabled/

# Testar configuração
sudo nginx -t

# Recarregar Nginx
sudo systemctl reload nginx

# Ou reiniciar
sudo systemctl restart nginx
"""

# ============================================================================
# LET'S ENCRYPT (SSL GRATUITO)
# ============================================================================

"""
# Instalar Certbot
sudo apt install certbot python3-certbot-nginx

# Obter certificado
sudo certbot --nginx -d seu-dominio.com -d www.seu-dominio.com

# Renovação automática (já configurado)
sudo certbot renew --dry-run
"""

# ============================================================================
# PROCESSO COMPLETO DE DEPLOY
# ============================================================================

"""
# 1. Preparar código
git clone https://github.com/usuario/projeto.git
cd projeto

# 2. Criar ambiente virtual
python -m venv venv
source venv/bin/activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar variáveis de ambiente
cp .env.example .env
nano .env  # Editar com valores de produção

# 5. Executar migrations
python manage.py migrate

# 6. Coletar arquivos estáticos
python manage.py collectstatic --noinput

# 7. Criar superusuário
python manage.py createsuperuser

# 8. Testar Gunicorn localmente
gunicorn projeto.wsgi:application

# 9. Configurar systemd para Gunicorn
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

# 10. Configurar Nginx
sudo nano /etc/nginx/sites-available/projeto
sudo ln -s /etc/nginx/sites-available/projeto /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# 11. Configurar SSL (Let's Encrypt)
sudo certbot --nginx -d seu-dominio.com

# 12. Verificar tudo está funcionando
sudo systemctl status gunicorn
sudo systemctl status nginx
"""

# ============================================================================
# MONITORAMENTO E LOGS
# ============================================================================

"""
# Ver logs do Gunicorn
sudo journalctl -u gunicorn -f

# Ver logs do Nginx
sudo tail -f /var/log/nginx/projeto_error.log
sudo tail -f /var/log/nginx/projeto_access.log

# Ver status dos serviços
sudo systemctl status gunicorn
sudo systemctl status nginx
"""

print("Arquivo de referência: Gunicorn e Nginx")
print("Gunicorn serve a aplicação Django, Nginx atua como reverse proxy")

