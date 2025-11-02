"""
01 - Setup do Ambiente API
============================
Configuração do ambiente para desenvolvimento de APIs REST com Flask
"""

print("=" * 60)
print("SETUP DO AMBIENTE API")
print("=" * 60)

# ============================================
# 1. INSTALAÇÃO DE DEPENDÊNCIAS
# ============================================

"""
Dependências necessárias:
--------------------------
pip install flask flask-cors flask-restful

Flask: Framework web minimalista
flask-cors: Suporte para CORS (Cross-Origin Resource Sharing)
flask-restful: Extensão para criar APIs REST de forma mais estruturada
"""

instalacao = """
# Instalar Flask e dependências
pip install flask flask-cors

# Para ambiente virtual (recomendado)
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\\Scripts\\activate

# Linux/Mac:
source venv/bin/activate

# Depois instalar:
pip install flask flask-cors
"""

print("\n" + "=" * 60)
print("INSTALAÇÃO DE DEPENDÊNCIAS")
print("=" * 60)
print(instalacao)


# ============================================
# 2. ESTRUTURA BÁSICA DE UM PROJETO API
# ============================================

estrutura_projeto = """
api_project/
├── app.py                 # Arquivo principal da aplicação
├── requirements.txt       # Dependências do projeto
├── .env                   # Variáveis de ambiente (opcional)
├── config.py             # Configurações
└── README.md             # Documentação
"""

print("\n" + "=" * 60)
print("ESTRUTURA BÁSICA DE PROJETO")
print("=" * 60)
print(estrutura_projeto)


# ============================================
# 3. APLICAÇÃO FLASK BÁSICA
# ============================================

print("\n" + "=" * 60)
print("APLICAÇÃO FLASK BÁSICA")
print("=" * 60)

from flask import Flask, jsonify, request
from flask_cors import CORS

# Criação da aplicação Flask
app = Flask(__name__)

# Habilitar CORS (permitir requisições de outros domínios)
CORS(app)

# Configurações básicas
app.config['DEBUG'] = True  # Apenas para desenvolvimento
app.config['JSON_AS_ASCII'] = False  # Suportar caracteres especiais em JSON


# Rota simples de teste
@app.route('/', methods=['GET'])
def home():
    """Rota inicial - verificação de funcionamento"""
    return jsonify({
        "message": "API funcionando!",
        "status": "ok",
        "version": "1.0.0"
    })


# Rota de health check
@app.route('/health', methods=['GET'])
def health():
    """Endpoint para verificar saúde da API"""
    return jsonify({
        "status": "healthy",
        "service": "API REST"
    }), 200


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("INICIANDO SERVIDOR FLASK")
    print("=" * 60)
    print("""
A aplicação está configurada e pronta para rodar.

Para executar:
1. Salve este arquivo como app.py
2. Execute: python app.py
3. Acesse: http://localhost:5000

Endpoints disponíveis:
- GET  http://localhost:5000/          → Página inicial
- GET  http://localhost:5000/health   → Health check

Próximos passos:
- Criar rotas específicas
- Implementar CRUD completo
- Adicionar autenticação
    """)
    # app.run(debug=True, host='0.0.0.0', port=5000)


# ============================================
# 4. REQUIREMENTS.TXT
# ============================================

requirements_content = """# Flask e extensões
Flask==3.0.0
flask-cors==4.0.0

# Ferramentas de desenvolvimento (opcional)
python-dotenv==1.0.0
"""

print("\n" + "=" * 60)
print("REQUIREMENTS.TXT")
print("=" * 60)
print(requirements_content)


# ============================================
# 5. CONFIGURAÇÃO COM VARIÁVEIS DE AMBIENTE
# ============================================

import os

class Config:
    """Classe de configuração base"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))


print("\n" + "=" * 60)
print("CONFIGURAÇÃO COM VARIÁVEIS DE AMBIENTE")
print("=" * 60)
print("""
Exemplo de arquivo .env:
------------------------
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui
HOST=0.0.0.0
PORT=5000

Uso:
----
from dotenv import load_dotenv
load_dotenv()

config = Config()
app.config['SECRET_KEY'] = config.SECRET_KEY
""")


# ============================================
# 6. VERIFICAÇÃO DE AMBIENTE
# ============================================

def verificar_ambiente():
    """Verifica se o ambiente está configurado corretamente"""
    print("\n" + "=" * 60)
    print("VERIFICAÇÃO DE AMBIENTE")
    print("=" * 60)
    
    try:
        import flask
        print(f"✓ Flask instalado: {flask.__version__}")
    except ImportError:
        print("✗ Flask não está instalado")
        print("  Execute: pip install flask flask-cors")
    
    try:
        import flask_cors
        print(f"✓ Flask-CORS instalado")
    except ImportError:
        print("✗ Flask-CORS não está instalado")
        print("  Execute: pip install flask-cors")
    
    print(f"\nPython: {os.sys.version.split()[0]}")
    print(f"Diretório atual: {os.getcwd()}")


verificar_ambiente()


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - SETUP DO AMBIENTE")
print("=" * 60)
print("""
Passos para configurar ambiente:

1. Criar ambiente virtual:
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\\Scripts\\activate     # Windows

2. Instalar dependências:
   pip install flask flask-cors

3. Criar arquivo requirements.txt:
   pip freeze > requirements.txt

4. Criar app.py com estrutura básica

5. Executar aplicação:
   python app.py

Próximos arquivos:
- 02_rotas_simples.py - Criando rotas básicas
- 03_requisicoes_respostas.py - Manipulação de requisições
""")

