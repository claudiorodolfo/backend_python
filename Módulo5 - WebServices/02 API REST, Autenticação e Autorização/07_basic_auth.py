"""
07 - Basic Authentication
===========================
Implementação simples de Basic Authentication
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import hashlib

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'

print("=" * 60)
print("BASIC AUTHENTICATION")
print("=" * 60)

# ============================================
# 1. SIMULAÇÃO DE BANCO DE USUÁRIOS
# ============================================

# Em produção, isso viria de um banco de dados
# As senhas estão "hasheadas" (em produção use bcrypt)
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


def verificar_senha(senha, password_hash):
    """Verifica se senha corresponde ao hash"""
    return hashlib.sha256(senha.encode()).hexdigest() == password_hash


# ============================================
# 2. DECODIFICAR BASIC AUTH
# ============================================

def decodificar_basic_auth(header):
    """
    Decodifica header Basic Authentication
    
    Formato: Authorization: Basic base64(username:password)
    """
    if not header or not header.startswith('Basic '):
        return None, None
    
    try:
        # Remover 'Basic ' e decodificar
        encoded = header.replace('Basic ', '')
        decoded = base64.b64decode(encoded).decode('utf-8')
        username, password = decoded.split(':', 1)
        return username, password
    except Exception:
        return None, None


# ============================================
# 3. DECORADOR DE AUTENTICAÇÃO
# ============================================

def requer_autenticacao(f):
    """Decorador para proteger rotas com Basic Auth"""
    def decorador(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if not auth_header:
            return jsonify({
                "status": 401,
                "error": "Autenticação necessária",
                "message": "Header Authorization com Basic Auth necessário"
            }), 401
        
        username, password = decodificar_basic_auth(auth_header)
        
        if not username or not password:
            return jsonify({
                "status": 401,
                "error": "Credenciais inválidas",
                "message": "Formato incorreto de Basic Auth"
            }), 401
        
        # Verificar credenciais
        if username not in usuarios_db:
            return jsonify({
                "status": 401,
                "error": "Credenciais inválidas",
                "message": "Usuário não encontrado"
            }), 401
        
        usuario = usuarios_db[username]
        
        if not verificar_senha(password, usuario['password_hash']):
            return jsonify({
                "status": 401,
                "error": "Credenciais inválidas",
                "message": "Senha incorreta"
            }), 401
        
        # Adicionar usuário ao request para uso na rota
        request.current_user = usuario
        
        return f(*args, **kwargs)
    
    decorador.__name__ = f.__name__
    return decorador


# ============================================
# 4. ROTAS PÚBLICAS E PROTEGIDAS
# ============================================

@app.route('/api/public', methods=['GET'])
def rota_publica():
    """Rota pública - não requer autenticação"""
    return jsonify({
        "status": 200,
        "message": "Esta é uma rota pública",
        "data": {
            "info": "Qualquer um pode acessar"
        }
    }), 200


@app.route('/api/protected', methods=['GET'])
@requer_autenticacao
def rota_protegida():
    """Rota protegida - requer Basic Auth"""
    usuario = request.current_user
    
    return jsonify({
        "status": 200,
        "message": "Acesso autorizado",
        "data": {
            "username": usuario['username'],
            "role": usuario['role'],
            "message": "Você está autenticado!"
        }
    }), 200


@app.route('/api/perfil', methods=['GET'])
@requer_autenticacao
def obter_perfil():
    """Obter perfil do usuário autenticado"""
    usuario = request.current_user
    
    return jsonify({
        "status": 200,
        "data": {
            "username": usuario['username'],
            "role": usuario['role']
        }
    }), 200


# ============================================
# 5. ROTA DE LOGIN (ALTERNATIVA)
# ============================================

@app.route('/api/login', methods=['POST'])
def login():
    """
    Endpoint de login alternativo
    Aceita credenciais no body JSON
    """
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
    
    if not verificar_senha(password, usuario['password_hash']):
        return jsonify({
            "status": 401,
            "error": "Credenciais inválidas"
        }), 401
    
    return jsonify({
        "status": 200,
        "message": "Login realizado com sucesso",
        "data": {
            "username": usuario['username'],
            "role": usuario['role']
        }
    }), 200


# ============================================
# 6. EXEMPLO DE USO
# ============================================

print("\n" + "=" * 60)
print("EXEMPLOS DE USO")
print("=" * 60)

print("""
1. Acessar rota pública (sem autenticação):
   curl -X GET http://localhost:5000/api/public

2. Acessar rota protegida com Basic Auth:
   curl -X GET http://localhost:5000/api/protected \\
     -u admin:senha123

3. Usando header Authorization diretamente:
   curl -X GET http://localhost:5000/api/protected \\
     -H "Authorization: Basic YWRtaW46c2VuaGExMjM="

4. Login alternativo (POST):
   curl -X POST http://localhost:5000/api/login \\
     -H "Content-Type: application/json" \\
     -d '{"username": "admin", "password": "senha123"}'
""")


# ============================================
# 7. GERAR BASIC AUTH HEADER (UTILITÁRIO)
# ============================================

def gerar_basic_auth_header(username, password):
    """Gera header Basic Auth"""
    credentials = f"{username}:{password}"
    encoded = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {encoded}"


print("\n" + "=" * 60)
print("GERAR BASIC AUTH")
print("=" * 60)

# Exemplo de geração
username_exemplo = "admin"
password_exemplo = "senha123"
header = gerar_basic_auth_header(username_exemplo, password_exemplo)
print(f"\nUsername: {username_exemplo}")
print(f"Password: {password_exemplo}")
print(f"Header gerado: {header}")


# ============================================
# 8. LIMITAÇÕES E SEGURANÇA
# ============================================

print("\n" + "=" * 60)
print("LIMITAÇÕES E SEGURANÇA")
print("=" * 60)

limitacoes = """
Limitações do Basic Auth:

1. Credenciais em cada requisição:
   - Usuário/senha enviados em cada requisição
   - Mesmo que em base64 (não é criptografia!)
   - Risco se interceptado

2. Sem expiração:
   - Credenciais válidas indefinidamente
   - Não há como revogar facilmente

3. Base64 não é criptografia:
   - Qualquer um pode decodificar
   - Apenas uma codificação

Recomendações:

✓ Use APENAS com HTTPS
✓ Não use em produção para APIs públicas
✓ Adequado para:
  - Desenvolvimento/testes
  - APIs internas
  - Autenticação simples

✗ NÃO use para:
  - APIs públicas
  - Dados sensíveis em produção
  - Sistemas que precisam de revogação de tokens
"""

print(limitacoes)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - BASIC AUTHENTICATION")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Basic Auth:
   - Formato: Authorization: Basic base64(username:password)
   - Simples de implementar
   - Credenciais em cada requisição

2. Implementação:
   - Decodificar header Authorization
   - Verificar credenciais
   - Decorador para proteger rotas

3. Limitações:
   - Credenciais em cada requisição
   - Base64 não é criptografia
   - Use apenas com HTTPS

4. Quando usar:
   - Desenvolvimento/testes
   - APIs internas
   - Não para APIs públicas

Próximos passos:
- Token Authentication (mais seguro)
- JWT Authentication (padrão moderno)
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 07_basic_auth.py")
    print("\nTestar:")
    print("curl -u admin:senha123 http://localhost:5000/api/protected")
    print("=" * 60)
    # app.run(debug=True, port=5000)

