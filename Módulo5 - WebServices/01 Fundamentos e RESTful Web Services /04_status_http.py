"""
04 - Status Codes HTTP
========================
Exploração detalhada dos códigos de status HTTP mais comuns
"""

import json
from typing import Dict, Any
from enum import IntEnum

print("=" * 60)
print("STATUS CODES HTTP")
print("=" * 60)


# ============================================
# 1. CLASSIFICAÇÃO DE STATUS CODES
# ============================================

"""
Classificação por faixa:
------------------------
1xx - Informativo: Requisição recebida, processando
2xx - Sucesso: Requisição recebida, entendida e aceita
3xx - Redirecionamento: Ação adicional necessária
4xx - Erro do Cliente: Requisição com sintaxe incorreta
5xx - Erro do Servidor: Servidor falhou ao processar
"""

class StatusCode(IntEnum):
    """Códigos de status HTTP comuns"""
    # 2xx - Sucesso
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    
    # 3xx - Redirecionamento
    MOVED_PERMANENTLY = 301
    FOUND = 302
    NOT_MODIFIED = 304
    
    # 4xx - Erro do Cliente
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    CONFLICT = 409
    UNPROCESSABLE_ENTITY = 422
    TOO_MANY_REQUESTS = 429
    
    # 5xx - Erro do Servidor
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503


# ============================================
# 2. STATUS CODES MAIS COMUNS - DETALHAMENTO
# ============================================

status_codes_info = {
    200: {
        "nome": "OK",
        "categoria": "2xx - Sucesso",
        "descricao": "Requisição bem-sucedida",
        "uso_comum": "GET, PUT, PATCH bem-sucedidos",
        "exemplo": "GET /api/users/123 retorna dados do usuário"
    },
    201: {
        "nome": "Created",
        "categoria": "2xx - Sucesso",
        "descricao": "Recurso criado com sucesso",
        "uso_comum": "POST bem-sucedido",
        "exemplo": "POST /api/users cria novo usuário"
    },
    204: {
        "nome": "No Content",
        "categoria": "2xx - Sucesso",
        "descricao": "Requisição bem-sucedida, sem conteúdo para retornar",
        "uso_comum": "DELETE bem-sucedido",
        "exemplo": "DELETE /api/users/123 deleta usuário"
    },
    400: {
        "nome": "Bad Request",
        "categoria": "4xx - Erro do Cliente",
        "descricao": "Requisição inválida ou mal formada",
        "uso_comum": "Erro de validação, dados faltando",
        "exemplo": "POST /api/users sem campo obrigatório"
    },
    401: {
        "nome": "Unauthorized",
        "categoria": "4xx - Erro do Cliente",
        "descricao": "Não autenticado, precisa de credenciais",
        "uso_comum": "Token ausente ou inválido",
        "exemplo": "GET /api/users sem token de autenticação"
    },
    403: {
        "nome": "Forbidden",
        "categoria": "4xx - Erro do Cliente",
        "descricao": "Autenticado mas sem permissão",
        "uso_comum": "Usuário não tem acesso ao recurso",
        "exemplo": "Usuário comum tentando acessar área admin"
    },
    404: {
        "nome": "Not Found",
        "categoria": "4xx - Erro do Cliente",
        "descricao": "Recurso não encontrado",
        "uso_comum": "ID inexistente, rota não encontrada",
        "exemplo": "GET /api/users/999 (usuário não existe)"
    },
    422: {
        "nome": "Unprocessable Entity",
        "categoria": "4xx - Erro do Cliente",
        "descricao": "Sintaxe correta mas semântica incorreta",
        "uso_comum": "Validação de negócio falhou",
        "exemplo": "Email já cadastrado, idade inválida"
    },
    500: {
        "nome": "Internal Server Error",
        "categoria": "5xx - Erro do Servidor",
        "descricao": "Erro interno do servidor",
        "uso_comum": "Exceção não tratada, erro de código",
        "exemplo": "Erro no banco de dados, bug no código"
    },
    503: {
        "nome": "Service Unavailable",
        "categoria": "5xx - Erro do Servidor",
        "descricao": "Serviço temporariamente indisponível",
        "uso_comum": "Manutenção, sobrecarga",
        "exemplo": "Servidor em manutenção, banco offline"
    }
}

