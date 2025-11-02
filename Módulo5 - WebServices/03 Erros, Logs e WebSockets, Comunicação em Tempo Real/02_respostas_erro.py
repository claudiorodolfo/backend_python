"""
02 - Respostas de Erro Padronizadas
======================================
Como retornar respostas de erro consistentes e úteis
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

print("=" * 60)
print("RESPOSTAS DE ERRO PADRONIZADAS")
print("=" * 60)


# ============================================
# 1. CLASSE PARA RESPOSTAS PADRONIZADAS
# ============================================

class RespostaErro:
    """Classe para criar respostas de erro padronizadas"""
    
    def __init__(self, status_code, error_type, message, details=None, error_id=None):
        self.status_code = status_code
        self.error_type = error_type
        self.message = message
        self.details = details or {}
        self.error_id = error_id or str(uuid.uuid4())
        self.timestamp = datetime.utcnow().isoformat()
    
    def to_dict(self):
        """Converte para dicionário"""
        resposta = {
            "success": False,
            "status": self.status_code,
            "error": {
                "type": self.error_type,
                "message": self.message,
                "error_id": self.error_id,
                "timestamp": self.timestamp
            }
        }
        
        if self.details:
            resposta["error"]["details"] = self.details
        
        return resposta
    
    def to_response(self):
        """Retorna resposta Flask"""
        return jsonify(self.to_dict()), self.status_code


# ============================================
# 2. FUNÇÕES AUXILIARES PARA ERROS COMUNS
# ============================================

def erro_bad_request(message="Requisição inválida", details=None):
    """400 Bad Request"""
    return RespostaErro(
        status_code=400,
        error_type="BadRequest",
        message=message,
        details=details
    ).to_response()


def erro_unauthorized(message="Autenticação necessária", details=None):
    """401 Unauthorized"""
    return RespostaErro(
        status_code=401,
        error_type="Unauthorized",
        message=message,
        details=details
    ).to_response()


def erro_forbidden(message="Acesso negado", details=None):
    """403 Forbidden"""
    return RespostaErro(
        status_code=403,
        error_type="Forbidden",
        message=message,
        details=details
    ).to_response()


def erro_not_found(resource="Recurso", resource_id=None, details=None):
    """404 Not Found"""
    message = f"{resource} não encontrado"
    if resource_id:
        message += f" (ID: {resource_id})"
    
    return RespostaErro(
        status_code=404,
        error_type="NotFound",
        message=message,
        details=details
    ).to_response()


def erro_validation(validation_errors, message="Erros de validação"):
    """422 Unprocessable Entity"""
    return RespostaErro(
        status_code=422,
        error_type="ValidationError",
        message=message,
        details={"validation_errors": validation_errors}
    ).to_response()


def erro_server(message="Erro interno do servidor", error_id=None):
    """500 Internal Server Error"""
    return RespostaErro(
        status_code=500,
        error_type="InternalServerError",
        message=message,
        error_id=error_id
    ).to_response()


# ============================================
# 3. EXEMPLOS DE USO
# ============================================

@app.route('/api/exemplo/bad-request', methods=['POST'])
def exemplo_bad_request():
    """Exemplo de Bad Request"""
    
    if not request.is_json:
        return erro_bad_request(
            "Content-Type deve ser application/json",
            details={"expected": "application/json"}
        )
    
    dados = request.get_json()
    
    if 'campo_obrigatorio' not in dados:
        return erro_bad_request(
            "Campo obrigatório faltando",
            details={
                "missing_field": "campo_obrigatorio",
                "required_fields": ["campo_obrigatorio"]
            }
        )
    
    return jsonify({"status": "ok"}), 200


@app.route('/api/exemplo/validation', methods=['POST'])
def exemplo_validation():
    """Exemplo de erro de validação"""
    
    if not request.is_json:
        return erro_bad_request("Content-Type deve ser application/json")
    
    dados = request.get_json()
    erros = []
    
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
    
    if 'idade' in dados:
        if not isinstance(dados['idade'], int):
            erros.append({
                "field": "idade",
                "message": "Deve ser um número inteiro",
                "code": "invalid_type"
            })
        elif dados['idade'] < 0 or dados['idade'] > 150:
            erros.append({
                "field": "idade",
                "message": "Deve estar entre 0 e 150",
                "code": "out_of_range"
            })
    
    if erros:
        return erro_validation(erros)
    
    return jsonify({"status": "ok"}), 200


@app.route('/api/exemplo/not-found', methods=['GET'])
def exemplo_not_found():
    """Exemplo de Not Found"""
    
    recurso_id = request.args.get('id')
    
    # Simulação: recurso não existe
    recursos = {1: "Recurso 1"}
    
    if not recurso_id or int(recurso_id) not in recursos:
        return erro_not_found(
            resource="Usuário",
            resource_id=recurso_id,
            details={"available_ids": list(recursos.keys())}
        )
    
    return jsonify({"data": recursos[int(recurso_id)]}), 200


# ============================================
# 4. FORMATO PADRONIZADO DE ERRO
# ============================================

print("\n" + "=" * 60)
print("FORMATO PADRONIZADO DE ERRO")
print("=" * 60)

formato_exemplo = """
{
  "success": false,
  "status": 422,
  "error": {
    "type": "ValidationError",
    "message": "Erros de validação",
    "error_id": "550e8400-e29b-41d4-a716-446655440000",
    "timestamp": "2024-01-15T10:30:00.000Z",
    "details": {
      "validation_errors": [
        {
          "field": "email",
          "message": "Email inválido",
          "code": "invalid_format"
        },
        {
          "field": "idade",
          "message": "Deve estar entre 0 e 150",
          "code": "out_of_range"
        }
      ]
    }
  }
}
"""

print(formato_exemplo)


# ============================================
# 5. BENEFÍCIOS DA PADRONIZAÇÃO
# ============================================

print("\n" + "=" * 60)
print("BENEFÍCIOS DA PADRONIZAÇÃO")
print("=" * 60)

beneficios = """
✓ Consistência:
  - Todas as respostas seguem o mesmo formato
  - Clientes sabem o que esperar

