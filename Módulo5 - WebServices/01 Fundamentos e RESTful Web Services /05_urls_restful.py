"""
05 - Estrutura de URLs RESTful
=================================
Padrões e boas práticas para estrutura de URLs RESTful
"""

import json
from typing import List, Dict, Any
from urllib.parse import urljoin, urlparse, parse_qs

print("=" * 60)
print("ESTRUTURA DE URLs RESTFUL")
print("=" * 60)


# ============================================
# 1. PRINCÍPIOS DE URLs RESTFUL
# ============================================

"""
Princípios de URLs RESTful:
----------------------------
1. Use substantivos, não verbos (GET /users, não GET /getUsers)
2. Use plural para recursos (/users, não /user)
3. Use hierarquia para relacionamentos (/users/1/posts)
4. Use letras minúsculas
5. Use hífens, não underscores (/user-profiles, não /user_profiles)
6. Não use extensões de arquivo (/users, não /users.json)
7. Versionamento na URL (/api/v1/users)
"""

class URIRestful:
    """Classe para construir e validar URLs RESTful"""
    
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url.rstrip('/')
        self.version = "v1"
    
    def colecao(self, recurso: str) -> str:
        """
        Retorna URL para coleção de recursos
        GET    /api/v1/users
        POST   /api/v1/users
        """
        return f"{self.base_url}/api/{self.version}/{recurso}"
    
    def recurso(self, recurso: str, id: Any) -> str:
        """
        Retorna URL para recurso específico
        GET    /api/v1/users/123
        PUT    /api/v1/users/123
        PATCH  /api/v1/users/123
        DELETE /api/v1/users/123
        """
        return f"{self.base_url}/api/{self.version}/{recurso}/{id}"
    
    def sub_recurso(self, recurso: str, id: Any, sub_recurso: str, sub_id: Any = None) -> str:
        """
        Retorna URL para sub-recurso
        GET    /api/v1/users/123/posts
        GET    /api/v1/users/123/posts/456
        """
        if sub_id:
            return f"{self.base_url}/api/{self.version}/{recurso}/{id}/{sub_recurso}/{sub_id}"
        return f"{self.base_url}/api/{self.version}/{recurso}/{id}/{sub_recurso}"
    
    def acao(self, recurso: str, id: Any, acao: str) -> str:
        """
        Retorna URL para ação específica (não RESTful puro, mas comum)
        POST   /api/v1/users/123/activate
        POST   /api/v1/posts/456/publish
        """
        return f"{self.base_url}/api/{self.version}/{recurso}/{id}/{acao}"


print("\n" + "=" * 60)
print("CONSTRUÇÃO DE URLs RESTFUL")
print("=" * 60)

uri = URIRestful("https://api.example.com")

print("\n1. URLs de Coleção:")
print(f"  {uri.colecao('users')}")
print(f"  {uri.colecao('products')}")
print(f"  {uri.colecao('orders')}")

print("\n2. URLs de Recurso Específico:")
print(f"  {uri.recurso('users', 123)}")
print(f"  {uri.recurso('products', 456)}")
print(f"  {uri.recurso('orders', 789)}")

print("\n3. URLs de Sub-recursos:")
print(f"  {uri.sub_recurso('users', 123, 'posts')}")
print(f"  {uri.sub_recurso('users', 123, 'posts', 456)}")
print(f"  {uri.sub_recurso('orders', 789, 'items')}")

print("\n4. URLs de Ações:")
print(f"  {uri.acao('users', 123, 'activate')}")
print(f"  {uri.acao('posts', 456, 'publish')}")


# ============================================
# 2. QUERY PARAMETERS EM URLs RESTFUL
# ============================================

"""
Query Parameters Comuns:
-------------------------
- Paginação: ?page=1&limit=10
- Filtros: ?status=active&category=electronics
- Ordenação: ?sort=name&order=asc
- Busca: ?search=termo
- Campos: ?fields=id,name,email (para limitar campos retornados)
"""

