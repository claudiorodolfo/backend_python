"""
08 - Token Authentication
===========================
Implementação de autenticação baseada em tokens
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import secrets
import hashlib
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'

print("=" * 60)
print("TOKEN AUTHENTICATION")
print("=" * 60)

# ============================================
# 1. BANCO DE USUÁRIOS E TOKENS
# ============================================

usuarios_db = {
    "admin": {
        "username": "admin",
        "password_hash": hashlib.sha256("senha123".encode()).hexdigest(),
        "role": "admin"
    },
    "usuario": {
        "username": "usuario",
        "password_hash": hashlib.sha256("senha456".encode()).hexdigest(),
        "role": "user"
    }
}

# Armazenamento de tokens (em produção, usar banco de dados)
tokens_db = {}  # {token: {"username": "...", "expires_at": datetime, "created_at": datetime}}


# ============================================
# 2. GERAR TOKEN
# ============================================

def gerar_token():
    """Gera um token aleatório seguro"""
    return secrets.token_urlsafe(32)


def criar_token(username, expira_horas=24):
    """Cria um novo token para o usuário"""
    token = gerar_token()
    expires_at = datetime.now() + timedelta(hours=expira_horas)
    
    tokens_db[token] = {
        "username": username,
        "created_at": datetime.now(),
        "expires_at": expires_at
    }
    
    return token, expires_at


def verificar_token(token):
    """Verifica se token é válido"""
    if token not in tokens_db:
        return None
    
    token_data = tokens_db[token]
    
    # Verificar expiração
    if datetime.now() > token_data['expires_at']:
        # Remover token expirado
        del tokens_db[token]
        return None
    
    return token_data


def revogar_token(token):
    """Revoga um token"""
    if token in tokens_db:
        del tokens_db[token]
        return True
    return False


# ============================================
# 3. DECORADOR DE AUTENTICAÇÃO
# ============================================

def requer_token(f):
    """Decorador para proteger rotas com Token Auth"""
    def decorador(*args, **kwargs):
        # Obter token do header Authorization
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({
                "status": 401,
                "error": "Token de autenticação necessário",
                "message": "Header Authorization: Bearer <token> necessário"
            }), 401
        
        token = auth_header.replace('Bearer ', '').strip()
        
        # Verificar token
        token_data = verificar_token(token)
        
        if not token_data:
            return jsonify({
                "status": 401,
                "error": "Token inválido ou expirado",
                "message": "Faça login novamente"
            }), 401
        
        # Obter dados do usuário
        username = token_data['username']
        usuario = usuarios_db[username]
        
        # Adicionar ao request
        request.current_user = usuario
        request.token = token
        
        return f(*args, **kwargs)
    
    decorador.__name__ = f.__name__
    return decorador


# ============================================
# 4. ROTAS DE AUTENTICAÇÃO
# ============================================

@app.route('/api/login', methods=['POST'])
def login():
    """Endpoint de login - retorna token"""
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    username = dados.get('username')
    password = dados.get('password')
    
    if not username or not password:
        return jsonify({
            "status": 400,
            "error": "Username e password são obrigatórios"
        }), 400
    
    # Verificar credenciais
    if username not in usuarios_db:
        return jsonify({
            "status": 401,
            "error": "Credenciais inválidas"
        }), 401
    
    usuario = usuarios_db[username]
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if password_hash != usuario['password_hash']:
        return jsonify({
            "status": 401,
            "error": "Credenciais inválidas"
        }), 401
    
    # Gerar token
    token, expires_at = criar_token(username, expira_horas=24)
    
    return jsonify({
        "status": 200,
        "message": "Login realizado com sucesso",
        "data": {
            "token": token,
            "token_type": "Bearer",
            "expires_at": expires_at.isoformat(),
            "user": {
                "username": usuario['username'],
                "role": usuario['role']
            }
        }
    }), 200


@app.route('/api/logout', methods=['POST'])
@requer_token
def logout():
    """Endpoint de logout - revoga token"""
    token = request.token
    
    if revogar_token(token):
        return jsonify({
            "status": 200,
            "message": "Logout realizado com sucesso"
        }), 200
    else:
        return jsonify({
            "status": 400,
            "error": "Token não encontrado"
        }), 400


@app.route('/api/token/verify', methods=['GET'])
@requer_token
def verificar_token_atual():
    """Verifica se token atual é válido"""
    token_data = tokens_db.get(request.token)
    
    return jsonify({
        "status": 200,
        "message": "Token válido",
        "data": {
            "username": token_data['username'],
            "created_at": token_data['created_at'].isoformat(),
            "expires_at": token_data['expires_at'].isoformat(),
            "expires_in_hours": (
                token_data['expires_at'] - datetime.now()
            ).total_seconds() / 3600
        }
    }), 200


# ============================================
# 5. ROTAS PROTEGIDAS
# ============================================

@app.route('/api/protected', methods=['GET'])
@requer_token
def rota_protegida():
    """Rota protegida - requer token"""
    usuario = request.current_user
    
    return jsonify({
        "status": 200,
        "message": "Acesso autorizado",
        "data": {
            "username": usuario['username'],
            "role": usuario['role'],
            "message": "Você está autenticado com token!"
        }
    }), 200


@app.route('/api/perfil', methods=['GET'])
@requer_token
def obter_perfil():
    """Obter perfil do usuário autenticado"""
    usuario = request.current_user
    token_data = tokens_db.get(request.token)
    
    return jsonify({
        "status": 200,
        "data": {
            "username": usuario['username'],
            "role": usuario['role'],
            "token_info": {
                "created_at": token_data['created_at'].isoformat(),
                "expires_at": token_data['expires_at'].isoformat()
            }
        }
    }), 200


# ============================================
# 6. Gerenciamento de Tokens
# ============================================

@app.route('/api/tokens', methods=['GET'])
@requer_token
def listar_tokens_usuario():
    """Lista tokens do usuário atual (exemplo)"""
    usuario = request.current_user
    
    # Encontrar todos os tokens do usuário
    tokens_usuario = [
        {
            "token": token[:20] + "...",  # Mostrar apenas parte do token
            "created_at": data['created_at'].isoformat(),
            "expires_at": data['expires_at'].isoformat(),
            "is_current": token == request.token
        }
        for token, data in tokens_db.items()
        if data['username'] == usuario['username']
    ]
    
    return jsonify({
        "status": 200,
        "data": {
            "total_tokens": len(tokens_usuario),
            "tokens": tokens_usuario
        }
    }), 200


# ============================================
# 7. EXEMPLOS DE USO
# ============================================

print("\n" + "=" * 60)
print("EXEMPLOS DE USO")
print("=" * 60)

print("""
1. Login (obter token):
   curl -X POST http://localhost:5000/api/login \\
     -H "Content-Type: application/json" \\
     -d '{"username": "admin", "password": "senha123"}'

