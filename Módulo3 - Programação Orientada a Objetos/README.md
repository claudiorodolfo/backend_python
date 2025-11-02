# Módulo 3 - Programação Orientada a Objetos

Este módulo apresenta os conceitos fundamentais de Programação Orientada a Objetos (POO) em Python, demonstrando como aplicar esses princípios na construção de aplicações backend robustas, organizadas e manuteníveis. Através de um projeto prático completo, você aprenderá a separar responsabilidades, criar abstrações e construir sistemas escaláveis.

## 📚 Conteúdo do Módulo

Este módulo está estruturado para ensinar POO através da prática, combinando teoria com um projeto real que integra conceitos de orientação a objetos com persistência de dados.

### 1. Fundamentos de POO
Os pilares fundamentais da programação orientada a objetos aplicados em Python.

**Pilares da POO:**
- **Encapsulamento**: Agrupamento de dados (atributos) e métodos que operam sobre esses dados em uma unidade coesa chamada classe
- **Abstração**: Simplificação da complexidade através de interfaces claras, escondendo detalhes de implementação
- **Herança**: Reutilização de código através de hierarquias de classes, permitindo especialização
- **Polimorfismo**: Capacidade de objetos diferentes responderem à mesma interface de formas diferentes

**Conceitos abordados:**
- Definição de classes e criação de objetos (instâncias)
- Métodos especiais (`__init__`, `__str__`, `__repr__`, `__eq__`, etc.)
- Propriedades e métodos getter/setter
- Métodos de classe (`@classmethod`) e métodos estáticos (`@staticmethod`)
- Atributos de classe vs atributos de instância
- Visibilidade e convenções (público, privado, protegido)
- Documentação com docstrings

### 2. Relacionamentos entre Classes
Como classes se relacionam e interagem em um sistema orientado a objetos.

**Tipos de relacionamentos:**
- **Associação**: Relacionamento fraco onde uma classe usa outra
- **Agregação**: Relacionamento "tem-um" onde o objeto agregado pode existir independentemente
- **Composição**: Relacionamento "parte-de" onde o objeto composto não pode existir sem o componente
- **Herança**: Relacionamento "é-um" onde uma classe especializa outra

**Conceitos abordados:**
- Composição de objetos
- Relacionamentos um-para-muitos e muitos-para-muitos
- Uso de objetos como atributos de outros objetos
- Hierarquias de classes e herança múltipla (quando necessário)

### 3. Organização de Código e Padrões
Estruturação de projetos Python usando POO e aplicação de padrões de projeto fundamentais.

**Conceitos abordados:**
- Módulos e pacotes em Python
- Importação e organização de classes
- Separação de responsabilidades (Separation of Concerns)
- Organização em camadas (layered architecture)

**Padrões de Projeto demonstrados:**
- **DAO (Data Access Object)**: Camada de abstração para acesso a dados, isolando a lógica de persistência
- **Service Layer**: Camada de serviços que contém a lógica de negócio, orquestrando chamadas aos DAOs
- **Repository Pattern**: Abstração da persistência de dados através de interfaces claras

## 📁 Projeto Prático: SQLite + POO

O módulo inclui um projeto completo que demonstra a aplicação prática de POO junto com persistência de dados em SQLite. Este projeto serve como exemplo de como estruturar uma aplicação backend real usando boas práticas.

### Estrutura do Projeto

```
SQLite+POO/
├── bd/
│   └── database.py           # Gerenciamento de conexões com banco (Singleton)
├── model/
│   ├── pessoa.py             # Modelo da entidade Pessoa
│   └── categoria.py          # Modelo da entidade Categoria
├── dao/
│   ├── pessoa_dao.py         # DAO para operações de Pessoa no banco
│   └── categoria_dao.py      # DAO para operações de Categoria no banco
├── app/
│   ├── main.py              # Ponto de entrada da aplicação (menu principal)
│   ├── pessoa_service.py    # Lógica de negócio e interface para Pessoa
│   └── categoria_service.py # Lógica de negócio e interface para Categoria
└── test/
    ├── exemplo_uso_orm.py   # Exemplos de uso das classes
    └── teste_projeto.py     # Testes automatizados do projeto
```

### Arquitetura em Camadas

O projeto demonstra uma arquitetura em camadas, separando responsabilidades:

1. **Model Layer** (`model/`): Classes que representam as entidades do domínio
   - Encapsulam dados e comportamentos básicos
   - Validações simples
   - Representação de relacionamentos

