# 01 - Introdução e Singleton

Este módulo apresenta a introdução aos padrões de projeto e o padrão Singleton.

## 📚 Conteúdo

### 1. Introdução aos Padrões de Projeto (`01_introducao_padroes.py`)
- O que são padrões de projeto (design patterns)
- Benefícios do uso de padrões
- Classificação: Criacionais, Estruturais e Comportamentais
- Exemplos práticos de aplicação

### 2. Conceito do Singleton (`02_singleton_conceito.py`)
- Conceito e finalidade do Singleton
- Vantagens e armadilhas
- Implementações em Python:
  - Singleton básico
  - Singleton com decorator
  - Singleton com metaclass
  - Singleton thread-safe

### 3. Casos Práticos de Uso (`03_singleton_casos_uso.py`)
- Gerenciador de conexão de banco de dados
- Sistema de logging global
- Cache de aplicação
- Gerenciador de configurações
- Exemplo de aplicação usando múltiplos Singletons

### 4. Exercícios (`04_exercicios_singleton.py`)
- Exercício 1: Singleton simples (ContadorGlobal)
- Exercício 2: Singleton com decorator
- Exercício 3: Singleton thread-safe (FileManager)
- Exercício 4: Singleton para gerenciamento de sessões
- Exercício 5: Análise crítica de quando usar Singleton

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Entender o que são padrões de projeto e sua importância
- Classificar padrões em criacionais, estruturais e comportamentais
- Implementar o padrão Singleton de diferentes formas
- Identificar quando usar e quando não usar Singleton
- Reconhecer as armadilhas do Singleton

## 📖 Como Estudar

1. **Comece pela introdução**: Leia `01_introducao_padroes.py` para entender o contexto
2. **Estude o conceito**: Analise `02_singleton_conceito.py` para ver diferentes implementações
3. **Veja casos reais**: Explore `03_singleton_casos_uso.py` para entender aplicações práticas
4. **Pratique**: Resolva os exercícios em `04_exercicios_singleton.py`

## ⚠️ Importante

**Singleton não é sempre a solução!**
- Use quando realmente precisa de uma única instância
- Considere alternativas como dependency injection
- Evite usar Singleton apenas por conveniência
- Lembre-se dos problemas de testabilidade

## 🔗 Próximos Passos

Depois de dominar Singleton, continue para:
- **02 Factory Method e Observer**: Padrões para criação de objetos e comunicação entre componentes

