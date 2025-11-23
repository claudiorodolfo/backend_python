# Abstract Factory Pattern

Este projeto demonstra a implementação do padrão **Abstract Factory** (Fábrica Abstrata) em Python, utilizando um exemplo prático de um sistema de delivery que cria famílias de produtos relacionados (comidas e bebidas).

## 📋 Sobre o Padrão

O **Abstract Factory** é um padrão de projeto criacional que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas. Este padrão é útil quando você precisa criar grupos de objetos que trabalham juntos e precisam ser consistentes entre si.

## 🏗️ Estrutura do Projeto

```
exemplo2/
├── main.py                          # Arquivo principal de demonstração
├── fabricas/
│   ├── abstract_factory.py          # Interface da fábrica abstrata
│   ├── pizzaria_factory.py          # Fábrica concreta para pizzaria
│   └── hamburgueria_factory.py      # Fábrica concreta para hamburgueria
├── comidas/
│   ├── comida.py                    # Interface abstrata de comida
│   ├── pizza.py                     # Implementação concreta de pizza
│   └── hamburguer.py                # Implementação concreta de hamburguer
└── bebidas/
    ├── bebida.py                    # Interface abstrata de bebida
    ├── refrigerante.py              # Implementação concreta de refrigerante
    └── milkshake.py                 # Implementação concreta de milkshake
```

## 🎯 Componentes do Padrão

### 1. Abstract Factory (Fábrica Abstrata)
- **`DeliveryFactory`**: Interface que define os métodos para criar produtos relacionados (comida e bebida)

### 2. Concrete Factories (Fábricas Concretas)
- **`PizzariaFactory`**: Cria produtos da família pizzaria (Pizza + Refrigerante)
- **`HamburgueriaFactory`**: Cria produtos da família hamburgueria (Hamburguer + Milkshake)

### 3. Abstract Products (Produtos Abstratos)
- **`Comida`**: Interface abstrata para produtos de comida
- **`Bebida`**: Interface abstrata para produtos de bebida

### 4. Concrete Products (Produtos Concretos)
- **`Pizza`**: Implementação concreta de comida
- **`Hamburguer`**: Implementação concreta de comida
- **`Refrigerante`**: Implementação concreta de bebida
- **`Milkshake`**: Implementação concreta de bebida

## 🚀 Como Executar

1. Navegue até o diretório do projeto:
```bash
cd "Módulo4 - Padrões de Desenvolvimento de Software/Criacionista/abstract_factory/exemplo2"
```

2. Execute o arquivo principal:
```bash
python main.py
```

3. Siga as instruções no terminal:
   - Digite o tipo de fábrica: `pizzaria` ou `hamburgueria`
   - Digite o ingrediente a ser removido

## 💡 Exemplo de Uso

```python
# Exemplo de uso programático
from fabricas.pizzaria_factory import PizzariaFactory
from fabricas.hamburgueria_factory import HamburgueriaFactory

# Criar uma fábrica de pizzaria
factory = PizzariaFactory()
comida = factory.criarComida()  # Retorna Pizza
bebida = factory.criarBebida()  # Retorna Refrigerante

# Criar uma fábrica de hamburgueria
factory = HamburgueriaFactory()
comida = factory.criarComida()   # Retorna Hamburguer
bebida = factory.criarBebida()  # Retorna Milkshake
```

## ✨ Benefícios do Padrão

1. **Consistência**: Garante que os produtos criados sejam compatíveis entre si
2. **Flexibilidade**: Facilita a adição de novas famílias de produtos
3. **Desacoplamento**: O código cliente não depende de classes concretas
4. **Extensibilidade**: Novas fábricas e produtos podem ser adicionados sem modificar código existente

## 🔄 Fluxo de Execução

1. O usuário escolhe o tipo de fábrica (pizzaria ou hamburgueria)
2. A fábrica correspondente é instanciada
3. A fábrica cria os produtos relacionados (comida + bebida)
4. Os produtos são utilizados através de suas interfaces abstratas

## 📚 Referências

- [Vídeo de Referência](https://www.youtube.com/watch?v=9gJYU28PHz4)
- Padrão de Projeto: Abstract Factory (Gang of Four)

## 🛠️ Tecnologias

- Python 3.x
- ABC (Abstract Base Classes) para interfaces abstratas

