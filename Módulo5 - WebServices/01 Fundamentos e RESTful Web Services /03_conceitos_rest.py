"""
03 - Conceitos REST (Representational State Transfer)
======================================================
Exploração detalhada dos princípios e conceitos REST
"""

import json
from typing import Dict, List, Any, Optional
from enum import Enum

print("=" * 60)
print("CONCEITOS REST - REPRESENTATIONAL STATE TRANSFER")
print("=" * 60)


# ============================================
# 1. O QUE É REST?
# ============================================

"""
REST (Representational State Transfer):
----------------------------------------
REST é um estilo arquitetural para projetar sistemas distribuídos,
baseado em princípios específicos que tornam as APIs simples,
escaláveis e fáceis de usar.

Princípios fundamentais:
1. Stateless (sem estado)
2. Client-Server (separação de responsabilidades)
3. Cacheable (pode ser cacheado)
4. Uniform Interface (interface uniforme)
5. Layered System (sistema em camadas)
6. Code on Demand (código sob demanda - opcional)
"""


# ============================================
# 2. RECURSOS E IDENTIFICADORES (URIs)
# ============================================

"""
Recursos REST:
--------------
Um recurso é qualquer coisa que pode ser identificado e acessado via URI.
Recursos são representações de dados ou funcionalidades.

Exemplos de recursos:
- /api/users           → Lista de usuários
- /api/users/123       → Usuário específico (ID 123)
- /api/users/123/posts → Posts do usuário 123
- /api/products/456    → Produto específico (ID 456)
"""

class RecursoREST:
    """Representa um recurso REST"""
    
    def __init__(self, nome: str, uri: str, descricao: str):
        self.nome = nome
        self.uri = uri
        self.descricao = descricao
    
    def __repr__(self):
        return f"Recurso: {self.nome} ({self.uri})"


print("\n" + "=" * 60)
print("RECURSOS REST")
print("=" * 60)

recursos_exemplo = [
    RecursoREST("Lista de Usuários", "/api/users", "Coleção de usuários"),
    RecursoREST("Usuário Específico", "/api/users/{id}", "Um usuário específico"),
    RecursoREST("Posts do Usuário", "/api/users/{id}/posts", "Posts de um usuário"),
    RecursoREST("Lista de Produtos", "/api/products", "Coleção de produtos"),
    RecursoREST("Produto Específico", "/api/products/{id}", "Um produto específico"),
]

for recurso in recursos_exemplo:
    print(f"\n{recurso.nome}:")
    print(f"  URI: {recurso.uri}")
    print(f"  Descrição: {recurso.descricao}")


# ============================================
# 3. MÉTODOS HTTP E SEUS SIGNIFICADOS REST
# ============================================

"""
Mapeamento de Métodos HTTP para Operações REST:
------------------------------------------------
GET    /api/users        → Listar todos os usuários
GET    /api/users/123    → Obter usuário específico
POST   /api/users        → Criar novo usuário
PUT    /api/users/123    → Atualizar usuário completo (substituir)
PATCH  /api/users/123    → Atualizar usuário parcialmente
DELETE /api/users/123    → Deletar usuário
"""

