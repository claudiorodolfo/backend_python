# Sistema Cadastral - Padrão MVC

Este projeto é uma implementação didática do Padrão de Projeto Arquitetural **MVC (Model-View-Controller)** em Python, demonstrando a separação de responsabilidades entre as camadas de apresentação, lógica de negócio e acesso a dados.

## 📋 Sobre o Projeto

Sistema de cadastro e busca de pessoas que exemplifica os conceitos fundamentais do padrão MVC, com uma arquitetura bem definida e separação clara de responsabilidades.

## 🏗️ Arquitetura MVC

O projeto está organizado seguindo o padrão MVC com as seguintes camadas:

### **Model (Modelo)**
Responsável pela representação dos dados e lógica de persistência.

- **`models/entities/pessoa.py`**: Entidade `Pessoa` com propriedades encapsuladas (e-mail, nome, idade, altura). O e-mail é o identificador único da entidade.
- **`models/repository/repositorio_pessoa.py`**: Repositório que gerencia o acesso aos dados (CRUD completo: criar, buscar, listar, atualizar e apagar)

### **View (Visão)**
Responsável apenas pela entrada e saída de dados (I/O), sem lógica de negócio.

- **`views/index_view.py`**: Menu principal do sistema
- **`views/cadastrar_pessoa_view.py`**: Interface para cadastro de pessoas
- **`views/buscar_pessoa_view.py`**: Interface para busca de pessoa por e-mail
- **`views/listar_todas_pessoas_view.py`**: Interface para listar todas as pessoas
- **`views/atualizar_pessoa.py`**: Interface para atualização de pessoas
- **`views/apagar_pessoa.py`**: Interface para exclusão de pessoas

### **Controller (Controlador)**
Coordena a comunicação entre View e Model, contendo a lógica de negócio e validações.

- **`controllers/pessoa_controller.py`**: Controlador que gerencia todas as operações CRUD (cadastrar, buscar, listar, atualizar e apagar), incluindo validações, conversão de tipos e formatação de dados no padrão de resposta da API

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
│   ├── apagar_pessoa.py
│   ├── atualizar_pessoa.py
│   ├── buscar_pessoa_view.py
│   ├── listar_todas_pessoas_view.py
│   ├── cadastrar_pessoa_view.py
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
   - **2** - Buscar Pessoa Por E-mail
   - **3** - Listar Todas as Pessoas
   - **4** - Atualizar Pessoa
   - **5** - Apagar Pessoa

## ✨ Funcionalidades

### Cadastrar Pessoa
- Permite cadastrar uma nova pessoa informando:
  - E-mail (obrigatório) - usado como identificador único
  - Nome (opcional)
  - Idade (opcional)
  - Altura (opcional)
- Valida os dados antes de persistir
- Exibe mensagem de sucesso ou erro

### Buscar Pessoa Por E-mail
- Busca uma pessoa pelo e-mail
- Exibe os dados completos da pessoa encontrada
- Retorna erro se a pessoa não for encontrada

### Listar Todas as Pessoas
- Lista todas as pessoas cadastradas no sistema
- Exibe o total de registros encontrados
- Retorna erro se não houver pessoas cadastradas

### Atualizar Pessoa
- Permite atualizar os dados de uma pessoa existente
- Busca a pessoa pelo e-mail
- Exibe os valores atuais para facilitar a edição
- Permite atualizar nome, idade e altura
- Valida os dados antes de atualizar
- Exibe mensagem de sucesso ou erro

### Apagar Pessoa
- Permite excluir uma pessoa do sistema
- Busca e remove a pessoa pelo e-mail
- Exibe mensagem de sucesso ou erro

## 🔍 Validações Implementadas

- **E-mail**: Campo obrigatório, não pode ser vazio ou apenas espaços
- **Nome**: Não pode ser vazio ou apenas espaços (se informado)
- **Idade**: Deve ser um número inteiro não negativo (se informada)
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

### Padrão de Resposta
- Todas as respostas seguem um padrão estruturado com `head` e `body`
- Respostas de sucesso incluem metadados (tipo, contagem)
- Respostas de erro seguem o mesmo padrão para consistência

### Manutenibilidade
- Código organizado e fácil de entender
- Fácil adicionar novas funcionalidades
- Testes podem ser escritos para cada camada independentemente

## 📝 Exemplo de Uso

```
Sistema Cadastral

* 0 - Sair
* 1 - Cadastrar Pessoa
* 2 - Buscar Pessoa Por E-mail
* 3 - Listar Todas as Pessoas
* 4 - Atualizar Pessoa
* 5 - Apagar Pessoa

Comando: 1

Cadastrar Nova Pessoa

Informe o e-mail (obrigatório): joao.silva@email.com
Informe o nome (opcional - pressione Enter para pular): João Silva
Informe a idade (opcional - pressione Enter para pular): 30
Informe a altura (opcional - pressione Enter para pular): 1.75

Usuário cadastrado com sucesso!

Tipo: Pessoa
Registros: 1
Informações:
    Email: joao.silva@email.com
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

