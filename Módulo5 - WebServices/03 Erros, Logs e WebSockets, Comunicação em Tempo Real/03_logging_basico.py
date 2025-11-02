"""
03 - Logging Básico
====================
O que registrar e conceitos fundamentais de logging
"""

import logging
from flask import Flask, request
from datetime import datetime

print("=" * 60)
print("LOGGING BÁSICO")
print("=" * 60)

# ============================================
# 1. CONCEITOS DE LOGGING
# ============================================

"""
Logging (Registro de Logs):
---------------------------
Processo de registrar eventos, erros e informações durante a execução
de uma aplicação para facilitar debug, monitoramento e auditoria.

Por que fazer logging?
- Debug de problemas
- Monitoramento da aplicação
- Auditoria e compliance
- Análise de performance
- Rastreamento de erros
"""

# ============================================
# 2. NÍVEIS DE LOG
# ============================================

print("\n" + "=" * 60)
print("NÍVEIS DE LOG")
print("=" * 60)

niveis_log = {
    "DEBUG": {
        "nivel": 10,
        "uso": "Informações detalhadas para debug",
        "exemplo": "Valor de variável, estado interno"
    },
    "INFO": {
        "nivel": 20,
        "uso": "Informações gerais sobre operações",
        "exemplo": "Usuário fez login, requisição processada"
    },
    "WARNING": {
        "nivel": 30,
        "uso": "Avisos sobre situações inesperadas",
        "exemplo": "Configuração padrão usada, rate limit próximo"
    },
    "ERROR": {
        "nivel": 40,
        "uso": "Erros que não impedem execução",
        "exemplo": "Falha ao enviar email, mas processo continua"
    },
    "CRITICAL": {
        "nivel": 50,
        "uso": "Erros críticos que podem parar aplicação",
        "exemplo": "Banco de dados offline, memória esgotada"
    }
}

for nivel, info in niveis_log.items():
    print(f"\n{nivel} ({info['nivel']}):")
    print(f"  Uso: {info['uso']}")
    print(f"  Exemplo: {info['exemplo']}")


# ============================================
# 3. CONFIGURAÇÃO BÁSICA
# ============================================

# Configurar logging
logging.basicConfig(
    level=logging.INFO,  # Nível mínimo de log
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Criar logger
logger = logging.getLogger(__name__)


# ============================================
# 4. O QUE REGISTRAR
# ============================================

print("\n" + "=" * 60)
print("O QUE REGISTRAR")
print("=" * 60)

o_que_registrar = """
✓ Registrar:
  - Início/fim de operações importantes
  - Erros e exceções
  - Operações de autenticação (login/logout)
  - Mudanças de estado críticas
  - Requisições importantes
  - Performance de operações lentas
  - Avisos sobre configuração

✗ NÃO registrar:
  - Senhas ou tokens
  - Dados sensíveis (CPF, cartão de crédito)
  - Informações pessoais desnecessárias
  - Dados muito grandes
  - Informações redundantes

Boas práticas:
- Use níveis apropriados
- Inclua contexto relevante
- Estruture logs para facilitar busca
- Considere privacidade
"""

print(o_que_registrar)


# ============================================
# 5. EXEMPLOS PRÁTICOS
# ============================================

def exemplo_logging_simples():
    """Exemplos de logging em diferentes situações"""
    
    # DEBUG - Para desenvolvimento
    logger.debug("Processando dados do usuário ID: 123")
    
    # INFO - Informações gerais
    logger.info("Usuário 'admin' fez login com sucesso")
    logger.info("Requisição GET /api/users processada em 0.05s")
    
    # WARNING - Avisos
    logger.warning("Taxa de requisições alta: 100 req/min")
    logger.warning("Usando configuração padrão para 'timeout'")
    
    # ERROR - Erros
    logger.error("Falha ao conectar com banco de dados", exc_info=True)
    logger.error("Erro ao enviar email de notificação")
    
    # CRITICAL - Crítico
    logger.critical("Banco de dados offline!")
    logger.critical("Memória disponível abaixo de 10%!")


# ============================================
# 6. LOGGING EM APLICAÇÕES WEB
# ============================================

app = Flask(__name__)

# Configurar logging para Flask
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console
        # logging.FileHandler('app.log')  # Arquivo
    ]
)

