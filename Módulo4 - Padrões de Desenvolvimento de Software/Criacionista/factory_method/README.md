# Padrão Factory Method (Factory Method Pattern)

## Descrição

O padrão **Factory Method** é um padrão de projeto criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados. Este padrão resolve o problema de criar objetos sem especificar a classe exata do objeto que será criado, delegando a responsabilidade de criação para subclasses ou métodos especializados.

## Estrutura

O padrão Factory Method consiste em:

- **Product (Animal)**: Interface abstrata que define o contrato para os objetos que serão criados
- **ConcreteProduct (Cao, Gato)**: Implementações concretas do produto
- **Creator (AnimalFactory)**: Classe que contém o método factory para criar objetos
- **Factory Method (criarAnimal)**: Método que encapsula a lógica de criação de objetos

## Vantagens

1. **Desacoplamento**: Separa o código que usa objetos do código que os cria
2. **Extensibilidade**: Facilita a adição de novos tipos de produtos sem modificar o código existente
3. **Princípio Aberto/Fechado**: Aberto para extensão, fechado para modificação
4. **Responsabilidade única**: Centraliza a lógica de criação em um único lugar
5. **Flexibilidade**: Permite criar diferentes implementações do mesmo tipo de objeto
6. **Testabilidade**: Facilita testes unitários através de mocks e stubs

## Estrutura do Código

### 1. Product - Animal

A classe abstrata `Animal` define a interface comum para todos os produtos:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazSom(self) -> str:
        pass
```

### 2. Concrete Products - Cao e Gato

Implementações concretas do produto:

```python
# cao.py
from animal import Animal

class Cao(Animal):
    def fazSom(self) -> str:
        return "Au au!"

# gato.py
from animal import Animal

class Gato(Animal):
    def fazSom(self) -> str:
        return "Miau!"
```

### 3. Factory - AnimalFactory

A classe factory que contém o método factory para criar objetos:

```python
from animal import Animal
from cao import Cao
from gato import Gato

class AnimalFactory:
    @staticmethod
    def criarAnimal(animalType: str) -> Animal:
        if animalType == "cao":
            return Cao()
        elif animalType == "gato":
            return Gato()
        else:
            raise ValueError(f"Tipo de animal não conhecido: {animalType}")
```

## Exemplo de Uso

### Uso Básico

```python
from animal_factory import AnimalFactory

# Criar um cão
animal1 = AnimalFactory.criarAnimal("cao")
print(animal1.fazSom())  # Saída: Au au!

# Criar um gato
animal2 = AnimalFactory.criarAnimal("gato")
print(animal2.fazSom())  # Saída: Miau!
```

### Tratamento de Erros

```python
from animal_factory import AnimalFactory

try:
    animal = AnimalFactory.criarAnimal("passaro")
except ValueError as e:
    print(e)  # Saída: Tipo de animal não conhecido: passaro
```

## Executando o Exemplo

Para executar a demonstração completa do padrão Factory Method:

```bash
python3 main.py
```

O script demonstra:
1. Criação de um cão usando a factory
2. Criação de um gato usando a factory
3. Exibição dos sons que cada animal faz

## Características Importantes

### Método Estático

O método `criarAnimal` é estático, permitindo chamá-lo diretamente na classe sem instanciar a factory:

```python
animal = AnimalFactory.criarAnimal("cao")
```

### Type Safety

O método retorna um tipo `Animal`, garantindo que o código cliente trabalhe com a interface abstrata, não com implementações concretas.

### Extensibilidade

Para adicionar um novo tipo de animal:

1. Criar uma nova classe que estende `Animal`:
```python
class Passaro(Animal):
    def fazSom(self) -> str:
        return "Piu piu!"
```

2. Adicionar o caso na factory:
```python
elif animalType == "passaro":
    return Passaro()
```

## Quando Usar

- Quando você não sabe antecipadamente os tipos exatos e dependências dos objetos que seu código deve trabalhar
- Quando você quer fornecer uma biblioteca de produtos e revelar apenas suas interfaces, não suas implementações
- Quando você quer permitir que os usuários estendam sua biblioteca ou framework com novos tipos de produtos
- Quando você quer economizar recursos do sistema reutilizando objetos existentes em vez de reconstruí-los
- Quando a criação de objetos envolve lógica complexa que deve ser centralizada

## Quando NÃO Usar

- Quando o código que cria objetos é simples e não muda frequentemente
- Quando você tem apenas um tipo de produto e não planeja adicionar mais
- Quando a complexidade adicional do padrão não traz benefícios claros
- Quando a criação de objetos é direta e não requer lógica especial

## Variações do Padrão

### Simple Factory (Factory Simples)

A implementação atual usa uma Simple Factory, onde um único método estático cria objetos baseado em um parâmetro:

```python
@staticmethod
def criarAnimal(animalType: str) -> Animal:
    # lógica de criação
```

### Factory Method Clássico

Uma variação mais complexa envolve classes abstratas de factory:

```python
class AnimalFactory(ABC):
    @abstractmethod
    def criarAnimal(self) -> Animal:
        pass

class CaoFactory(AnimalFactory):
    def criarAnimal(self) -> Animal:
        return Cao()
```

### Abstract Factory

Quando você precisa criar famílias de objetos relacionados:

```python
class AnimalFactory(ABC):
    @abstractmethod
    def criarAnimal(self) -> Animal:
        pass
    
    @abstractmethod
    def criarHabitat(self) -> Habitat:
        pass
```

## Diferenças de Outros Padrões

### Factory Method vs Simple Factory

- **Simple Factory**: Um único método cria objetos baseado em parâmetros (implementação atual)
- **Factory Method**: Cada subclasse implementa seu próprio método de criação

### Factory Method vs Abstract Factory

- **Factory Method**: Cria um tipo de produto
- **Abstract Factory**: Cria famílias de produtos relacionados

### Factory Method vs Builder

- **Factory Method**: Foca em criar objetos de diferentes tipos
- **Builder**: Foca em construir objetos complexos passo a passo

### Factory Method vs Prototype

- **Factory Method**: Cria objetos do zero usando construtores
- **Prototype**: Cria objetos clonando uma instância existente

## Diagrama de Classes

```
┌─────────────────┐
│     Animal      │ (Product)
│  (interface)    │
├─────────────────┤
│ + fazSom(): str │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼────┐
│  Cao  │ │ Gato  │ (Concrete Products)
└───────┘ └───────┘

┌─────────────────┐
│ AnimalFactory   │ (Creator)
├─────────────────┤
│ + criarAnimal() │ (Factory Method)
└─────────────────┘
```

## Fluxo de Execução

1. Cliente chama `AnimalFactory.criarAnimal("cao")`
2. Factory verifica o tipo solicitado
3. Factory instancia a classe concreta apropriada (`Cao`)
4. Factory retorna a instância como tipo `Animal`
5. Cliente usa a instância através da interface `Animal`

## Boas Práticas

1. **Nomes descritivos**: Use nomes claros para métodos factory (ex: `criarAnimal`, `criarVeiculo`)
2. **Tratamento de erros**: Sempre valide parâmetros e lance exceções apropriadas
3. **Documentação**: Documente quais tipos de objetos podem ser criados
4. **Consistência**: Mantenha uma interface consistente para todos os produtos
5. **Extensibilidade**: Projete a factory pensando em futuras extensões

## Referências

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) - Gang of Four
- [Refactoring Guru - Factory Method Pattern](https://refactoring.guru/design-patterns/factory-method)
- [Source Making - Factory Method](https://sourcemaking.com/design_patterns/factory_method)

