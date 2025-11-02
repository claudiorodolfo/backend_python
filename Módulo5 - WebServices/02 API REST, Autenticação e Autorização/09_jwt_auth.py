"""
09 - JWT (JSON Web Token) Authentication
==========================================
Implementação de autenticação usando JWT
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import jwt
import hashlib
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'sua-chave-secreta-muito-segura-aqui'
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
app.config['JWT_ALGORITHM'] = 'HS256'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=24)

print("=" * 60)
print("JWT (JSON WEB TOKEN) AUTHENTICATION")
print("=" * 60)

# ============================================
# 1. BANCO DE USUÁRIOS
# ============================================

usuarios_db = {
    "admin": {
        "username": "admin",
        "password_hash": hashlib.sha256("senha123".encode()).hexdigest(),
        "role": "admin",
        "user_id": 1
    },
    "usuario": {
        "username": "usuario",
        "password_hash": hashlib.sha256("senha456".encode()).hexdigest(),
        "role": "user",
        "user_id": 2
    }
}


# ============================================
# 2. FUNÇÕES JWT
# ============================================

def gerar_jwt(username, user_data):
    """
    Gera um JWT token
    
    Payload típico:
    {
        "user_id": 1,
        "username": "admin",
        "role": "admin",
        "exp": 1234567890,  # Expiration time
        "iat": 1234567890   # Issued at
    }
    """
    payload = {
        "user_id": user_data['user_id'],
        "username": username,
        "role": user_data['role'],
        "iat": datetime.utcnow(),  # Issued at
        "exp": datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']  # Expiration
    }
    
    token = jwt.encode(
        payload,
        app.config['JWT_SECRET_KEY'],
        algorithm=app.config['JWT_ALGORITHM']
    )
    
    # jwt.encode retorna bytes em algumas versões, converter para string
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    
    return token


def verificar_jwt(token):
    """
    Verifica e decodifica um JWT token
    Retorna o payload se válido, None se inválido
    """
    try:
        payload = jwt.decode(
            token,
            app.config['JWT_SECRET_KEY'],
            algorithms=[app.config['JWT_ALGORITHM']]
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido


# ============================================
# 3. DECORADOR DE AUTENTICAÇÃO
# ============================================

def requer_jwt(f):
    """Decorador para proteger rotas com JWT"""
    def decorador(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({
                "status": 401,
                "error": "Token JWT necessário",
                "message": "Header Authorization: Bearer <token> necessário"
            }), 401
        
        token = auth_header.replace('Bearer ', '').strip()
        
        # Verificar token
        payload = verificar_jwt(token)
        
        if not payload:
            return jsonify({
                "status": 401,
                "error": "Token inválido ou expirado",
                "message": "Faça login novamente"
            }), 401
        
        # Obter dados do usuário
        username = payload['username']
        
        if username not in usuarios_db:
            return jsonify({
                "status": 401,
                "error": "Usuário não encontrado"
            }), 401
        
        usuario = usuarios_db[username]
        
        # Adicionar ao request
        request.current_user = usuario
        request.jwt_payload = payload
        
        return f(*args, **kwargs)
    
    decorador.__name__ = f.__name__
    return decorador


# ============================================
# 4. ROTAS DE AUTENTICAÇÃO
# ============================================

@app.route('/api/login', methods=['POST'])
def login():
    """Endpoint de login - retorna JWT token"""
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
    
    # Gerar JWT
    token = gerar_jwt(username, usuario)
    expires_at = datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']
    
    return jsonify({
        "status": 200,
        "message": "Login realizado com sucesso",
        "data": {
            "token": token,
            "token_type": "Bearer",
            "expires_at": expires_at.isoformat(),
            "expires_in_seconds": int(app.config['JWT_EXPIRATION_DELTA'].total_seconds()),
            "user": {
                "user_id": usuario['user_id'],
                "username": usuario['username'],
                "role": usuario['role']
            }
        }
    }), 200


@app.route('/api/token/verify', methods=['GET'])
@requer_jwt
def verificar_token_atual():
    """Verifica se JWT atual é válido e retorna informações"""
    payload = request.jwt_payload
    
    return jsonify({
        "status": 200,
        "message": "Token JWT válido",
        "data": {
            "payload": payload,
            "user": {
                "username": request.current_user['username'],
                "role": request.current_user['role']
            }
        }
    }), 200


@app.route('/api/token/decode', methods=['POST'])
def decodificar_token():
    """Decodifica um JWT sem verificar (útil para debug)"""
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    token = dados.get('token')
    
    if not token:
        return jsonify({
            "status": 400,
            "error": "Token é obrigatório"
        }), 400
    
    try:
        # Decodificar sem verificar (apenas para visualização)
        payload = jwt.decode(
            token,
            options={"verify_signature": False}
        )
        
        return jsonify({
            "status": 200,
            "data": {
                "payload": payload,
                "note": "Token decodificado sem verificação de assinatura"
            }
        }), 200
    except Exception as e:
        return jsonify({
            "status": 400,
            "error": "Token inválido",
            "message": str(e)
        }), 400


# ============================================
# 5. ROTAS PROTEGIDAS
# ============================================

@app.route('/api/protected', methods=['GET'])
@requer_jwt
def rota_protegida():
    """Rota protegida - requer JWT"""
    usuario = request.current_user
    payload = request.jwt_payload
    
    return jsonify({
        "status": 200,
        "message": "Acesso autorizado com JWT",
        "data": {
            "user": {
                "username": usuario['username'],
                "role": usuario['role']
            },
            "token_info": {
                "issued_at": payload.get('iat'),
                "expires_at": payload.get('exp')
            }
        }
    }), 200


@app.route('/api/perfil', methods=['GET'])
@requer_jwt
def obter_perfil():
    """Obter perfil do usuário autenticado"""
    usuario = request.current_user
    payload = request.jwt_payload
    
    return jsonify({
        "status": 200,
        "data": {
            "user_id": usuario['user_id'],
            "username": usuario['username'],
            "role": usuario['role'],
            "token_issued_at": payload.get('iat'),
            "token_expires_at": payload.get('exp')
        }
    }), 200


# ============================================
# 6. ESTRUTURA DO JWT
# ============================================

print("\n" + "=" * 60)
print("ESTRUTURA DO JWT")
print("=" * 60)

print("""
JWT tem 3 partes separadas por ponto (.):

