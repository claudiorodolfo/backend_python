"""
04 - EXEMPLOS PRÁTICOS DO MVC
=============================

Casos de uso reais:
1. Sistema de gerenciamento de blog
2. Sistema de autenticação
3. API REST com MVC
4. Aplicação de gerenciamento de contatos
"""

from abc import ABC, abstractmethod

# EXEMPLO 1: Sistema de Blog (Post)
# ==================================

class ModelPost:
    """Model - Gerencia posts do blog"""
    
    def __init__(self):
        self._posts = []
        self._observers = []
        self._next_id = 1
    
    def adicionar_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self, evento, dados=None):
        for observer in self._observers:
            observer.atualizar(evento, dados)
    
    def criar_post(self, titulo, conteudo, autor):
        post = {
            "id": self._next_id,
            "titulo": titulo,
            "conteudo": conteudo,
            "autor": autor,
            "data_criacao": "2024-01-01",
            "visualizacoes": 0
        }
        self._posts.append(post)
        self._next_id += 1
        self._notificar("post_criado", post)
        return post["id"]
    
    def obter_post(self, post_id):
        for post in self._posts:
            if post["id"] == post_id:
                post["visualizacoes"] += 1
                self._notificar("post_visualizado", post)
                return post.copy()
        return None
    
    def listar_posts(self):
        return [post.copy() for post in self._posts]
    
    def buscar_posts(self, termo):
        resultados = [
            post for post in self._posts
            if termo.lower() in post["titulo"].lower() or 
               termo.lower() in post["conteudo"].lower()
        ]
        return resultados


class ViewPost:
    """View - Apresenta posts"""
    
    def __init__(self, model):
        self.model = model
        self.model.adicionar_observer(self)
    
    def atualizar(self, evento, dados):
        if evento == "post_criado":
            print(f"[VIEW] Novo post criado: {dados['titulo']}")
        elif evento == "post_visualizado":
            print(f"[VIEW] Post visualizado: {dados['titulo']} ({dados['visualizacoes']} views)")
    
    def renderizar_post(self, post):
        """Renderiza um post individual"""
        print("\n" + "=" * 50)
        print(f"TÍTULO: {post['titulo']}")
        print("=" * 50)
        print(f"Autor: {post['autor']}")
        print(f"Data: {post['data_criacao']}")
        print(f"Visualizações: {post['visualizacoes']}")
        print("-" * 50)
        print(post['conteudo'])
        print("=" * 50)
    
    def renderizar_lista(self, posts):
        """Renderiza lista de posts"""
        print("\n" + "=" * 50)
        print("LISTA DE POSTS")
        print("=" * 50)
        if not posts:
            print("Nenhum post encontrado.")
        else:
            for post in posts:
                print(f"[{post['id']}] {post['titulo']} - {post['autor']} ({post['visualizacoes']} views)")
        print("=" * 50)


class ControllerPost:
    """Controller - Gerencia operações de blog"""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def criar_post(self, titulo, conteudo, autor):
        """Cria novo post"""
        if not titulo or not conteudo:
            print("Erro: Título e conteúdo são obrigatórios")
            return None
        
        post_id = self.model.criar_post(titulo, conteudo, autor)
        print(f"Post #{post_id} criado com sucesso!")
        return post_id
    
    def visualizar_post(self, post_id):
        """Visualiza post específico"""
        post = self.model.obter_post(post_id)
        if post:
            self.view.renderizar_post(post)
        else:
            print(f"Post #{post_id} não encontrado")
    
    def listar_posts(self):
        """Lista todos os posts"""
        posts = self.model.listar_posts()
        self.view.renderizar_lista(posts)
    
    def buscar(self, termo):
        """Busca posts"""
        resultados = self.model.buscar_posts(termo)
        self.view.renderizar_lista(resultados)


# EXEMPLO 2: Sistema de Autenticação
# ====================================

