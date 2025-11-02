"""
02 - Criando Rotas Simples
============================
Exemplos práticos de criação de rotas em Flask
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

print("=" * 60)
print("CRIANDO ROTAS SIMPLES")
print("=" * 60)


# ============================================
# 1. ROTAS BÁSICAS - GET
# ============================================

@app.route('/api/users', methods=['GET'])
def listar_usuarios():
    """GET - Lista todos os usuários"""
    usuarios = [
        {"id": 1, "nome": "João Silva", "email": "joao@example.com"},
        {"id": 2, "nome": "Maria Santos", "email": "maria@example.com"},
        {"id": 3, "nome": "Pedro Costa", "email": "pedro@example.com"}
    ]
    return jsonify({
        "status": 200,
        "total": len(usuarios),
        "data": usuarios
    }), 200


@app.route('/api/users/<int:user_id>', methods=['GET'])
def obter_usuario(user_id):
    """GET - Obter usuário específico por ID"""
    # Simulação de busca em banco de dados
    usuarios = {
        1: {"id": 1, "nome": "João Silva", "email": "joao@example.com", "idade": 30},
        2: {"id": 2, "nome": "Maria Santos", "email": "maria@example.com", "idade": 25},
        3: {"id": 3, "nome": "Pedro Costa", "email": "pedro@example.com", "idade": 35}
    }
    
    usuario = usuarios.get(user_id)
    if usuario:
        return jsonify({
            "status": 200,
            "data": usuario
        }), 200
    else:
        return jsonify({
            "status": 404,
            "error": f"Usuário com ID {user_id} não encontrado"
        }), 404


# ============================================
# 2. ROTAS COM POST - CRIAR RECURSO
# ============================================

@app.route('/api/users', methods=['POST'])
def criar_usuario():
    """POST - Criar novo usuário"""
    dados = request.get_json()
    
    # Validação básica
    if not dados:
        return jsonify({
            "status": 400,
            "error": "Dados JSON necessários"
        }), 400
    
    campos_obrigatorios = ['nome', 'email']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({
                "status": 400,
                "error": f"Campo '{campo}' é obrigatório"
            }), 400
    
    # Simulação: gerar novo ID
    novo_usuario = {
        "id": 4,  # Em produção, viria do banco de dados
        "nome": dados['nome'],
        "email": dados['email'],
        "idade": dados.get('idade', None)
    }
    
    return jsonify({
        "status": 201,
        "message": "Usuário criado com sucesso",
        "data": novo_usuario,
        "location": f"/api/users/{novo_usuario['id']}"
    }), 201


# ============================================
# 3. ROTAS COM PUT - ATUALIZAR COMPLETAMENTE
# ============================================

# Simulação de armazenamento em memória
usuarios_db = {
    1: {"id": 1, "nome": "João Silva", "email": "joao@example.com", "idade": 30},
    2: {"id": 2, "nome": "Maria Santos", "email": "maria@example.com", "idade": 25},
    3: {"id": 3, "nome": "Pedro Costa", "email": "pedro@example.com", "idade": 35}
}


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    """PUT - Atualizar usuário completamente"""
    if user_id not in usuarios_db:
        return jsonify({
            "status": 404,
            "error": f"Usuário com ID {user_id} não encontrado"
        }), 404
    
    dados = request.get_json()
    if not dados:
        return jsonify({
            "status": 400,
            "error": "Dados JSON necessários"
        }), 400
    
    # Substituir completamente
    usuarios_db[user_id] = {
        "id": user_id,
        **dados  # Atualiza com todos os dados enviados
    }
    
    return jsonify({
        "status": 200,
        "message": "Usuário atualizado com sucesso",
        "data": usuarios_db[user_id]
    }), 200


# ============================================
# 4. ROTAS COM PATCH - ATUALIZAÇÃO PARCIAL
# ============================================

@app.route('/api/users/<int:user_id>', methods=['PATCH'])
def atualizar_usuario_parcial(user_id):
    """PATCH - Atualizar usuário parcialmente"""
    if user_id not in usuarios_db:
        return jsonify({
            "status": 404,
            "error": f"Usuário com ID {user_id} não encontrado"
        }), 404
    
    dados = request.get_json()
    if not dados:
        return jsonify({
            "status": 400,
            "error": "Dados JSON necessários"
        }), 400
    
    # Atualizar apenas campos enviados
    usuarios_db[user_id].update(dados)
    
    return jsonify({
        "status": 200,
        "message": "Usuário atualizado parcialmente",
        "data": usuarios_db[user_id]
    }), 200


# ============================================
# 5. ROTAS COM DELETE
# ============================================

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def deletar_usuario(user_id):
    """DELETE - Deletar usuário"""
    if user_id not in usuarios_db:
        return jsonify({
            "status": 404,
            "error": f"Usuário com ID {user_id} não encontrado"
        }), 404
    
    del usuarios_db[user_id]
    
    return jsonify({
        "status": 204,
        "message": "Usuário deletado com sucesso"
    }), 204


# ============================================
# 6. ROTAS COM QUERY PARAMETERS
# ============================================

@app.route('/api/users', methods=['GET'])
def listar_usuarios_com_filtros():
    """GET - Lista usuários com filtros via query parameters"""
    # Obter query parameters
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    busca = request.args.get('search', '')
    ordenar = request.args.get('sort', 'id')
    
    # Todos os usuários
    todos_usuarios = list(usuarios_db.values())
    
    # Filtro por busca
    if busca:
        todos_usuarios = [
            u for u in todos_usuarios
            if busca.lower() in u['nome'].lower() or busca.lower() in u['email'].lower()
        ]
    
    # Ordenação
    if ordenar in ['nome', 'email', 'idade', 'id']:
        todos_usuarios.sort(key=lambda x: x.get(ordenar, ''))
    
    # Paginação
    inicio = (page - 1) * limit
    fim = inicio + limit
    usuarios_paginados = todos_usuarios[inicio:fim]
    
    return jsonify({
        "status": 200,
        "page": page,
        "limit": limit,
        "total": len(todos_usuarios),
        "data": usuarios_paginados
    }), 200


# ============================================
# 7. EXEMPLO COMPLETO - CRUD COMPLETO
# ============================================

print("\n" + "=" * 60)
print("ROTAS CRIADAS")
print("=" * 60)
print("""
Endpoints disponíveis:

