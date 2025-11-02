"""
05 - EXERCÍCIOS: DECORATOR E MVC
=================================

Exercícios práticos para implementar os padrões Decorator e MVC.
"""

from abc import ABC, abstractmethod

# ===========================================
# EXERCÍCIOS DECORATOR
# ===========================================

# EXERCÍCIO 1: Decorator para Funcionalidades de Carro
# =======================================================
"""
Crie um sistema de carros com decorators para adicionar funcionalidades.

Requisitos:
- Classe Carro básica com método dirigir()
- Decorators: CarroComArCondicionado, CarroComGPS, CarroComRadio
- Cada decorator adiciona funcionalidade específica
- Teste combinando múltiplos decorators

Implemente:
- Classe base Carro
- Interface CarroDecorator
- Implementações dos decorators
- Teste com diferentes combinações
"""

# TODO: Implemente aqui
class Carro(ABC):
    """Interface para carro"""
    pass

class CarroDecorator(ABC):
    """Base para decorators de carro"""
    pass


# EXERCÍCIO 2: Decorator para Processamento de Imagens
# ======================================================
"""
Crie um sistema de processamento de imagens com decorators.

Requisitos:
- Classe Imagem básica com método processar()
- Decorators: 
  * FiltroPretoBranco
  * Redimensionar (com largura, altura)
  * AplicarBorda (com cor e espessura)
  * AdicionarMarcaDAgua (com texto)
- Combine decorators para criar diferentes efeitos

Teste processando imagens com diferentes combinações de decorators.
"""

# TODO: Implemente aqui
class Imagem(ABC):
    """Interface para imagem"""
    pass

class ImagemDecorator(ABC):
    """Base para decorators de imagem"""
    pass


# EXERCÍCIO 3: Decorator Funcional para Validação
# ================================================
"""
Crie decorators funcionais para validação de dados.

Requisitos:
- Decorator @validar_email que valida formato de email
- Decorator @validar_numero_positivo que valida números positivos
- Decorator @validar_string_nao_vazia que valida strings
- Decorator @log_execucao que registra execução de função
- Combine decorators em uma função

Exemplo de uso:
@validar_email
@log_execucao
def enviar_email(email, mensagem):
    return f"Email enviado para {email}"
"""

# TODO: Implemente aqui
def validar_email(func):
    """Decorator para validar email"""
    pass

def validar_numero_positivo(func):
    """Decorator para validar número positivo"""
    pass


# ===========================================
# EXERCÍCIOS MVC
# ===========================================

# EXERCÍCIO 4: MVC para Sistema de Biblioteca
# =============================================
"""
Crie um sistema MVC para gerenciar livros de uma biblioteca.

Requisitos:
- Model Livro: gerencia livros (criar, listar, buscar, emprestar, devolver)
- View Livro: renderiza informações de livros de diferentes formas
- Controller Livro: coordena operações de biblioteca

Operações:
- Adicionar livro (título, autor, ISBN)
- Listar livros
- Buscar livro por título ou autor
- Emprestar livro (marca como emprestado)
- Devolver livro (marca como disponível)

Crie múltiplas views:
- ViewLista: lista todos os livros
- ViewDetalhes: mostra detalhes de um livro
- ViewDisponiveis: mostra apenas livros disponíveis
"""

# TODO: Implemente aqui
class ModelLivro:
    """Model para livros"""
    pass

class ViewLivro(ABC):
    """View abstrata para livros"""
    pass

class ControllerLivro:
    """Controller para livros"""
    pass


# EXERCÍCIO 5: MVC para Sistema de Agenda
# =========================================
"""
Crie um sistema MVC para gerenciar eventos de uma agenda.

Requisitos:
- Model Evento: gerencia eventos (criar, listar, atualizar, deletar, buscar por data)
- View Evento: renderiza eventos (lista, calendário, detalhes)
- Controller Evento: coordena operações da agenda

Propriedades de Evento:
- título, descrição, data, hora, local

Views:
- ViewLista: lista eventos
- ViewCalendario: mostra eventos por data
- ViewDetalhes: mostra detalhes completos de um evento
"""

