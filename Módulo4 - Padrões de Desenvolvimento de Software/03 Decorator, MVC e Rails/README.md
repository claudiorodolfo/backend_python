# 03 - Decorator, MVC e Rails

Este módulo apresenta o padrão Decorator (estrutural) e o padrão MVC (arquitetural), que são fundamentais no desenvolvimento de software.

## 📚 Conteúdo

### 1. Decorator - Conceito (`01_decorator_conceito.py`)
- Definição e motivação do Decorator
- Diferença entre herança e composição via decorator
- Vantagens e desvantagens
- Implementações:
  - Decorator clássico estrutural
  - Decorator para processamento de texto
  - Decorator funcional (Python nativo)
  - Decorator para streaming de dados

### 2. Decorator - Exemplos Práticos (`02_decorator_exemplos.py`)
- Sistema de permissões e autenticação
- Pipeline de processamento de dados
- Decorators funcionais (performance, retry, rate limit)
- Sistema de notificações com diferentes canais
- Wrapper para APIs externas

### 3. MVC - Conceito (`03_mvc_conceito.py`)
- O que é MVC e sua importância
- Componentes Model, View e Controller
- Responsabilidades de cada componente
- Como padrões facilitam organização
- Implementações:
  - MVC básico
  - MVC com múltiplas views
  - MVC para sistema de tarefas
  - MVC simplificado para API

### 4. MVC - Exemplos Práticos (`04_mvc_exemplos.py`)
- Sistema de gerenciamento de blog
- Sistema de autenticação
- API REST com MVC
- Aplicação de gerenciamento de contatos

### 5. Exercícios (`05_exercicios_decorator_mvc.py`)
- **Decorator:**
  - Exercício 1: Decorator para funcionalidades de carro
  - Exercício 2: Decorator para processamento de imagens
  - Exercício 3: Decorator funcional para validação
- **MVC:**
  - Exercício 4: MVC para sistema de biblioteca
  - Exercício 5: MVC para sistema de agenda
  - Exercício 6: MVC para API de produtos
- **Análise:**
  - Exercício 7: Identificar e aplicar MVC em diferentes cenários

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Entender a diferença entre herança e composição via decorator
- Implementar decorators estruturais e funcionais
- Identificar quando usar decorators
- Compreender a arquitetura MVC
- Implementar MVC em aplicações Python
- Separar responsabilidades entre Model, View e Controller
- Reconhecer MVC em frameworks web

## 📖 Como Estudar

1. **Decorator primeiro:**
   - Leia `01_decorator_conceito.py` para entender a teoria
   - Analise `02_decorator_exemplos.py` para ver aplicações reais
   - Pratique os exercícios 1-3

2. **MVC depois:**
   - Leia `03_mvc_conceito.py` para entender a arquitetura
   - Explore `04_mvc_exemplos.py` para casos práticos
   - Pratique os exercícios 4-7

3. **Integração:**
   - Veja como decorators podem melhorar views
   - Entenda como MVC organiza código complexo

## 💡 Dicas Importantes

### Decorator
- Use quando precisa adicionar funcionalidades dinamicamente
- Ideal para evitar explosão de subclasses
- Python tem suporte nativo a decorators (@decorator)
- Pode ser usado estruturalmente ou funcionalmente
- Ordem dos decorators pode importar

### MVC
- **Model:** Lógica de negócio e dados (não deve conhecer View)
- **View:** Apresentação (não deve conter lógica de negócio)
- **Controller:** Coordenação (processa entrada, atualiza Model, escolhe View)
- Use Observer para Model notificar View sobre mudanças
- Mantenha componentes desacoplados

## 🔗 Relação entre Padrões

- **Decorator + MVC:** Decorators podem melhorar Views (formatação, cache)
- **Observer + MVC:** Fundamental - Model notifica View via Observer
- **Factory + MVC:** Factories podem criar Controllers e Views
- **Singleton + MVC:** Configurações e serviços globais

## 🌐 MVC em Frameworks Web

### Django
- Model: ORM (classes que herdam de models.Model)
- View: Templates (HTML)
- Controller: Views (funções ou classes que processam requisições)

### Flask
- Model: Classes de dados
- View: Templates Jinja2
- Controller: Rotas (@app.route)

### Rails (Ruby)
- Model: ActiveRecord (similar ao Django)
- View: ERB templates
- Controller: Classes Controller

## 🔗 Próximos Passos

Depois de dominar Decorator e MVC:
- Aplicar em projetos reais
- Estudar frameworks web (Django, Flask)
- Explorar padrões arquiteturais avançados (Repository, Service Layer)
- Integrar múltiplos padrões em soluções complexas

## ⚠️ Importante

### Não Force Padrões
- Use MVC quando precisa de separação clara de responsabilidades
- Não use MVC em projetos muito simples
- Decorators são úteis, mas podem tornar código difícil de depurar
- Mantenha código simples quando possível

### Boas Práticas MVC
- Model não deve conhecer View ou Controller
- View não deve conter lógica de negócio
- Controller deve ser fino (delegar para Model)
- Use Observer para comunicação Model → View