2. **DAO Layer** (`dao/`): Responsável pelo acesso e manipulação dos dados no banco
   - Abstrai operações SQL
   - Implementa CRUD completo
   - Gerencia conversão entre objetos Python e dados do banco

3. **Service Layer** (`app/`): Contém a lógica de negócio da aplicação
   - Orquestra chamadas aos DAOs
   - Implementa regras de negócio complexas
   - Fornece interfaces para interação com usuário

4. **Application Layer** (`app/main.py`): Interface e orquestração das funcionalidades
   - Menu principal
   - Coordenação entre serviços
   - Fluxo de navegação

### Entidades do Domínio

**Categoria:**
- Representa uma categoria de pessoas
- Atributos: `id`, `nome`
- Relacionamento: Uma categoria pode ter múltiplas pessoas

**Pessoa:**
- Representa uma pessoa no sistema
- Atributos: `id`, `nome`, `email`, `idade`, `altura`, `peso`, `data_nascimento`, `ativo`, `observacoes`, `telefone`, `momento_cadastro`
- Relacionamento: Pertence a uma categoria (Many-to-One)
- Validações: email único, idade entre 0-120, etc.

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Criar classes e objetos em Python de forma eficiente
- Implementar encapsulamento usando propriedades e métodos privados (convenção `_` e `__`)
- Aplicar herança e polimorfismo em situações práticas
- Separar responsabilidades usando camadas (Model, DAO, Service)
- Implementar o padrão DAO para acesso a dados de forma desacoplada
- Construir aplicações escaláveis e manuteníveis usando POO
- Entender a importância da separação de concerns (separação de preocupações)
- Organizar código em módulos e pacotes Python
- Documentar classes e métodos usando docstrings
- Criar e utilizar relacionamentos entre classes (composição, agregação, herança)
- Aplicar princípios SOLID na prática (especialmente Single Responsibility)

## 🔧 Tecnologias e Conceitos

### Classes e Objetos em Python
- **Definição de classes**: Sintaxe `class NomeClasse:`
- **Métodos especiais**: 
  - `__init__()`: Construtor
  - `__str__()`: Representação legível do objeto
  - `__repr__()`: Representação técnica do objeto
  - `__eq__()`: Comparação de igualdade
  - `__hash__()`: Para uso em conjuntos e dicionários
- **Propriedades**: Uso de `@property` para getters e setters
- **Métodos de classe**: `@classmethod` para métodos relacionados à classe
- **Métodos estáticos**: `@staticmethod` para funções utilitárias
- **Visibilidade**: Convenções de naming (`_privado`, `__muito_privado`)

### Relacionamentos entre Objetos
- **Composição**: Objeto como atributo de outro objeto
- **Agregação**: Objeto referenciado por outro objeto
- **Herança**: Classes que especializam outras classes
- **Polimorfismo**: Objetos diferentes respondendo à mesma interface

### Organização de Código
- **Módulos**: Arquivos `.py` contendo código relacionado
- **Pacotes**: Diretórios contendo módulos (com `__init__.py`)
- **Importação**: `import`, `from ... import`, `import ... as`
- **Namespaces**: Organização de nomes e evitar conflitos
- **Separação de responsabilidades**: Cada módulo/pacote tem uma função específica

### Padrões de Projeto Aplicados
- **DAO Pattern**: Abstração do acesso a dados
- **Service Layer**: Isolamento da lógica de negócio
- **Repository Pattern**: Interface unificada para persistência
- **Singleton Pattern**: Para gerenciamento de conexão com banco

## 🚀 Como Utilizar Este Módulo

### Ordem Recomendada de Estudo

1. **Estude os fundamentos**: Revise conceitos de classes, objetos, encapsulamento
2. **Explore a estrutura do projeto**: Entenda a organização em camadas
3. **Analise os modelos**: Comece pelos arquivos em `model/` para entender as entidades
4. **Estude os DAOs**: Veja como a persistência é abstraída em `dao/`
5. **Explore os serviços**: Entenda a lógica de negócio em `app/`
6. **Execute e modifique**: Teste o projeto e faça suas próprias modificações

### Explorando o Projeto SQLite+POO

#### 1. Entenda a Estrutura

```bash
# Navegue até o diretório do projeto
cd "Módulo3 - Programação Orientada a Objetos/SQLite+POO"

# Leia o README específico do projeto
cat README.md
```

