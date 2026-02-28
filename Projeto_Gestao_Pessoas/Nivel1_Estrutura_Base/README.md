# Nível 1 - Estrutura Base

Este é o nível mais básico do projeto, contendo apenas a estrutura inicial do Django.

## 📁 Estrutura

```
Nivel1_Estrutura_Base/
├── manage.py                 # Script de gerenciamento do Django
├── gestao_pessoas/           # Diretório de configuração do projeto
│   ├── __init__.py
│   ├── settings.py           # Configurações do projeto
│   ├── urls.py               # URLs principais
│   ├── wsgi.py               # Interface WSGI
│   └── asgi.py               # Interface ASGI
├── requirements.txt          # Dependências do projeto
└── README.md                 # Este arquivo
```

## 🚀 Como Executar

### 1. Criar e ativar ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Aplicar migrations iniciais

```bash
python manage.py migrate
```

### 4. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 5. Executar servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará disponível em: http://127.0.0.1:8000/

### 6. Acessar o admin

Acesse: http://127.0.0.1:8000/admin/

## 📝 Comandos Úteis

- `python manage.py runserver` - Inicia o servidor de desenvolvimento
- `python manage.py migrate` - Aplica as migrations do banco de dados
- `python manage.py makemigrations` - Cria novas migrations
- `python manage.py createsuperuser` - Cria um usuário administrador
- `python manage.py shell` - Abre o shell interativo do Django

## 🎯 O que este nível contém?

- Estrutura básica do projeto Django
- Configurações iniciais (settings.py)
- Sistema de admin do Django
- Banco de dados SQLite configurado
- Configuração de URLs básica

## ➡️ Próximo Nível

No **Nível 2**, vamos adicionar os modelos de dados para gestão de pessoas.
