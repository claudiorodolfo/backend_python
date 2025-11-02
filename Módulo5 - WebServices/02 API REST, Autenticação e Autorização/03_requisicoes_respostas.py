"""
03 - Manipulação de Requisições e Respostas HTTP
==================================================
Trabalhando com headers, body, query parameters e formatos de resposta
"""

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

print("=" * 60)
print("MANIPULAÇÃO DE REQUISIÇÕES E RESPOSTAS")
print("=" * 60)


# ============================================
# 1. ACESSANDO DADOS DA REQUISIÇÃO
# ============================================

@app.route('/api/exemplo/requisicao', methods=['GET', 'POST', 'PUT', 'PATCH'])
def exemplo_requisicao():
    """Demonstra como acessar diferentes partes da requisição"""
    
    dados = {
        "method": request.method,
        "url": request.url,
        "path": request.path,
        "query_string": request.query_string.decode('utf-8'),
    }
    
    # Query parameters
    if request.args:
        dados["query_params"] = dict(request.args)
    
    # Headers
    dados["headers"] = {
        "Content-Type": request.headers.get('Content-Type'),
        "Accept": request.headers.get('Accept'),
        "Authorization": request.headers.get('Authorization'),
        "User-Agent": request.headers.get('User-Agent')
    }
    
    # Body (JSON)
    if request.is_json:
        dados["json_body"] = request.get_json()
    
    # Form data
    if request.form:
        dados["form_data"] = dict(request.form)
    
    # Files
    if request.files:
        dados["files"] = list(request.files.keys())
    
    return jsonify(dados), 200


# ============================================
# 2. TRABALHANDO COM HEADERS
# ============================================

@app.route('/api/exemplo/headers', methods=['GET'])
def exemplo_headers():
    """Demonstra leitura e escrita de headers"""
    
    # Ler headers da requisição
    content_type = request.headers.get('Content-Type', 'Não especificado')
    accept = request.headers.get('Accept', '*/*')
    user_agent = request.headers.get('User-Agent', 'Desconhecido')
    
    # Criar resposta
    resposta = {
        "headers_recebidos": {
            "Content-Type": content_type,
            "Accept": accept,
            "User-Agent": user_agent
        }
    }
    
    # Criar resposta HTTP com headers customizados
    response = make_response(jsonify(resposta), 200)
    response.headers['X-Custom-Header'] = 'Valor-Customizado'
    response.headers['X-API-Version'] = '1.0'
    response.headers['Cache-Control'] = 'no-cache'
    
    return response


# ============================================
# 3. VALIDAÇÃO DE CONTENT-TYPE
# ============================================

@app.route('/api/exemplo/validate-content-type', methods=['POST'])
def validar_content_type():
    """Valida se o Content-Type é JSON"""
    
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    
    return jsonify({
        "status": 200,
        "message": "JSON válido recebido",
        "data": dados
    }), 200


# ============================================
# 4. QUERY PARAMETERS
# ============================================

@app.route('/api/exemplo/query', methods=['GET'])
def exemplo_query():
    """Trabalha com query parameters"""
    
    # Obter parâmetros individuais
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    busca = request.args.get('search', '')
    
    # Obter todos os parâmetros
    todos_params = request.args.to_dict()
    
    # Obter parâmetros múltiplos (ex: ?tags=python&tags=api)
    tags = request.args.getlist('tags')
    
    return jsonify({
        "status": 200,
        "page": page,
        "limit": limit,
        "search": busca,
        "tags": tags,
        "all_params": todos_params
    }), 200


# ============================================
# 5. TRABALHANDO COM JSON
# ============================================

@app.route('/api/exemplo/json', methods=['POST', 'PUT', 'PATCH'])
def exemplo_json():
    """Manipula dados JSON"""
    
    # Verificar se é JSON
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    
    # Validar estrutura básica
    if not isinstance(dados, dict):
        return jsonify({
            "status": 400,
            "error": "JSON deve ser um objeto"
        }), 400
    
    # Processar dados
    dados_processados = {
        "recebido": dados,
        "campos": list(dados.keys()),
        "total_campos": len(dados)
    }
    
    return jsonify({
        "status": 200,
        "message": "Dados JSON processados com sucesso",
        "data": dados_processados
    }), 200


# ============================================
# 6. RESPOSTAS COM DIFERENTES STATUS CODES
# ============================================

@app.route('/api/exemplo/status/<int:code>', methods=['GET'])
def exemplo_status(code):
    """Retorna diferentes status codes"""
    
    status_codes = {
        200: {"message": "OK - Sucesso"},
        201: {"message": "Created - Recurso criado"},
        204: {"message": "No Content - Sucesso sem conteúdo"},
        400: {"message": "Bad Request - Requisição inválida"},
        401: {"message": "Unauthorized - Não autenticado"},
        403: {"message": "Forbidden - Sem permissão"},
        404: {"message": "Not Found - Recurso não encontrado"},
        500: {"message": "Internal Server Error - Erro do servidor"}
    }
    
    if code in status_codes:
        mensagem = status_codes[code]
        
        # 204 não deve ter body
        if code == 204:
            response = make_response('', 204)
        else:
            response = jsonify({
                "status": code,
                **mensagem
            })
            response.status_code = code
        
        return response
    else:
        return jsonify({
            "status": 400,
            "error": f"Status code {code} não é um código válido para este exemplo"
        }), 400


# ============================================
# 7. FORMATAÇÃO DE RESPOSTAS PADRONIZADAS
# ============================================

