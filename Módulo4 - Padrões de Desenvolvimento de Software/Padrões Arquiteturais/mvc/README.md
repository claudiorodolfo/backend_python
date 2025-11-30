# Sistema Cadastral - Padrão MVC

Este projeto é uma implementação didática do Padrão de Projeto Arquitetural **MVC (Model-View-Controller)** em Python, demonstrando a separação de responsabilidades entre as camadas de apresentação, lógica de negócio e acesso a dados.

## 📋 Sobre o Projeto

Sistema de cadastro e busca de pessoas que exemplifica os conceitos fundamentais do padrão MVC, com uma arquitetura bem definida e separação clara de responsabilidades.

## 🏗️ Arquitetura MVC

O projeto está organizado seguindo o padrão MVC com as seguintes camadas:

### **Model (Modelo)**
Responsável pela representação dos dados e lógica de persistência.

- **`models/entities/pessoa.py`**: Entidade `Pessoa` com propriedades encapsuladas (nome, idade, altura)
- **`models/repository/repositorio_pessoa.py`**: Repositório que gerencia o acesso aos dados (CRUD)

### **View (Visão)**
Responsável apenas pela entrada e saída de dados (I/O), sem lógica de negócio.

- **`views/index_view.py`**: Menu principal do sistema
- **`views/cadastrar_pessoas_view.py`**: Interface para cadastro de pessoas
- **`views/buscar_pessoas_view.py`**: Interface para busca de pessoas

### **Controller (Controlador)**
Coordena a comunicação entre View e Model, contendo a lógica de negócio e validações.

- **`controllers/pessoa_controller.py`**: Controlador que gerencia as operações de cadastro e busca, incluindo validações e formatação de dados

### **Routes (Rotas)**
Subcamada do Controller que gerencia o roteamento das requisições.

- **`routes/pessoa_routes.py`**: Gerencia as rotas da aplicação, conectando Views aos Controllers

### **Main (Principal)**
Ponto de entrada da aplicação, responsável pela inicialização e configuração.

- **`main/process_handle.py`**: Classe que configura as dependências e inicializa o sistema

## 📁 Estrutura de Diretórios

```
mvc/
├── controllers/
│   └── pessoa_controller.py
├── main/
│   └── process_handle.py
├── models/
│   ├── entities/
│   │   └── pessoa.py
│   └── repository/
│       └── repositorio_pessoa.py
├── routes/
│   └── pessoa_routes.py
├── views/
│   ├── buscar_pessoas_view.py
│   ├── cadastrar_pessoas_view.py
│   └── index_view.py
├── run.py
└── README.md
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior

### Executando o Projeto

1. Navegue até o diretório do projeto:
```bash
cd "Módulo4 - Padrões de Desenvolvimento de Software/Padrões Arquiteturais/mvc"
```

2. Execute o arquivo principal:
```bash
python run.py
```

3. Siga as instruções no menu:
   - **0** - Sair do sistema
   - **1** - Cadastrar Pessoa
   - **2** - Buscar Pessoa Por Nome

## ✨ Funcionalidades

### Cadastrar Pessoa
- Permite cadastrar uma nova pessoa informando:
  - Nome (obrigatório)
  - Idade (opcional)
  - Altura (opcional)
- Valida os dados antes de persistir
- Exibe mensagem de sucesso ou erro

### Buscar Pessoa
- Busca uma pessoa pelo nome
- Exibe os dados completos da pessoa encontrada
- Retorna erro se a pessoa não for encontrada

## 🔍 Validações Implementadas

- **Nome**: Não pode ser vazio ou apenas espaços
- **Idade**: Deve ser um número inteiro positivo (se informada)
- **Altura**: Deve ser um número maior que zero (se informada)

## 🎯 Características do Padrão MVC

### Separação de Responsabilidades
- **View**: Apenas I/O, sem lógica de negócio
- **Controller**: Lógica de negócio, validações e coordenação
- **Model**: Entidades e acesso a dados

### Desacoplamento
- Views recebem e retornam dicionários (não entidades diretamente)
- Controllers fazem a conversão entre dicionários e entidades
- Repository abstrai o acesso aos dados

### Manutenibilidade
- Código organizado e fácil de entender
- Fácil adicionar novas funcionalidades
- Testes podem ser escritos para cada camada independentemente

## 📝 Exemplo de Uso

```
Sistema Cadastral

* 0 - Sair
* 1 - Cadastrar Pessoa
* 2 - Buscar Pessoa Por Nome

Comando: 1

Cadastrar Nova Pessoa

Informe o nome da pessoa: João Silva
Informe a idade da pessoa: 30
Informe a altura da pessoa: 1.75

Usuário cadastrado com sucesso!

Tipo: Pessoa
Registros: 1
Informações:
    Nome: João Silva
    Idade: 30
    Altura: 1.75
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**: Linguagem de programação
- **Padrão MVC**: Arquitetura de software
- **Type Hints**: Tipagem estática para melhor documentação do código

## 📚 Conceitos Demonstrados

- Padrão Arquitetural MVC
- Separação de Responsabilidades
- Encapsulamento
- Validação de Dados
- Tratamento de Exceções

## 👨‍💻 Autor

Projeto desenvolvido como parte do Módulo 4 - Padrões de Desenvolvimento de Software.

## 📄 Licença

Este projeto é de caráter educacional e didático.

