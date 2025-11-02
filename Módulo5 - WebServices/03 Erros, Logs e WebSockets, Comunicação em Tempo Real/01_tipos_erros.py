"""
01 - Tipos Comuns de Erros em WebServices
===========================================
Exploração dos tipos de erros mais comuns em APIs
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

print("=" * 60)
print("TIPOS DE ERROS EM WEBSERVICES")
print("=" * 60)


# ============================================
# 1. ERROS DO CLIENTE (4xx)
# ============================================

"""
Erros 4xx - Erro do Cliente:
---------------------------
O cliente fez uma requisição inválida. O servidor não processou a requisição.
"""

@app.route('/api/erros/400', methods=['POST'])
def erro_400_exemplo():
    """400 Bad Request - Requisição mal formada"""
    
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Bad Request",
            "message": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    
    # Exemplo: campo obrigatório faltando
    if 'nome' not in dados:
        return jsonify({
            "status": 400,
            "error": "Bad Request",
            "message": "Campo 'nome' é obrigatório"
        }), 400
    
    return jsonify({"status": "ok"}), 200


@app.route('/api/erros/401', methods=['GET'])
def erro_401_exemplo():
    """401 Unauthorized - Não autenticado"""
    
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({
            "status": 401,
            "error": "Unauthorized",
            "message": "Token de autenticação necessário"
        }), 401
    
    return jsonify({"status": "ok"}), 200


@app.route('/api/erros/403', methods=['GET'])
def erro_403_exemplo():
    """403 Forbidden - Sem permissão"""
    
    # Simulação: usuário comum tentando acessar área admin
    role = request.headers.get('X-User-Role', 'user')
    
    if role != 'admin':
        return jsonify({
            "status": 403,
            "error": "Forbidden",
            "message": "Acesso negado. Você não tem permissão para este recurso."
        }), 403
    
    return jsonify({"status": "ok"}), 200


@app.route('/api/erros/404', methods=['GET'])
def erro_404_exemplo():
    """404 Not Found - Recurso não encontrado"""
    
    recurso_id = request.args.get('id')
    
    # Simulação: recurso não existe
    recursos = {1: "Recurso 1", 2: "Recurso 2"}
    
    if not recurso_id or int(recurso_id) not in recursos:
        return jsonify({
            "status": 404,
            "error": "Not Found",
            "message": f"Recurso com ID {recurso_id} não encontrado"
        }), 404
    
    return jsonify({"data": recursos[int(recurso_id)]}), 200


@app.route('/api/erros/422', methods=['POST'])
def erro_422_exemplo():
    """422 Unprocessable Entity - Erro de validação"""
    
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    erros = []
    
    # Validações
    if 'email' in dados and '@' not in dados['email']:
        erros.append("Email inválido")
    
    if 'idade' in dados and (not isinstance(dados['idade'], int) or dados['idade'] < 0):
        erros.append("Idade deve ser um número inteiro positivo")
    
    if erros:
        return jsonify({
            "status": 422,
            "error": "Unprocessable Entity",
            "message": "Erros de validação",
            "validation_errors": erros
        }), 422
    
    return jsonify({"status": "ok"}), 200


# ============================================
# 2. ERROS DO SERVIDOR (5xx)
# ============================================

"""
Erros 5xx - Erro do Servidor:
-----------------------------
Erro interno do servidor. O servidor não conseguiu processar a requisição.
"""

@app.route('/api/erros/500', methods=['GET'])
def erro_500_exemplo():
    """500 Internal Server Error - Erro interno"""
    
    # Simulação de erro interno
    try:
        # Código que pode falhar
        resultado = 1 / 0  # Isso vai gerar ZeroDivisionError
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        # Em produção, não exponha detalhes do erro
        return jsonify({
            "status": 500,
            "error": "Internal Server Error",
            "message": "Ocorreu um erro interno. Tente novamente mais tarde."
            # Não exponha: "message": str(e) em produção
        }), 500


@app.route('/api/erros/503', methods=['GET'])
def erro_503_exemplo():
    """503 Service Unavailable - Serviço indisponível"""
    
    # Simulação: serviço em manutenção
    em_manutencao = True  # Em produção, viria de configuração
    
    if em_manutencao:
        return jsonify({
            "status": 503,
            "error": "Service Unavailable",
            "message": "Serviço temporariamente indisponível para manutenção"
        }), 503
    
    return jsonify({"status": "ok"}), 200


# ============================================
# 3. CATEGORIZAÇÃO DE ERROS
# ============================================

print("\n" + "=" * 60)
print("CATEGORIZAÇÃO DE ERROS")
print("=" * 60)

categorias_erros = {
    "Erros de Validação": {
        "codigos": [400, 422],
        "causas": [
            "Dados faltando",
            "Formato incorreto",
            "Tipos inválidos",
            "Valores fora do range permitido"
        ],
        "solução": "Validar dados de entrada antes de processar"
    },
    "Erros de Autenticação": {
        "codigos": [401],
        "causas": [
            "Token ausente",
            "Token inválido",
            "Token expirado",
            "Credenciais incorretas"
        ],
        "solução": "Implementar autenticação adequada"
    },
    "Erros de Autorização": {
        "codigos": [403],
        "causas": [
            "Usuário sem permissão",
            "Role insuficiente",
            "Tentativa de acessar recurso de outro usuário"
        ],
        "solução": "Verificar permissões antes de acessar recursos"
    },
    "Erros de Recurso": {
        "codigos": [404],
        "causas": [
            "URL incorreta",
            "Recurso não existe",
            "ID inválido"
        ],
        "solução": "Verificar se recurso existe antes de processar"
    },
    "Erros de Servidor": {
        "codigos": [500, 502, 503],
        "causas": [
            "Bug no código",
            "Erro no banco de dados",
            "Serviço externo indisponível",
            "Sobrecarga do servidor"
        ],
        "solução": "Tratar exceções, monitorar erros, ter fallbacks"
    }
}

for categoria, info in categorias_erros.items():
    print(f"\n{categoria}:")
    print(f"  Códigos: {info['codigos']}")
    print(f"  Causas comuns:")
    for causa in info['causas']:
        print(f"    - {causa}")
    print(f"  Solução: {info['solução']}")


# ============================================
# 4. BOAS PRÁTICAS PARA ERROS
# ============================================

print("\n" + "=" * 60)
print("BOAS PRÁTICAS PARA TRATAMENTO DE ERROS")
print("=" * 60)

boas_praticas = """
1. Sempre retorne status code apropriado:
   - 4xx para erros do cliente
   - 5xx para erros do servidor