class RespostaAPI:
    """Classe auxiliar para padronizar respostas"""
    
    @staticmethod
    def sucesso(dados=None, mensagem="Operação realizada com sucesso", status=200):
        """Resposta de sucesso padronizada"""
        resposta = {
            "success": True,
            "status": status,
            "message": mensagem
        }
        if dados is not None:
            resposta["data"] = dados
        return jsonify(resposta), status
    
    @staticmethod
    def erro(mensagem, status=400, detalhes=None):
        """Resposta de erro padronizada"""
        resposta = {
            "success": False,
            "status": status,
            "error": mensagem
        }
        if detalhes:
            resposta["details"] = detalhes
        return jsonify(resposta), status
    
    @staticmethod
    def criado(dados, location=None):
        """Resposta 201 Created"""
        resposta = {
            "success": True,
            "status": 201,
            "message": "Recurso criado com sucesso",
            "data": dados
        }
        if location:
            resposta["location"] = location
        
        response = make_response(jsonify(resposta), 201)
        if location:
            response.headers['Location'] = location
        return response


@app.route('/api/exemplo/resposta-sucesso', methods=['GET'])
def exemplo_resposta_sucesso():
    """Exemplo de resposta de sucesso"""
    dados = {"id": 1, "nome": "João", "email": "joao@example.com"}
    return RespostaAPI.sucesso(dados, "Usuário encontrado")


@app.route('/api/exemplo/resposta-erro', methods=['GET'])
def exemplo_resposta_erro():
    """Exemplo de resposta de erro"""
    return RespostaAPI.erro(
        "Recurso não encontrado",
        status=404,
        detalhes={"recurso_id": 999}
    )


@app.route('/api/exemplo/resposta-criado', methods=['POST'])
def exemplo_resposta_criado():
    """Exemplo de resposta 201 Created"""
    dados = request.get_json() or {}
    novo_recurso = {"id": 123, **dados}
    return RespostaAPI.criado(
        novo_recurso,
        location="/api/exemplo/resposta-criado/123"
    )


# ============================================
# 8. TRATAMENTO DE ERROS EM REQUISIÇÕES
# ============================================

@app.route('/api/exemplo/validacao', methods=['POST'])
def exemplo_validacao():
    """Exemplo de validação de dados"""
    
    if not request.is_json:
        return RespostaAPI.erro("Content-Type deve ser application/json", 400)
    
    dados = request.get_json()
    erros = []
    
    # Validar campos obrigatórios
    if 'nome' not in dados:
        erros.append("Campo 'nome' é obrigatório")
    
    if 'email' not in dados:
        erros.append("Campo 'email' é obrigatório")
    elif '@' not in dados.get('email', ''):
        erros.append("Email inválido")
    
    # Validar tipos
    if 'idade' in dados and not isinstance(dados['idade'], int):
        erros.append("Campo 'idade' deve ser um número inteiro")
    
    if erros:
        return RespostaAPI.erro(
            "Erros de validação",
            status=422,
            detalhes={"validation_errors": erros}
        )
    
    return RespostaAPI.sucesso(dados, "Dados válidos")


# ============================================
# 9. EXEMPLO COMPLETO - API DE USUÁRIOS
# ============================================

usuarios_exemplo = {
    1: {"id": 1, "nome": "João Silva", "email": "joao@example.com", "idade": 30},
    2: {"id": 2, "nome": "Maria Santos", "email": "maria@example.com", "idade": 25}
}


@app.route('/api/usuarios', methods=['GET'])
def listar_usuarios():
    """GET - Lista usuários com filtros"""
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    usuarios_lista = list(usuarios_exemplo.values())
    total = len(usuarios_lista)
    
    inicio = (page - 1) * limit
    fim = inicio + limit
    usuarios_paginados = usuarios_lista[inicio:fim]
    
    return RespostaAPI.sucesso({
        "usuarios": usuarios_paginados,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit
        }
    })


@app.route('/api/usuarios/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    """GET - Obter usuário específico"""
    usuario = usuarios_exemplo.get(user_id)
    
    if not usuario:
        return RespostaAPI.erro(f"Usuário {user_id} não encontrado", 404)
    
    return RespostaAPI.sucesso(usuario, "Usuário encontrado")


@app.route('/api/usuarios', methods=['POST'])
def criar_usuario():
    """POST - Criar novo usuário"""
    if not request.is_json:
        return RespostaAPI.erro("Content-Type deve ser application/json", 400)
    
    dados = request.get_json()
    
    # Validação
    if 'nome' not in dados or 'email' not in dados:
        return RespostaAPI.erro(
            "Campos 'nome' e 'email' são obrigatórios",
            status=422
        )
    
    # Criar novo usuário
    novo_id = max(usuarios_exemplo.keys()) + 1 if usuarios_exemplo else 1
    novo_usuario = {
        "id": novo_id,
        "nome": dados['nome'],
        "email": dados['email'],
        "idade": dados.get('idade')
    }
    
    usuarios_exemplo[novo_id] = novo_usuario
    
    return RespostaAPI.criado(
        novo_usuario,
        location=f"/api/usuarios/{novo_id}"
    )


print("\n" + "=" * 60)
print("RESUMO - REQUISIÇÕES E RESPOSTAS")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Acessar dados da requisição:
   - request.method - Método HTTP
   - request.args - Query parameters
   - request.get_json() - Body JSON
   - request.headers - Headers HTTP

2. Criar respostas:
   - jsonify() - Resposta JSON
   - make_response() - Resposta customizada
   - Status codes apropriados

3. Headers:
   - Ler: request.headers.get('Header-Name')
   - Escrever: response.headers['Header'] = 'Value'

4. Validação:
   - Verificar Content-Type
   - Validar estrutura de dados
   - Retornar erros claros

5. Padronização:
   - Usar classe auxiliar para respostas
   - Manter formato consistente
   - Incluir informações úteis

Próximos passos:
- Enviar dados JSON complexos
- Testar com Postman ou curl
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 03_requisicoes_respostas.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

