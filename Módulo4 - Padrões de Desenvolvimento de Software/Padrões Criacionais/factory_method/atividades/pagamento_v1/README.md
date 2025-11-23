# Sistema de Pagamento - Padrões de Projet Simple Factory e Factory Method

Este projeto demonstra a implementação do padrão **Factory Method** para um sistema de processamento de pagamentos, permitindo criar diferentes tipos de pagamento (PIX, Cartão, Boleto) através de fábricas especializadas (Online e Offline).

## 📋 Sobre o Projeto

O sistema permite processar pagamentos de diferentes formas, com fábricas que determinam quais métodos de pagamento estão disponíveis conforme o contexto (online ou offline). Cada fábrica implementa suas próprias regras de negócio sobre quais tipos de pagamento são permitidos.

## 🏗️ Estrutura do Projeto

```
pagamento_v1/
├── pagamento.py              # Hierarquia de classes de pagamento
├── fabrica_abstrata.py       # Classe abstrata da fábrica
├── fabricas_concretas.py     # Implementações concretas das fábricas
├── main.py                   # Exemplo de uso
└── README.md                 # Este arquivo
```

## 📚 Componentes

### 1. Hierarquia de Pagamentos (`pagamento.py`)

Define a classe abstrata `Pagamento` e suas implementações concretas:

- **`Pagamento`** (classe abstrata): Define o contrato para processamento de pagamentos
- **`PagamentoPix`**: Implementa pagamento via PIX
- **`PagamentoCartao`**: Implementa pagamento via cartão
- **`PagamentoBoleto`**: Implementa pagamento via boleto

### 2. Fábrica Abstrata (`fabrica_abstrata.py`)

- **`PagamentoFactory`**: Classe abstrata que define:
  - `criarPagamento(tipo: str)`: Método abstrato para criar instâncias de pagamento
  - `realizarPagamento(tipo: str, valor: float)`: Método template que orquestra a criação e execução do pagamento

### 3. Fábricas Concretas (`fabricas_concretas.py`)

Implementações específicas da fábrica abstrata:

- **`FactoryPagamentoOnline`**: 
  - Suporta: PIX e Cartão
  - Não suporta: Boleto
  
- **`FactoryPagamentoOffline`**: 
  - Suporta: Boleto e Cartão
  - Não suporta: PIX

> **Nota**: Nesta versão (v1), as fábricas concretas utilizam o padrão Simple Factory internamente para criar os objetos de pagamento. A versão 2 implementa o Factory Method também nesta camada.

## 🎯 Padrão Factory Method

O **Factory Method** é um padrão criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados.

### Vantagens

- ✅ **Separação de responsabilidades**: A criação de objetos é isolada do código cliente
- ✅ **Extensibilidade**: Fácil adicionar novos tipos de pagamento ou novas fábricas
- ✅ **Flexibilidade**: Cada fábrica pode ter suas próprias regras de criação
- ✅ **Manutenibilidade**: Mudanças nas regras de criação ficam isoladas nas fábricas

## 🚀 Como Usar

### Executando o exemplo

```bash
python main.py
```

### Exemplo de código

```python
from fabricas_concretas import FactoryPagamentoOnline, FactoryPagamentoOffline
from fabrica_abstrata import PagamentoFactory

def cliente_pagamento(factory: PagamentoFactory, tipo: str, valor: float):
    factory.realizarPagamento(tipo, valor)

# Fábrica online
factoryOnline = FactoryPagamentoOnline()
cliente_pagamento(factoryOnline, "pix", 120.0)
cliente_pagamento(factoryOnline, "cartao", 300.0)

# Fábrica offline
factoryOffline = FactoryPagamentoOffline()
cliente_pagamento(factoryOffline, "boleto", 500.0)
cliente_pagamento(factoryOffline, "cartao", 75.25)
```

### Saída esperada

```
Pagamento online. Enviando PIX para valor de R$ 120.00.
Pagamento online. Pagando R$ 300.00 com cartão.
Pagamento offline. Gerando boleto para R$ 500.00.
Pagamento offline. Pagando R$ 75.25 com cartão.
```

## ⚠️ Tratamento de Erros

O sistema valida os tipos de pagamento permitidos por cada fábrica:

- Tentar usar `boleto` com `FactoryPagamentoOnline` resultará em `ValueError`
- Tentar usar `pix` com `FactoryPagamentoOffline` resultará em `ValueError`

Exemplo de erro:
```python
factoryOnline = FactoryPagamentoOnline()
factoryOnline.realizarPagamento("boleto", 100.0)  # ValueError: Pagamento online não suporta tipo: boleto
```

## 🔄 Diferenças entre Versões

- **v1**: Fábricas concretas usam Simple Factory internamente
- **v2**: Fábricas concretas implementam Factory Method completo

## 📝 Requisitos

- Python 3.6+

## 🎓 Conceitos Demonstrados

- Padrão Factory Method
- Classes abstratas (`ABC`, `@abstractmethod`)
- Método Template
- Polimorfismo
- Inversão de dependência

## 📖 Referências

Este projeto faz parte do estudo de **Padrões Criacionais** do Módulo 4 - Padrões de Desenvolvimento de Software.