class QueryParamsBuilder:
    """Constrói query strings para URLs RESTful"""
    
    @staticmethod
    def paginacao(page: int = 1, limit: int = 10) -> str:
        """Adiciona parâmetros de paginação"""
        return f"page={page}&limit={limit}"
    
    @staticmethod
    def filtros(filtros: Dict[str, Any]) -> str:
        """Adiciona parâmetros de filtro"""
        params = []
        for key, value in filtros.items():
            params.append(f"{key}={value}")
        return "&".join(params)
    
    @staticmethod
    def ordenacao(campo: str, ordem: str = "asc") -> str:
        """Adiciona parâmetros de ordenação"""
        return f"sort={campo}&order={ordem}"
    
    @staticmethod
    def busca(termo: str) -> str:
        """Adiciona parâmetro de busca"""
        return f"search={termo}"
    
    @staticmethod
    def campos(campos: List[str]) -> str:
        """Adiciona parâmetro de seleção de campos"""
        return f"fields={','.join(campos)}"
    
    @staticmethod
    def construir(**kwargs) -> str:
        """Constrói query string completa"""
        params = []
        
        # Paginação
        if 'page' in kwargs or 'limit' in kwargs:
            page = kwargs.get('page', 1)
            limit = kwargs.get('limit', 10)
            params.append(QueryParamsBuilder.paginacao(page, limit))
        
        # Filtros
        if 'filtros' in kwargs:
            params.append(QueryParamsBuilder.filtros(kwargs['filtros']))
        
        # Ordenação
        if 'sort' in kwargs:
            ordem = kwargs.get('order', 'asc')
            params.append(QueryParamsBuilder.ordenacao(kwargs['sort'], ordem))
        
        # Busca
        if 'search' in kwargs:
            params.append(QueryParamsBuilder.busca(kwargs['search']))
        
        # Campos
        if 'fields' in kwargs:
            params.append(QueryParamsBuilder.campos(kwargs['fields']))
        
        return "&".join(params) if params else ""


print("\n" + "=" * 60)
print("QUERY PARAMETERS")
print("=" * 60)

query_builder = QueryParamsBuilder()

print("\n1. Paginação:")
query = query_builder.paginacao(page=2, limit=20)
print(f"  ?{query}")
print(f"  URL completa: {uri.colecao('users')}?{query}")

print("\n2. Filtros:")
query = query_builder.filtros({"status": "active", "role": "admin"})
print(f"  ?{query}")
print(f"  URL completa: {uri.colecao('users')}?{query}")

print("\n3. Ordenação:")
query = query_builder.ordenacao("nome", "asc")
print(f"  ?{query}")
print(f"  URL completa: {uri.colecao('users')}?{query}")

print("\n4. Busca:")
query = query_builder.busca("joão")
print(f"  ?{query}")
print(f"  URL completa: {uri.colecao('users')}?{query}")

print("\n5. Query completa combinada:")
query = query_builder.construir(
    page=1,
    limit=10,
    sort="nome",
    order="asc",
    filtros={"status": "active"},
    search="joão",
    fields=["id", "nome", "email"]
)
print(f"  ?{query}")
print(f"  URL completa: {uri.colecao('users')}?{query}")


# ============================================
# 3. EXEMPLOS DE URLs RESTFUL BEM ESTRUTURADAS
# ============================================

print("\n" + "=" * 60)
print("EXEMPLOS DE URLs RESTFUL")
print("=" * 60)

exemplos_restful = {
    "Bom": [
        "GET    /api/v1/users",
        "GET    /api/v1/users/123",
        "POST   /api/v1/users",
        "PUT    /api/v1/users/123",
        "DELETE /api/v1/users/123",
        "GET    /api/v1/users/123/posts",
        "GET    /api/v1/users/123/posts/456",
        "GET    /api/v1/products?page=1&limit=10",
        "GET    /api/v1/products?category=electronics&sort=price&order=asc",
    ],
    "Ruim": [
        "GET    /api/v1/getUsers",           # Verbo na URL
        "GET    /api/v1/user",               # Singular em vez de plural
        "POST   /api/v1/createUser",          # Verbo na URL
        "GET    /api/v1/users/123/getPosts",  # Verbo na URL
        "GET    /api/v1/users_123",           # Underscore
        "GET    /api/v1/users.json",          # Extensão de arquivo
        "POST   /api/v1/userCreate",          # Verbo na URL
    ]
}

for categoria, urls in exemplos_restful.items():
    print(f"\n{categoria}:")
    for url in urls:
        print(f"  {url}")


# ============================================
# 4. VERSIONAMENTO DE APIs
# ============================================

"""
Estratégias de Versionamento:
------------------------------
1. URL Versioning: /api/v1/users (mais comum, explícito)
2. Header Versioning: Accept: application/vnd.api.v1+json
3. Query Parameter: /api/users?version=1
"""