2. Acessar rota protegida com token:
   curl -X GET http://localhost:5000/api/protected \\
     -H "Authorization: Bearer <seu_token_aqui>"

3. Verificar token:
   curl -X GET http://localhost:5000/api/token/verify \\
     -H "Authorization: Bearer <seu_token_aqui>"

4. Logout (revogar token):
   curl -X POST http://localhost:5000/api/logout \\
     -H "Authorization: Bearer <seu_token_aqui>"
""")


# ============================================
# 8. VANTAGENS DO TOKEN AUTH
# ============================================

print("\n" + "=" * 60)
print("VANTAGENS DO TOKEN AUTH")
print("=" * 60)

vantagens = """
✓ Mais seguro que Basic Auth:
  - Credenciais não são enviadas a cada requisição
  - Apenas token é enviado

✓ Controle de expiração:
  - Tokens podem expirar
  - Reduz janela de ataque se token for comprometido

✓ Pode ser revogado:
  - Logout revoga token
  - Útil para segurança

✓ Escalável:
  - Pode armazenar em banco de dados
  - Fácil de gerenciar múltiplos dispositivos

Limitações:
✗ Precisa armazenar tokens (não stateless)
✗ Requer verificação em banco/armazenamento
✗ Menos escalável que JWT para sistemas grandes
"""

print(vantagens)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - TOKEN AUTHENTICATION")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Token Authentication:
   - Login retorna token
   - Token enviado em cada requisição: Authorization: Bearer <token>
   - Token pode expirar
   - Token pode ser revogado

2. Fluxo:
   - POST /api/login → Recebe token
   - GET /api/protected → Envia token no header
   - POST /api/logout → Revoga token

3. Vantagens:
   - Mais seguro que Basic Auth
   - Controle de expiração
   - Pode ser revogado

4. Limitações:
   - Precisa armazenar tokens
   - Não é stateless

Próximos passos:
- JWT Authentication (stateless, mais escalável)
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 08_token_auth.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

