"""
Exemplo Completo: Sistema de Biblioteca

Este exemplo integra todos os conceitos fundamentais:
- Definição de classe
- Construtor (__init__)
- Atributos
- Métodos
- Instanciação de objetos
"""

# ==========================================
# SISTEMA DE BIBLIOTECA
# ==========================================

class Livro:
    """
    Representa um livro na biblioteca.
    
    Esta classe demonstra todos os conceitos fundamentais de POO.
    """
    
    def __init__(self, titulo, autor, isbn, ano_publicacao):
        """
        Construtor: inicializa um livro.
        
        Args:
            titulo: Título do livro
            autor: Autor do livro
            isbn: Código ISBN único
            ano_publicacao: Ano de publicação
        """
        # ATRIBUTOS: características do livro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.ano_publicacao = ano_publicacao
        
        # Atributos de estado
        self.emprestado = False
        self.leitor_atual = None
    
    # MÉTODOS: comportamentos do livro
    def emprestar(self, nome_leitor):
        """
        Empresta o livro para um leitor.
        
        Args:
            nome_leitor: Nome de quem está pegando o livro
        
        Returns:
            True se emprestou com sucesso, False caso contrário
        """
        if not self.emprestado:
            self.emprestado = True
            self.leitor_atual = nome_leitor
            print(f"✓ '{self.titulo}' foi emprestado para {nome_leitor}")
            return True
        else:
            print(f"✗ '{self.titulo}' já está emprestado para {self.leitor_atual}")
            return False
    
    def devolver(self):
        """Devolve o livro à biblioteca."""
        if self.emprestado:
            leitor = self.leitor_atual
            self.emprestado = False
            self.leitor_atual = None
            print(f"✓ '{self.titulo}' foi devolvido por {leitor}")
            return True
        else:
            print(f"✗ '{self.titulo}' não estava emprestado")
            return False
    
    def esta_disponivel(self):
        """Verifica se o livro está disponível."""
        return not self.emprestado
    
    def exibir_info(self):
        """Exibe todas as informações do livro."""
        status = "Emprestado" if self.emprestado else "Disponível"
        leitor_info = f" (para {self.leitor_atual})" if self.emprestado else ""
        
        print(f"""
        {'=' * 50}
        Livro: {self.titulo}
        Autor: {self.autor}
        ISBN: {self.isbn}
        Ano: {self.ano_publicacao}
        Status: {status}{leitor_info}
        {'=' * 50}
        """)


