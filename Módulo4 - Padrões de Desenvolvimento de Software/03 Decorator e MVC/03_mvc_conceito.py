"""
03 - PADRÃO MVC (MODEL-VIEW-CONTROLLER)
========================================

O que é MVC e sua Importância
------------------------------
MVC é um padrão arquitetural que separa uma aplicação em três componentes 
interconectados:

1. MODEL (Modelo): Gerencia dados e lógica de negócio
2. VIEW (Visão): Gerencia apresentação e interface com usuário
3. CONTROLLER (Controlador): Coordena entre Model e View

Importância:
- Separação de responsabilidades
- Facilita manutenção e testes
- Reutilização de componentes
- Escalabilidade
- Organização do código

Componentes e Responsabilidades
-------------------------------
MODEL (Modelo):
- Representa dados da aplicação
- Contém lógica de negócio
- Notifica View sobre mudanças (usando Observer)
- Independente de UI

VIEW (Visão):
- Apresenta dados ao usuário
- Observa Model para atualizações
- Não contém lógica de negócio
- Pode haver múltiplas views para um model

CONTROLLER (Controlador):
- Processa entrada do usuário
- Coordena Model e View
- Decide qual View mostrar
- Interpreta ações do usuário

Como Padrões Facilitam Organização
-----------------------------------
- Observer: Model notifica View (comunicação)
- Factory: Cria controllers e views
- Decorator: Adiciona funcionalidades às views
- Strategy: Diferentes estratégias de renderização
"""

# IMPLEMENTAÇÃO 1: MVC Básico
# ============================

class Model:
    """Model - Gerencia dados e lógica de negócio"""
    
    def __init__(self):
        self._dados = {}
        self._observers = []  # Views que observam
    
    def adicionar_observer(self, observer):
        """Adiciona um observer (View)"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remover_observer(self, observer):
        """Remove um observer"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notificar(self):
        """Notifica todos os observers sobre mudanças"""
        for observer in self._observers:
            observer.atualizar(self._dados)
    
    def set_dados(self, chave, valor):
        """Atualiza dados e notifica observers"""
        self._dados[chave] = valor
        self._notificar()
    
    def get_dados(self, chave=None):
        """Obtém dados"""
        if chave:
            return self._dados.get(chave)
        return self._dados.copy()


class View:
    """View - Apresenta dados ao usuário"""
    
    def __init__(self, model):
        self.model = model
        self.model.adicionar_observer(self)
    
    def atualizar(self, dados):
        """Chamado quando Model é atualizado"""
        print(f"[VIEW] Dados atualizados: {dados}")
    
    def renderizar(self):
        """Renderiza a view"""
        dados = self.model.get_dados()
        print(f"[VIEW] Renderizando com dados: {dados}")


class Controller:
    """Controller - Coordena Model e View"""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def processar_entrada(self, acao, **kwargs):
        """Processa entrada do usuário"""
        if acao == "atualizar":
            for chave, valor in kwargs.items():
                self.model.set_dados(chave, valor)
        elif acao == "visualizar":
            self.view.renderizar()
        else:
            print(f"Ação desconhecida: {acao}")


# IMPLEMENTAÇÃO 2: MVC com Múltiplas Views
# ==========================================

class ModelUsuario:
    """Model para usuário"""
    
    def __init__(self):
        self._nome = ""
        self._email = ""
        self._observers = []
    
    def adicionar_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self):
        for observer in self._observers:
            observer.atualizar(self)
    
    def set_nome(self, nome):
        self._nome = nome
        self._notificar()
    
    def set_email(self, email):
        self._email = email
        self._notificar()
    
    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email


class ViewPerfil(View):
    """View para exibir perfil do usuário"""
    
    def atualizar(self, model):
        print(f"[VIEW PERFIL] Nome: {model.get_nome()}, Email: {model.get_email()}")
    
    def renderizar(self):
        print("=" * 40)
        print("PERFIL DO USUÁRIO")
        print("=" * 40)
        print(f"Nome: {self.model.get_nome()}")
        print(f"Email: {self.model.get_email()}")
        print("=" * 40)


class ViewFormulario(View):
    """View para formulário de edição"""
    
    def atualizar(self, model):
        print(f"[VIEW FORMULÁRIO] Campos atualizados")


class ControllerUsuario:
    """Controller para gerenciar usuário"""
    
    def __init__(self, model):
        self.model = model
        self.views = {}
    
    def registrar_view(self, nome, view):
        """Registra uma view"""
        self.views[nome] = view
    
    def atualizar_nome(self, nome):
        """Atualiza nome do usuário"""
        self.model.set_nome(nome)
    
    def atualizar_email(self, email):
        """Atualiza email do usuário"""
        self.model.set_email(email)
    
    def mostrar_perfil(self):
        """Mostra view de perfil"""
        if "perfil" in self.views:
            self.views["perfil"].renderizar()
    
    def mostrar_formulario(self):
        """Mostra view de formulário"""
        if "formulario" in self.views:
            self.views["formulario"].renderizar()


# IMPLEMENTAÇÃO 3: MVC para Sistema de Tarefas
# ==============================================

class ModelTarefa:
    """Model para gerenciar tarefas"""
    
    def __init__(self):
        self._tarefas = []
        self._observers = []
    
    def adicionar_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self):
        for observer in self._observers:
            observer.atualizar(self._tarefas.copy())
    
    def adicionar_tarefa(self, descricao):
        tarefa = {
            "id": len(self._tarefas) + 1,
            "descricao": descricao,
            "concluida": False
        }
        self._tarefas.append(tarefa)
        self._notificar()
        return tarefa["id"]
    
    def concluir_tarefa(self, tarefa_id):
        for tarefa in self._tarefas:
            if tarefa["id"] == tarefa_id:
                tarefa["concluida"] = True
                self._notificar()
                return True
        return False
    
    def listar_tarefas(self):
        return self._tarefas.copy()