logger = logging.getLogger(__name__)


@app.before_request
def log_request():
    """Registra todas as requisições"""
    logger.info(f"{request.method} {request.path} - IP: {request.remote_addr}")


@app.after_request
def log_response(response):
    """Registra respostas"""
    logger.info(
        f"{request.method} {request.path} - "
        f"Status: {response.status_code} - "
        f"Tempo: {getattr(request, 'elapsed_time', 'N/A')}"
    )
    return response


@app.route('/api/exemplo', methods=['GET'])
def exemplo_endpoint():
    """Endpoint de exemplo com logging"""
    
    logger.info("Processando requisição em /api/exemplo")
    
    try:
        # Simulação de processamento
        parametro = request.args.get('param', 'padrao')
        logger.debug(f"Parâmetro recebido: {parametro}")
        
        if parametro == 'erro':
            raise ValueError("Erro simulado")
        
        logger.info("Processamento concluído com sucesso")
        return {"status": "ok"}, 200
    
    except Exception as e:
        logger.error(f"Erro ao processar requisição: {str(e)}", exc_info=True)
        return {"error": "Erro interno"}, 500


# ============================================
# 7. LOGGING ESTRUTURADO
# ============================================

def logar_requisicao(method, path, status_code, tempo, user_id=None):
    """Log estruturado de requisição"""
    log_data = {
        "event": "http_request",
        "method": method,
        "path": path,
        "status_code": status_code,
        "tempo_ms": tempo,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if user_id:
        log_data["user_id"] = user_id
    
    logger.info(f"HTTP_REQUEST: {log_data}")


def logar_erro(erro, contexto=None):
    """Log estruturado de erro"""
    log_data = {
        "event": "error",
        "error_type": type(erro).__name__,
        "error_message": str(erro),
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if contexto:
        log_data["context"] = contexto
    
    logger.error(f"ERROR: {log_data}", exc_info=True)


# ============================================
# 8. LOGGING EM ARQUIVO
# ============================================

def configurar_logging_arquivo(nome_arquivo='app.log'):
    """Configura logging para arquivo"""
    
    # Criar formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Handler para arquivo
    file_handler = logging.FileHandler(nome_arquivo)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    
    # Configurar root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)


# ============================================
# 9. BOAS PRÁTICAS
# ============================================

print("\n" + "=" * 60)
print("BOAS PRÁTICAS DE LOGGING")
print("=" * 60)

boas_praticas = """
1. Use níveis apropriados:
   - DEBUG: Apenas em desenvolvimento
   - INFO: Eventos normais importantes
   - WARNING: Situações anômalas mas não críticas
   - ERROR: Erros que precisam atenção
   - CRITICAL: Problemas graves

2. Inclua contexto:
   - IDs de usuário/requisição
   - Timestamps
   - Parâmetros relevantes
   - Status codes

3. Estruture logs:
   - Formato consistente
   - JSON para fácil parsing
   - Separação de campos

4. Privacidade:
   - Nunca logue senhas
   - Nunca logue tokens completos
   - Cuidado com dados pessoais
   - Cumpra LGPD/GDPR

5. Performance:
   - Não logue em loops intensivos
   - Use níveis apropriados em produção
   - Considere logging assíncrono

6. Rotação de logs:
   - Limite tamanho de arquivos
   - Mantenha apenas logs recentes
   - Archive logs antigos
"""

print(boas_praticas)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - LOGGING BÁSICO")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Níveis de log:
   - DEBUG, INFO, WARNING, ERROR, CRITICAL
   - Escolha nível apropriado

2. O que registrar:
   - Eventos importantes
   - Erros e exceções
   - Operações críticas
   - NÃO registrar dados sensíveis

3. Boas práticas:
   - Contexto relevante
   - Estrutura consistente
   - Privacidade
   - Performance

4. Configuração:
   - Formato apropriado
   - Handlers (console, arquivo)
   - Níveis por ambiente

Próximos passos:
- Ferramentas de logging avançadas
- Integração com serviços de monitoramento
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 03_logging_basico.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