class ModelUsuario:
    """Model - Gerencia usuários"""
    
    def __init__(self):
        self._usuarios = {
            "admin": {"senha": "admin123", "nome": "Administrador", "nivel": "admin"},
            "user1": {"senha": "user123", "nome": "Usuário 1", "nivel": "user"}
        }
        self._usuario_logado = None
        self._observers = []
    
    def adicionar_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self, evento, dados=None):
        for observer in self._observers:
            observer.atualizar(evento, dados)
    
    def autenticar(self, usuario, senha):
        """Autentica usuário"""
        if usuario in self._usuarios:
            if self._usuarios[usuario]["senha"] == senha:
                self._usuario_logado = usuario
                self._notificar("login_sucesso", {
                    "usuario": usuario,
                    "nome": self._usuarios[usuario]["nome"]
                })
                return True
        
        self._notificar("login_falha", {"usuario": usuario})
        return False
    
    def logout(self):
        """Faz logout"""
        usuario = self._usuario_logado
        self._usuario_logado = None
        if usuario:
            self._notificar("logout", {"usuario": usuario})
    
    def get_usuario_logado(self):
        """Obtém usuário logado"""
        if self._usuario_logado:
            return {
                "usuario": self._usuario_logado,
                "nome": self._usuarios[self._usuario_logado]["nome"],
                "nivel": self._usuarios[self._usuario_logado]["nivel"]
            }
        return None


class ViewAuth:
    """View - Interface de autenticação"""
    
    def __init__(self, model):
        self.model = model
        self.model.adicionar_observer(self)
    
    def atualizar(self, evento, dados):
        if evento == "login_sucesso":
            print(f"[VIEW] Bem-vindo, {dados['nome']}!")
        elif evento == "login_falha":
            print("[VIEW] Usuário ou senha incorretos")
        elif evento == "logout":
            print(f"[VIEW] {dados['usuario']} deslogado")
    
    def renderizar_tela_login(self):
        """Renderiza tela de login"""
        print("\n" + "=" * 40)
        print("TELA DE LOGIN")
        print("=" * 40)
    
    def renderizar_dashboard(self, usuario_info):
        """Renderiza dashboard do usuário"""
        print("\n" + "=" * 40)
        print("DASHBOARD")
        print("=" * 40)
        print(f"Usuário: {usuario_info['nome']}")
        print(f"Nível: {usuario_info['nivel']}")
        print("=" * 40)


class ControllerAuth:
    """Controller - Gerencia autenticação"""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def login(self, usuario, senha):
        """Realiza login"""
        self.view.renderizar_tela_login()
        if self.model.autenticar(usuario, senha):
            usuario_info = self.model.get_usuario_logado()
            self.view.renderizar_dashboard(usuario_info)
            return True
        return False
    
    def logout(self):
        """Realiza logout"""
        self.model.logout()
    
    def verificar_autenticacao(self):
        """Verifica se usuário está autenticado"""
        return self.model.get_usuario_logado() is not None


# EXEMPLO 3: API REST com MVC
# ============================

class ModelContato:
    """Model - Gerencia contatos"""
    
    def __init__(self):
        self._contatos = {}
        self._next_id = 1
    
    def criar(self, nome, email, telefone):
        contato = {
            "id": self._next_id,
            "nome": nome,
            "email": email,
            "telefone": telefone
        }
        self._contatos[self._next_id] = contato
        self._next_id += 1
        return contato.copy()
    
    def listar(self):
        return [contato.copy() for contato in self._contatos.values()]
    
    def obter(self, contato_id):
        contato = self._contatos.get(contato_id)
        return contato.copy() if contato else None
    
    def atualizar(self, contato_id, **kwargs):
        if contato_id in self._contatos:
            self._contatos[contato_id].update(kwargs)
            return self._contatos[contato_id].copy()
        return None
    
    def deletar(self, contato_id):
        if contato_id in self._contatos:
            contato = self._contatos.pop(contato_id)
            return contato
        return None


class ViewJSON:
    """View - Renderiza JSON"""
    
    def renderizar(self, dados, status_code=200):
        import json
        response = {
            "status": status_code,
            "data": dados
        }
        return json.dumps(response, indent=2, ensure_ascii=False)
    
    def renderizar_erro(self, mensagem, status_code=400):
        import json
        response = {
            "status": status_code,
            "error": mensagem
        }
        return json.dumps(response, indent=2, ensure_ascii=False)