Explore cada camada começando pelos modelos em `model/`, depois os DAOs em `dao/`, e finalmente os serviços em `app/`.

#### 2. Execute os Exemplos

O projeto inclui exemplos práticos de uso:

```bash
cd SQLite+POO
python3 test/exemplo_uso_orm.py
```

Este script demonstra:
- Criação de objetos
- Persistência através de DAOs
- Consultas e busca de dados
- Atualização e exclusão
- Relacionamentos entre objetos

#### 3. Execute os Testes

O projeto inclui uma suite de testes automatizados:

```bash
python3 test/teste_projeto.py
```

Os testes verificam:
- Operações CRUD de Categoria
- Operações CRUD de Pessoa
- Integridade referencial e constraints
- Validações de dados

#### 4. Execute a Aplicação Principal

Rode a aplicação interativa completa:

```bash
python3 app/main.py
```

O sistema oferece um menu que permite:
- Gerenciar Categorias (criar, listar, buscar, atualizar, deletar)
- Gerenciar Pessoas (criar, listar, buscar, atualizar, deletar)
- Navegação entre módulos

#### 5. Explore os Serviços Individuais

Execute os serviços separadamente:

```bash
# Gerenciar pessoas
python3 app/pessoa_service.py

# Gerenciar categorias
python3 app/categoria_service.py
```

## 📋 Pré-requisitos

- Python 3.7 ou superior instalado
- Conhecimento sólido dos conceitos do Módulo 1 (Lógica de Programação), especialmente:
  - Funções e escopo de variáveis
  - Estruturas de dados (listas, dicionários)
  - Tratamento de exceções
  - Trabalho com arquivos
- Familiaridade com bancos de dados (Módulo 2)
  - Entendimento básico de SQL
  - Conceito de relacionamentos entre tabelas
  - Operações CRUD

## 📖 Recursos Adicionais