GET    /api/users              → Lista todos os usuários
GET    /api/users?page=1&limit=10 → Lista com paginação e filtros
GET    /api/users/<id>         → Obter usuário específico
POST   /api/users              → Criar novo usuário
PUT    /api/users/<id>         → Atualizar usuário completamente
PATCH  /api/users/<id>         → Atualizar usuário parcialmente
DELETE /api/users/<id>         → Deletar usuário

Exemplos de uso:

1. Criar usuário:
   POST /api/users
   Body: {"nome": "João", "email": "joao@example.com", "idade": 30}

2. Atualizar parcialmente:
   PATCH /api/users/1
   Body: {"idade": 31}

3. Buscar usuários:
   GET /api/users?search=joão&sort=nome&page=1&limit=5
""")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - ROTAS SIMPLES")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Rotas GET:
   - Recuperar dados
   - Pode receber parâmetros de rota (<int:id>)
   - Pode receber query parameters (?page=1)

2. Rotas POST:
   - Criar novos recursos
   - Dados vêm no body (JSON)
   - Retorna 201 Created

3. Rotas PUT:
   - Atualizar recurso completamente
   - Substitui todos os campos

4. Rotas PATCH:
   - Atualizar recurso parcialmente
   - Atualiza apenas campos enviados

5. Rotas DELETE:
   - Remover recurso
   - Retorna 204 No Content

Próximos passos:
- Manipular requisições e respostas mais complexas
- Enviar e receber dados JSON
- Testar com Postman ou curl
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 02_rotas_simples.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