class Biblioteca:
    """
    Representa uma biblioteca com uma coleção de livros.
    
    Demonstra uso de objetos como atributos de outros objetos.
    """
    
    def __init__(self, nome):
        """
        Inicializa uma biblioteca.
        
        Args:
            nome: Nome da biblioteca
        """
        self.nome = nome
        self.livros = []  # Lista para armazenar objetos Livro
    
    def adicionar_livro(self, livro):
        """
        Adiciona um livro à biblioteca.
        
        Args:
            livro: Objeto Livro
        """
        self.livros.append(livro)
        print(f"✓ Livro '{livro.titulo}' adicionado à biblioteca")
    
    def buscar_livro(self, titulo):
        """
        Busca um livro pelo título.
        
        Args:
            titulo: Título do livro a buscar
        
        Returns:
            Objeto Livro se encontrado, None caso contrário
        """
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
    
    def listar_livros_disponiveis(self):
        """Lista todos os livros disponíveis."""
        disponiveis = [livro for livro in self.livros if livro.esta_disponivel()]
        
        if disponiveis:
            print(f"\n📚 Livros disponíveis na {self.nome}:")
            for livro in disponiveis:
                print(f"  • {livro.titulo} - {livro.autor}")
        else:
            print(f"\nNenhum livro disponível na {self.nome}")
        
        return disponiveis
    
    def listar_todos_livros(self):
        """Lista todos os livros da biblioteca."""
        print(f"\n📚 Todos os livros na {self.nome}:")
        for livro in self.livros:
            status = "✓ Disponível" if livro.esta_disponivel() else f"✗ Emprestado ({livro.leitor_atual})"
            print(f"  • {livro.titulo} - {livro.autor} [{status}]")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    """Demonstra o uso das classes."""
    
    print("=" * 60)
    print("SISTEMA DE BIBLIOTECA - EXEMPLO COMPLETO")
    print("=" * 60)
    
    # ==========================================
    # 1. INSTANCIAÇÃO DE OBJETOS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("1. CRIANDO OBJETOS (INSTANCIAÇÃO)")
    print("=" * 60)
    
    # Criando a biblioteca
    biblioteca = Biblioteca("Biblioteca Central")
    
    # Criando vários livros (instâncias)
    livro1 = Livro("1984", "George Orwell", "978-0451524935", 1949)
    livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-0544003415", 1954)
    livro3 = Livro("Dom Casmurro", "Machado de Assis", "978-8535902779", 1899)
    livro4 = Livro("A Revolução dos Bichos", "George Orwell", "978-0452284241", 1945)
    
    print(f"\n✓ Criados {4} objetos Livro")
    
    # ==========================================
    # 2. ADICIONANDO LIVROS À BIBLIOTECA
    # ==========================================
    
    print("\n" + "=" * 60)
    print("2. ADICIONANDO LIVROS")
    print("=" * 60)
    
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)
    biblioteca.adicionar_livro(livro4)
    
    # ==========================================
    # 3. EXIBINDO INFORMAÇÕES
    # ==========================================
    
    print("\n" + "=" * 60)
    print("3. EXIBINDO INFORMAÇÕES DOS OBJETOS")
    print("=" * 60)
    
    livro1.exibir_info()
    livro2.exibir_info()
    
    # ==========================================
    # 4. USANDO MÉTODOS DOS OBJETOS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("4. EMPRESTANDO LIVROS (USANDO MÉTODOS)")
    print("=" * 60)
    
    livro1.emprestar("Maria Silva")
    livro2.emprestar("João Santos")
    livro3.emprestar("Ana Costa")
    
    print("\nTentando emprestar livro já emprestado:")
    livro1.emprestar("Pedro Alves")  # Não vai funcionar
    
    # ==========================================
    # 5. VERIFICANDO STATUS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("5. VERIFICANDO DISPONIBILIDADE")
    print("=" * 60)
    
    print(f"\n'{livro1.titulo}' disponível? {livro1.esta_disponivel()}")
    print(f"'{livro4.titulo}' disponível? {livro4.esta_disponivel()}")
    
    biblioteca.listar_livros_disponiveis()
    
    # ==========================================
    # 6. DEVOLVENDO LIVROS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("6. DEVOLVENDO LIVROS")
    print("=" * 60)
    
    livro1.devolver()
    livro2.devolver()
    
    # ==========================================
    # 7. BUSCANDO LIVROS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("7. BUSCANDO LIVROS")
    print("=" * 60)
    
    livro_encontrado = biblioteca.buscar_livro("dom casmurro")
    if livro_encontrado:
        livro_encontrado.exibir_info()
    
    # ==========================================
    # 8. ESTADO FINAL
    # ==========================================
    
    print("\n" + "=" * 60)
    print("8. ESTADO FINAL DA BIBLIOTECA")
    print("=" * 60)
    
    biblioteca.listar_todos_livros()
    
    # ==========================================
    # RESUMO DOS CONCEITOS APLICADOS
    # ==========================================
    
    print("\n" + "=" * 60)
    print("CONCEITOS APLICADOS NESTE EXEMPLO")
    print("=" * 60)
    
    print("""
    ✓ DEFINIÇÃO DE CLASSES: Criamos classes Livro e Biblioteca
    ✓ CONSTRUTOR (__init__): Inicializamos atributos dos objetos
    ✓ ATRIBUTOS: Cada objeto tem seus próprios dados (título, autor, etc.)
    ✓ MÉTODOS: Comportamentos definidos nas classes (emprestar, devolver, etc.)
    ✓ INSTANCIAÇÃO: Criamos múltiplos objetos da classe Livro
    ✓ INDEPENDÊNCIA: Cada objeto mantém seu próprio estado
    ✓ INTERAÇÃO: Objetos interagem entre si (biblioteca contém livros)
    """)


if __name__ == "__main__":
    main()

