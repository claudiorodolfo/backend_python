# Padrão Simple Factory (Simple Factory Pattern)

## Descrição

O padrão **Simple Factory** (também conhecido como **Static Factory Method**) é um padrão de projeto criacional simplificado que centraliza a lógica de criação de objetos em uma única classe. Diferente do Factory Method, o Simple Factory usa um único método estático que recebe um parâmetro para determinar qual tipo de objeto criar, utilizando estruturas condicionais (if/elif) para decidir qual classe instanciar.

Este padrão resolve o problema de criar objetos sem especificar a classe exata do objeto que será criado, mas de forma mais simples que o Factory Method, ideal para cenários onde não há necessidade de múltiplas factories ou hierarquias complexas.

## Estrutura

O padrão Simple Factory consiste em:

- **Product (Animal)**: Interface abstrata que define o contrato para os objetos que serão criados
- **ConcreteProduct (Cao, Gato)**: Implementações concretas do produto
- **SimpleFactory (AnimalFactory)**: Classe concreta (não abstrata) que contém um método estático para criar objetos
- **Factory Method (criarAnimal)**: Método estático que encapsula a lógica de criação de objetos usando parâmetros

## Vantagens

1. **Simplicidade**: Implementação mais simples que Factory Method, sem necessidade de hierarquias de classes
2. **Desacoplamento**: Separa o código que usa objetos do código que os cria
3. **Responsabilidade única**: Centraliza a lógica de criação em um único lugar
4. **Facilidade de uso**: Método estático permite uso direto sem necessidade de instanciar a factory
5. **Flexibilidade**: Permite criar diferentes implementações do mesmo tipo de objeto
6. **Testabilidade**: Facilita testes unitários através de mocks e stubs

## Desvantagens

1. **Violação do Princípio Aberto/Fechado**: Adicionar novos tipos requer modificar o método factory (adicionar novos if/elif)
2. **Complexidade crescente**: Com muitos tipos, o método factory pode ficar grande e difícil de manter
3. **Acoplamento**: A factory conhece todas as classes concretas de produtos
4. **Menos flexível**: Não permite diferentes estratégias de criação através de subclasses

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

### 3. Simple Factory - AnimalFactory

A classe factory concreta que contém o método estático para criar objetos:

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

Para executar a demonstração completa do padrão Simple Factory:

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

2. **Modificar** o método factory adicionando um novo caso:
```python
elif animalType == "passaro":
    return Passaro()
```

**Nota**: Diferente do Factory Method, o Simple Factory requer modificação do código existente para adicionar novos tipos, violando o princípio Aberto/Fechado. Isso é aceitável quando o número de tipos é limitado e não muda frequentemente.

## Quando Usar

- Quando você tem um número limitado e estável de tipos de produtos
- Quando a lógica de criação é simples e não requer hierarquias complexas
- Quando você quer centralizar a criação de objetos sem a complexidade do Factory Method
- Quando você não precisa de diferentes estratégias de criação (diferentes factories)
- Quando a simplicidade é mais importante que a extensibilidade sem modificação
- Quando você quer esconder a lógica de criação do cliente

## Quando NÃO Usar

- Quando você precisa adicionar novos tipos frequentemente (prefira Factory Method)
- Quando você tem muitos tipos de produtos (o método factory ficaria muito grande)
- Quando você precisa de diferentes estratégias de criação (prefira Factory Method)
- Quando você quer seguir estritamente o princípio Aberto/Fechado (prefira Factory Method)
- Quando a criação de objetos é direta e não requer lógica especial

## Comparativo: Simple Factory vs Factory Method

### Simple Factory (Implementação Atual)

**Características:**
- Uma única classe concreta (`AnimalFactory`)
- Método estático que recebe parâmetro para decidir qual objeto criar
- Usa estruturas condicionais (if/elif) para determinar a classe a instanciar
- Não requer hierarquia de classes

**Exemplo:**
```python
class AnimalFactory:
    @staticmethod
    def criarAnimal(animalType: str) -> Animal:
        if animalType == "cao":
            return Cao()
        elif animalType == "gato":
            return Gato()
        else:
            raise ValueError(f"Tipo não conhecido: {animalType}")
```

**Vantagens:**
- ✅ Simples de implementar e entender
- ✅ Não requer múltiplas classes
- ✅ Fácil de usar (método estático)

