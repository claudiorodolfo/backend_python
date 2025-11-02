"""
05 - Tratamento de Erros
==========================
Exercícios de simulação e tratamento de erros
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

print("=" * 60)
print("TRATAMENTO DE ERROS")
print("=" * 60)


# ============================================
# 1. SIMULAÇÃO DE ERROS COMUNS
# ============================================

@app.route('/api/simular/erro-validacao', methods=['POST'])
def simular_erro_validacao():
    """Simula erro de validação"""
    
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    erros = []
    
    # Validações
    if 'nome' not in dados:
        erros.append({
            "field": "nome",
            "message": "Campo obrigatório",
            "code": "required"
        })
    
    if 'email' not in dados:
        erros.append({
            "field": "email",
            "message": "Campo obrigatório",
            "code": "required"
        })
    elif '@' not in dados['email']:
        erros.append({
            "field": "email",
            "message": "Email inválido",
            "code": "invalid_format"
        })
    
    if erros:
        logger.warning(f"Erro de validação: {erros}")
        return jsonify({
            "status": 422,
            "error": "Erros de validação",
            "validation_errors": erros
        }), 422
    
    logger.info("Dados validados com sucesso")
    return jsonify({"status": "ok", "message": "Dados válidos"}), 200


@app.route('/api/simular/erro-not-found', methods=['GET'])
def simular_erro_not_found():
    """Simula erro 404"""
    
    recurso_id = request.args.get('id', type=int)
    
    # Simulação: banco de dados
    recursos = {1: "Recurso 1", 2: "Recurso 2"}
    
    if recurso_id not in recursos:
        logger.warning(f"Recurso {recurso_id} não encontrado")
        return jsonify({
            "status": 404,
            "error": "Not Found",
            "message": f"Recurso com ID {recurso_id} não encontrado",
            "available_ids": list(recursos.keys())
        }), 404
    
    return jsonify({"data": recursos[recurso_id]}), 200


@app.route('/api/simular/erro-autenticacao', methods=['GET'])
def simular_erro_autenticacao():
    """Simula erro de autenticação"""
    
    token = request.headers.get('Authorization')
    
    if not token:
        logger.warning("Tentativa de acesso sem token")
        return jsonify({
            "status": 401,
            "error": "Unauthorized",
            "message": "Token de autenticação necessário",
            "hint": "Envie: Authorization: Bearer <token>"
        }), 401
    
    if not token.startswith('Bearer '):
        logger.warning("Formato de token inválido")
        return jsonify({
            "status": 401,
            "error": "Unauthorized",
            "message": "Formato de token inválido",
            "expected_format": "Bearer <token>"
        }), 401
    
    token_value = token.replace('Bearer ', '')
    
    # Simulação: verificar token
    tokens_validos = ['token123', 'token456']
    
    if token_value not in tokens_validos:
        logger.warning(f"Tentativa de acesso com token inválido: {token_value[:10]}...")
        return jsonify({
            "status": 401,
            "error": "Unauthorized",
            "message": "Token inválido ou expirado"
        }), 401
    
    return jsonify({"status": "ok", "message": "Autenticado"}), 200


@app.route('/api/simular/erro-servidor', methods=['GET'])
def simular_erro_servidor():
    """Simula erro interno do servidor"""
    
    erro_tipo = request.args.get('tipo', 'generico')
    
    try:
        if erro_tipo == 'divisao_zero':
            resultado = 1 / 0  # Vai gerar ZeroDivisionError
        
        elif erro_tipo == 'chave_inexistente':
            dicio = {}
            valor = dicio['chave_inexistente']  # Vai gerar KeyError
        
        elif erro_tipo == 'atributo_inexistente':
            obj = None
            obj.metodo_inexistente()  # Vai gerar AttributeError
        
        else:
            raise ValueError("Erro genérico simulado")
    
    except Exception as e:
        # Em produção, não exponha detalhes do erro
        error_id = f"ERR-{hash(str(e)) % 10000}"
        logger.error(f"Erro interno [{error_id}]: {type(e).__name__}: {str(e)}", exc_info=True)
        
        return jsonify({
            "status": 500,
            "error": "Internal Server Error",
            "message": "Ocorreu um erro interno. Tente novamente mais tarde.",
            "error_id": error_id
            # Em desenvolvimento, pode incluir: "details": str(e)
        }), 500


# ============================================
# 2. HANDLER GLOBAL DE ERROS
# ============================================

@app.errorhandler(404)
def handle_404(e):
    """Handler para 404"""
    logger.warning(f"404: {request.path}")
    return jsonify({
        "status": 404,
        "error": "Not Found",
        "message": f"Endpoint {request.path} não encontrado"
    }), 404


@app.errorhandler(405)
def handle_405(e):
    """Handler para 405 Method Not Allowed"""
    logger.warning(f"405: {request.method} {request.path}")
    return jsonify({
        "status": 405,
        "error": "Method Not Allowed",
        "message": f"Método {request.method} não permitido para {request.path}"
    }), 405


@app.errorhandler(500)
def handle_500(e):
    """Handler para 500"""
    error_id = f"ERR-{hash(str(e)) % 10000}"
    logger.error(f"Erro 500 [{error_id}]: {str(e)}", exc_info=True)
    return jsonify({
        "status": 500,
        "error": "Internal Server Error",
        "message": "Ocorreu um erro interno",
        "error_id": error_id
    }), 500


@app.errorhandler(Exception)
def handle_generic_error(e):
    """Handler genérico para exceções não tratadas"""
    error_id = f"ERR-{hash(str(e)) % 10000}"
    logger.error(f"Erro não tratado [{error_id}]: {type(e).__name__}: {str(e)}", exc_info=True)
    return jsonify({
        "status": 500,
        "error": "Internal Server Error",
        "message": "Ocorreu um erro inesperado",
        "error_id": error_id
    }), 500


# ============================================
# 3. TRATAMENTO DE ERROS COM TRY/EXCEPT
# ============================================

@app.route('/api/exemplo/tratamento', methods=['POST'])
def exemplo_tratamento():
    """Exemplo de tratamento adequado de erros"""
    
    try:
        if not request.is_json:
            raise ValueError("Content-Type deve ser application/json")
        
        dados = request.get_json()
        
        if not dados:
            raise ValueError("Dados JSON necessários")
        
        # Processamento que pode falhar
        resultado = processar_dados(dados)
        
        logger.info("Dados processados com sucesso")
        return jsonify({
            "status": 200,
            "data": resultado
        }), 200
    
    except ValueError as e:
        logger.warning(f"Erro de validação: {str(e)}")
        return jsonify({
            "status": 400,
            "error": "Bad Request",
            "message": str(e)
        }), 400
    
    except KeyError as e:
        logger.warning(f"Campo obrigatório faltando: {str(e)}")
        return jsonify({
            "status": 400,
            "error": "Bad Request",
            "message": f"Campo obrigatório faltando: {str(e)}"
        }), 400
    
    except Exception as e:
        error_id = f"ERR-{hash(str(e)) % 10000}"
        logger.error(f"Erro ao processar [{error_id}]: {type(e).__name__}: {str(e)}", exc_info=True)
        return jsonify({
            "status": 500,
            "error": "Internal Server Error",
            "message": "Erro ao processar requisição",
            "error_id": error_id
        }), 500


def processar_dados(dados):
    """Função que processa dados (pode gerar erros)"""
    if 'operacao' not in dados:
        raise KeyError("operacao")
    
    if dados['operacao'] == 'erro':
        raise ValueError("Erro simulado")
    
    return {"processado": True, "dados": dados}


# ============================================
# 4. EXERCÍCIOS PRÁTICOS
# ============================================

print("\n" + "=" * 60)
print("EXERCÍCIOS DE TRATAMENTO DE ERROS")
print("=" * 60)

exercicios = """
1. Implementar validação completa:
   - Validar todos os campos obrigatórios
   - Validar tipos de dados
   - Validar ranges (idade, preço, etc.)
   - Retornar lista de todos os erros