print("\n" + "=" * 60)
print("STATUS CODES MAIS COMUNS")
print("=" * 60)

for code, info in sorted(status_codes_info.items()):
    print(f"\n{code} {info['nome']} ({info['categoria']})")
    print(f"  Descrição: {info['descricao']}")
    print(f"  Uso comum: {info['uso_comum']}")
    print(f"  Exemplo: {info['exemplo']}")


# ============================================
# 3. CLASSE PARA GERENCIAR RESPOSTAS HTTP
# ============================================

class RespostaHTTP:
    """Classe para padronizar respostas HTTP"""
    
    @staticmethod
    def sucesso(dados: Any = None, status: int = 200, mensagem: str = None) -> Dict[str, Any]:
        """Cria resposta de sucesso"""
        resposta = {
            "status": status,
            "success": True
        }
        
        if dados is not None:
            resposta["data"] = dados
        
        if mensagem:
            resposta["message"] = mensagem
        
        return resposta
    
    @staticmethod
    def erro(mensagem: str, status: int = 400, detalhes: Any = None) -> Dict[str, Any]:
        """Cria resposta de erro"""
        resposta = {
            "status": status,
            "success": False,
            "error": mensagem
        }
        
        if detalhes:
            resposta["details"] = detalhes
        
        return resposta
    
    @staticmethod
    def criado(dados: Any, location: str = None) -> Dict[str, Any]:
        """Cria resposta 201 Created"""
        resposta = {
            "status": 201,
            "success": True,
            "data": dados,
            "message": "Recurso criado com sucesso"
        }
        
        if location:
            resposta["location"] = location
        
        return resposta
    
    @staticmethod
    def sem_conteudo() -> Dict[str, Any]:
        """Cria resposta 204 No Content"""
        return {
            "status": 204,
            "success": True,
            "message": "Recurso deletado com sucesso"
        }
    
    @staticmethod
    def nao_encontrado(recurso: str = "Recurso") -> Dict[str, Any]:
        """Cria resposta 404 Not Found"""
        return {
            "status": 404,
            "success": False,
            "error": f"{recurso} não encontrado"
        }
    
    @staticmethod
    def nao_autorizado() -> Dict[str, Any]:
        """Cria resposta 401 Unauthorized"""
        return {
            "status": 401,
            "success": False,
            "error": "Não autorizado. Token de autenticação necessário."
        }
    
    @staticmethod
    def proibido() -> Dict[str, Any]:
        """Cria resposta 403 Forbidden"""
        return {
            "status": 403,
            "success": False,
            "error": "Acesso negado. Você não tem permissão para este recurso."
        }
    
    @staticmethod
    def erro_validacao(erros: Dict[str, Any]) -> Dict[str, Any]:
        """Cria resposta 422 Unprocessable Entity"""
        return {
            "status": 422,
            "success": False,
            "error": "Erro de validação",
            "validation_errors": erros
        }
    
    @staticmethod
    def erro_servidor(mensagem: str = "Erro interno do servidor") -> Dict[str, Any]:
        """Cria resposta 500 Internal Server Error"""
        return {
            "status": 500,
            "success": False,
            "error": mensagem
        }


# ============================================
# 4. EXEMPLOS PRÁTICOS DE USO
# ============================================

print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS DE RESPOSTAS HTTP")
print("=" * 60)

# Exemplo 1: Sucesso - GET
print("\n1. GET /api/users/1 - Sucesso (200):")
resposta_get = RespostaHTTP.sucesso({
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com"
})
print(json.dumps(resposta_get, indent=2, ensure_ascii=False))

# Exemplo 2: Criado - POST
print("\n2. POST /api/users - Criado (201):")
resposta_post = RespostaHTTP.criado(
    {
        "id": 2,
        "nome": "Maria Santos",
        "email": "maria@example.com"
    },
    location="/api/users/2"
)
print(json.dumps(resposta_post, indent=2, ensure_ascii=False))

# Exemplo 3: Sem conteúdo - DELETE
print("\n3. DELETE /api/users/1 - Sem conteúdo (204):")
resposta_delete = RespostaHTTP.sem_conteudo()
print(json.dumps(resposta_delete, indent=2, ensure_ascii=False))