✓ Rastreamento:
  - error_id único para cada erro
  - Facilita debug e suporte

✓ Informações úteis:
  - Timestamp do erro
  - Detalhes específicos
  - Códigos de erro padronizados

✓ Facilita integração:
  - Clientes podem tratar erros de forma consistente
  - Melhor experiência do desenvolvedor

✓ Debug:
  - error_id pode ser usado para buscar logs
  - Timestamp ajuda a correlacionar eventos
"""

print(beneficios)


# ============================================
# 6. HANDLER GLOBAL DE ERROS
# ============================================

@app.errorhandler(404)
def handle_not_found(e):
    """Handler global para 404"""
    return erro_not_found()


@app.errorhandler(500)
def handle_internal_error(e):
    """Handler global para 500"""
    error_id = str(uuid.uuid4())
    # Em produção, logue o error_id e detalhes do erro
    return erro_server(
        "Ocorreu um erro interno. Tente novamente mais tarde.",
        error_id=error_id
    )


@app.errorhandler(Exception)
def handle_generic_error(e):
    """Handler genérico para exceções não tratadas"""
    error_id = str(uuid.uuid4())
    # Em produção, logue o erro completo
    # Em desenvolvimento, pode expor mais detalhes
    return erro_server(
        "Ocorreu um erro inesperado",
        error_id=error_id
    )


# ============================================
# 7. DIFERENÇA ENTRE DESENVOLVIMENTO E PRODUÇÃO
# ============================================

print("\n" + "=" * 60)
print("DESENVOLVIMENTO vs PRODUÇÃO")
print("=" * 60)

diferencas = """
DESENVOLVIMENTO:
- Mais detalhes no erro
- Stack traces úteis
- Mensagens técnicas
- Facilita debug

PRODUÇÃO:
- Mensagens genéricas
- Sem stack traces
- error_id para rastreamento
- Foco em UX
- Logs completos no servidor

Exemplo:

Desenvolvimento:
{
  "error": "ZeroDivisionError",
  "message": "division by zero",
  "traceback": ["File 'app.py', line 10, ..."]
}

Produção:
{
  "error": {
    "type": "InternalServerError",
    "message": "Ocorreu um erro interno",
    "error_id": "abc-123"
  }
}
"""

print(diferencas)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - RESPOSTAS DE ERRO PADRONIZADAS")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Padronização:
   - Formato consistente de erro
   - Estrutura bem definida
   - Funções auxiliares

2. Informações úteis:
   - error_id para rastreamento
   - timestamp
   - detalhes específicos

3. Boas práticas:
   - Mensagens claras
   - Códigos de erro padronizados
   - Diferentes níveis de detalhe (dev vs prod)

4. Handlers globais:
   - Tratamento centralizado
   - Consistência automática

Próximos passos:
- Implementar logging
- Monitorar erros
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 02_respostas_erro.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

