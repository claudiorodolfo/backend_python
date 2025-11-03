"""
Exemplo Completo: Sistema de Biblioteca

Este exemplo integra todos os conceitos:
- Composição (Biblioteca TEM Livros)
- Associação (Pessoa USA Biblioteca)
- Exceções customizadas
- Tratamento de exceções em classes
- Validação com exceções
"""

# ==========================================
# EXCEÇÕES CUSTOMIZADAS
# ==========================================

class LivroNaoEncontradoError(Exception):
    """Exceção para livro não encontrado."""
    pass


class LivroJaEmprestadoError(Exception):
    """Exceção para livro já emprestado."""
    pass


class LivroNaoEmprestadoError(Exception):
    """Exceção para livro não emprestado."""
    pass


class PessoaNaoEncontradaError(Exception):
    """Exceção para pessoa não encontrada."""
    pass


# ==========================================
# COMPOSIÇÃO: Biblioteca TEM Livros
# ==========================================

class Livro:
    """
    Componente - Livro é parte essencial da biblioteca.
    
    Composição: Livro é criado dentro de Biblioteca.
    """
    
    def __init__(self, titulo, autor, isbn):
        """
        Cria um livro.
        
        Raises:
            ValueError: Se dados forem inválidos
        """
        # Validação
        if not titulo or len(titulo.strip()) == 0:
            raise ValueError("Título não pode ser vazio")
        
        if not autor or len(autor.strip()) == 0:
            raise ValueError("Autor não pode ser vazio")
        
        if not isbn or len(isbn.strip()) == 0:
            raise ValueError("ISBN não pode ser vazio")
        
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.isbn = isbn.strip()
        self.emprestado = False
        self.leitorAtual = None
    
    def __str__(self):
        return f"{self.titulo} - {self.autor}"
    
    def emprestarPara(self, pessoa):
        """
        Empresta livro para uma pessoa.
        
        Raises:
            LivroJaEmprestadoError: Se livro já estiver emprestado
        """
        if self.emprestado:
            raise LivroJaEmprestadoError(
                f"'{self.titulo}' já está emprestado para {self.leitorAtual.nome}"
            )
        
        self.emprestado = True
        self.leitorAtual = pessoa
    
    def devolver(self):
        """
        Devolve livro à biblioteca.
        
        Raises:
            LivroNaoEmprestadoError: Se livro não estiver emprestado
        """
        if not self.emprestado:
            raise LivroNaoEmprestadoError(f"'{self.titulo}' não está emprestado")
        
        leitor = self.leitorAtual.nome
        self.emprestado = False
        self.leitorAtual = None
        return leitor
    
    def exibirInfo(self):
        """Exibe informações do livro."""
        status = "Emprestado" if self.emprestado else "Disponível"
        leitor = f" ({self.leitorAtual.nome})" if self.emprestado else ""
        
        print(f"""
        {'=' * 50}
        Título: {self.titulo}
        Autor: {self.autor}
        ISBN: {self.isbn}
        Status: {status}{leitor}
        {'=' * 50}
        """)


# ==========================================
# ASSOCIAÇÃO: Pessoa USA Biblioteca
# ==========================================

class Pessoa:
    """
    Classe independente - Pessoa pode existir sem biblioteca.
    
    Associação: Pessoa usa Biblioteca, mas não possui.
    """
    
    def __init__(self, nome, cpf):
        """
        Cria uma pessoa.
        
        Raises:
            ValueError: Se nome estiver vazio
            ValueError: Se CPF for inválido
        """
        # Validação
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        
        if not cpf or len(''.join(filter(str.isdigit, str(cpf)))) != 11:
            raise ValueError("CPF deve ter 11 dígitos")
        
        self.nome = nome.strip()
        self.cpf = cpf
        self.livrosEmprestados = []  # Associação: pessoa tem lista de livros
    
    def __str__(self):
        return self.nome
    
    def adicionarLivro(self, livro):
        """Adiciona livro à lista de empréstimos."""
        if livro not in self.livrosEmprestados:
            self.livrosEmprestados.append(livro)
    
    def removerLivro(self, livro):
        """Remove livro da lista de empréstimos."""
        if livro in self.livrosEmprestados:
            self.livrosEmprestados.remove(livro)
    
    def exibirInfo(self):
        """Exibe informações da pessoa."""
        print(f"""
        {'=' * 50}
        Nome: {self.nome}
        CPF: {self.cpf}
        Livros Emprestados: {len(self.livrosEmprestados)}
        {'=' * 50}
        """)