2. Mensagens de erro claras e úteis:
   - O que está errado?
   - Como corrigir?
   - Evite mensagens técnicas genéricas

3. Formato consistente de erro:
   {
     "status": 400,
     "error": "Nome do erro",
     "message": "Descrição clara",
     "details": {...}  // Opcional
   }

4. Em produção:
   - Não exponha stack traces
   - Não exponha detalhes de código
   - Use IDs de erro para rastreamento

5. Em desenvolvimento:
   - Mais detalhes são úteis
   - Stack traces ajudam no debug
   - Logs detalhados

6. Erros de validação:
   - Liste todos os erros
   - Seja específico sobre o campo
   - Forneça exemplos se útil
"""

print(boas_praticas)


# ============================================
# 5. EXEMPLO DE CLASSE PARA ERROS
# ============================================

class APIError(Exception):
    """Classe base para erros de API"""
    def __init__(self, message, status_code=400, details=None):
        self.message = message
        self.status_code = status_code
        self.details = details or {}


class ValidationError(APIError):
    """Erro de validação"""
    def __init__(self, message, validation_errors=None):
        super().__init__(
            message,
            status_code=422,
            details={"validation_errors": validation_errors or []}
        )


class NotFoundError(APIError):
    """Recurso não encontrado"""
    def __init__(self, message="Recurso não encontrado"):
        super().__init__(message, status_code=404)


class UnauthorizedError(APIError):
    """Não autenticado"""
    def __init__(self, message="Autenticação necessária"):
        super().__init__(message, status_code=401)


class ForbiddenError(APIError):
    """Sem permissão"""
    def __init__(self, message="Acesso negado"):
        super().__init__(message, status_code=403)


# Handler global de erros
@app.errorhandler(APIError)
def handle_api_error(error):
    """Handler para erros customizados da API"""
    response = {
        "status": error.status_code,
        "error": error.__class__.__name__,
        "message": error.message
    }
    if error.details:
        response["details"] = error.details
    
    return jsonify(response), error.status_code


@app.errorhandler(404)
def handle_not_found(e):
    """Handler para 404"""
    return jsonify({
        "status": 404,
        "error": "Not Found",
        "message": "Endpoint não encontrado"
    }), 404


@app.errorhandler(500)
def handle_internal_error(e):
    """Handler para 500"""
    return jsonify({
        "status": 500,
        "error": "Internal Server Error",
        "message": "Ocorreu um erro interno"
    }), 500


# Exemplo de uso
@app.route('/api/exemplo/erro-customizado', methods=['POST'])
def exemplo_erro_customizado():
    """Exemplo usando erros customizados"""
    
    dados = request.get_json()
    
    if not dados:
        raise ValidationError("Dados JSON necessários")
    
    if 'id' not in dados:
        raise ValidationError(
            "Campo 'id' é obrigatório",
            validation_errors=["id: campo obrigatório"]
        )
    
    recurso_id = dados['id']
    if recurso_id not in [1, 2, 3]:
        raise NotFoundError(f"Recurso {recurso_id} não encontrado")
    
    return jsonify({"status": "ok"}), 200


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - TIPOS DE ERROS")
print("=" * 60)
print("""
Tipos de erros comuns:

1. Erros do Cliente (4xx):
   - 400 Bad Request
   - 401 Unauthorized
   - 403 Forbidden
   - 404 Not Found
   - 422 Unprocessable Entity

2. Erros do Servidor (5xx):
   - 500 Internal Server Error
   - 502 Bad Gateway
   - 503 Service Unavailable

3. Boas práticas:
   - Status codes apropriados
   - Mensagens claras
   - Formato consistente
   - Não expor detalhes em produção

4. Tratamento:
   - Use classes de erro customizadas
   - Handlers globais
   - Logs adequados
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 01_tipos_erros.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

