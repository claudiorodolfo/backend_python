"""
04 - Enviando Dados em JSON
============================
Enviar e receber dados JSON em requisições HTTP
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

print("=" * 60)
print("ENVIANDO DADOS EM JSON")
print("=" * 60)


# ============================================
# 1. ENVIAR JSON SIMPLES
# ============================================

@app.route('/api/exemplo/json-simples', methods=['POST'])
def receber_json_simples():
    """Recebe e processa JSON simples"""
    
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 400
    
    dados = request.get_json()
    
    return jsonify({
        "status": 200,
        "message": "JSON recebido com sucesso",
        "dados_recebidos": dados,
        "tipo": type(dados).__name__
    }), 200


# ============================================
# 2. ENVIAR JSON COMPLEXO
# ============================================

@app.route('/api/exemplo/json-complexo', methods=['POST'])
def receber_json_complexo():
    """Recebe JSON com estruturas complexas"""
    
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 400
    
    dados = request.get_json()
    
    # Processar diferentes tipos de dados
    resultado = {
        "status": 200,
        "dados_recebidos": dados,
        "analise": {}
    }
    
    if isinstance(dados, dict):
        resultado["analise"] = {
            "tipo": "Objeto",
            "campos": list(dados.keys()),
            "total_campos": len(dados)
        }
        
        # Verificar tipos de valores
        tipos_valores = {}
        for chave, valor in dados.items():
            tipo = type(valor).__name__
            tipos_valores[chave] = tipo
        
        resultado["analise"]["tipos_valores"] = tipos_valores
    
    elif isinstance(dados, list):
        resultado["analise"] = {
            "tipo": "Array",
            "total_itens": len(dados)
        }
    
    return jsonify(resultado), 200


# ============================================
# 3. VALIDAÇÃO DE ESTRUTURA JSON
# ============================================

def validar_usuario(dados):
    """Valida estrutura de dados de usuário"""
    erros = []
    
    # Campos obrigatórios
    campos_obrigatorios = ['nome', 'email']
    for campo in campos_obrigatorios:
        if campo not in dados:
            erros.append(f"Campo '{campo}' é obrigatório")
    
    # Validações específicas
    if 'email' in dados:
        if '@' not in dados['email']:
            erros.append("Email inválido")
    
    if 'idade' in dados:
        if not isinstance(dados['idade'], int):
            erros.append("Idade deve ser um número inteiro")
        elif dados['idade'] < 0 or dados['idade'] > 150:
            erros.append("Idade deve estar entre 0 e 150")
    
    return erros


@app.route('/api/usuarios/criar', methods=['POST'])
def criar_usuario_validado():
    """Cria usuário com validação de JSON"""
    
    if not request.is_json:
        return jsonify({
            "status": 400,
            "error": "Content-Type deve ser application/json"
        }), 400
    
    dados = request.get_json()
    
    # Validar
    erros = validar_usuario(dados)
    if erros:
        return jsonify({
            "status": 422,
            "error": "Erros de validação",
            "validation_errors": erros
        }), 422
    
    # Criar usuário (simulação)
    novo_usuario = {
        "id": 1,
        "nome": dados['nome'],
        "email": dados['email'],
        "idade": dados.get('idade'),
        "criado_em": datetime.now().isoformat()
    }
    
    return jsonify({
        "status": 201,
        "message": "Usuário criado com sucesso",
        "data": novo_usuario
    }), 201


# ============================================
# 4. JSON COM ARRAYS E OBJETOS ANINHADOS
# ============================================

@app.route('/api/pedidos/criar', methods=['POST'])
def criar_pedido_completo():
    """Recebe JSON com estrutura aninhada complexa"""
    
    if not request.is_json:
        return jsonify({"error": "Content-Type deve ser application/json"}), 400
    
    dados = request.get_json()
    
    # Estrutura esperada:
    # {
    #   "cliente": {"nome": "...", "email": "..."},
    #   "itens": [{"produto_id": 1, "quantidade": 2}, ...],
    #   "endereco_entrega": {"rua": "...", "cidade": "..."}
    # }
    
    erros = []
    
    # Validar estrutura
    if 'cliente' not in dados:
        erros.append("Campo 'cliente' é obrigatório")
    elif not isinstance(dados['cliente'], dict):
        erros.append("Campo 'cliente' deve ser um objeto")
    
    if 'itens' not in dados:
        erros.append("Campo 'itens' é obrigatório")
    elif not isinstance(dados['itens'], list):
        erros.append("Campo 'itens' deve ser um array")
    elif len(dados['itens']) == 0:
        erros.append("Pedido deve ter pelo menos um item")
    
    if erros:
        return jsonify({
            "status": 422,
            "error": "Erros de validação",
            "validation_errors": erros
        }), 422
    
    # Processar pedido
    pedido = {
        "id": 123,
        "cliente": dados['cliente'],
        "itens": dados['itens'],
        "endereco_entrega": dados.get('endereco_entrega'),
        "total_itens": len(dados['itens']),
        "criado_em": datetime.now().isoformat()
    }
    
    return jsonify({
        "status": 201,
        "message": "Pedido criado com sucesso",
        "data": pedido
    }), 201


# ============================================
# 5. RETORNAR JSON COM TIPOS ESPECIAIS
# ============================================

from decimal import Decimal
from datetime import date

class JSONEncoder(json.JSONEncoder):
    """Encoder customizado para tipos especiais"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