# ==========================================
# COMPOSIÇÃO + ASSOCIAÇÃO: Biblioteca
# ==========================================

class Biblioteca:
    """
    Biblioteca integra composição e associação.
    
    Composição: TEM lista de Livros (componentes)
    Associação: USA lista de Pessoas (visitantes)
    """
    
    def __init__(self, nome):
        """
        Cria uma biblioteca.
        
        Raises:
            ValueError: Se nome estiver vazio
        """
        if not nome or len(nome.strip()) == 0:
            raise ValueError("Nome da biblioteca não pode ser vazio")
        
        self.nome = nome.strip()
        
        # COMPOSIÇÃO: Lista de livros (componentes)
        self.livros = {}
        
        # ASSOCIAÇÃO: Lista de pessoas (visitantes)
        self.visitantes = {}
    
    def adicionarLivro(self, titulo, autor, isbn):
        """
        Adiciona livro à biblioteca (composição).
        
        Raises:
            ValueError: Se livro já existir
        """
        try:
            if isbn in self.livros:
                raise ValueError(f"Livro com ISBN {isbn} já existe")
            
            # COMPOSIÇÃO: Cria livro dentro da biblioteca
            livro = Livro(titulo, autor, isbn)
            self.livros[isbn] = livro
            
            print(f"✓ Livro '{titulo}' adicionado à biblioteca")
            return livro
            
        except (ValueError, Exception) as e:
            print(f"✗ Erro ao adicionar livro: {e}")
            raise
    
    def registrarVisitante(self, pessoa):
        """
        Registra visitante na biblioteca (associação).
        
        Raises:
            ValueError: Se pessoa já estiver registrada
        """
        try:
            if pessoa.cpf in self.visitantes:
                raise ValueError(f"Pessoa {pessoa.nome} já está registrada")
            
            # ASSOCIAÇÃO: Referencia pessoa (não cria)
            self.visitantes[pessoa.cpf] = pessoa
            
            print(f"✓ {pessoa.nome} registrado(a) como visitante")
            
        except (ValueError, Exception) as e:
            print(f"✗ Erro ao registrar visitante: {e}")
            raise
    
    def buscarLivro(self, isbn):
        """
        Busca livro por ISBN.
        
        Raises:
            LivroNaoEncontradoError: Se livro não for encontrado
        """
        if isbn not in self.livros:
            raise LivroNaoEncontradoError(f"Livro com ISBN {isbn} não encontrado")
        
        return self.livros[isbn]
    
    def buscarPessoa(self, cpf):
        """
        Busca pessoa por CPF.
        
        Raises:
            PessoaNaoEncontradaError: Se pessoa não for encontrada
        """
        if cpf not in self.visitantes:
            raise PessoaNaoEncontradaError(f"Pessoa com CPF {cpf} não encontrada")
        
        return self.visitantes[cpf]
    
    def emprestarLivro(self, isbn, cpf):
        """
        Empresta livro para pessoa.
        
        Integra composição (livro) e associação (pessoa).
        
        Raises:
            LivroNaoEncontradoError: Se livro não existir
            PessoaNaoEncontradaError: Se pessoa não estiver registrada
            LivroJaEmprestadoError: Se livro já estiver emprestado
        """
        try:
            # Busca livro (composição)
            livro = self.buscarLivro(isbn)
            
            # Busca pessoa (associação)
            pessoa = self.buscarPessoa(cpf)
            
            # Empresta
            livro.emprestarPara(pessoa)
            pessoa.adicionarLivro(livro)
            
            print(f"✓ '{livro.titulo}' emprestado para {pessoa.nome}")
            
        except (LivroNaoEncontradoError, PessoaNaoEncontradaError, LivroJaEmprestadoError) as e:
            print(f"✗ Erro ao emprestar: {e}")
            raise
    
    def devolverLivro(self, isbn):
        """
        Devolve livro à biblioteca.
        
        Raises:
            LivroNaoEncontradoError: Se livro não existir
            LivroNaoEmprestadoError: Se livro não estiver emprestado
        """
        try:
            livro = self.buscarLivro(isbn)
            leitor = livro.devolver()
            pessoa = self.buscarPessoaByLivro(livro)
            
            if pessoa:
                pessoa.removerLivro(livro)
            
            print(f"✓ '{livro.titulo}' devolvido por {leitor}")
            
        except (LivroNaoEncontradoError, LivroNaoEmprestadoError) as e:
            print(f"✗ Erro ao devolver: {e}")
            raise
    
    def buscarPessoaByLivro(self, livro):
        """Busca pessoa que tem o livro emprestado."""
        for pessoa in self.visitantes.values():
            if livro in pessoa.livrosEmprestados:
                return pessoa
        return None
    
    def listarLivrosDisponiveis(self):
        """Lista livros disponíveis."""
        disponiveis = [livro for livro in self.livros.values() if not livro.emprestado]
        
        print(f"\n📚 Livros disponíveis na {self.nome}:")
        if disponiveis:
            for livro in disponiveis:
                print(f"  • {livro}")
        else:
            print("  Nenhum livro disponível")
    
    def exibirRelatorio(self):
        """Exibe relatório completo da biblioteca."""
        print(f"""
        {'=' * 60}
        RELATÓRIO DA {self.nome.upper()}
        {'=' * 60}
        Total de Livros: {len(self.livros)}
        Livros Emprestados: {sum(1 for l in self.livros.values() if l.emprestado)}
        Livros Disponíveis: {sum(1 for l in self.livros.values() if not l.emprestado)}
        Visitantes Registrados: {len(self.visitantes)}
        {'=' * 60}
        """)


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

