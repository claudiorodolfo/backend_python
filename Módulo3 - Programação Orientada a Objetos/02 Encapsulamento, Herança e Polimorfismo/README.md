# Encapsulamento, Herança e Polimorfismo

Este material aborda três dos quatro pilares fundamentais da Programação Orientada a Objetos, essenciais para criar código robusto, reutilizável e manutenível.

## 📚 Conteúdo

1. [Encapsulamento](#encapsulamento)
2. [Modificadores de Acesso](#modificadores-de-acesso)
3. [Getters e Setters](#getters-e-setters)
4. [Herança](#herança)
5. [Sobrescrita de Métodos (Override)](#sobrescrita-de-métodos-override)
6. [Polimorfismo](#polimorfismo)

---

## Encapsulamento

**Encapsulamento** é o princípio que agrupa dados (atributos) e métodos que operam sobre esses dados em uma única unidade (classe), e controla o acesso a esses dados.

### Importância do Encapsulamento:

- ✅ **Proteção de dados**: Previne acesso não autorizado ou modificações indevidas
- ✅ **Validação**: Permite validar dados antes de atribuí-los
- ✅ **Flexibilidade**: Facilita mudanças na implementação sem afetar o código que usa a classe
- ✅ **Manutenibilidade**: Código mais fácil de manter e debugar

### Conceito:

Em vez de expor diretamente os atributos, o encapsulamento usa métodos para controlar como os dados são acessados e modificados.

```python
# SEM encapsulamento (ruim)
pessoa.idade = -5  # Idade negativa! ❌

# COM encapsulamento (bom)
pessoa.set_idade(-5)  # Validação: idade não pode ser negativa ✅
```

---

## Modificadores de Acesso

Python não possui modificadores de acesso rígidos como Java ou C++, mas usa **convenções de nomenclatura** para indicar a visibilidade:

### 1. Público (Public)

Atributos e métodos sem prefixo são considerados **públicos** e podem ser acessados de qualquer lugar.

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Público
    
    def apresentar(self):  # Método público
        print(f"Sou {self.nome}")
```

### 2. Protegido (Protected)

Atributos e métodos com **um underscore** (`_`) são considerados **protegidos**. Convenção: não devem ser acessados fora da classe, mas Python não impede.

```python
class Pessoa:
    def __init__(self, nome):
        self._nome = nome  # Protegido (convenção)
    
    def _validar_nome(self):  # Método protegido
        pass
```

### 3. Privado (Private)

Atributos e métodos com **dois underscores** (`__`) são considerados **privados**. Python faz name mangling, dificultando (mas não impossibilitando) o acesso externo.

```python
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Privado
    
    def __validar_dados(self):  # Método privado
        pass
```

### Tabela de Comparação:

| Tipo | Sintaxe | Acesso | Uso |
|------|---------|--------|-----|
| Público | `atributo` | Qualquer lugar | Interface da classe |
| Protegido | `_atributo` | Classe e subclasses (convenção) | Para uso interno |
| Privado | `__atributo` | Apenas dentro da classe | Detalhes de implementação |

---

## Getters e Setters

**Getters** e **Setters** são métodos usados para acessar e modificar atributos de forma controlada.

### Por que usar?

1. **Validação**: Validar dados antes de atribuir
2. **Controle**: Controlar como os dados são acessados
3. **Computação**: Calcular valores derivados
4. **Logging**: Registrar acessos e modificações

### Método Tradicional:

```python
class Pessoa:
    def __init__(self, idade):
        self._idade = idade  # Protegido
    
    def get_idade(self):
        """Getter: retorna a idade."""
        return self._idade
    
    def set_idade(self, idade):
        """Setter: define a idade com validação."""
        if idade < 0 or idade > 150:
            raise ValueError("Idade deve estar entre 0 e 150")
        self._idade = idade
```

### Usando @property (Recomendado):

Python oferece o decorador `@property` para criar getters e setters de forma mais elegante:

```python
class Pessoa:
    def __init__(self, idade):
        self._idade = idade
    
    @property
    def idade(self):
        """Getter usando @property."""
        return self._idade
    
    @idade.setter
    def idade(self, valor):
        """Setter usando @property."""
        if valor < 0 or valor > 150:
            raise ValueError("Idade inválida")
        self._idade = valor

# Uso parece natural
pessoa = Pessoa(25)
pessoa.idade = 30  # Chama o setter automaticamente
print(pessoa.idade)  # Chama o getter automaticamente
```

---

## Herança

**Herança** permite criar uma nova classe (subclasse) baseada em uma classe existente (superclasse), reutilizando código e especializando comportamento.

### Vantagens:

- ✅ **Reutilização de código**: Evita duplicação
- ✅ **Especialização**: Criar classes mais específicas
- ✅ **Manutenibilidade**: Mudanças na classe pai afetam todas as filhas
- ✅ **Modelagem**: Representa relacionamentos "é-um"

### Sintaxe:

```python
class ClassePai:
    pass

class ClasseFilha(ClassePai):  # Herda de ClassePai
    pass
```

### Exemplo:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        print("Algum som")

class Cachorro(Animal):  # Cachorro É-UM Animal
    def fazer_som(self):
        print("Au au!")

class Gato(Animal):  # Gato É-UM Animal
    def fazer_som(self):
        print("Miau!")
```

### Herança Múltipla:

Python suporta herança múltipla (herdar de várias classes):

```python
class A:
    pass

class B:
    pass

class C(A, B):  # Herda de A e B
    pass
```

---

## Sobrescrita de Métodos (Override)

**Sobrescrita** (override) é quando uma subclasse redefine um método da classe pai, fornecendo uma implementação específica.

### Conceito:

A subclasse pode:
- Manter a mesma assinatura do método pai
- Fornecer uma implementação diferente
- Chamar o método pai usando `super()`

### Exemplo:

```python
class Veiculo:
    def acelerar(self):
        print("Acelerando...")

class Carro(Veiculo):
    def acelerar(self):  # Sobrescreve o método
        print("Pisando no acelerador!")

class Moto(Veiculo):
    def acelerar(self):  # Sobrescreve o método
        print("Girando o punho do acelerador!")
```

### Usando super():

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)  # Chama construtor do pai
        self.raca = raca
```

---

## Polimorfismo

**Polimorfismo** é a capacidade de objetos de diferentes classes responderem à mesma interface (mesmo método) de formas diferentes.

### Conceito:

"Um mesmo método pode ter comportamentos diferentes dependendo do objeto que o chama."

### Exemplo Clássico:

```python
class Forma:
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def calcular_area(self):
        return 3.14 * self.raio ** 2

# Polimorfismo em ação
formas = [Retangulo(), Circulo()]
for forma in formas:
    print(forma.calcular_area())  # Cada uma calcula de forma diferente
```

### Vantagens:

- ✅ **Flexibilidade**: Código genérico que funciona com diferentes tipos
- ✅ **Extensibilidade**: Fácil adicionar novos tipos
- ✅ **Manutenibilidade**: Mudanças isoladas por classe

---

## 📁 Arquivos de Exemplo

Este diretório contém exemplos práticos:

1. **01_encapsulamento.py** - Conceitos de encapsulamento
2. **02_modificadores_acesso.py** - Public, protected, private
3. **03_getters_setters.py** - Métodos get e set
4. **04_property.py** - Usando @property
5. **05_heranca.py** - Herança básica
6. **06_sobrescrita.py** - Override de métodos
7. **07_super.py** - Usando super()
8. **08_polimorfismo.py** - Polimorfismo na prática
9. **09_exemplo_completo.py** - Sistema completo integrando todos os conceitos

Execute cada arquivo para ver os exemplos em ação:

```bash
python3 01_encapsulamento.py
python3 02_modificadores_acesso.py
# ... e assim por diante
```

---

## 🎯 Próximos Passos

Após dominar encapsulamento, herança e polimorfismo, avance para:
- **Composição, Associação e Tratamento de Exceções**: Relacionamentos entre classes e tratamento de erros

---

## 💡 Dicas

1. **Use encapsulamento sempre**: Proteja seus dados com getters/setters
2. **Prefira @property**: Mais elegante que métodos get/set tradicionais
3. **Herança quando fizer sentido**: Use quando há relação "é-um"
4. **Evite herança múltipla complexa**: Pode ficar difícil de entender
5. **Aproveite o polimorfismo**: Permite código mais flexível e genérico
6. **Use super()**: Para chamar métodos da classe pai
7. **Documente bem**: Especialmente em hierarquias de classes