# TODO: Implemente aqui
class ModelEvento:
    """Model para eventos"""
    pass

class ViewEvento(ABC):
    """View abstrata para eventos"""
    pass

class ControllerEvento:
    """Controller para eventos"""
    pass


# EXERCÍCIO 6: MVC para API de Produtos
# =======================================
"""
Crie um sistema MVC para API de produtos (e-commerce).

Requisitos:
- Model Produto: gerencia produtos (CRUD completo)
- View JSON/XML: renderiza produtos em diferentes formatos
- Controller API: coordena endpoints REST

Endpoints:
- GET /produtos - lista todos
- GET /produtos/{id} - obtém produto específico
- POST /produtos - cria produto
- PUT /produtos/{id} - atualiza produto
- DELETE /produtos/{id} - deleta produto

Propriedades de Produto:
- id, nome, descrição, preço, estoque, categoria
"""

# TODO: Implemente aqui
class ModelProduto:
    """Model para produtos"""
    pass

class ViewAPI(ABC):
    """View abstrata para API"""
    pass

class ControllerProdutoAPI:
    """Controller para API de produtos"""
    pass


# EXERCÍCIO 7: Identificar e Aplicar MVC
# =======================================
"""
Analise os seguintes cenários e identifique como aplicar MVC:

a) Sistema de comentários em um blog
b) Dashboard de métricas em tempo real
c) Sistema de notificações push
d) Editor de texto online colaborativo
e) Sistema de gestão de pedidos online

Para cada caso:
- Identifique Model, View e Controller
- Descreva responsabilidades de cada componente
- Explique como se comunicam
"""

def analisar_cenarios_mvc():
    """Complete as respostas abaixo"""
    cenarios = {
        "a) Comentários em blog": {
            "model": "",
            "view": "",
            "controller": "",
            "comunicacao": ""
        },
        "b) Dashboard de métricas": {
            "model": "",
            "view": "",
            "controller": "",
            "comunicacao": ""
        },
        "c) Notificações push": {
            "model": "",
            "view": "",
            "controller": "",
            "comunicacao": ""
        },
        "d) Editor de texto colaborativo": {
            "model": "",
            "view": "",
            "controller": "",
            "comunicacao": ""
        },
        "e) Gestão de pedidos": {
            "model": "",
            "view": "",
            "controller": "",
            "comunicacao": ""
        }
    }
    return cenarios


# ===========================================
# SOLUÇÕES DOS EXERCÍCIOS
# ===========================================

class SolucaoExercicio1:
    """Solução do Exercício 1 - Carros com Decorators"""
    
    class Carro(ABC):
        @abstractmethod
        def dirigir(self):
            pass
    
    class CarroBasico(Carro):
        def __init__(self, modelo):
            self.modelo = modelo
        
        def dirigir(self):
            return f"{self.modelo} está dirigindo"
    
    class CarroDecorator(Carro):
        def __init__(self, carro: Carro):
            self._carro = carro
        
        def dirigir(self):
            return self._carro.dirigir()
    
    class CarroComArCondicionado(CarroDecorator):
        def dirigir(self):
            return f"{self._carro.dirigir()} com ar condicionado ligado"
    
    class CarroComGPS(CarroDecorator):
        def dirigir(self):
            return f"{self._carro.dirigir()} com GPS navegando"
    
    class CarroComRadio(CarroDecorator):
        def __init__(self, carro: Carro, estacao="FM 89.5"):
            super().__init__(carro)
            self.estacao = estacao
        
        def dirigir(self):
            return f"{self._carro.dirigir()} ouvindo rádio {self.estacao}"


