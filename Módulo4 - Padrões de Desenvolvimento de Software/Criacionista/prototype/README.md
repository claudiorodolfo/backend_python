# Padrão Prototype (Prototype Pattern)

## Descrição

O padrão **Prototype** é um padrão de projeto criacional que permite criar novos objetos copiando instâncias existentes (protótipos), em vez de criar objetos do zero. Isso é especialmente útil quando a criação de um objeto é custosa ou complexa.

## Estrutura

O padrão Prototype consiste em:

- **Prototype (Protótipo)**: Interface ou classe abstrata que declara o método `clone()`
- **ConcretePrototype (Protótipo Concreto)**: Implementação concreta que implementa o método `clone()`
- **Client (Cliente)**: Usa o protótipo para criar novos objetos através da clonagem

## Vantagens

1. **Reduz custo de criação**: Evita criar objetos complexos do zero
2. **Flexibilidade**: Permite criar objetos em tempo de execução
3. **Isolamento**: Cliente não precisa conhecer as classes concretas
4. **Cópia profunda**: Garante independência entre o objeto original e o clone

## Exemplo de Uso

Neste exemplo, a classe `Pessoa` herda de `Prototype` e implementa o método `clone()` que utiliza cópia profunda (`deepcopy`) para garantir que objetos aninhados (como dicionários) sejam completamente independentes.

### Código

```python
import copy

class Prototype:
    def clone(self):
        # usa cópia profunda
        return copy.deepcopy(self)

class Pessoa(Prototype):
    def __init__(self, nome, idade, endereco):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco

    def __str__(self):
        return f"Pessoa(nome={self._nome}, idade={self._idade}, endereco={self._endereco})"
```

### Execução

```python
original = Pessoa("Alice", 30, {"cidade": "Salvador", "cep": "40000"})
pessoaClone = original.clone()
pessoaClone._nome = "Bob"
pessoaClone._endereco["cidade"] = "Vitória"
print(original)       # Pessoa(nome=Alice, idade=30, endereco={'cidade': 'Salvador', …})
print(pessoaClone)   # Pessoa(nome=Bob, idade=30, endereco={'cidade': 'Vitória', …})
```

## Observações Importantes

- **Cópia Profunda vs Cópia Rasa**: 
  - `copy.deepcopy()` cria uma cópia completa e independente de todos os objetos aninhados
  - `copy.copy()` criaria apenas uma cópia rasa, onde objetos aninhados ainda seriam referências compartilhadas

- **Independência**: Com cópia profunda, modificações no clone não afetam o objeto original e vice-versa

## Quando Usar

- Quando a criação de objetos é custosa ou complexa
- Quando você precisa criar muitas instâncias similares
- Quando quer evitar subclasses para criar objetos
- Quando precisa criar objetos em tempo de execução com configurações dinâmicas

## Quando NÃO Usar

- Quando objetos são simples e fáceis de criar
- Quando há poucas variações de objetos
- Quando a clonagem pode ser mais custosa que a criação direta