class APIVersioning:
    """Gerencia versionamento de APIs"""
    
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url.rstrip('/')
        self.versao_atual = "v1"
        self.versoes_suportadas = ["v1", "v2"]
    
    def url_com_versao(self, recurso: str, versao: str = None) -> str:
        """Constrói URL com versão"""
        versao = versao or self.versao_atual
        return f"{self.base_url}/api/{versao}/{recurso}"
    
    def migrar_versao(self, url_antiga: str, nova_versao: str) -> str:
        """Migra URL de uma versão para outra"""
        # Substitui a versão na URL
        partes = url_antiga.split('/')
        for i, parte in enumerate(partes):
            if parte.startswith('v') and parte[1:].isdigit():
                partes[i] = nova_versao
                break
        return '/'.join(partes)
    
    def validar_versao(self, versao: str) -> bool:
        """Valida se versão é suportada"""
        return versao in self.versoes_suportadas


print("\n" + "=" * 60)
print("VERSIONAMENTO DE APIs")
print("=" * 60)

versioning = APIVersioning()

print("\n1. URLs com diferentes versões:")
print(f"  v1: {versioning.url_com_versao('users', 'v1')}")
print(f"  v2: {versioning.url_com_versao('users', 'v2')}")

print("\n2. Migração de versão:")
url_v1 = "https://api.example.com/api/v1/users/123"
url_v2 = versioning.migrar_versao(url_v1, "v2")
print(f"  Original:  {url_v1}")
print(f"  Migrada:   {url_v2}")

print("\n3. Validação de versão:")
for versao in ["v1", "v2", "v3"]:
    valida = versioning.validar_versao(versao)
    print(f"  v{versao[1:]}: {'✓ Suportada' if valida else '✗ Não suportada'}")


# ============================================
# 5. HIERARQUIA DE RECURSOS
# ============================================

"""
Hierarquia de Recursos:
------------------------
Representa relacionamentos entre recursos através de URLs aninhadas

Exemplos:
- /api/v1/users/123/posts          → Posts do usuário 123
- /api/v1/users/123/posts/456       → Post específico do usuário 123
- /api/v1/orders/789/items          → Itens do pedido 789
- /api/v1/orders/789/items/1        → Item específico do pedido 789
"""

class HierarquiaRecursos:
    """Gerencia hierarquia de recursos em URLs RESTful"""
    
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url.rstrip('/')
        self.version = "v1"
    
    def recursos_aninhados(self, *recursos) -> str:
        """
        Constrói URL para recursos aninhados
        Exemplo: recursos_aninhados('users', 123, 'posts') 
                 → /api/v1/users/123/posts
        """
        caminho = "/".join(str(r) for r in recursos)
        return f"{self.base_url}/api/{self.version}/{caminho}"


print("\n" + "=" * 60)
print("HIERARQUIA DE RECURSOS")
print("=" * 60)

hierarquia = HierarquiaRecursos()

exemplos_hierarquia = [
    ("users", 123, "posts"),
    ("users", 123, "posts", 456),
    ("users", 123, "comments"),
    ("orders", 789, "items"),
    ("orders", 789, "items", 1),
    ("posts", 456, "comments"),
    ("posts", 456, "comments", 10),
]

print("\nExemplos de hierarquia de recursos:")
for recursos in exemplos_hierarquia:
    url = hierarquia.recursos_aninhados(*recursos)
    print(f"  {url}")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - URLs RESTFUL")
print("=" * 60)
print("""
Boas práticas para URLs RESTful:

1. Estrutura:
   - Use substantivos (não verbos)
   - Use plural para recursos (/users)
   - Use hierarquia para relacionamentos (/users/1/posts)

2. Query Parameters:
   - Paginação: ?page=1&limit=10
   - Filtros: ?status=active
   - Ordenação: ?sort=name&order=asc
   - Busca: ?search=termo

3. Versionamento:
   - Use /api/v1/ na URL
   - Mantenha versões antigas funcionando
   - Documente mudanças entre versões

4. Hierarquia:
   - Represente relacionamentos através de URLs aninhadas
   - /recurso/{id}/sub-recurso/{sub-id}

5. Evite:
   - Verbos na URL (GET, POST, etc.)
   - Underlines (use hífens)
   - Extensões de arquivo (.json, .xml)
   - URLs muito profundas (mais de 3 níveis)
""")