def main():
    """Demonstra o sistema completo."""
    
    print("=" * 60)
    print("SISTEMA DE BIBLIOTECA - EXEMPLO COMPLETO")
    print("=" * 60)
    
    # Criando biblioteca
    print("\nCriando biblioteca:")
    biblioteca = Biblioteca("Biblioteca Central")
    
    # Adicionando livros (COMPOSIÇÃO)
    print("\nAdicionando livros (COMPOSIÇÃO):")
    try:
        biblioteca.adicionarLivro("1984", "George Orwell", "978-0451524935")
        biblioteca.adicionarLivro("Dom Casmurro", "Machado de Assis", "978-8535902779")
        biblioteca.adicionarLivro("O Senhor dos Anéis", "J.R.R. Tolkien", "978-0544003415")
    except ValueError as e:
        print(f"Erro: {e}")
    
    # Registrando pessoas (ASSOCIAÇÃO)
    print("\nRegistrando pessoas (ASSOCIAÇÃO):")
    try:
        pessoa1 = Pessoa("Maria Silva", "12345678901")
        pessoa2 = Pessoa("João Santos", "98765432100")
        
        biblioteca.registrarVisitante(pessoa1)
        biblioteca.registrarVisitante(pessoa2)
    except ValueError as e:
        print(f"Erro: {e}")
    
    # Emprestando livros
    print("\nEmprestando livros:")
    try:
        biblioteca.emprestarLivro("978-0451524935", "12345678901")
        biblioteca.emprestarLivro("978-8535902779", "98765432100")
    except (LivroNaoEncontradoError, PessoaNaoEncontradaError, LivroJaEmprestadoError) as e:
        print(f"Erro: {e}")
    
    # Tentando emprestar livro já emprestado
    print("\nTentando emprestar livro já emprestado:")
    try:
        biblioteca.emprestarLivro("978-0451524935", "98765432100")
    except LivroJaEmprestadoError as e:
        print(f"Erro esperado: {e}")
    
    # Listando livros disponíveis
    biblioteca.listarLivrosDisponiveis()
    
    # Devolvendo livros
    print("\nDevolvendo livros:")
    try:
        biblioteca.devolverLivro("978-0451524935")
    except (LivroNaoEncontradoError, LivroNaoEmprestadoError) as e:
        print(f"Erro: {e}")
    
    # Relatório final
    biblioteca.exibirRelatorio()
    
    # Exibindo informações de objetos
    print("\nInformações dos objetos:")
    livro = biblioteca.buscarLivro("978-8535902779")
    livro.exibirInfo()
    
    pessoa = biblioteca.buscarPessoa("12345678901")
    pessoa.exibirInfo()


if __name__ == "__main__":
    main()

