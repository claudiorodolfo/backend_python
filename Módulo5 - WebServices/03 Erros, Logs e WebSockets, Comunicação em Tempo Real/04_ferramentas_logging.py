"""
04 - Ferramentas Básicas para Logging
=======================================
Ferramentas e bibliotecas para logging em Python
"""

import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import json
from datetime import datetime

print("=" * 60)
print("FERRAMENTAS DE LOGGING")
print("=" * 60)


# ============================================
# 1. LOGGING PADRÃO DO PYTHON
# ============================================

print("\n" + "=" * 60)
print("1. LOGGING MÓDULO PADRÃO")
print("=" * 60)

"""
O módulo logging do Python é suficiente para a maioria dos casos.
Inclui:
- Múltiplos handlers (console, arquivo, etc.)
- Formatters customizados
- Níveis de log
- Filtros
"""

# Configuração básica
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.info("Exemplo de log usando módulo padrão")


# ============================================
# 2. ROTATING FILE HANDLER
# ============================================

print("\n" + "=" * 60)
print("2. ROTATING FILE HANDLER")
print("=" * 60)

"""
RotatingFileHandler: Rotaciona logs quando atingem tamanho máximo
Útil para evitar arquivos de log muito grandes.
"""

def configurar_rotating_log(nome_arquivo='app.log', max_bytes=10*1024*1024, backup_count=5):
    """Configura logging com rotação por tamanho"""
    
    # Criar handler que rotaciona quando atinge tamanho
    handler = RotatingFileHandler(
        nome_arquivo,
        maxBytes=max_bytes,  # 10MB
        backupCount=backup_count  # Manter 5 arquivos de backup
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    print(f"Logging configurado: {nome_arquivo}")
    print(f"  - Tamanho máximo: {max_bytes / (1024*1024)}MB")
    print(f"  - Arquivos de backup: {backup_count}")


# ============================================
# 3. TIMED ROTATING FILE HANDLER
# ============================================

print("\n" + "=" * 60)
print("3. TIMED ROTATING FILE HANDLER")
print("=" * 60)

"""
TimedRotatingFileHandler: Rotaciona logs por tempo
Útil para ter logs diários, semanais, etc.
"""

def configurar_timed_rotating_log(nome_arquivo='app.log', when='midnight', interval=1, backup_count=7):
    """Configura logging com rotação por tempo"""
    
    handler = TimedRotatingFileHandler(
        nome_arquivo,
        when=when,  # 'midnight', 'H' (hora), 'D' (dia), 'W' (semana)
        interval=interval,
        backupCount=backup_count
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    print(f"Logging configurado: {nome_arquivo}")
    print(f"  - Rotação: {when} a cada {interval}")
    print(f"  - Arquivos de backup: {backup_count}")


# ============================================
# 4. LOGGING ESTRUTURADO (JSON)
# ============================================

print("\n" + "=" * 60)
print("4. LOGGING ESTRUTURADO (JSON)")
print("=" * 60)

"""
Logging estruturado em JSON facilita:
- Parsing automático
- Integração com ferramentas (ELK, Splunk)
- Busca e análise
"""

class JSONFormatter(logging.Formatter):
    """Formatter que produz logs em JSON"""
    
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Adicionar exception se houver
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        
        # Adicionar campos extras se houver
        if hasattr(record, 'user_id'):
            log_entry["user_id"] = record.user_id
        
        if hasattr(record, 'request_id'):
            log_entry["request_id"] = record.request_id
        
        return json.dumps(log_entry, ensure_ascii=False)


def configurar_json_logging(nome_arquivo='app.json.log'):
    """Configura logging em formato JSON"""
    
    handler = logging.FileHandler(nome_arquivo)
    handler.setFormatter(JSONFormatter())
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger


# Exemplo de uso
logger_json = configurar_json_logging()
logger_json.info("Exemplo de log JSON", extra={
    "user_id": 123,
    "request_id": "req-abc-123"
})


# ============================================
# 5. MÚLTIPLOS HANDLERS
# ============================================

print("\n" + "=" * 60)
print("5. CONFIGURAÇÃO COMPLETA COM MÚLTIPLOS HANDLERS")
print("=" * 60)

def configurar_logging_completo():
    """Configura logging completo com múltiplos handlers"""
    
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Handler para console (INFO e acima)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    console_handler.setFormatter(console_formatter)
    
    # Handler para arquivo (todos os níveis)
    file_handler = RotatingFileHandler(
        'app.log',
        maxBytes=10*1024*1024,
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    file_handler.setFormatter(file_formatter)
    
    # Handler para erros (arquivo separado)
    error_handler = RotatingFileHandler(
        'errors.log',
        maxBytes=10*1024*1024,
        backupCount=10
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(file_formatter)
    
    # Adicionar handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    
    return logger


# ============================================
# 6. LOGGER CUSTOMIZADO PARA APLICAÇÕES WEB
# ============================================

class WebLogger:
    """Logger customizado para aplicações web"""
    
    def __init__(self, name):
        self.logger = logging.getLogger(name)
    
    def log_request(self, method, path, status_code, tempo_ms, user_id=None):
        """Log de requisição HTTP"""
        log_data = {
            "event": "http_request",
            "method": method,
            "path": path,
            "status_code": status_code,
            "tempo_ms": tempo_ms
        }
        
        if user_id:
            log_data["user_id"] = user_id
        
        self.logger.info(json.dumps(log_data))
    
    def log_error(self, error, contexto=None):
        """Log de erro"""
        log_data = {
            "event": "error",
            "error_type": type(error).__name__,
            "error_message": str(error)
        }
        
        if contexto:
            log_data.update(contexto)
        
        self.logger.error(json.dumps(log_data), exc_info=True)
    
    def log_auth(self, event, username, success=True):
        """Log de eventos de autenticação"""
        log_data = {
            "event": "auth",
            "auth_event": event,  # login, logout, token_refresh
            "username": username,
            "success": success
        }
        
        level = logging.INFO if success else logging.WARNING
        self.logger.log(level, json.dumps(log_data))


# Exemplo de uso
web_logger = WebLogger('api')
web_logger.log_request('GET', '/api/users', 200, 45.2, user_id=123)
web_logger.log_auth('login', 'admin', success=True)
web_logger.log_error(ValueError("Teste"), {"endpoint": "/api/test"})


# ============================================
# 7. FERRAMENTAS EXTERNAS (INFORMAÇÕES)
# ============================================

print("\n" + "=" * 60)
print("6. FERRAMENTAS EXTERNAS")
print("=" * 60)

ferramentas = """
Bibliotecas Python:
- structlog: Logging estruturado avançado
- python-json-logger: Formatter JSON
- loguru: API mais simples e poderosa

Serviços de Logging:
- Sentry: Rastreamento de erros
- Loggly: Análise de logs
- Papertrail: Logging em nuvem
- CloudWatch: AWS
- Azure Monitor: Azure

Ferramentas de Análise:
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Splunk
- Grafana Loki
- Datadog
"""

print(ferramentas)


# ============================================
# 8. EXEMPLO COMPLETO
# ============================================

def exemplo_completo():
    """Exemplo completo de configuração de logging"""
    
    logger = configurar_logging_completo()
    
    # Diferentes níveis de log
    logger.debug("Mensagem de debug (não aparece no console)")
    logger.info("Operação realizada com sucesso")
    logger.warning("Taxa de requisições alta")
    logger.error("Erro ao processar requisição")
    logger.critical("Sistema crítico offline")
    
    # Log com contexto
    logger.info("Usuário fez login", extra={"user_id": 123})
    
    # Log de exceção
    try:
        resultado = 1 / 0
    except Exception as e:
        logger.error("Divisão por zero", exc_info=True)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - FERRAMENTAS DE LOGGING")
print("=" * 60)
print("""
Ferramentas aprendidas:

1. Módulo logging padrão:
   - Básico e suficiente
   - Múltiplos handlers
   - Formatters customizados

2. RotatingFileHandler:
   - Rotação por tamanho
   - Evita arquivos muito grandes

3. TimedRotatingFileHandler:
   - Rotação por tempo
   - Logs diários/semanais

4. Logging estruturado:
   - Formato JSON
   - Facilita análise
   - Integração com ferramentas

5. Boas práticas:
   - Múltiplos handlers
   - Níveis apropriados
   - Formato consistente
   - Rotação adequada
""")

if __name__ == '__main__':
    exemplo_completo()
    print("\nLogs foram criados. Verifique os arquivos:")
    print("  - app.log")
    print("  - errors.log")
    print("  - app.json.log")

