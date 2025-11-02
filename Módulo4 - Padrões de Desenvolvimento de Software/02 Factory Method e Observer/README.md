# 02 - Factory Method e Observer

Este módulo apresenta dois padrões importantes: Factory Method (criacional) e Observer (comportamental).

## 📚 Conteúdo

### 1. Factory Method - Conceito (`01_factory_method_conceito.py`)
- Conceito do Factory Method
- Diferenças entre Factory Method e Simple Factory
- Vantagens e desvantagens
- Implementações básicas
- Exemplos com diferentes produtos

### 2. Factory Method - Exemplos Práticos (`02_factory_method_exemplos.py`)
- Factory para notificações (Email, SMS, Push)
- Factory para exportação de dados (CSV, JSON, Excel)
- Factory para estratégias de pagamento (Cartão, Boleto, PIX)
- Factory para autenticação (LDAP, OAuth, Database)
- Exemplo de sistema completo usando múltiplos factories

### 3. Observer - Conceito (`03_observer_conceito.py`)
- Conceito do Observer
- Quando utilizar Observer
- Uso em eventos e notificações
- Implementações:
  - Observer básico
  - Observer com eventos tipados
  - Observer com callbacks
  - Observer com filtros

### 4. Observer - Casos Práticos (`04_observer_casos_uso.py`)
- Sistema de notificações de usuário
- Monitoramento de mudanças em dados
- Sistema de cache invalidation
- Sistema de eventos de pedidos (E-commerce)
- Editor de texto com múltiplas visualizações

### 5. Exercícios (`05_exercicios_factory_observer.py`)
- **Factory Method:**
  - Exercício 1: Factory para formatos de arquivo
  - Exercício 2: Factory para estratégias de desconto
  - Exercício 3: Factory para conexões de API
- **Observer:**
  - Exercício 4: Sistema de monitoramento de temperatura
  - Exercício 5: Sistema de eventos de chat
  - Exercício 6: Sistema de pedidos com Observer
- **Análise:**
  - Exercício 7: Análise comparativa dos padrões

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Diferenciar Factory Method de Simple Factory
- Implementar Factory Method para criar objetos flexivelmente
- Identificar quando usar Factory Method
- Implementar o padrão Observer
- Reconhecer casos de uso para Observer
- Combinar Factory Method e Observer em soluções práticas

## 📖 Como Estudar

1. **Factory Method primeiro:**
   - Leia `01_factory_method_conceito.py` para entender a teoria
   - Analise `02_factory_method_exemplos.py` para ver aplicações reais
   - Pratique os exercícios 1-3

2. **Observer depois:**
   - Leia `03_observer_conceito.py` para entender o padrão
   - Explore `04_observer_casos_uso.py` para casos práticos
   - Pratique os exercícios 4-6

3. **Integração:**
   - Veja como os padrões podem trabalhar juntos
   - Complete o exercício de análise comparativa

## 💡 Dicas Importantes

### Factory Method
- Use quando precisa criar objetos sem especificar classes exatas
- Ideal para quando há múltiplos tipos relacionados de objetos
- Segue o princípio aberto/fechado (fácil adicionar novos tipos)
- Não use quando há apenas um tipo de objeto simples

### Observer
- Use quando precisa notificar múltiplos objetos sobre mudanças
- Ideal para sistemas de eventos e notificações
- Mantém baixo acoplamento entre componentes
- Cuidado com cascatas de notificações não intencionais

## 🔗 Relação entre Padrões

- **Factory Method + Observer:** Factories podem criar observers, observers podem usar factories
- **Observer + MVC:** Padrão fundamental no MVC (Model notifica View)
- **Factory Method + Strategy:** Factories podem criar estratégias diferentes

## 🔗 Próximos Passos

Depois de dominar Factory Method e Observer, continue para:
- **03 Decorator, MVC e Rails**: Padrões estruturais e arquiteturais

