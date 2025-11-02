"""
06 - Exercícios de Modelagem de Recursos REST
==============================================
Exercícios práticos para modelar recursos RESTful
"""

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

print("=" * 60)
print("EXERCÍCIOS DE MODELAGEM REST")
print("=" * 60)


# ============================================
# EXERCÍCIO 1: SISTEMA DE BIBLIOTECA
# ============================================

"""
Exercício 1: Sistema de Biblioteca
-----------------------------------
Modele as URLs RESTful para um sistema de biblioteca que gerencia:
- Livros (books)
- Autores (authors)
- Empréstimos (loans)
- Usuários (users)

Relacionamentos:
- Um livro pode ter múltiplos autores
- Um autor pode ter múltiplos livros
- Um usuário pode fazer múltiplos empréstimos
- Um livro pode ser emprestado múltiplas vezes
"""

print("\n" + "=" * 60)
print("EXERCÍCIO 1: SISTEMA DE BIBLIOTECA")
print("=" * 60)

class BibliotecaREST:
    """Modelagem REST para sistema de biblioteca"""
    
    def __init__(self, base_url: str = "https://api.biblioteca.com"):
        self.base_url = base_url.rstrip('/')
        self.version = "v1"
    
    # Livros
    def listar_livros(self) -> str:
        """GET - Lista todos os livros"""
        return f"{self.base_url}/api/{self.version}/books"
    
    def obter_livro(self, livro_id: int) -> str:
        """GET - Obter livro específico"""
        return f"{self.base_url}/api/{self.version}/books/{livro_id}"
    
    def criar_livro(self) -> str:
        """POST - Criar novo livro"""
        return f"{self.base_url}/api/{self.version}/books"
    
    def atualizar_livro(self, livro_id: int) -> str:
        """PUT - Atualizar livro"""
        return f"{self.base_url}/api/{self.version}/books/{livro_id}"
    
    def deletar_livro(self, livro_id: int) -> str:
        """DELETE - Deletar livro"""
        return f"{self.base_url}/api/{self.version}/books/{livro_id}"
    
    # Autores
    def listar_autores(self) -> str:
        """GET - Lista todos os autores"""
        return f"{self.base_url}/api/{self.version}/authors"
    
    def obter_autor(self, autor_id: int) -> str:
        """GET - Obter autor específico"""
        return f"{self.base_url}/api/{self.version}/authors/{autor_id}"
    
    def livros_do_autor(self, autor_id: int) -> str:
        """GET - Livros de um autor"""
        return f"{self.base_url}/api/{self.version}/authors/{autor_id}/books"
    
    # Empréstimos
    def listar_emprestimos(self) -> str:
        """GET - Lista todos os empréstimos"""
        return f"{self.base_url}/api/{self.version}/loans"
    
    def obter_emprestimo(self, emprestimo_id: int) -> str:
        """GET - Obter empréstimo específico"""
        return f"{self.base_url}/api/{self.version}/loans/{emprestimo_id}"
    
    def criar_emprestimo(self) -> str:
        """POST - Criar novo empréstimo"""
        return f"{self.base_url}/api/{self.version}/loans"
    
    def devolver_emprestimo(self, emprestimo_id: int) -> str:
        """POST - Devolver livro (marcar como devolvido)"""
        return f"{self.base_url}/api/{self.version}/loans/{emprestimo_id}/return"
    
    # Usuários
    def emprestimos_do_usuario(self, usuario_id: int) -> str:
        """GET - Empréstimos de um usuário"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/loans"
    
    def livros_emprestados(self) -> str:
        """GET - Lista livros atualmente emprestados"""
        return f"{self.base_url}/api/{self.version}/books?status=borrowed"


biblioteca = BibliotecaREST()

print("\nURLs para Livros:")
print(f"  GET    {biblioteca.listar_livros()}")
print(f"  GET    {biblioteca.obter_livro(123)}")
print(f"  POST   {biblioteca.criar_livro()}")
print(f"  PUT    {biblioteca.atualizar_livro(123)}")
print(f"  DELETE {biblioteca.deletar_livro(123)}")

print("\nURLs para Autores:")
print(f"  GET    {biblioteca.listar_autores()}")
print(f"  GET    {biblioteca.obter_autor(456)}")
print(f"  GET    {biblioteca.livros_do_autor(456)}")

print("\nURLs para Empréstimos:")
print(f"  GET    {biblioteca.listar_emprestimos()}")
print(f"  GET    {biblioteca.obter_emprestimo(789)}")
print(f"  POST   {biblioteca.criar_emprestimo()}")
print(f"  POST   {biblioteca.devolver_emprestimo(789)}")

print("\nURLs para Usuários:")
print(f"  GET    {biblioteca.emprestimos_do_usuario(321)}")
print(f"  GET    {biblioteca.livros_emprestados()}")


# ============================================
# EXERCÍCIO 2: E-COMMERCE
# ============================================

"""
Exercício 2: Sistema E-Commerce
--------------------------------
Modele URLs RESTful para:
- Produtos (products)
- Categorias (categories)
- Carrinho (cart)
- Pedidos (orders)
- Clientes (customers)
- Avaliações (reviews)
"""

print("\n" + "=" * 60)
print("EXERCÍCIO 2: SISTEMA E-COMMERCE")
print("=" * 60)

class ECommerceREST:
    """Modelagem REST para e-commerce"""
    
    def __init__(self, base_url: str = "https://api.ecommerce.com"):
        self.base_url = base_url.rstrip('/')
        self.version = "v1"
    
    # Produtos
    def listar_produtos(self, categoria: str = None, busca: str = None) -> str:
        """GET - Lista produtos com filtros opcionais"""
        params = []
        if categoria:
            params.append(f"category={categoria}")
        if busca:
            params.append(f"search={busca}")
        query = "&".join(params)
        base = f"{self.base_url}/api/{self.version}/products"
        return f"{base}?{query}" if query else base
    
    def obter_produto(self, produto_id: int) -> str:
        """GET - Obter produto específico"""
        return f"{self.base_url}/api/{self.version}/products/{produto_id}"
    
    def avaliacoes_do_produto(self, produto_id: int) -> str:
        """GET - Avaliações de um produto"""
        return f"{self.base_url}/api/{self.version}/products/{produto_id}/reviews"
    
    # Categorias
    def listar_categorias(self) -> str:
        """GET - Lista categorias"""
        return f"{self.base_url}/api/{self.version}/categories"
    
    def produtos_da_categoria(self, categoria_id: int) -> str:
        """GET - Produtos de uma categoria"""
        return f"{self.base_url}/api/{self.version}/categories/{categoria_id}/products"
    
    # Carrinho
    def obter_carrinho(self, usuario_id: int) -> str:
        """GET - Obter carrinho do usuário"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/cart"
    
    def adicionar_ao_carrinho(self, usuario_id: int) -> str:
        """POST - Adicionar item ao carrinho"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/cart/items"
    
    def atualizar_item_carrinho(self, usuario_id: int, item_id: int) -> str:
        """PUT - Atualizar item do carrinho"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/cart/items/{item_id}"
    
    def remover_item_carrinho(self, usuario_id: int, item_id: int) -> str:
        """DELETE - Remover item do carrinho"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/cart/items/{item_id}"
    
    # Pedidos
    def criar_pedido(self, usuario_id: int) -> str:
        """POST - Criar pedido a partir do carrinho"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/orders"
    
    def listar_pedidos_usuario(self, usuario_id: int) -> str:
        """GET - Lista pedidos de um usuário"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/orders"
    
    def obter_pedido(self, usuario_id: int, pedido_id: int) -> str:
        """GET - Obter pedido específico"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/orders/{pedido_id}"
    
    def cancelar_pedido(self, usuario_id: int, pedido_id: int) -> str:
        """POST - Cancelar pedido"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/orders/{pedido_id}/cancel"


ecommerce = ECommerceREST()

print("\nURLs para Produtos:")
print(f"  GET    {ecommerce.listar_produtos()}")
print(f"  GET    {ecommerce.listar_produtos(categoria='electronics')}")
print(f"  GET    {ecommerce.listar_produtos(busca='notebook')}")
print(f"  GET    {ecommerce.obter_produto(123)}")
print(f"  GET    {ecommerce.avaliacoes_do_produto(123)}")

print("\nURLs para Carrinho:")
print(f"  GET    {ecommerce.obter_carrinho(456)}")
print(f"  POST   {ecommerce.adicionar_ao_carrinho(456)}")
print(f"  PUT    {ecommerce.atualizar_item_carrinho(456, 1)}")
print(f"  DELETE {ecommerce.remover_item_carrinho(456, 1)}")

print("\nURLs para Pedidos:")
print(f"  POST   {ecommerce.criar_pedido(456)}")
print(f"  GET    {ecommerce.listar_pedidos_usuario(456)}")
print(f"  GET    {ecommerce.obter_pedido(456, 789)}")
print(f"  POST   {ecommerce.cancelar_pedido(456, 789)}")


# ============================================
# EXERCÍCIO 3: REDE SOCIAL
# ============================================

"""
Exercício 3: Rede Social
-------------------------
Modele URLs RESTful para:
- Usuários (users)
- Posts (posts)
- Comentários (comments)
- Curtidas (likes)
- Amigos/Seguidores (friends/followers)
"""

print("\n" + "=" * 60)
print("EXERCÍCIO 3: REDE SOCIAL")
print("=" * 60)

class RedeSocialREST:
    """Modelagem REST para rede social"""
    
    def __init__(self, base_url: str = "https://api.social.com"):
        self.base_url = base_url.rstrip('/')
        self.version = "v1"
    
    # Usuários
    def listar_usuarios(self) -> str:
        """GET - Lista usuários"""
        return f"{self.base_url}/api/{self.version}/users"
    
    def obter_usuario(self, usuario_id: int) -> str:
        """GET - Obter usuário"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}"
    
    def seguir_usuario(self, usuario_id: int) -> str:
        """POST - Seguir usuário"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/follow"
    
    def deixar_de_seguir(self, usuario_id: int) -> str:
        """DELETE - Deixar de seguir"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/follow"
    
    def seguidores(self, usuario_id: int) -> str:
        """GET - Lista seguidores"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/followers"
    
    def seguindo(self, usuario_id: int) -> str:
        """GET - Lista quem está seguindo"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/following"
    
    # Posts
    def feed_usuario(self, usuario_id: int) -> str:
        """GET - Feed de posts do usuário"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/posts"
    
    def criar_post(self, usuario_id: int) -> str:
        """POST - Criar novo post"""
        return f"{self.base_url}/api/{self.version}/users/{usuario_id}/posts"
    
    def obter_post(self, post_id: int) -> str:
        """GET - Obter post específico"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}"
    
    def deletar_post(self, post_id: int) -> str:
        """DELETE - Deletar post"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}"
    
    # Comentários
    def comentarios_do_post(self, post_id: int) -> str:
        """GET - Comentários de um post"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}/comments"
    
    def criar_comentario(self, post_id: int) -> str:
        """POST - Criar comentário"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}/comments"
    
    # Curtidas
    def curtir_post(self, post_id: int) -> str:
        """POST - Curtir post"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}/like"
    
    def descurtir_post(self, post_id: int) -> str:
        """DELETE - Descurtir post"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}/like"
    
    def curtidas_do_post(self, post_id: int) -> str:
        """GET - Lista quem curtiu o post"""
        return f"{self.base_url}/api/{self.version}/posts/{post_id}/likes"


rede_social = RedeSocialREST()

print("\nURLs para Usuários:")
print(f"  GET    {rede_social.listar_usuarios()}")
print(f"  GET    {rede_social.obter_usuario(123)}")
print(f"  POST   {rede_social.seguir_usuario(123)}")
print(f"  DELETE {rede_social.deixar_de_seguir(123)}")
print(f"  GET    {rede_social.seguidores(123)}")
print(f"  GET    {rede_social.seguindo(123)}")

print("\nURLs para Posts:")
print(f"  GET    {rede_social.feed_usuario(456)}")
print(f"  POST   {rede_social.criar_post(456)}")
print(f"  GET    {rede_social.obter_post(789)}")
print(f"  DELETE {rede_social.deletar_post(789)}")

print("\nURLs para Interações:")
print(f"  GET    {rede_social.comentarios_do_post(789)}")
print(f"  POST   {rede_social.criar_comentario(789)}")
print(f"  POST   {rede_social.curtir_post(789)}")
print(f"  DELETE {rede_social.descurtir_post(789)}")
print(f"  GET    {rede_social.curtidas_do_post(789)}")


# ============================================
# DESAFIO: MODELAR SEU PRÓPRIO SISTEMA
# ============================================

print("\n" + "=" * 60)
print("DESAFIO: CRIE SUA PRÓPRIA MODELAGEM")
print("=" * 60)
print("""
Exercício prático:

