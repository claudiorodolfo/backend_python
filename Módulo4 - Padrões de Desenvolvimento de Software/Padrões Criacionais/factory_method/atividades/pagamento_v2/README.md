# Sistema de Pagamento - Padrão de Projeto Factory Method 

Este projeto demonstra a implementação do padrão **Factory Method** para gerenciar diferentes tipos de pagamento em um sistema, com fábricas especializadas para contextos online e offline.

## 📋 Sobre o Projeto

O sistema permite processar pagamentos através de diferentes canais (online e offline) e diferentes métodos de pagamento (PIX, Cartão e Boleto), utilizando o padrão Factory Method para criar instâncias apropriadas de pagamento através de fábricas concretas especializadas.

## 🎯 Padrão de Projeto

**Factory Method Pattern**: Um padrão criacional que define uma interface para criar objetos, mas permite que as subclasses decidam qual classe instanciar. O Factory Method permite que uma classe delegue a criação de objetos para suas subclasses, promovendo maior flexibilidade e extensibilidade.

## 📁 Estrutura do Projeto

```
pagamento_v2/
├── pagamento.py          # Classes abstratas e concretas de pagamento
├── fabrica_abstrata.py   # Interface abstrata da fábrica
├── fabricas_concretas.py # Implementações concretas da fábrica
├── main.py              # Exemplos de uso
└── README.md            # Documentação do projeto
```

## 🔧 Componentes

### `pagamento.py`
Define a hierarquia de classes de pagamento:
- **`Pagamento`**: Classe abstrata base com método abstrato `pagar()`
- **`PagamentoCartao`**: Implementação para pagamento com cartão
- **`PagamentoBoleto`**: Implementação para pagamento com boleto
- **`PagamentoPix`**: Implementação para pagamento via PIX

### `fabrica_abstrata.py`
Contém a classe abstrata **`PagamentoFactory`** que define a interface:
- `criarPix() -> Pagamento`: Método abstrato para criar pagamento PIX
- `criarCartao() -> Pagamento`: Método abstrato para criar pagamento com cartão
- `criarBoleto() -> Pagamento`: Método abstrato para criar pagamento com boleto

### `fabricas_concretas.py`
Contém as implementações concretas da fábrica:

#### `FactoryPagamentoOnline`
Fábrica especializada para pagamentos online:
- ✅ Suporta: PIX e Cartão
- ❌ Não suporta: Boleto (lança `ValueError`)

#### `FactoryPagamentoOffline`
Fábrica especializada para pagamentos offline:
- ✅ Suporta: Cartão e Boleto
- ❌ Não suporta: PIX (lança `ValueError`)

### `main.py`
Demonstra o uso das fábricas concretas com exemplos práticos.

## 🚀 Como Usar

### Executando o projeto

```bash
python main.py
```

### Exemplo de uso programático

```python
from fabricas_concretas import FactoryPagamentoOnline, FactoryPagamentoOffline

# Fábrica para pagamentos online
factory_online = FactoryPagamentoOnline()
pagamento_pix = factory_online.criarPix()
pagamento_pix.pagar(120.0)

pagamento_cartao_online = factory_online.criarCartao()
pagamento_cartao_online.pagar(300.0)

# Fábrica para pagamentos offline
factory_offline = FactoryPagamentoOffline()
pagamento_boleto = factory_offline.criarBoleto()
pagamento_boleto.pagar(500.0)

pagamento_cartao_offline = factory_offline.criarCartao()
pagamento_cartao_offline.pagar(75.25)
```

## 📊 Canais e Tipos Suportados

| Canal  | Tipos Suportados        | Fábrica Concreta           |
|--------|-------------------------|----------------------------|
| Online | PIX, Cartão             | `FactoryPagamentoOnline`   |
| Offline| Boleto, Cartão          | `FactoryPagamentoOffline`  |

## ⚠️ Tratamento de Erros

As fábricas concretas lançam `ValueError` quando:
- Tentativa de criar boleto na fábrica online
- Tentativa de criar PIX na fábrica offline

Exemplos:
```python
factory_online = FactoryPagamentoOnline()

# Isso lançará ValueError
factory_online.criarBoleto()  # Boleto não suportado online

factory_offline = FactoryPagamentoOffline()

# Isso lançará ValueError
factory_offline.criarPix()  # PIX não suportado offline
```

## 🎓 Objetivos de Aprendizado

- Compreender o padrão Factory Method
- Aprender a criar hierarquias de fábricas (abstrata e concretas)
- Entender como delegar a criação de objetos para subclasses
- Praticar polimorfismo e extensibilidade
- Diferenciar Factory Method de Simple Factory

## 🔄 Diferenças entre Factory Method e Simple Factory

### Simple Factory
- Uma única classe factory com métodos estáticos
- Lógica de criação centralizada em um único lugar
- Menos flexível para extensão

### Factory Method
- Classe abstrata define a interface
- Subclasses implementam a criação específica
- Mais flexível e extensível
- Segue o princípio Open/Closed (aberto para extensão, fechado para modificação)

## 📝 Vantagens do Factory Method

1. **Extensibilidade**: Fácil adicionar novos tipos de fábricas sem modificar código existente
2. **Separação de Responsabilidades**: Cada fábrica concreta conhece apenas seus tipos de pagamento
3. **Polimorfismo**: Cliente trabalha com a interface abstrata, não com implementações concretas
4. **Testabilidade**: Fácil criar mocks e stubs para testes

## 🔮 Possíveis Extensões

- Adicionar novas fábricas concretas (ex: `FactoryPagamentoInternacional`)
- Adicionar novos tipos de pagamento (ex: `PagamentoCriptomoeda`)
- Implementar validações adicionais nas fábricas
- Adicionar logging e monitoramento na criação de pagamentos