### Documentação e Tutoriais
- [Documentação Python - Classes](https://docs.python.org/pt-br/3/tutorial/classes.html) - Tutorial oficial sobre classes
- [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/) - Guia completo de OOP em Python
- [Python.org - Classes e Objetos](https://docs.python.org/pt-br/3/tutorial/classes.html) - Documentação oficial
- [Design Patterns em Python](https://refactoring.guru/design-patterns/python) - Padrões de projeto explicados

### Livros Recomendados
- "Python Tricks: The Book" - Dan Bader
- "Fluent Python" - Luciano Ramalho
- "Clean Code" - Robert C. Martin (capítulos sobre POO)

### Princípios e Boas Práticas
- [SOLID Principles in Python](https://realpython.com/solid-principles-python/) - Aplicação de SOLID
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/) - Convenções de código Python
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) - Arquitetura limpa

## 🏗️ Boas Práticas de POO

### 1. Single Responsibility Principle
Cada classe deve ter uma única responsabilidade:
- ✅ **Bom**: Classe `Pessoa` apenas representa uma pessoa
- ❌ **Ruim**: Classe `Pessoa` que também salva no banco e faz validações complexas

### 2. Encapsulamento
Proteja os atributos usando propriedades adequadas:
- Use `@property` para acesso controlado
- Use convenções de naming (`_privado`) para indicar atributos privados
- Documente interfaces públicas claramente

### 3. Nomes Descritivos
Use nomes claros para classes, métodos e variáveis:
- Classes: substantivos (`Pessoa`, `Categoria`, `DatabaseConnection`)
- Métodos: verbos (`salvar()`, `buscarPorId()`, `deletar()`)
- Atributos: substantivos ou adjetivos (`nome`, `idade`, `ativo`)

### 4. Documentação
Documente classes e métodos usando docstrings:
```python
class Pessoa:
    """
    Representa uma pessoa no sistema.
    
    Attributes:
        id: Identificador único da pessoa
        nome: Nome completo da pessoa
        email: Email único da pessoa
    """
```

### 5. Separação de Concerns
Separe lógica de negócio de acesso a dados:
- **Model**: Apenas dados e validações básicas
- **DAO**: Apenas acesso ao banco
- **Service**: Lógica de negócio e orquestração

### 6. Reutilização
Evite duplicação de código usando herança e composição:
- Use herança quando há relação "é-um"
- Use composição quando há relação "tem-um"
- Crie classes base quando há código comum

## 💡 Dicas de Aprendizado

### Analise o Código Existente
- **Estude a estrutura do projeto SQLite+POO**: Veja como as camadas interagem
- **Leia os docstrings**: Entenda o propósito de cada classe e método
- **Rastreie o fluxo de dados**: Veja como um objeto passa pelas camadas

### Implemente Variações
- **Crie novas entidades**: Adicione uma classe `Produto` seguindo o mesmo padrão
- **Adicione funcionalidades**: Implemente busca por intervalo de idade
- **Modifique relacionamentos**: Crie relacionamentos muitos-para-muitos

### Pratique Refatoração
- **Converta código procedural para POO**: Pegue código do Módulo 1 e transforme em classes
- **Separe responsabilidades**: Quebre classes grandes em menores
- **Aplique padrões**: Implemente novos padrões de projeto

### Pense em Abstrações
- **Identifique padrões**: Veja o que se repete e crie abstrações
- **Generalize soluções**: Crie classes base quando apropriado
- **Defina interfaces claras**: Torne as interfaces das classes intuitivas

## 🎓 Estrutura Pedagógica

Este módulo segue uma abordagem prática e progressiva:

1. **Aprendizado baseado em projeto**: Todo conhecimento é aplicado em um projeto real
2. **Arquitetura em camadas**: Aprenda organizando código profissionalmente
3. **Padrões de projeto**: Veja padrões aplicados, não apenas teoria
4. **Código limpo**: Exemplos seguem boas práticas desde o início
5. **Testes incluídos**: Veja como testar código orientado a objetos

## ⚠️ Importante

### Base para Módulos Futuros

A Programação Orientada a Objetos é fundamental para desenvolvimento backend escalável. Este módulo estabelece as bases para:
- **Módulo 4 (Padrões de Desenvolvimento)**: Aprofundamento em padrões avançados
- **Módulo 5 (WebServices)**: APIs estruturadas usando classes e objetos
- **Módulo 6 (Django)**: Framework que usa POO extensivamente (Models, Views, Forms)

### Por que POO é Importante para Backend?

1. **Organização**: Código backend pode ser complexo - POO ajuda a organizar
2. **Reutilização**: Classes podem ser reutilizadas em diferentes contextos
3. **Manutenibilidade**: Código organizado é mais fácil de manter e modificar
4. **Escalabilidade**: Estruturas em camadas facilitam crescimento
5. **Testabilidade**: Classes isoladas são mais fáceis de testar
6. **Colaboração**: Código organizado facilita trabalho em equipe

### Transição do Código Procedural

Se você veio do Módulo 1 (que é mais procedural), a transição pode parecer estranha. Lembre-se:
- **Funções → Métodos**: Agora funções pertencem a classes
- **Variáveis globais → Atributos**: Dados são encapsulados em objetos
- **Scripts → Classes**: Lógica é organizada em classes especializadas
- **Código linear → Código em camadas**: Diferentes responsabilidades em diferentes lugares

## 🏆 Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Entender o que é uma classe e como criar objetos
- [ ] Compreender os quatro pilares da POO (Encapsulamento, Abstração, Herança, Polimorfismo)
- [ ] Ser capaz de criar classes com métodos e propriedades
- [ ] Entender a diferença entre atributos de classe e de instância
- [ ] Compreender relacionamentos entre classes (composição, herança)
- [ ] Entender a arquitetura em camadas do projeto SQLite+POO
- [ ] Ser capaz de criar um DAO simples para uma nova entidade
- [ ] Compreender o padrão Service Layer e sua importância
- [ ] Conseguir ler e entender código orientado a objetos
- [ ] Ser capaz de documentar classes usando docstrings

## 💻 Executando os Projetos

### Pré-requisitos
```bash
# Verificar Python
python3 --version

# SQLite já vem incluído no Python
python3 -c "import sqlite3; print('SQLite OK')"
```

### Executar Projeto Principal
```bash
cd "Módulo3 - Programação Orientada a Objetos/SQLite+POO"
python3 app/main.py
```

### Executar Exemplos
```bash
python3 test/exemplo_uso_orm.py
```

### Executar Testes
```bash
python3 test/teste_projeto.py
```

## 🎯 Próximos Passos

Após dominar este módulo:
1. **Módulo 4**: Aprofundar em padrões de projeto mais avançados
2. **Módulo 5**: Criar APIs RESTful usando classes e objetos
3. **Módulo 6**: Usar Django, que é fortemente baseado em POO

**Recomendação**: Não avance até se sentir confortável criando suas próprias classes e entendendo a separação de responsabilidades. POO é uma mudança de paradigma importante que requer prática.