class ControllerAPI:
    """Controller - Gerencia endpoints da API"""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def criar_contato(self, nome, email, telefone):
        """POST /contatos"""
        if not nome or not email:
            return self.view.renderizar_erro("Nome e email são obrigatórios", 400)
        
        contato = self.model.criar(nome, email, telefone)
        return self.view.renderizar(contato, 201)
    
    def listar_contatos(self):
        """GET /contatos"""
        contatos = self.model.listar()
        return self.view.renderizar(contatos)
    
    def obter_contato(self, contato_id):
        """GET /contatos/{id}"""
        contato = self.model.obter(contato_id)
        if contato:
            return self.view.renderizar(contato)
        return self.view.renderizar_erro("Contato não encontrado", 404)
    
    def atualizar_contato(self, contato_id, **kwargs):
        """PUT /contatos/{id}"""
        contato = self.model.atualizar(contato_id, **kwargs)
        if contato:
            return self.view.renderizar(contato)
        return self.view.renderizar_erro("Contato não encontrado", 404)
    
    def deletar_contato(self, contato_id):
        """DELETE /contatos/{id}"""
        contato = self.model.deletar(contato_id)
        if contato:
            return self.view.renderizar({"message": "Contato deletado com sucesso"})
        return self.view.renderizar_erro("Contato não encontrado", 404)


# EXEMPLO 4: Aplicação de Gerenciamento de Contatos Completo
# ============================================================

def exemplo_blog():
    """Demonstra sistema de blog"""
    print("\n" + "=" * 60)
    print("EXEMPLO: SISTEMA DE BLOG")
    print("=" * 60)
    
    model = ModelPost()
    view = ViewPost(model)
    controller = ControllerPost(model, view)
    
    controller.criar_post(
        "Primeiro Post",
        "Este é o conteúdo do primeiro post do blog.",
        "Autor 1"
    )
    
    controller.criar_post(
        "Segundo Post",
        "Este é o conteúdo do segundo post.",
        "Autor 2"
    )
    
    controller.listar_posts()
    controller.visualizar_post(1)
    controller.buscar("segundo")


def exemplo_autenticacao():
    """Demonstra sistema de autenticação"""
    print("\n" + "=" * 60)
    print("EXEMPLO: SISTEMA DE AUTENTICAÇÃO")
    print("=" * 60)
    
    model = ModelUsuario()
    view = ViewAuth(model)
    controller = ControllerAuth(model, view)
    
    controller.login("admin", "admin123")
    print("\nOperações após login...")
    controller.logout()
    
    print("\nTentativa de login falha:")
    controller.login("admin", "senha_errada")


def exemplo_api():
    """Demonstra API REST"""
    print("\n" + "=" * 60)
    print("EXEMPLO: API REST")
    print("=" * 60)
    
    model = ModelContato()
    view = ViewJSON()
    controller = ControllerAPI(model, view)
    
    print("\n1. Criar contato:")
    print(controller.criar_contato("João Silva", "joao@email.com", "11999999999"))
    
    print("\n2. Criar outro contato:")
    print(controller.criar_contato("Maria Santos", "maria@email.com", "11888888888"))
    
    print("\n3. Listar contatos:")
    print(controller.listar_contatos())
    
    print("\n4. Obter contato específico:")
    print(controller.obter_contato(1))
    
    print("\n5. Atualizar contato:")
    print(controller.atualizar_contato(1, nome="João Silva Santos"))
    
    print("\n6. Deletar contato:")
    print(controller.deletar_contato(2))
    
    print("\n7. Listar contatos após deleção:")
    print(controller.listar_contatos())


if __name__ == "__main__":
    print("=" * 60)
    print("EXEMPLOS PRÁTICOS - MVC")
    print("=" * 60)
    
    exemplo_blog()
    exemplo_autenticacao()
    exemplo_api()

