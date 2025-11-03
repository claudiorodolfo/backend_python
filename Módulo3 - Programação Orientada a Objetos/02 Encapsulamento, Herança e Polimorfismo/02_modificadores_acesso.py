"""
Modificadores de Acesso: Public, Protected, Private

Python usa convenções de nomenclatura para indicar visibilidade.
"""

# ==========================================
# TIPOS DE MODIFICADORES EM PYTHON
# ==========================================

print("=" * 60)
print("MODIFICADORES DE ACESSO EM PYTHON")
print("=" * 60)

print("""
Python não tem modificadores rígidos como Java ou C++.
Em vez disso, usa CONVENÇÕES DE NOMENCLATURA:

1. PÚBLICO: sem prefixo (ex: nome, idade)
2. PROTEGIDO: um underscore (ex: _nome, _idade)
3. PRIVADO: dois underscores (ex: __nome, __idade)
""")


# ==========================================
# PÚBLICO (Public)
# ==========================================

print("\n" + "=" * 60)
print("1. PÚBLICO (Public)")
print("=" * 60)

class PessoaPublic:
    """
    Atributos e métodos públicos.
    
    Podem ser acessados de qualquer lugar.
    """
    
    def __init__(self, nome, idade):
        self.nome = nome      # Público
        self.idade = idade    # Público
    
    def apresentar(self):    # Método público
        """Método público."""
        print(f"Sou {self.nome} e tenho {self.idade} anos")
    
    def fazerAniversario(self):  # Método público
        """Método público."""
        self.idade += 1


# Acesso público - tudo acessível
pessoa = PessoaPublic("Maria", 25)
pessoa.nome = "João"  # Pode modificar diretamente
pessoa.idade = 30      # Pode modificar diretamente
pessoa.apresentar()


# ==========================================
# PROTEGIDO (Protected)
# ==========================================

print("\n" + "=" * 60)
print("2. PROTEGIDO (Protected) - Convenção _")
print("=" * 60)

class PessoaProtected:
    """
    Atributos e métodos protegidos.
    
    Convenção: não devem ser acessados fora da classe,
    mas Python não impede. Usados principalmente em herança.
    """
    
    def __init__(self, nome, idade):
        self._nome = nome      # Protegido (convenção)
        self._idade = idade    # Protegido (convenção)
    
    def _validarIdade(self, idade):
        """
        Método protegido.
        
        Convenção: para uso interno da classe e subclasses.
        """
        return 0 <= idade <= 150
    
    def setIdade(self, idade):
        """Método público que usa método protegido."""
        if self._validarIdade(idade):
            self._idade = idade
        else:
            raise ValueError("Idade inválida")
    
    def exibirInfo(self):
        """Método público."""
        print(f"{self._nome} tem {self._idade} anos")


# Uso
pessoa_prot = PessoaProtected("Ana", 30)
pessoa_prot.setIdade(35)
pessoa_prot.exibirInfo()

# ⚠️ ATENÇÃO: Ainda é possível acessar diretamente
# Mas por CONVENÇÃO não devemos fazer isso
pessoa_prot._nome = "Bruno"  # Funciona, mas não recomendado
print(f"\nAcesso direto (não recomendado): {pessoa_prot._nome}")


# ==========================================
# PRIVADO (Private)
# ==========================================

print("\n" + "=" * 60)
print("3. PRIVADO (Private) - Convenção __")
print("=" * 60)

class PessoaPrivate:
    """
    Atributos e métodos privados.
    
    Python faz "name mangling" (renomeia o atributo),
    dificultando (mas não impossibilitando) o acesso.
    """
    
    def __init__(self, nome, idade):
        self.__nome = nome      # Privado
        self.__idade = idade    # Privado
        self.publico = "Acessível"  # Público (para comparação)
    
    def __metodoPrivado(self):
        """Método privado."""
        print("Este é um método privado")
    
    def getNome(self):
        """Getter público para acessar nome privado."""
        return self.__nome
    
    def setIdade(self, idade):
        """Setter público com validação."""
        if 0 <= idade <= 150:
            self.__idade = idade
        else:
            raise ValueError("Idade inválida")
    
    def getIdade(self):
        """Getter público para acessar idade privada."""
        return self.__idade
    
    def usarMetodoPrivado(self):
        """Método público que usa método privado."""
        self.__metodo_privado()
    
    def exibirInfo(self):
        """Método público."""
        print(f"{self.__nome} tem {self.__idade} anos")