2. Tratar erros de banco de dados:
   - Conexão falha → 503 Service Unavailable
   - Query inválida → 400 Bad Request
   - Recurso não encontrado → 404 Not Found

3. Tratar erros de serviços externos:
   - Timeout → 504 Gateway Timeout
   - Serviço offline → 503 Service Unavailable
   - Retry logic

4. Implementar retry com backoff:
   - Tentar novamente em caso de erro transitório
   - Esperar antes de retentar
   - Limitar número de tentativas

5. Logging de erros:
   - Registrar todos os erros
   - Incluir contexto relevante
   - Não expor dados sensíveis
"""

print(exercicios)


# ============================================
# 5. PADRÃO DE TRATAMENTO
# ============================================

class ErrorHandler:
    """Classe para tratamento padronizado de erros"""
    
    @staticmethod
    def handle_validation_error(erros):
        """Trata erros de validação"""
        logger.warning(f"Erros de validação: {erros}")
        return jsonify({
            "status": 422,
            "error": "ValidationError",
            "message": "Erros de validação encontrados",
            "validation_errors": erros
        }), 422
    
    @staticmethod
    def handle_not_found(resource, resource_id=None):
        """Trata recurso não encontrado"""
        logger.warning(f"Recurso não encontrado: {resource} (ID: {resource_id})")
        message = f"{resource} não encontrado"
        if resource_id:
            message += f" (ID: {resource_id})"
        
        return jsonify({
            "status": 404,
            "error": "NotFound",
            "message": message
        }), 404
    
    @staticmethod
    def handle_unauthorized(message="Autenticação necessária"):
        """Trata erro de autenticação"""
        logger.warning(f"Não autorizado: {message}")
        return jsonify({
            "status": 401,
            "error": "Unauthorized",
            "message": message
        }), 401
    
    @staticmethod
    def handle_forbidden(message="Acesso negado"):
        """Trata erro de autorização"""
        logger.warning(f"Acesso negado: {message}")
        return jsonify({
            "status": 403,
            "error": "Forbidden",
            "message": message
        }), 403
    
    @staticmethod
    def handle_server_error(error, error_id=None):
        """Trata erro do servidor"""
        if not error_id:
            error_id = f"ERR-{hash(str(error)) % 10000}"
        
        logger.error(f"Erro do servidor [{error_id}]: {type(error).__name__}: {str(error)}", exc_info=True)
        
        return jsonify({
            "status": 500,
            "error": "InternalServerError",
            "message": "Ocorreu um erro interno. Tente novamente mais tarde.",
            "error_id": error_id
        }), 500


# Exemplo de uso
error_handler = ErrorHandler()

@app.route('/api/exemplo/error-handler', methods=['POST'])
def exemplo_error_handler():
    """Exemplo usando ErrorHandler"""
    
    try:
        dados = request.get_json()
        
        if not dados:
            return error_handler.handle_validation_error([
                {"field": "body", "message": "Dados JSON necessários"}
            ])
        
        if 'id' not in dados:
            return error_handler.handle_not_found("Usuário", dados.get('id'))
        
        return jsonify({"status": "ok"}), 200
    
    except Exception as e:
        return error_handler.handle_server_error(e)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - TRATAMENTO DE ERROS")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Tipos de erros:
   - Erros do cliente (4xx)
   - Erros do servidor (5xx)

2. Tratamento:
   - Try/except apropriado
   - Handlers globais
   - Classes auxiliares

3. Logging:
   - Registrar todos os erros
   - Incluir contexto
   - Error IDs para rastreamento

4. Boas práticas:
   - Mensagens claras
   - Não expor detalhes em produção
   - Status codes apropriados
   - Formato consistente
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 05_tratamento_erros.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