**Desvantagens:**
- ❌ Viola princípio Aberto/Fechado (precisa modificar para adicionar tipos)
- ❌ Método pode ficar grande com muitos tipos
- ❌ Acoplamento com todas as classes concretas

### Factory Method

**Características:**
- Classe abstrata (`AnimalFactory`) define o Factory Method
- Subclasses concretas (`CaoFactory`, `GatoFactory`) implementam o método
- Cada factory cria apenas um tipo de produto
- Não usa parâmetros, usa diferentes factories

**Exemplo:**
```python
class AnimalFactory(ABC):
    @abstractmethod
    def criarAnimal(self) -> Animal:
        pass

class CaoFactory(AnimalFactory):
    def criarAnimal(self) -> Animal:
        return Cao()

class GatoFactory(AnimalFactory):
    def criarAnimal(self) -> Animal:
        return Gato()
```

**Vantagens:**
- ✅ Segue princípio Aberto/Fechado (extensão sem modificação)
- ✅ Cada factory tem responsabilidade única
- ✅ Mais flexível para diferentes estratégias de criação

**Desvantagens:**
- ❌ Mais complexo (requer múltiplas classes)
- ❌ Mais verboso (uma factory por tipo)
- ❌ Pode ser excessivo para casos simples

### Tabela Comparativa

| Aspecto | Simple Factory | Factory Method |
|--------|----------------|----------------|
| **Complexidade** | Baixa | Média/Alta |
| **Número de Classes** | 1 factory | 1 abstrata + N concretas |
| **Extensibilidade** | Requer modificação | Extensão sem modificação |
| **Princípio OCP** | Viola | Respeita |
| **Uso de Parâmetros** | Sim (if/elif) | Não (subclasses) |
| **Quando Usar** | Poucos tipos, estável | Muitos tipos, extensível |
| **Manutenibilidade** | Pior com muitos tipos | Melhor com muitos tipos |

### Quando Escolher Cada Um?

**Escolha Simple Factory quando:**
- Você tem poucos tipos de produtos (2-5 tipos)
- Os tipos não mudam frequentemente
- Você prioriza simplicidade sobre extensibilidade
- A lógica de criação é simples

**Escolha Factory Method quando:**
- Você tem muitos tipos ou planeja adicionar muitos
- Você precisa de extensibilidade sem modificar código existente
- Você precisa de diferentes estratégias de criação
- Você quer seguir estritamente princípios SOLID

## Diferenças de Outros Padrões

### Simple Factory vs Abstract Factory

- **Simple Factory**: Cria um tipo de produto usando parâmetros
- **Abstract Factory**: Cria famílias de produtos relacionados através de interfaces

### Simple Factory vs Builder

- **Simple Factory**: Foca em criar objetos de diferentes tipos
- **Builder**: Foca em construir objetos complexos passo a passo

### Simple Factory vs Prototype

- **Simple Factory**: Cria objetos do zero usando construtores
- **Prototype**: Cria objetos clonando uma instância existente

## Diagrama de Classes

```
┌─────────────────┐
│     Animal      │ (Product - Abstract)
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
│ AnimalFactory   │ (Simple Factory - Concrete)
├─────────────────┤
│ + criarAnimal() │ (Static Factory Method)
│   (type: str)   │
└─────────────────┘
         │
         │ usa if/elif para decidir
         ▼
    ┌────────┐
    │  Cao() │ ou │ Gato() │
    └────────┘
```

**Nota**: A seta indica que `AnimalFactory` usa estruturas condicionais para decidir qual classe concreta instanciar.

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
5. **Limite de tipos**: Mantenha o número de tipos gerenciáveis (considere Factory Method se exceder 5-7 tipos)
6. **Método estático**: Use `@staticmethod` para permitir uso sem instanciar a factory
7. **Validação de entrada**: Valide sempre os parâmetros antes de criar objetos

## Referências

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) - Gang of Four
- [Refactoring Guru - Factory Method Pattern](https://refactoring.guru/design-patterns/factory-method)
- [Source Making - Factory Method](https://sourcemaking.com/design_patterns/factory_method)
- [Baeldung - Simple Factory Pattern](https://www.baeldung.com/java-simple-factory-pattern)
