"""
Exemplos Práticos de Associação

Este arquivo apresenta exemplos práticos e comuns de associação
entre classes em diferentes contextos.
"""

# ==========================================
# EXEMPLO 1: ASSOCIAÇÃO UM-PARA-MUITOS
# ==========================================

print("=" * 60)
print("EXEMPLO 1: Associação Um-para-Muitos")
print("=" * 60)

class Professor:
    """
    Um professor tem muitos alunos.
    
    Associação: Professor referencia lista de Alunos.
    """
    
    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina
        self.alunos = []  # Associação: um-para-muitos
    
    def adicionarAluno(self, aluno):
        """Adiciona aluno à turma."""
        if aluno not in self.alunos:
            self.alunos.append(aluno)
            aluno.professor = self  # Bidirecional
            print(f"✓ {aluno.nome} adicionado à turma de {self.disciplina}")
    
    def removerAluno(self, aluno):
        """Remove aluno da turma."""
        if aluno in self.alunos:
            self.alunos.remove(aluno)
            aluno.professor = None
    
    def listarAlunos(self):
        """Lista todos os alunos."""
        print(f"\nAlunos do Prof. {self.nome} ({self.disciplina}):")
        for aluno in self.alunos:
            print(f"  • {aluno.nome} (Mat: {aluno.matricula})")


class Aluno:
    """
    Um aluno tem um professor.
    
    Associação: Aluno referencia um Professor.
    """
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.professor = None  # Associação: um-para-um
    
    def exibirInfo(self):
        """Exibe informações do aluno."""
        prof_nome = self.professor.nome if self.professor else "Nenhum"
        print(f"{self.nome} (Mat: {self.matricula}) - Professor: {prof_nome}")


# Testando associação um-para-muitos
print("\nCriando professor e alunos:")
professor = Professor("Ana Silva", "Python")
aluno1 = Aluno("Bruno", "2024001")
aluno2 = Aluno("Carla", "2024002")
aluno3 = Aluno("Daniel", "2024003")

print("\nAssociando alunos ao professor:")
professor.adicionarAluno(aluno1)
professor.adicionarAluno(aluno2)
professor.adicionarAluno(aluno3)

professor.listarAlunos()

print("\nVerificando associação bidirecional:")
aluno1.exibirInfo()


# ==========================================
# EXEMPLO 2: ASSOCIAÇÃO MUITOS-PARA-MUITOS
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 2: Associação Muitos-para-Muitos")
print("=" * 60)

class Estudante:
    """
    Um estudante tem muitos cursos.
    
    Associação: Estudante referencia lista de Cursos.
    """
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.cursos = []  # Associação: muitos-para-muitos
    
    def matricularCurso(self, curso):
        """Matricula estudante em curso."""
        if curso not in self.cursos:
            self.cursos.append(curso)
            curso.adicionarEstudante(self)  # Bidirecional
            print(f"✓ {self.nome} matriculado em {curso.nome}")
    
    def desmatricularCurso(self, curso):
        """Desmatricula estudante de curso."""
        if curso in self.cursos:
            self.cursos.remove(curso)
            curso.removerEstudante(self)
    
    def listarCursos(self):
        """Lista cursos do estudante."""
        print(f"\nCursos de {self.nome}:")
        for curso in self.cursos:
            print(f"  • {curso.nome} ({curso.codigo})")


class Curso:
    """
    Um curso tem muitos estudantes.
    
    Associação: Curso referencia lista de Estudantes.
    """
    
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.estudantes = []  # Associação: muitos-para-muitos
    
    def adicionarEstudante(self, estudante):
        """Adiciona estudante ao curso."""
        if estudante not in self.estudantes:
            self.estudantes.append(estudante)
    
    def removerEstudante(self, estudante):
        """Remove estudante do curso."""
        if estudante in self.estudantes:
            self.estudantes.remove(estudante)
    
    def listarEstudantes(self):
        """Lista estudantes do curso."""
        print(f"\nEstudantes de {self.nome}:")
        for estudante in self.estudantes:
            print(f"  • {estudante.nome} (Mat: {estudante.matricula})")


# Testando associação muitos-para-muitos
print("\nCriando estudantes e cursos:")
estudante1 = Estudante("Maria", "2024001")
estudante2 = Estudante("João", "2024002")

curso1 = Curso("Python", "PYT101")
curso2 = Curso("Java", "JAV201")
curso3 = Curso("JavaScript", "JS301")

print("\nMatriculando estudantes:")
estudante1.matricularCurso(curso1)
estudante1.matricularCurso(curso2)
estudante2.matricularCurso(curso1)
estudante2.matricularCurso(curso3)

print("\nVisualizando associações:")
estudante1.listarCursos()
estudante2.listarCursos()

curso1.listarEstudantes()


# ==========================================
# EXEMPLO 3: ASSOCIAÇÃO COM AGREGAÇÃO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 3: Associação com Agregação")
print("=" * 60)

class Funcionario:
    """
    Funcionário pode existir sem departamento.
    
    Agregação: Funcionário é agregado ao Departamento.
    """
    
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.departamento = None  # Pode ser None
    
    def __str__(self):
        return f"{self.nome} - {self.cargo} (R${self.salario:.2f})"
    
    def definirDepartamento(self, departamento):
        """Define departamento do funcionário."""
        if self.departamento:
            self.departamento.removerFuncionario(self)
        
        self.departamento = departamento
        if departamento:
            departamento.adicionarFuncionario(self)


