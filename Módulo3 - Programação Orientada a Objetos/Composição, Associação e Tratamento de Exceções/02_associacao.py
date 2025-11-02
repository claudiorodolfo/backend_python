"""
Associação

Associação é um relacionamento fraco onde uma classe USA outra classe,
mas não possui necessariamente. Os objetos podem existir independentemente.
"""

# ==========================================
# CONCEITO DE ASSOCIAÇÃO
# ==========================================

print("=" * 60)
print("ASSOCIAÇÃO")
print("=" * 60)

print("""
ASSOCIAÇÃO:
  • Relacionamento FRACO
  • Uma classe USA outra, mas não possui
  • Objetos podem existir independentemente
  • Ciclo de vida independente

Tipos:
  • Associação Simples: Referência simples
  • Agregação: "TEM-UM" fraco (agregado pode existir sem)
  • Composição: "TEM-UM" forte (não pode existir sem) - visto anteriormente
""")


# ==========================================
# EXEMPLO 1: ASSOCIAÇÃO SIMPLES
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 1: Associação Simples - Pessoa e Biblioteca")
print("=" * 60)

class Pessoa:
    """Classe independente."""
    
    def __init__(self, nome):
        self.nome = nome
    
    def visitar_biblioteca(self, biblioteca):
        """Associação: Pessoa usa Biblioteca."""
        print(f"{self.nome} está visitando {biblioteca.nome}")


class Biblioteca:
    """Classe independente."""
    
    def __init__(self, nome):
        self.nome = nome
        # ASSOCIAÇÃO: Lista de pessoas que visitam
        self.visitantes = []
    
    def registrar_visitante(self, pessoa):
        """Associação: Biblioteca referencia Pessoa."""
        if pessoa not in self.visitantes:
            self.visitantes.append(pessoa)
            print(f"✓ {pessoa.nome} registrado(a) como visitante")
    
    def listar_visitantes(self):
        """Lista visitantes."""
        print(f"\nVisitantes da {self.nome}:")
        for visitante in self.visitantes:
            print(f"  • {visitante.nome}")


# Objetos existem independentemente
print("\nCriando objetos independentes:")
pessoa1 = Pessoa("Maria")
pessoa2 = Pessoa("João")
biblioteca = Biblioteca("Biblioteca Central")

print("\nAssociação: Registrando visitantes")
biblioteca.registrar_visitante(pessoa1)
biblioteca.registrar_visitante(pessoa2)

biblioteca.listar_visitantes()

print("\nPessoas podem existir sem biblioteca:")
print(f"{pessoa1.nome} existe independentemente")
print(f"{pessoa2.nome} existe independentemente")


# ==========================================
# EXEMPLO 2: ASSOCIAÇÃO UM-PARA-MUITOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Associação Um-para-Muitos - Professor e Alunos")
print("=" * 60)

class Aluno:
    """Classe independente."""
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.professor = None  # Associação: um aluno tem um professor
    
    def definir_professor(self, professor):
        """Associação: Aluno referencia Professor."""
        self.professor = professor
    
    def exibir_info(self):
        """Exibe informações do aluno."""
        prof_nome = self.professor.nome if self.professor else "Nenhum"
        print(f"{self.nome} (Mat: {self.matricula}) - Professor: {prof_nome}")


class Professor:
    """Classe independente."""
    
    def __init__(self, nome):
        self.nome = nome
        # ASSOCIAÇÃO: Um professor tem muitos alunos
        self.alunos = []
    
    def adicionar_aluno(self, aluno):
        """Associação: Professor referencia lista de Alunos."""
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.definir_professor(self)  # Bidirecional
            print(f"✓ {aluno.nome} adicionado à turma do Prof. {self.nome}")
    
    def listar_alunos(self):
        """Lista alunos do professor."""
        print(f"\nAlunos do Prof. {self.nome}:")
        for aluno in self.alunos:
            print(f"  • {aluno.nome} (Mat: {aluno.matricula})")


# Criando objetos independentes
print("\nCriando objetos:")
professor = Professor("Ana Silva")
aluno1 = Aluno("Bruno", "2024001")
aluno2 = Aluno("Carla", "2024002")
aluno3 = Aluno("Daniel", "2024003")

print("\nAssociação: Vinculando professor e alunos")
professor.adicionar_aluno(aluno1)
professor.adicionar_aluno(aluno2)
professor.adicionar_aluno(aluno3)

professor.listar_alunos()

print("\nVerificando associação bidirecional:")
aluno1.exibir_info()
aluno2.exibir_info()


# ==========================================
# EXEMPLO 3: ASSOCIAÇÃO MUITOS-PARA-MUITOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Associação Muitos-para-Muitos - Estudante e Curso")
print("=" * 60)