class ViewTarefas:
    """View para exibir lista de tarefas"""
    
    def __init__(self, model):
        self.model = model
        self.model.adicionar_observer(self)
    
    def atualizar(self, tarefas):
        print("\n[VIEW] Lista de tarefas atualizada:")
        self.renderizar()
    
    def renderizar(self):
        tarefas = self.model.listar_tarefas()
        if not tarefas:
            print("Nenhuma tarefa.")
        else:
            for tarefa in tarefas:
                status = "✓" if tarefa["concluida"] else "○"
                print(f"  {status} [{tarefa['id']}] {tarefa['descricao']}")


class ControllerTarefas:
    """Controller para gerenciar tarefas"""
    
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def criar_tarefa(self, descricao):
        """Cria nova tarefa"""
        if not descricao:
            print("Erro: Descrição não pode estar vazia")
            return
        tarefa_id = self.model.adicionar_tarefa(descricao)
        print(f"Tarefa #{tarefa_id} criada com sucesso!")
        return tarefa_id
    
    def marcar_concluida(self, tarefa_id):
        """Marca tarefa como concluída"""
        if self.model.concluir_tarefa(tarefa_id):
            print(f"Tarefa #{tarefa_id} marcada como concluída!")
        else:
            print(f"Tarefa #{tarefa_id} não encontrada")
    
    def listar(self):
        """Lista todas as tarefas"""
        self.view.renderizar()


# IMPLEMENTAÇÃO 4: MVC Simplificado para API
# ============================================

class ModelProduto:
    """Model para produtos (simulado)"""
    
    def __init__(self):
        self.produtos = {
            1: {"id": 1, "nome": "Produto A", "preco": 100.00},
            2: {"id": 2, "nome": "Produto B", "preco": 200.00}
        }
    
    def listar(self):
        return list(self.produtos.values())
    
    def obter(self, produto_id):
        return self.produtos.get(produto_id)
    
    def criar(self, nome, preco):
        novo_id = max(self.produtos.keys()) + 1 if self.produtos else 1
        produto = {"id": novo_id, "nome": nome, "preco": preco}
        self.produtos[novo_id] = produto
        return produto


class ViewJSON:
    """View que renderiza JSON"""
    
    def renderizar(self, dados):
        import json
        return json.dumps(dados, indent=2, ensure_ascii=False)


class ViewHTML:
    """View que renderiza HTML"""
    
    def renderizar(self, dados):
        html = "<ul>\n"
        if isinstance(dados, list):
            for item in dados:
                html += f"  <li>{item}</li>\n"
        else:
            html += f"  <li>{dados}</li>\n"
        html += "</ul>"
        return html


class ControllerAPI:
    """Controller que coordena requisições"""
    
    def __init__(self, model):
        self.model = model
        self.view_json = ViewJSON()
        self.view_html = ViewHTML()
    
    def listar_produtos(self, formato="json"):
        """Lista produtos no formato especificado"""
        produtos = self.model.listar()
        
        if formato == "json":
            return self.view_json.renderizar(produtos)
        elif formato == "html":
            return self.view_html.renderizar([f"{p['nome']} - R${p['preco']:.2f}" for p in produtos])
        else:
            return str(produtos)
    
    def obter_produto(self, produto_id, formato="json"):
        """Obtém produto específico"""
        produto = self.model.obter(produto_id)
        if not produto:
            return None
        
        if formato == "json":
            return self.view_json.renderizar(produto)
        elif formato == "html":
            return self.view_html.renderizar([f"{produto['nome']} - R${produto['preco']:.2f}"])
        else:
            return str(produto)


if __name__ == "__main__":
    print("=" * 60)
    print("PADRÃO MVC (MODEL-VIEW-CONTROLLER)")
    print("=" * 60)
    
    # TESTE 1: MVC Básico
    print("\n1. MVC Básico:")
    model = Model()
    view = View(model)
    controller = Controller(model, view)
    
    controller.processar_entrada("atualizar", nome="João", idade=30)
    controller.processar_entrada("visualizar")
    
    # TESTE 2: MVC com Múltiplas Views
    print("\n2. MVC com Múltiplas Views:")
    model_usuario = ModelUsuario()
    view_perfil = ViewPerfil(model_usuario)
    view_formulario = ViewFormulario(model_usuario)
    
    controller_usuario = ControllerUsuario(model_usuario)
    controller_usuario.registrar_view("perfil", view_perfil)
    controller_usuario.registrar_view("formulario", view_formulario)
    
    controller_usuario.atualizar_nome("Maria Silva")
    controller_usuario.atualizar_email("maria@email.com")
    controller_usuario.mostrar_perfil()
    
    # TESTE 3: MVC para Sistema de Tarefas
    print("\n3. MVC para Sistema de Tarefas:")
    model_tarefa = ModelTarefa()
    view_tarefa = ViewTarefas(model_tarefa)
    controller_tarefa = ControllerTarefas(model_tarefa, view_tarefa)
    
    controller_tarefa.criar_tarefa("Comprar leite")
    controller_tarefa.criar_tarefa("Estudar Python")
    controller_tarefa.marcar_concluida(1)
    controller_tarefa.criar_tarefa("Ler documentação")
    
    # TESTE 4: MVC para API
    print("\n4. MVC Simplificado para API:")
    model_produto = ModelProduto()
    controller_api = ControllerAPI(model_produto)
    
    print("JSON:")
    print(controller_api.listar_produtos("json"))
    print("\nHTML:")
    print(controller_api.listar_produtos("html"))

