# Módulo 3 - Programação Orientada a Objetos

Este módulo apresenta os conceitos fundamentais de Programação Orientada a Objetos (POO) em Python, demonstrando como aplicar esses princípios na construção de aplicações backend robustas e organizadas.

## 📚 Conceitos Abordados

### Pilares da POO
- **Encapsulamento**: Agrupamento de dados e métodos que operam sobre esses dados
- **Abstração**: Simplificação da complexidade através de interfaces claras
- **Herança**: Reutilização de código através de hierarquias de classes
- **Polimorfismo**: Capacidade de objetos diferentes responderem à mesma interface

### Padrões de Projeto
Este módulo demonstra a aplicação prática de padrões de projeto fundamentais:
- **DAO (Data Access Object)**: Camada de abstração para acesso a dados
- **Service Layer**: Lógica de negócio separada da camada de acesso a dados
- **Repository Pattern**: Abstração da persistência de dados

## 📁 Projeto: SQLite + POO

O módulo inclui um projeto completo que demonstra a aplicação de POO junto com persistência de dados em SQLite.

### Estrutura do Projeto

```
SQLite+POO/
├── bd/
│   └── database.py           # Gerenciamento de conexões com banco
├── model/
│   ├── pessoa.py             # Modelo da entidade Pessoa
│   └── categoria.py          # Modelo da entidade Categoria
├── dao/
│   ├── pessoa_dao.py         # DAO para operações de Pessoa
│   └── categoria_dao.py     # DAO para operações de Categoria
├── app/
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── pessoa_service.py    # Lógica de negócio para Pessoa
│   └── categoria_service.py # Lógica de negócio para Categoria
└── test/
    ├── exemplo_uso_orm.py   # Exemplos de uso
    └── teste_projeto.py     # Testes do projeto
```

### Arquitetura em Camadas

1. **Model Layer**: Classes que representam as entidades do domínio
2. **DAO Layer**: Responsável pelo acesso e manipulação dos dados no banco
3. **Service Layer**: Contém a lógica de negócio da aplicação
4. **Application Layer**: Interface e orquestração das funcionalidades

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Criar classes e objetos em Python
- Implementar encapsulamento usando propriedades e métodos privados
- Aplicar herança e polimorfismo
- Separar responsabilidades usando camadas (Model, DAO, Service)
- Implementar o padrão DAO para acesso a dados
- Construir aplicações escaláveis e manuteníveis usando POO
- Entender a importância da separação de concerns

## 🔧 Tecnologias e Conceitos

### Classes e Objetos
- Definição de classes
- Métodos especiais (`__init__`, `__str__`, `__repr__`)
- Propriedades e métodos getter/setter
- Métodos de classe e métodos estáticos

### Relacionamentos
- Associação
- Agregação
- Composição
- Herança

### Organização de Código
- Módulos e pacotes
- Importação e organização de classes
- Separação de responsabilidades

## 🚀 Como Utilizar Este Módulo

### Explorando o Projeto SQLite+POO

1. **Entenda a estrutura**:
   - Leia o [README.md do projeto](./SQLite+POO/README.md) para detalhes completos
   - Explore cada camada começando pelos modelos

2. **Execute os exemplos**:
   ```bash
   cd SQLite+POO
   python3 test/exemplo_uso_orm.py
   ```

3. **Execute os testes**:
   ```bash
   python3 test/teste_projeto.py
   ```

4. **Rode a aplicação principal**:
   ```bash
   python3 app/main.py
   ```

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conhecimento sólido dos conceitos do Módulo 1 (Lógica de Programação)
- Familiaridade com bancos de dados (Módulo 2)
- Compreensão básica de SQL

## 📖 Recursos Adicionais

- [Documentação Python - Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- [Design Patterns em Python](https://refactoring.guru/design-patterns/python)
- [Clean Code Principles](https://www.python.org/dev/peps/pep-0008/)

## 🏗️ Boas Práticas de POO

1. **Single Responsibility Principle**: Cada classe deve ter uma única responsabilidade
2. **Encapsulamento**: Proteja os atributos usando propriedades adequadas
3. **Nomes descritivos**: Use nomes claros para classes, métodos e variáveis
4. **Documentação**: Documente classes e métodos usando docstrings
5. **Separação de concerns**: Separe lógica de negócio de acesso a dados
6. **Reutilização**: Evite duplicação de código usando herança e composição

## 💡 Dicas de Aprendizado

- **Analise o código existente**: Estude a estrutura do projeto SQLite+POO
- **Implemente variações**: Crie novas entidades seguindo o mesmo padrão
- **Refatore código procedural**: Pratique convertendo código funcional para POO
- **Pense em abstrações**: Identifique padrões e crie classes que os representem

## ⚠️ Importante

A Programação Orientada a Objetos é fundamental para desenvolvimento backend escalável. Este módulo estabelece as bases para padrões mais avançados que serão vistos no Módulo 4 (Padrões de Desenvolvimento de Software).