class Estudante:
    """Classe independente."""
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        # ASSOCIAÇÃO: Um estudante tem muitos cursos
        self.cursos = []
    
    def matricular_curso(self, curso):
        """Associação: Estudante referencia Curso."""
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.adicionar_estudante(self)  # Bidirecional
            print(f"✓ {self.nome} matriculado em {curso.nome}")
    
    def listar_cursos(self):
        """Lista cursos do estudante."""
        print(f"\nCursos de {self.nome}:")
        for curso in self.cursos:
            print(f"  • {curso.nome}")


class Curso:
    """Classe independente."""
    
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        # ASSOCIAÇÃO: Um curso tem muitos estudantes
        self.estudantes = []
    
    def adicionar_estudante(self, estudante):
        """Associação: Curso referencia Estudante."""
        if estudante not in self.estudantes:
            self.estudantes.append(estudante)
    
    def listar_estudantes(self):
        """Lista estudantes do curso."""
        print(f"\nEstudantes de {self.nome}:")
        for estudante in self.estudantes:
            print(f"  • {estudante.nome} (Mat: {estudante.matricula})")


# Criando objetos independentes
print("\nCriando objetos:")
estudante1 = Estudante("Maria", "2024001")
estudante2 = Estudante("João", "2024002")

curso1 = Curso("Python", "PYT101")
curso2 = Curso("Java", "JAV201")
curso3 = Curso("JavaScript", "JS301")

print("\nAssociação: Matriculando estudantes em cursos")
estudante1.matricular_curso(curso1)
estudante1.matricular_curso(curso2)
estudante2.matricular_curso(curso1)
estudante2.matricular_curso(curso3)

print("\nVisualizando associações:")
estudante1.listar_cursos()
estudante2.listar_cursos()

curso1.listar_estudantes()
curso2.listar_estudantes()


# ==========================================
# EXEMPLO 4: AGREGAÇÃO (Tipo de Associação)
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Agregação - Departamento e Funcionários")
print("=" * 60)

class Funcionario:
    """Classe independente - pode existir sem departamento."""
    
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    
    def __str__(self):
        return f"{self.nome} - {self.cargo}"


class Departamento:
    """
    Classe que agrega funcionários.
    
    Agregação: Funcionários podem existir sem departamento.
    """
    
    def __init__(self, nome):
        self.nome = nome
        # AGREGAÇÃO: Lista de funcionários (podem existir sem departamento)
        self.funcionarios = []
    
    def contratar(self, funcionario):
        """Agregação: Departamento referencia Funcionário."""
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
            print(f"✓ {funcionario.nome} contratado para {self.nome}")
    
    def demitir(self, funcionario):
        """Remove funcionário do departamento."""
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f"✓ {funcionario.nome} removido de {self.nome}")
    
    def listar_funcionarios(self):
        """Lista funcionários do departamento."""
        print(f"\nFuncionários do {self.nome}:")
        for func in self.funcionarios:
            print(f"  • {func}")


# Funcionários existem independentemente
print("\nCriando funcionários (independentes):")
func1 = Funcionario("Ana", "Desenvolvedora")
func2 = Funcionario("Bruno", "Designer")
func3 = Funcionario("Carla", "Gerente")

print("\nCriando departamento:")
dept = Departamento("TI")

print("\nAgregação: Contratando funcionários")
dept.contratar(func1)
dept.contratar(func2)
dept.contratar(func3)

dept.listar_funcionarios()

print("\nFuncionários ainda existem mesmo fora do departamento:")
print(f"{func1.nome} existe independentemente")
print(f"{func2.nome} existe independentemente")

print("\nDemitindo funcionário:")
dept.demitir(func2)
dept.listar_funcionarios()

print(f"\n{func2.nome} ainda existe: {func2}")


# ==========================================
# CARACTERÍSTICAS DA ASSOCIAÇÃO
# ==========================================

print("\n" + "=" * 60)
print("CARACTERÍSTICAS DA ASSOCIAÇÃO")
print("=" * 60)

print("""
✓ Relacionamento FRACO
✓ Objetos podem existir independentemente
✓ Uma classe USA outra, mas não possui
✓ Ciclo de vida independente
✓ Pode ser bidirecional (duas classes se referenciam)
✓ Exemplos: Pessoa-Biblioteca, Professor-Aluno

TIPOS:
  • Associação Simples: Referência simples
  • Agregação: "TEM-UM" fraco
  • Composição: "TEM-UM" forte (visto anteriormente)
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE ASSOCIAÇÃO")
print("=" * 60)

print("""
✓ Associação = relacionamento fraco "USA"
✓ Objetos existem independentemente
✓ Uma classe referencia outra
✓ Ciclo de vida independente
✓ Use quando objetos podem viver separadamente
✓ Pode ser um-para-muitos ou muitos-para-muitos
✓ Exemplos: Pessoa-Biblioteca, Estudante-Curso, Professor-Aluno
""")

