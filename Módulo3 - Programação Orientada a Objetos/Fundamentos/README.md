# Fundamentos de Programação Orientada a Objetos

Este material introduz os conceitos fundamentais da Programação Orientada a Objetos (POO) em Python, comparando com a programação procedural e apresentando os elementos básicos necessários para começar a trabalhar com classes e objetos.

## 📚 Conteúdo

1. [O que é Programação Orientada a Objetos](#o-que-é-programação-orientada-a-objetos)
2. [Comparação: Procedural vs Orientado a Objetos](#comparação-procedural-vs-orientado-a-objetos)
3. [Conceitos-Chave](#conceitos-chave)
4. [Definição de Classes](#definição-de-classes)
5. [Métodos Construtores (__init__)](#métodos-construtores-__init__)
6. [Instanciação de Objetos](#instanciação-de-objetos)

---

## O que é Programação Orientada a Objetos

**Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de **objetos** e **classes**, ao invés de funções e procedimentos.

### Características Principais:

- **Encapsulamento**: Dados e métodos relacionados são agrupados em uma unidade (classe)
- **Abstração**: Esconde detalhes complexos e mostra apenas o essencial
- **Herança**: Permite reutilizar código através de hierarquias de classes
- **Polimorfismo**: Diferentes objetos podem responder à mesma interface de formas diferentes

### Vantagens da POO:

- ✅ **Organização**: Código mais organizado e fácil de entender
- ✅ **Reutilização**: Classes podem ser reutilizadas em diferentes contextos
- ✅ **Manutenibilidade**: Mais fácil de manter e modificar
- ✅ **Escalabilidade**: Facilita o crescimento do projeto
- ✅ **Modelagem**: Representa melhor o mundo real

---

## Comparação: Procedural vs Orientado a Objetos

### Abordagem Procedural

Na programação procedural, o código é organizado em **funções** que operam sobre **dados separados**:

```python
# Programação Procedural
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def verificar_obesidade(imc):
    if imc >= 30:
        return True
    return False

# Uso
peso = 75.5
altura = 1.75
imc = calcular_imc(peso, altura)
print(f"IMC: {imc:.2f}")
print(f"Obesidade: {verificar_obesidade(imc)}")
```

### Abordagem Orientada a Objetos

Na POO, **dados e funções relacionadas são agrupados** em uma classe:

```python
# Programação Orientada a Objetos
class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
    
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def verificar_obesidade(self):
        imc = self.calcular_imc()
        return imc >= 30

# Uso
pessoa = Pessoa(75.5, 1.75)
imc = pessoa.calcular_imc()
print(f"IMC: {imc:.2f}")
print(f"Obesidade: {pessoa.verificar_obesidade()}")
```

### Diferenças Principais:

| Procedural | Orientado a Objetos |
|------------|---------------------|
| Dados e funções separados | Dados e métodos agrupados |
| Foco em funções | Foco em objetos |
| Dados passados como parâmetros | Dados armazenados no objeto |
| Menos organização em projetos grandes | Melhor organização e escalabilidade |

---

## Conceitos-Chave

### 1. Classe

Uma **classe** é um molde ou template que define:
- **Atributos** (características/dados)
- **Métodos** (comportamentos/ações)

Pense em uma classe como uma receita ou um projeto de arquitetura.

```python
class Carro:
    # Atributos (definidos no __init__)
    # Métodos (funções dentro da classe)
    pass
```

### 2. Objeto (Instância)

Um **objeto** é uma instância específica de uma classe. É como uma "casa construída" a partir do "projeto de arquitetura" (classe).

```python
# Carro é a classe
# meu_carro é um objeto (instância) da classe Carro
meu_carro = Carro()
```

### 3. Atributo

**Atributos** são características ou propriedades de um objeto. Armazenam dados sobre o objeto.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome      # Atributo 'nome'
        self.idade = idade    # Atributo 'idade'
```

### 4. Método

**Métodos** são funções definidas dentro de uma classe que definem comportamentos ou ações que o objeto pode realizar.

```python
class Pessoa:
    def apresentar(self):  # Método
        print(f"Olá, sou {self.nome}")
```

---

## Definição de Classes

### Sintaxe Básica

```python
class NomeDaClasse:
    """Docstring da classe (opcional mas recomendado)"""
    
    def metodo1(self):
        pass
    
    def metodo2(self):
        pass
```

### Exemplo Prático

```python
class Retangulo:
    """Representa um retângulo com largura e altura."""
    
    def calcular_area(self):
        """Calcula a área do retângulo."""
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        """Calcula o perímetro do retângulo."""
        return 2 * (self.largura + self.altura)
```

---

## Métodos Construtores (__init__)

O método `__init__` é o **construtor** da classe. Ele é chamado automaticamente quando um objeto é criado e é usado para **inicializar os atributos** do objeto.

### Características:

- Sempre se chama `__init__` (com dois underscores antes e depois)
- Recebe `self` como primeiro parâmetro
- É executado automaticamente quando o objeto é criado
- Usa-se para definir valores iniciais dos atributos

### Sintaxe:

```python
class NomeClasse:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```

### Exemplo:

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print(f"{nome} foi criado(a)!")

# Ao criar o objeto, __init__ é chamado automaticamente
pessoa1 = Pessoa("Maria", 25)  # Imprime: "Maria foi criado(a)!"
```

### Construtor sem Parâmetros

```python
class Carro:
    def __init__(self):
        self.modelo = "Desconhecido"
        self.ano = 0
        self.cor = "Branco"

# Criação sem parâmetros
meu_carro = Carro()
```

### Construtor com Parâmetros Opcionais

```python
class Carro:
    def __init__(self, modelo="Desconhecido", ano=0, cor="Branco"):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

# Pode criar com ou sem parâmetros
carro1 = Carro()  # Usa valores padrão
carro2 = Carro("Fusca", 1975)  # Especifica alguns parâmetros
carro3 = Carro("Gol", 2020, "Vermelho")  # Especifica todos
```

---

## Instanciação de Objetos

**Instanciação** é o processo de criar um objeto (instância) a partir de uma classe.

### Sintaxe:

```python
objeto = NomeDaClasse(parametros)
```

### Processo de Instanciação:

1. Python chama automaticamente o método `__init__`
2. Os parâmetros passados são atribuídos aos atributos do objeto
3. O objeto criado é retornado e pode ser armazenado em uma variável

### Exemplo Completo:

```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente!")
    
    def exibir_saldo(self):
        print(f"Saldo da conta de {self.titular}: R${self.saldo:.2f}")

# Instanciação de objetos
conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 500)

# Cada objeto é independente
conta1.depositar(200)
conta2.sacar(100)
conta1.exibir_saldo()
conta2.exibir_saldo()
```

### Múltiplas Instâncias

Cada instância é **independente** e possui seus próprios atributos:

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def exibir_info(self):
        print(f"{self.nome}: {self.nota}")

# Criando múltiplos objetos
aluno1 = Aluno("Ana", 8.5)
aluno2 = Aluno("Bruno", 9.0)
aluno3 = Aluno("Carla", 7.5)

# Cada objeto tem seus próprios valores
aluno1.exibir_info()  # Ana: 8.5
aluno2.exibir_info()  # Bruno: 9.0
aluno3.exibir_info()  # Carla: 7.5
```

---

## 📁 Arquivos de Exemplo

Este diretório contém exemplos práticos:

1. **01_o_que_e_poo.py** - Introdução conceitual
2. **02_procedural_vs_oop.py** - Comparação entre abordagens
3. **03_conceitos_basicos.py** - Classes, objetos, atributos e métodos
4. **04_definicao_classes.py** - Como definir classes
5. **05_construtores.py** - Métodos __init__
6. **06_instanciacao.py** - Criando objetos
7. **07_exemplo_completo.py** - Exemplo prático completo

Execute cada arquivo para ver os exemplos em ação:

```bash
python3 01_o_que_e_poo.py
python3 02_procedural_vs_oop.py
# ... e assim por diante
```

---

## 🎯 Próximos Passos

Após dominar os fundamentos, avance para:
- **Encapsulamento, Herança e Polimorfismo**: Controle de acesso, herança e polimorfismo
- **Composição, Associação e Tratamento de Exceções**: Relacionamentos entre classes e tratamento de erros

---

## 💡 Dicas

1. **Pratique criando classes**: Crie classes para coisas do seu dia a dia
2. **Entenda o `self`**: Sempre necessário em métodos de instância
3. **Use nomes descritivos**: Classes em PascalCase, métodos em snake_case
4. **Documente suas classes**: Use docstrings para explicar o propósito
5. **Pense em objetos**: Modelar o problema pensando em objetos, não em funções