class SolucaoExercicio4:
    """Solução do Exercício 4 - MVC Biblioteca"""
    
    class ModelLivro:
        def __init__(self):
            self._livros = {}
            self._next_id = 1
            self._observers = []
        
        def adicionar_observer(self, observer):
            if observer not in self._observers:
                self._observers.append(observer)
        
        def _notificar(self, evento, dados):
            for observer in self._observers:
                observer.atualizar(evento, dados)
        
        def adicionar(self, titulo, autor, isbn):
            livro = {
                "id": self._next_id,
                "titulo": titulo,
                "autor": autor,
                "isbn": isbn,
                "disponivel": True
            }
            self._livros[self._next_id] = livro
            self._next_id += 1
            self._notificar("livro_adicionado", livro)
            return livro["id"]
        
        def listar(self):
            return [livro.copy() for livro in self._livros.values()]
        
        def buscar(self, termo):
            termo_lower = termo.lower()
            return [
                livro.copy() for livro in self._livros.values()
                if termo_lower in livro["titulo"].lower() or 
                   termo_lower in livro["autor"].lower()
            ]
        
        def emprestar(self, livro_id):
            if livro_id in self._livros:
                if self._livros[livro_id]["disponivel"]:
                    self._livros[livro_id]["disponivel"] = False
                    self._notificar("livro_emprestado", self._livros[livro_id])
                    return True
            return False
        
        def devolver(self, livro_id):
            if livro_id in self._livros:
                if not self._livros[livro_id]["disponivel"]:
                    self._livros[livro_id]["disponivel"] = True
                    self._notificar("livro_devolvido", self._livros[livro_id])
                    return True
            return False
    
    class ViewLivro(ABC):
        def atualizar(self, evento, dados):
            pass
        
        @abstractmethod
        def renderizar(self, dados):
            pass
    
    class ViewLista(ViewLivro):
        def renderizar(self, livros):
            print("\n" + "=" * 50)
            print("LISTA DE LIVROS")
            print("=" * 50)
            for livro in livros:
                status = "Disponível" if livro["disponivel"] else "Emprestado"
                print(f"[{livro['id']}] {livro['titulo']} - {livro['autor']} ({status})")
            print("=" * 50)
    
    class ViewDetalhes(ViewLivro):
        def renderizar(self, livro):
            print("\n" + "=" * 50)
            print("DETALHES DO LIVRO")
            print("=" * 50)
            print(f"ID: {livro['id']}")
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"ISBN: {livro['isbn']}")
            print(f"Status: {'Disponível' if livro['disponivel'] else 'Emprestado'}")
            print("=" * 50)
    
    class ViewDisponiveis(ViewLivro):
        def renderizar(self, livros):
            disponiveis = [l for l in livros if l["disponivel"]]
            print("\n" + "=" * 50)
            print("LIVROS DISPONÍVEIS")
            print("=" * 50)
            if disponiveis:
                for livro in disponiveis:
                    print(f"[{livro['id']}] {livro['titulo']} - {livro['autor']}")
            else:
                print("Nenhum livro disponível")
            print("=" * 50)
    
    class ControllerLivro:
        def __init__(self, model):
            self.model = model
            self.views = {}
        
        def registrar_view(self, nome, view):
            self.model.adicionar_observer(view)
            self.views[nome] = view
        
        def adicionar_livro(self, titulo, autor, isbn):
            return self.model.adicionar(titulo, autor, isbn)
        
        def listar_livros(self):
            livros = self.model.listar()
            if "lista" in self.views:
                self.views["lista"].renderizar(livros)
            return livros
        
        def buscar_livro(self, termo):
            resultados = self.model.buscar(termo)
            if "lista" in self.views:
                self.views["lista"].renderizar(resultados)
            return resultados
        
        def emprestar_livro(self, livro_id):
            return self.model.emprestar(livro_id)
        
        def devolver_livro(self, livro_id):
            return self.model.devolver(livro_id)


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCÍCIOS - DECORATOR E MVC")
    print("=" * 60)
    print("\nComplete os exercícios acima e teste suas implementações!")
    print("\nPara ver as soluções, consulte as classes SolucaoExercicio*")