class Departamento:
    """
    Departamento agrega funcionários.
    
    Agregação: Funcionários podem existir sem departamento.
    """
    
    def __init__(self, nome, orcamento):
        self.nome = nome
        self.orcamento = orcamento
        self.funcionarios = []  # Agregação: lista de funcionários
    
    def adicionarFuncionario(self, funcionario):
        """Adiciona funcionário ao departamento."""
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)
            print(f"✓ {funcionario.nome} adicionado a {self.nome}")
    
    def removerFuncionario(self, funcionario):
        """Remove funcionário do departamento."""
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
    
    def listarFuncionarios(self):
        """Lista funcionários do departamento."""
        print(f"\nFuncionários de {self.nome}:")
        if self.funcionarios:
            for func in self.funcionarios:
                print(f"  • {func}")
        else:
            print("  Nenhum funcionário")
    
    def calcularFolhaPagamento(self):
        """Calcula folha de pagamento do departamento."""
        total = sum(func.salario for func in self.funcionarios)
        return total


# Testando agregação
print("\nCriando funcionários (independentes):")
func1 = Funcionario("Ana", "Desenvolvedora", 5000)
func2 = Funcionario("Bruno", "Designer", 4000)
func3 = Funcionario("Carla", "Gerente", 7000)

print("\nCriando departamento:")
dept_ti = Departamento("TI", 100000)

print("\nAgregando funcionários ao departamento:")
func1.definirDepartamento(dept_ti)
func2.definirDepartamento(dept_ti)
func3.definirDepartamento(dept_ti)

dept_ti.listarFuncionarios()

print(f"\nFolha de pagamento: R${dept_ti.calcularFolhaPagamento():.2f}")

print("\nFuncionários ainda existem sem departamento:")
func1.definirDepartamento(None)
print(f"{func1.nome} existe independentemente")


# ==========================================
# EXEMPLO 4: ASSOCIAÇÃO COM HISTÓRICO
# ==========================================

print("\n" + "=" * 60)
print("EXEMPLO 4: Associação com Histórico")
print("=" * 60)

class Transacao:
    """Representa uma transação."""
    
    def __init__(self, valor, tipo, descricao):
        self.valor = valor
        self.tipo = tipo  # "entrada" ou "saida"
        self.descricao = descricao
    
    def __str__(self):
        sinal = "+" if self.tipo == "entrada" else "-"
        return f"{sinal} R${self.valor:.2f} - {self.descricao}"


class Conta:
    """
    Conta tem histórico de transações.
    
    Associação: Conta referencia lista de Transações.
    """
    
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.transacoes = []  # Associação: lista de transações
    
    def depositar(self, valor, descricao="Depósito"):
        """Deposita dinheiro e registra transação."""
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        self.saldo += valor
        transacao = Transacao(valor, "entrada", descricao)
        self.transacoes.append(transacao)
        print(f"✓ {transacao}")
    
    def sacar(self, valor, descricao="Saque"):
        """Saca dinheiro e registra transação."""
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        
        self.saldo -= valor
        transacao = Transacao(valor, "saida", descricao)
        self.transacoes.append(transacao)
        print(f"✓ {transacao}")
    
    def exibirExtrato(self):
        """Exibe extrato com histórico de transações."""
        print(f"\n{'=' * 50}")
        print(f"Extrato de {self.titular}")
        print("=" * 50)
        
        for transacao in self.transacoes:
            print(f"  {transacao}")
        
        print("=" * 50)
        print(f"Saldo: R${self.saldo:.2f}")
        print("=" * 50)


# Testando associação com histórico
print("\nCriando conta:")
conta = Conta("Ana Silva")

print("\nRealizando transações:")
conta.depositar(1000, "Salário")
conta.depositar(500, "Bônus")
conta.sacar(200, "Compras")
conta.sacar(100, "Almoço")
conta.depositar(300, "Reembolso")

conta.exibirExtrato()


# ==========================================
# RESUMO DOS TIPOS DE ASSOCIAÇÃO
# ==========================================

print("\n" + "=" * 60)
print("TIPOS DE ASSOCIAÇÃO")
print("=" * 60)

print("""
1. UM-PARA-MUITOS:
   • Um objeto referencia muitos outros
   • Exemplo: Professor → Alunos
   • Implementação: Lista no objeto "um"

2. MUITOS-PARA-MUITOS:
   • Muitos objetos se referenciam mutuamente
   • Exemplo: Estudante ↔ Cursos
   • Implementação: Lista em ambos os lados

3. AGREGAÇÃO:
   • Relacionamento "TEM-UM" fraco
   • Objetos agregados podem existir independentemente
   • Exemplo: Departamento → Funcionários

4. ASSOCIAÇÃO COM HISTÓRICO:
   • Um objeto mantém histórico de associações
   • Exemplo: Conta → Transações
   • Útil para auditoria e rastreamento
""")


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO SOBRE EXEMPLOS DE ASSOCIAÇÃO")
print("=" * 60)

print("""
✓ Associação permite objetos se referenciarem
✓ Pode ser um-para-muitos, muitos-para-muitos
✓ Agregação é tipo especial de associação
✓ Objetos associados existem independentemente
✓ Use listas para representar "muitos"
✓ Pode ser bidirecional (ambos se referenciam)
✓ Útil para modelar relacionamentos do mundo real
""")