# Uso
pessoa_priv = PessoaPrivate("Carla", 28)
pessoa_priv.exibirInfo()

# Acesso através de métodos públicos
print(f"\nNome via getter: {pessoa_priv.getNome()}")
print(f"Idade via getter: {pessoa_priv.getIdade()}")

# Tentando acessar diretamente (não funciona normalmente)
try:
    print(f"\nTentando: pessoa_priv.__nome")
    print(pessoa_priv.__nome)  # Isso vai dar erro!
except AttributeError as e:
    print(f"Erro: {e}")

# Mas note que o atributo existe com nome "mangled"
print(f"\nAcesso público normal: {pessoa_priv.publico}")
print(f"Python renomeou: {pessoa_priv._PessoaPrivate__nome}")  # Name mangling


# ==========================================
# EXEMPLO COMPARATIVO
# ==========================================

print("\n" + "=" * 60)
print("COMPARAÇÃO: Public vs Protected vs Private")
print("=" * 60)

class ExemploCompleto:
    """Demonstra todos os níveis de acesso."""
    
    def __init__(self):
        self.publico = "Acessível de qualquer lugar"
        self._protegido = "Convenção: use apenas na classe/subclasses"
        self.__privado = "Dificulta acesso externo"
    
    def metodo_publico(self):
        """Método público."""
        print("Método público chamado")
        self._metodo_protegido()
        self.__metodo_privado()
    
    def _metodo_protegido(self):
        """Método protegido."""
        print("Método protegido chamado")
    
    def __metodo_privado(self):
        """Método privado."""
        print("Método privado chamado")


obj = ExemploCompleto()

print("\nAcesso público:")
print(f"  obj.publico = {obj.publico}")
obj.metodo_publico()

print("\nAcesso protegido (convenção):")
print(f"  obj._protegido = {obj._protegido}")  # Funciona, mas não recomendado
obj._metodo_protegido()  # Funciona, mas não recomendado

print("\nAcesso privado:")
try:
    print(f"  obj.__privado = {obj.__privado}")  # Erro
except AttributeError:
    print("  Não acessível normalmente")
    print(f"  Mas existe como: {obj._ExemploCompleto__privado}")


# ==========================================
# HERANÇA E MODIFICADORES
# ==========================================

print("\n" + "=" * 60)
print("HERANÇA E MODIFICADORES")
print("=" * 60)

class Pai:
    """Classe pai para demonstrar herança."""
    
    def __init__(self):
        self.publico = "Público"
        self._protegido = "Protegido"
        self.__privado = "Privado"
    
    def metodo_publico(self):
        print("Método público do pai")
    
    def _metodo_protegido(self):
        print("Método protegido do pai")
    
    def __metodo_privado(self):
        print("Método privado do pai")


class Filho(Pai):
    """Classe filha que herda do pai."""
    
    def testar_acesso(self):
        """Testa acesso a atributos e métodos herdados."""
        # Público: acessível
        print(f"\nPúblico: {self.publico}")
        self.metodo_publico()
        
        # Protegido: acessível em subclasses
        print(f"\nProtegido: {self._protegido}")
        self._metodo_protegido()
        
        # Privado: NÃO acessível (name mangling diferente)
        # self.__privado não funciona, mas self._Pai__privado funcionaria
        print(f"\nPrivado (via name mangling): {self._Pai__privado}")


filho = Filho()
filho.testar_acesso()


# ==========================================
# RESUMO
# ==========================================

print("\n" + "=" * 60)
print("RESUMO DOS MODIFICADORES")
print("=" * 60)

print("""
┌─────────────────────────────────────────────────────┐
│ PÚBLICO (sem prefixo)                               │
├─────────────────────────────────────────────────────┤
│ • Acessível de qualquer lugar                       │
│ • Interface da classe                               │
│ • Exemplo: self.nome, self.idade                    │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ PROTEGIDO (_ um underscore)                         │
├─────────────────────────────────────────────────────┤
│ • Convenção: use na classe e subclasses             │
│ • Python não impede acesso                          │
│ • Para uso interno                                  │
│ • Exemplo: self._nome, self._validar()              │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ PRIVADO (__ dois underscores)                       │
├─────────────────────────────────────────────────────┤
│ • Python faz name mangling                          │
│ • Dificulta acesso externo                          │
│ • Para detalhes de implementação                    │
│ • Exemplo: self.__nome, self.__calcular()           │
└─────────────────────────────────────────────────────┘

DICA: Em Python, a convenção é mais importante que
      a proteção técnica. Siga as convenções!
""")

