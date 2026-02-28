# Nível 2 - Modelos de Dados

Este nível adiciona o app `pessoas` com o modelo `Pessoa` completo para gestão de pessoas.

## 📁 Estrutura

```
Nivel2_Modelos/
├── manage.py
├── gestao_pessoas/
│   ├── settings.py          # Configurações (com app 'pessoas' adicionado)
│   ├── urls.py
│   └── ...
└── pessoas/                  # Novo app
    ├── __init__.py
    ├── apps.py
    ├── models.py             # Modelo Pessoa
    ├── admin.py              # Configuração do admin
    └── migrations/
        └── __init__.py
```

## 🚀 Como Executar

### 1. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate      # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Criar migrations

```bash
python manage.py makemigrations
```

### 4. Aplicar migrations

```bash
python manage.py migrate
```

### 5. Criar superusuário

```bash
python manage.py createsuperuser
```

### 6. Executar servidor

```bash
python manage.py runserver
```

### 7. Acessar o admin

Acesse: http://127.0.0.1:8000/admin/

Você poderá criar, editar e listar pessoas através da interface administrativa do Django.

## 📊 Modelo Pessoa

O modelo `Pessoa` contém os seguintes campos:

### Campos Básicos
- **nome**: Nome completo (CharField, max_length=100)
- **cpf**: CPF único (CharField, formato XXX.XXX.XXX-XX)
- **email**: E-mail único (EmailField)
- **telefone**: Telefone (CharField, formato (XX) XXXXX-XXXX)

### Dados Pessoais
- **data_nascimento**: Data de nascimento (DateField)
- **sexo**: Sexo (CharField com choices: M, F, O, N)
- **estado_civil**: Estado civil (CharField com choices)

### Endereço
- **endereco**: Endereço completo
- **cidade**: Cidade
- **estado**: Estado (UF)
- **cep**: CEP (formato XXXXX-XXX)

### Controle
- **data_cadastro**: Data/hora de cadastro (auto_now_add)
- **data_atualizacao**: Data/hora de última atualização (auto_now)
- **ativo**: Status ativo/inativo (BooleanField)
- **observacoes**: Observações adicionais (TextField)

### Métodos
- `idade()`: Calcula a idade da pessoa
- `nome_completo()`: Retorna o nome completo

## 🎯 O que este nível adiciona?

- App `pessoas` criado
- Modelo `Pessoa` completo com validações
- Configuração do admin para gerenciar pessoas
- Migrations do banco de dados
- Validações de CPF, telefone e CEP
- Índices no banco para melhor performance

## ➡️ Próximo Nível

No **Nível 3**, vamos adicionar views e templates para exibir e gerenciar pessoas através de uma interface web.