class MetodoHTTP(Enum):
    """Enumeração dos métodos HTTP"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"


class OperacaoREST:
    """Representa uma operação REST"""
    
    def __init__(self, metodo: MetodoHTTP, uri: str, descricao: str, idempotente: bool = False):
        self.metodo = metodo
        self.uri = uri
        self.descricao = descricao
        self.idempotente = idempotente  # Pode ser executado múltiplas vezes com mesmo resultado
    
    def __repr__(self):
        idem_texto = " (Idempotente)" if self.idempotente else ""
        return f"{self.metodo.value} {self.uri} - {self.descricao}{idem_texto}"


print("\n" + "=" * 60)
print("MÉTODOS HTTP EM REST")
print("=" * 60)

operacoes_rest = [
    OperacaoREST(MetodoHTTP.GET, "/api/users", "Listar todos os usuários", True),
    OperacaoREST(MetodoHTTP.GET, "/api/users/{id}", "Obter usuário específico", True),
    OperacaoREST(MetodoHTTP.POST, "/api/users", "Criar novo usuário", False),
    OperacaoREST(MetodoHTTP.PUT, "/api/users/{id}", "Atualizar usuário completo", True),
    OperacaoREST(MetodoHTTP.PATCH, "/api/users/{id}", "Atualizar usuário parcialmente", False),
    OperacaoREST(MetodoHTTP.DELETE, "/api/users/{id}", "Deletar usuário", True),
]

for op in operacoes_rest:
    print(f"\n{op}")


# ============================================
# 4. PRINCÍPIOS REST EM PRÁTICA
# ============================================

class APIREST:
    """Simulação de uma API REST seguindo os princípios REST"""
    
    def __init__(self):
        self.recursos = {}
        self.contador_ids = {}
        self.cache = {}  # Simula cache (princípio cacheable)
    
    def _get_contador(self, recurso: str) -> int:
        """Obtém ou cria contador para um recurso"""
        if recurso not in self.contador_ids:
            self.contador_ids[recurso] = 1
        return self.contador_ids[recurso]
    
    def _incrementar_contador(self, recurso: str):
        """Incrementa contador para um recurso"""
        if recurso not in self.contador_ids:
            self.contador_ids[recurso] = 1
        else:
            self.contador_ids[recurso] += 1
    
    def listar(self, recurso: str) -> Dict[str, Any]:
        """
        GET /api/{recurso}
        Lista todos os recursos
        """
        if recurso not in self.recursos:
            return {
                "status": 200,
                "data": [],
                "total": 0
            }
        
        items = list(self.recursos[recurso].values())
        return {
            "status": 200,
            "data": items,
            "total": len(items)
        }
    
    def obter(self, recurso: str, id: int) -> Dict[str, Any]:
        """
        GET /api/{recurso}/{id}
        Obtém um recurso específico
        """
        if recurso not in self.recursos or id not in self.recursos[recurso]:
            return {
                "status": 404,
                "error": "Recurso não encontrado"
            }
        
        return {
            "status": 200,
            "data": self.recursos[recurso][id]
        }
    
    def criar(self, recurso: str, dados: Dict[str, Any]) -> Dict[str, Any]:
        """
        POST /api/{recurso}
        Cria um novo recurso
        """
        if recurso not in self.recursos:
            self.recursos[recurso] = {}
        
        novo_id = self._get_contador(recurso)
        self._incrementar_contador(recurso)
        
        novo_recurso = {"id": novo_id, **dados}
        self.recursos[recurso][novo_id] = novo_recurso
        
        return {
            "status": 201,
            "data": novo_recurso,
            "location": f"/api/{recurso}/{novo_id}"
        }
    
    def atualizar_completo(self, recurso: str, id: int, dados: Dict[str, Any]) -> Dict[str, Any]:
        """
        PUT /api/{recurso}/{id}
        Atualiza um recurso completamente (substitui)
        """
        if recurso not in self.recursos or id not in self.recursos[recurso]:
            return {
                "status": 404,
                "error": "Recurso não encontrado"
            }
        
        dados_atualizados = {"id": id, **dados}
        self.recursos[recurso][id] = dados_atualizados
        
        return {
            "status": 200,
            "data": dados_atualizados
        }
    
    def atualizar_parcial(self, recurso: str, id: int, dados_parciais: Dict[str, Any]) -> Dict[str, Any]:
        """
        PATCH /api/{recurso}/{id}
        Atualiza um recurso parcialmente
        """
        if recurso not in self.recursos or id not in self.recursos[recurso]:
            return {
                "status": 404,
                "error": "Recurso não encontrado"
            }
        
        self.recursos[recurso][id].update(dados_parciais)
        
        return {
            "status": 200,
            "data": self.recursos[recurso][id]
        }
    
    def deletar(self, recurso: str, id: int) -> Dict[str, Any]:
        """
        DELETE /api/{recurso}/{id}
        Deleta um recurso
        """
        if recurso not in self.recursos or id not in self.recursos[recurso]:
            return {
                "status": 404,
                "error": "Recurso não encontrado"
            }
        
        del self.recursos[recurso][id]
        
        return {
            "status": 204,
            "message": "Recurso deletado com sucesso"
        }


print("\n" + "=" * 60)
print("DEMONSTRAÇÃO PRÁTICA DE API REST")
print("=" * 60)

api = APIREST()

# Criar recursos
print("\n1. POST /api/users - Criar usuários:")
user1 = api.criar("users", {"nome": "João Silva", "email": "joao@example.com", "idade": 30})
print(json.dumps(user1, indent=2, ensure_ascii=False))

user2 = api.criar("users", {"nome": "Maria Santos", "email": "maria@example.com", "idade": 25})
print(json.dumps(user2, indent=2, ensure_ascii=False))

# Listar recursos
print("\n2. GET /api/users - Listar todos os usuários:")
lista = api.listar("users")
print(json.dumps(lista, indent=2, ensure_ascii=False))

# Obter recurso específico
print("\n3. GET /api/users/1 - Obter usuário específico:")
usuario = api.obter("users", 1)
print(json.dumps(usuario, indent=2, ensure_ascii=False))

# Atualizar completamente (PUT)
print("\n4. PUT /api/users/1 - Atualizar completamente:")
atualizado = api.atualizar_completo("users", 1, {
    "nome": "João Silva Santos",
    "email": "joao.silva@example.com",
    "idade": 31,
    "cidade": "São Paulo"
})
print(json.dumps(atualizado, indent=2, ensure_ascii=False))

# Atualizar parcialmente (PATCH)
print("\n5. PATCH /api/users/1 - Atualizar apenas idade:")
parcial = api.atualizar_parcial("users", 1, {"idade": 32})
print(json.dumps(parcial, indent=2, ensure_ascii=False))

# Deletar recurso
print("\n6. DELETE /api/users/2 - Deletar usuário:")
deletado = api.deletar("users", 2)
print(json.dumps(deletado, indent=2, ensure_ascii=False))

# Verificar que foi deletado
print("\n7. GET /api/users - Listar após deletar:")
lista_final = api.listar("users")
print(json.dumps(lista_final, indent=2, ensure_ascii=False))


# ============================================
# 5. CARACTERÍSTICAS REST
# ============================================

print("\n" + "=" * 60)
print("CARACTERÍSTICAS REST")
print("=" * 60)

caracteristicas_rest = {
    "Stateless (Sem Estado)": {
        "descricao": "Cada requisição contém toda informação necessária",
        "exemplo": "Não mantém sessão entre requisições",
        "beneficio": "Facilita escalabilidade e cache"
    },
    "Client-Server": {
        "descricao": "Separação clara entre cliente e servidor",
        "exemplo": "Cliente faz requisições, servidor processa e responde",
        "beneficio": "Permite evolução independente"
    },
    "Cacheable": {
        "descricao": "Respostas podem ser cacheadas",
        "exemplo": "GET /api/users pode ser cacheado",
        "beneficio": "Melhora performance e reduz carga no servidor"
    },
    "Uniform Interface": {
        "descricao": "Interface consistente para todos os recursos",
        "exemplo": "Sempre usa GET/POST/PUT/DELETE da mesma forma",
        "beneficio": "Facilita uso e entendimento"
    },
    "Layered System": {
        "descricao": "Sistema pode ter múltiplas camadas (proxies, gateways)",
        "exemplo": "Load balancer → API Gateway → Servidor",
        "beneficio": "Melhora segurança e performance"
    }
}

for caracteristica, info in caracteristicas_rest.items():
    print(f"\n{caracteristica}:")
    print(f"  Descrição: {info['descricao']}")
    print(f"  Exemplo: {info['exemplo']}")
    print(f"  Benefício: {info['beneficio']}")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO DOS CONCEITOS REST")
print("=" * 60)
print("""
Princípios REST:
1. Stateless - Cada requisição é independente
2. Client-Server - Separação de responsabilidades
3. Cacheable - Respostas podem ser cacheadas
4. Uniform Interface - Interface consistente
5. Layered System - Múltiplas camadas possíveis

Métodos HTTP em REST:
- GET: Recuperar dados (idempotente)
- POST: Criar novo recurso (não idempotente)
- PUT: Atualizar completamente (idempotente)
- PATCH: Atualizar parcialmente (não idempotente)
- DELETE: Remover recurso (idempotente)

Estrutura de URIs RESTful:
- /api/{recurso}          → Coleção
- /api/{recurso}/{id}     → Recurso específico
- /api/{recurso}/{id}/{subrecurso} → Sub-recurso
""")