1. HEADER:
   {
     "alg": "HS256",  # Algoritmo de assinatura
     "typ": "JWT"     # Tipo do token
   }
   → Codificado em Base64URL

2. PAYLOAD (Claims):
   {
     "user_id": 1,
     "username": "admin",
     "role": "admin",
     "iat": 1234567890,  # Issued at
     "exp": 1234567890   # Expiration
   }
   → Codificado em Base64URL

3. SIGNATURE:
   HMACSHA256(
     base64UrlEncode(header) + "." + base64UrlEncode(payload),
     secret
   )
   → Assinatura para verificar integridade

Formato final:
header.payload.signature

Exemplo:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
""")


# ============================================
# 7. VANTAGENS DO JWT
# ============================================

print("\n" + "=" * 60)
print("VANTAGENS DO JWT")
print("=" * 60)

vantagens = """
✓ Stateless:
  - Não precisa armazenar tokens no servidor
  - Informações estão no próprio token
  - Muito escalável

✓ Self-contained:
  - Token contém informações do usuário
  - Não precisa consultar banco para cada requisição

✓ Padrão da indústria:
  - Amplamente usado (Google, Facebook, etc.)
  - Bibliotecas em todas as linguagens

✓ Assinatura:
  - Token assinado, não pode ser modificado
  - Verificação de integridade automática

Limitações:
✗ Não pode ser revogado facilmente (sem blacklist)
✗ Tamanho maior que tokens simples
✗ Se comprometido, válido até expirar
"""

print(vantagens)


# ============================================
# 8. EXEMPLOS DE USO
# ============================================

print("\n" + "=" * 60)
print("EXEMPLOS DE USO")
print("=" * 60)

print("""
1. Login (obter JWT):
   curl -X POST http://localhost:5000/api/login \\
     -H "Content-Type: application/json" \\
     -d '{"username": "admin", "password": "senha123"}'

2. Acessar rota protegida:
   curl -X GET http://localhost:5000/api/protected \\
     -H "Authorization: Bearer <seu_jwt_token>"

3. Verificar token:
   curl -X GET http://localhost:5000/api/token/verify \\
     -H "Authorization: Bearer <seu_jwt_token>"

4. Decodificar token (sem verificar):
   curl -X POST http://localhost:5000/api/token/decode \\
     -H "Content-Type: application/json" \\
     -d '{"token": "<seu_jwt_token>"}'
""")


# ============================================
# 9. INSTALAÇÃO
# ============================================

print("\n" + "=" * 60)
print("INSTALAÇÃO")
print("=" * 60)

print("""
Para usar JWT, instale a biblioteca PyJWT:

pip install PyJWT

Ou use python-jose (mais recursos):
pip install python-jose[cryptography]
""")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - JWT AUTHENTICATION")
print("=" * 60)
print("""
Conceitos aprendidos:

1. JWT (JSON Web Token):
   - Token auto-contido com informações
   - 3 partes: header.payload.signature
   - Stateless (não armazena no servidor)

2. Vantagens:
   - Muito escalável
   - Self-contained
   - Padrão da indústria
   - Assinatura para integridade

3. Limitações:
   - Não pode ser revogado facilmente
   - Se comprometido, válido até expirar

4. Uso:
   - APIs modernas
   - Microserviços
   - Aplicações distribuídas

Comparação:
- Basic Auth: Simples, menos seguro
- Token Auth: Médio, precisa armazenar
- JWT: Avançado, stateless, escalável
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("NOTA: Este exemplo usa PyJWT")
    print("Instale: pip install PyJWT")
    print("\nPara executar:")
    print("python 09_jwt_auth.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