# Exemplo 4: Não encontrado - GET
print("\n4. GET /api/users/999 - Não encontrado (404):")
resposta_404 = RespostaHTTP.nao_encontrado("Usuário")
print(json.dumps(resposta_404, indent=2, ensure_ascii=False))

# Exemplo 5: Não autorizado - GET
print("\n5. GET /api/users (sem token) - Não autorizado (401):")
resposta_401 = RespostaHTTP.nao_autorizado()
print(json.dumps(resposta_401, indent=2, ensure_ascii=False))

# Exemplo 6: Erro de validação - POST
print("\n6. POST /api/users (dados inválidos) - Erro de validação (422):")
resposta_422 = RespostaHTTP.erro_validacao({
    "email": ["Email já está em uso"],
    "idade": ["Idade deve ser entre 18 e 120 anos"]
})
print(json.dumps(resposta_422, indent=2, ensure_ascii=False))

# Exemplo 7: Erro do servidor - Qualquer operação
print("\n7. Qualquer operação com erro interno - Erro do servidor (500):")
resposta_500 = RespostaHTTP.erro_servidor("Erro ao conectar com banco de dados")
print(json.dumps(resposta_500, indent=2, ensure_ascii=False))


# ============================================
# 5. FLUXO DE DECISÃO PARA STATUS CODES
# ============================================

def determinar_status_code(operacao: str, sucesso: bool, erro_tipo: str = None) -> int:
    """
    Determina o status code apropriado baseado na operação e resultado
    
    Args:
        operacao: Tipo de operação (GET, POST, PUT, PATCH, DELETE)
        sucesso: Se a operação foi bem-sucedida
        erro_tipo: Tipo de erro se houver (None, 'not_found', 'validation', 'auth', 'server')
    
    Returns:
        Código de status HTTP apropriado
    """
    if sucesso:
        if operacao == "GET":
            return 200
        elif operacao == "POST":
            return 201
        elif operacao == "PUT" or operacao == "PATCH":
            return 200
        elif operacao == "DELETE":
            return 204
        else:
            return 200
    else:
        if erro_tipo == "not_found":
            return 404
        elif erro_tipo == "validation":
            return 422
        elif erro_tipo == "auth":
            return 401
        elif erro_tipo == "forbidden":
            return 403
        elif erro_tipo == "server":
            return 500
        else:
            return 400


print("\n" + "=" * 60)
print("FLUXO DE DECISÃO PARA STATUS CODES")
print("=" * 60)

cenarios = [
    ("GET", True, None, "Buscar usuário existente"),
    ("GET", False, "not_found", "Buscar usuário inexistente"),
    ("POST", True, None, "Criar novo usuário"),
    ("POST", False, "validation", "Criar usuário com dados inválidos"),
    ("PUT", True, None, "Atualizar usuário"),
    ("DELETE", True, None, "Deletar usuário"),
    ("GET", False, "auth", "Acessar sem autenticação"),
    ("GET", False, "forbidden", "Acessar sem permissão"),
    ("GET", False, "server", "Erro interno do servidor"),
]

print("\nCenários e status codes apropriados:")
for operacao, sucesso, erro, descricao in cenarios:
    status = determinar_status_code(operacao, sucesso, erro)
    print(f"\n  {descricao}:")
    print(f"    Operação: {operacao}")
    print(f"    Status: {status} ({status_codes_info.get(status, {}).get('nome', 'Desconhecido')})")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - STATUS CODES HTTP")
print("=" * 60)
print("""
Status Codes mais importantes:

Sucesso (2xx):
- 200 OK: Operação bem-sucedida
- 201 Created: Recurso criado
- 204 No Content: Sucesso sem conteúdo (DELETE)

Erro do Cliente (4xx):
- 400 Bad Request: Requisição inválida
- 401 Unauthorized: Não autenticado
- 403 Forbidden: Sem permissão
- 404 Not Found: Recurso não encontrado
- 422 Unprocessable Entity: Erro de validação

Erro do Servidor (5xx):
- 500 Internal Server Error: Erro interno
- 503 Service Unavailable: Serviço indisponível

Boas práticas:
1. Use sempre o status code apropriado
2. Retorne mensagens de erro claras
3. Inclua detalhes úteis para desenvolvedores
4. Mantenha formato de resposta consistente
5. Use 422 para erros de validação de negócio
""")

