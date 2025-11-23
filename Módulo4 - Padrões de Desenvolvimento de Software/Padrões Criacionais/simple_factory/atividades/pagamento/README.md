# Sistema de Pagamento -  Padrão de Projeto Simple Factory

Este projeto demonstra a implementação do padrão **Simple Factory** (Fábrica Simples) para gerenciar diferentes tipos de pagamento em um sistema.

## 📋 Sobre o Projeto

O sistema permite processar pagamentos através de diferentes canais (online e offline) e diferentes métodos de pagamento (PIX, Cartão e Boleto), utilizando o padrão Simple Factory para criar instâncias apropriadas de pagamento.

## 🎯 Padrão de Projeto

**Simple Factory Pattern**: Um padrão criacional que encapsula a lógica de criação de objetos em uma única classe (Factory), simplificando a criação de objetos relacionados sem expor a lógica de instanciação ao cliente.

## 📁 Estrutura do Projeto

```
pagamento/
├── pagamento.py      # Classes abstratas e concretas de pagamento
├── factory.py        # Factory para criação de instâncias de pagamento
├── main.py          # Exemplos de uso
└── README.md        # Documentação do projeto
```

## 🔧 Componentes

### `pagamento.py`
Define a hierarquia de classes de pagamento:
- **`Pagamento`**: Classe abstrata base com método `pagar()`
- **`PagamentoCartao`**: Implementação para pagamento com cartão
- **`PagamentoBoleto`**: Implementação para pagamento com boleto
- **`PagamentoPix`**: Implementação para pagamento via PIX

### `factory.py`
Contém a classe **`PagamentoFactory`** que:
- Recebe `canal` (online/offline) e `tipo` (pix/cartao/boleto)
- Retorna a instância apropriada de pagamento
- Valida combinações permitidas:
  - **Online**: PIX e Cartão
  - **Offline**: Boleto e Cartão

### `main.py`
Demonstra o uso do factory com exemplos práticos.

## 🚀 Como Usar

### Executando o projeto

```bash
python main.py
```

### Exemplo de uso programático

```python
from factory import PagamentoFactory

def realizar_pagamento(canal: str, tipo: str, valor: float):
    factory = PagamentoFactory()
    pagamento = factory.criarPagamento(canal, tipo)
    pagamento.pagar(valor)

# Exemplos
realizar_pagamento("online", "pix", 120.0)         # PIX online
realizar_pagamento("online", "cartao", 300.0)      # Cartão online
realizar_pagamento("offline", "boleto", 500.0)     # Boleto offline
realizar_pagamento("offline", "cartao", 75.25)     # Cartão offline
```

## 📊 Canais e Tipos Suportados

| Canal  | Tipos Suportados        |
|--------|-------------------------|
| Online | PIX, Cartão             |
| Offline| Boleto, Cartão          |

## ⚠️ Tratamento de Erros

O factory lança `ValueError` quando:
- O canal especificado não é reconhecido
- O tipo de pagamento não é suportado pelo canal selecionado

Exemplo:
```python
# Isso lançará ValueError
factory.criarPagamento("online", "boleto", 100.0)  # Boleto não suportado online
```

## 🎓 Objetivos de Aprendizado

- Compreender o padrão Simple Factory
- Aprender a encapsular lógica de criação de objetos
- Entender como simplificar a criação de objetos relacionados
- Praticar validação e tratamento de erros em factories

## 📝 Notas

- O padrão Simple Factory é útil quando há uma lógica de criação relativamente simples
- Para casos mais complexos, considere usar Factory Method ou Abstract Factory
- O factory centraliza a lógica de criação, facilitando manutenção e extensão

