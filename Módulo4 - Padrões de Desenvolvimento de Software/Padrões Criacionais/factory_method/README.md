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

### 3. Creator Abstrato - AnimalFactory

A classe abstrata que define o Factory Method:

```python
from abc import ABC, abstractmethod
from animal import Animal

class AnimalFactory(ABC):
    
    @abstractmethod
    def criarAnimal(self) -> Animal:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass
```

### 4. Concrete Creators - CaoFactory e GatoFactory

Subclasses concretas que implementam o Factory Method:

```python
# cao_factory.py
from animal_factory import AnimalFactory
from animal import Animal
from cao import Cao

class CaoFactory(AnimalFactory):
    
    def criarAnimal(self) -> Animal:
        """Factory Method: cria uma instância de Cao"""
        return Cao()

# gato_factory.py
from animal_factory import AnimalFactory
from animal import Animal
from gato import Gato

class GatoFactory(AnimalFactory):
    
    def criarAnimal(self) -> Animal:
        """Factory Method: cria uma instância de Gato"""
        return Gato()
```

## Exemplo de Uso

### Uso Básico

```python
from cao_factory import CaoFactory
from gato_factory import GatoFactory

# Cada factory concreta cria seu próprio tipo de animal
cao_factory = CaoFactory()
animal1 = cao_factory.criarAnimal()
print(animal1.fazSom())  # Saída: Au au!

gato_factory = GatoFactory()
animal2 = gato_factory.criarAnimal()
print(animal2.fazSom())  # Saída: Miau!
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

### Creator Abstrato

A classe `AnimalFactory` é abstrata e define o contrato (Factory Method) que todas as factories concretas devem implementar. Isso garante que cada factory concreta tenha seu próprio método de criação.

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

2. Criar uma nova factory concreta que estende `AnimalFactory`:
```python
class PassaroFactory(AnimalFactory):
    def criarAnimal(self) -> Animal:
        return Passaro()
```

**Vantagem**: Não precisa modificar código existente, apenas adicionar novas classes (princípio Aberto/Fechado).

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

### Factory Method Clássico (Implementação Atual)

A implementação atual usa o Factory Method verdadeiro, onde:

- Uma classe abstrata `AnimalFactory` define o Factory Method abstrato
- Subclasses concretas (`CaoFactory`, `GatoFactory`) implementam o método
- Cada factory concreta cria apenas um tipo de produto

```python
class AnimalFactory(ABC):
    @abstractmethod
    def criarAnimal(self) -> Animal:
        pass

class CaoFactory(AnimalFactory):
    def criarAnimal(self) -> Animal:
        return Cao()
```

### Simple Factory (Factory Simples)

Uma variação mais simples usa um único método estático que cria objetos baseado em um parâmetro:

```python
class AnimalFactory:
    @staticmethod
    def criarAnimal(animalType: str) -> Animal:
        if animalType == "cao":
            return Cao()
        elif animalType == "gato":
            return Gato()
```

**Diferença**: Simple Factory usa parâmetros para decidir qual objeto criar, enquanto Factory Method usa subclasses diferentes.

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

- **Simple Factory**: Um único método cria objetos baseado em parâmetros (usa if/elif)
- **Factory Method**: Cada subclasse implementa seu próprio método de criação (implementação atual)

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
┌───▼───┐ ┌───▼───┐
│  Cao  │ │ Gato  │ (Concrete Products)
└───────┘ └───────┘

┌─────────────────┐
│ AnimalFactory   │ (Creator - Abstract)
│   (abstract)    │
├─────────────────┤
│ + criarAnimal() │ (Factory Method - abstract)
└────────┬────────┘
         │
    ┌────┴──────┐
    │           │
┌───▼──────┐ ┌──▼──────────┐
│CaoFactory│ │GatoFactory  │ (Concrete Creators)
├──────────┤ ├─────────────┤
│+criar... │ │+criar...    │
└──────────┘ └─────────────┘
```

## Fluxo de Execução

1. Cliente instancia uma factory concreta (ex: `CaoFactory()`)
2. Cliente chama `criarAnimal()` na factory concreta
3. Factory concreta instancia a classe de produto correspondente (`Cao`)
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