@app.route('/api/exemplo/tipos-especiais', methods=['GET'])
def exemplo_tipos_especiais():
    """Retorna JSON com tipos especiais (datetime, Decimal)"""
    
    dados = {
        "id": 1,
        "nome": "Produto Exemplo",
        "preco": Decimal("29.99"),
        "data_criacao": datetime.now(),
        "data_validade": date(2025, 12, 31),
        "desconto_percentual": Decimal("10.5")
    }
    
    # Usar encoder customizado
    json_str = json.dumps(dados, cls=JSONEncoder, ensure_ascii=False, indent=2)
    
    return app.response_class(
        response=json_str,
        status=200,
        mimetype='application/json'
    )


# ============================================
# 6. EXEMPLOS DE JSONs PARA TESTE
# ============================================

print("\n" + "=" * 60)
print("EXEMPLOS DE JSONs PARA TESTE")
print("=" * 60)

exemplo_usuario_simples = {
    "nome": "João Silva",
    "email": "joao@example.com",
    "idade": 30
}

exemplo_usuario_completo = {
    "nome": "Maria Santos",
    "email": "maria@example.com",
    "idade": 25,
    "telefone": "+55 11 99999-9999",
    "endereco": {
        "rua": "Rua Exemplo, 123",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01234-567"
    },
    "preferencias": {
        "notificacoes": True,
        "tema": "escuro",
        "idioma": "pt-BR"
    }
}

exemplo_pedido = {
    "cliente": {
        "nome": "Pedro Costa",
        "email": "pedro@example.com"
    },
    "itens": [
        {
            "produto_id": 1,
            "nome": "Notebook",
            "quantidade": 1,
            "preco": 2500.00
        },
        {
            "produto_id": 2,
            "nome": "Mouse",
            "quantidade": 2,
            "preco": 50.00
        }
    ],
    "endereco_entrega": {
        "rua": "Av. Principal, 456",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01234-567"
    }
}

print("\n1. JSON Simples - Criar Usuário:")
print(json.dumps(exemplo_usuario_simples, indent=2, ensure_ascii=False))

print("\n2. JSON Completo - Usuário com Nested Objects:")
print(json.dumps(exemplo_usuario_completo, indent=2, ensure_ascii=False))

print("\n3. JSON Complexo - Pedido com Array:")
print(json.dumps(exemplo_pedido, indent=2, ensure_ascii=False))


# ============================================
# 7. TESTANDO RECEBIMENTO DE JSON
# ============================================

@app.route('/api/test/json', methods=['POST'])
def testar_json():
    """Endpoint para testar recebimento de JSON"""
    
    try:
        if not request.is_json:
            return jsonify({
                "error": "Content-Type deve ser application/json",
                "received_content_type": request.content_type
            }), 400
        
        dados = request.get_json(force=True)  # force=True tenta parse mesmo sem Content-Type correto
        
        return jsonify({
            "status": "success",
            "message": "JSON recebido e parseado com sucesso",
            "received_data": dados,
            "data_type": type(dados).__name__,
            "data_keys": list(dados.keys()) if isinstance(dados, dict) else None,
            "data_length": len(dados) if isinstance(dados, (dict, list)) else None
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": "Erro ao processar JSON",
            "message": str(e)
        }), 400


print("\n" + "=" * 60)
print("COMO TESTAR")
print("=" * 60)
print("""
Usando curl:

1. JSON Simples:
curl -X POST http://localhost:5000/api/exemplo/json-simples \\
  -H "Content-Type: application/json" \\
  -d '{"nome": "João", "email": "joao@example.com"}'

2. JSON Complexo:
curl -X POST http://localhost:5000/api/usuarios/criar \\
  -H "Content-Type: application/json" \\
  -d '{
    "nome": "Maria Santos",
    "email": "maria@example.com",
    "idade": 25
  }'

3. Pedido Completo:
curl -X POST http://localhost:5000/api/pedidos/criar \\
  -H "Content-Type: application/json" \\
  -d '{
    "cliente": {"nome": "João", "email": "joao@example.com"},
    "itens": [
      {"produto_id": 1, "quantidade": 2}
    ]
  }'
""")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - ENVIANDO JSON")
print("=" * 60)
print("""
Conceitos aprendidos:

1. Enviar JSON:
   - Content-Type: application/json
   - Body da requisição contém JSON
   - request.get_json() para ler

2. Validação:
   - Verificar estrutura
   - Validar tipos de dados
   - Campos obrigatórios

3. Tipos especiais:
   - datetime → ISO format
   - Decimal → float
   - Custom JSON encoder

4. Estruturas complexas:
   - Objetos aninhados
   - Arrays
   - Arrays de objetos

5. Tratamento de erros:
   - Verificar Content-Type
   - Try/except para parsing
   - Mensagens de erro claras

Próximos passos:
- Testar com Postman ou curl
- Implementar testes automatizados
- Adicionar autenticação
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("python 04_enviando_json.py")
    print("=" * 60)
    # app.run(debug=True, port=5000)