Escolha um sistema do seu interesse e modele suas URLs RESTful:
1. Identifique os recursos principais
2. Identifique os relacionamentos
3. Crie URLs seguindo os princípios REST
4. Defina quais métodos HTTP serão usados
5. Inclua query parameters quando necessário

Exemplos de sistemas:
- Sistema de delivery
- Plataforma de cursos online
- Aplicativo de tarefas (todo list)
- Sistema de agendamento
- Plataforma de streaming
- Sistema de mensagens

Critérios de avaliação:
✓ URLs usam substantivos (não verbos)
✓ URLs usam plural para recursos
✓ Hierarquia representa relacionamentos
✓ Métodos HTTP apropriados
✓ Query parameters bem definidos
✓ Versionamento incluído
""")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO DOS EXERCÍCIOS")
print("=" * 60)
print("""
Conceitos praticados:

1. Modelagem de recursos:
   - Identificar recursos principais
   - Identificar relacionamentos
   - Criar hierarquia de URLs

2. Métodos HTTP apropriados:
   - GET para recuperar
   - POST para criar
   - PUT/PATCH para atualizar
   - DELETE para remover

3. Query parameters:
   - Filtros
   - Paginação
   - Ordenação
   - Busca

4. Boas práticas:
   - URLs claras e consistentes
   - Hierarquia lógica
   - Versionamento
   - Seguir padrões REST

Próximos passos:
- Implementar essas URLs em uma API real
- Adicionar autenticação e autorização
- Testar com ferramentas como Postman
""")

