# Comandos Django - Projeto Gestão de Pessoas

Este arquivo contém todos os comandos necessários para trabalhar com o projeto Django de Gestão de Pessoas.

## 📋 Comandos Básicos

### 1. Configuração Inicial

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Instalar Django
pip install django

# Ou instalar todas as dependências
pip install -r requirements.txt
```

### 2. Criar Projeto Django

```bash
# Criar projeto
django-admin startproject gestao_pessoas .

# Criar app
python manage.py startapp pessoas
```

### 3. Banco de Dados

```bash
# Criar migrations
python manage.py makemigrations

# Ver SQL das migrations
python manage.py sqlmigrate pessoas 0001

# Aplicar migrations
python manage.py migrate

# Reverter última migration
python manage.py migrate pessoas 0001

# Listar migrations pendentes
python manage.py showmigrations
```

### 4. Usuário Administrador

```bash
# Criar superusuário
python manage.py createsuperuser

# Alterar senha de usuário
python manage.py changepassword username
```

### 5. Servidor de Desenvolvimento

```bash
# Executar servidor
python manage.py runserver

# Executar em porta específica
python manage.py runserver 8080

# Executar em IP específico
python manage.py runserver 0.0.0.0:8000
```

### 6. Shell Interativo

```bash
# Abrir shell do Django
python manage.py shell

# Exemplo de uso no shell:
# >>> from pessoas.models import Pessoa
# >>> Pessoa.objects.all()
# >>> Pessoa.objects.create(nome="João Silva", cpf="123.456.789-00", ...)
```

### 7. Coletar Arquivos Estáticos

```bash
# Coletar arquivos estáticos para produção
python manage.py collectstatic
```

### 8. Testes

```bash
# Executar todos os testes
python manage.py test

# Executar testes de um app específico
python manage.py test pessoas

# Executar um teste específico
python manage.py test pessoas.tests.TestPessoaModel
```

### 9. Validação

```bash
# Verificar problemas no projeto
python manage.py check

# Verificar configurações
python manage.py check --deploy
```

### 10. Limpar Banco de Dados

```bash
# Deletar banco e recriar (CUIDADO!)
rm db.sqlite3
python manage.py migrate
```

## 🔧 Comandos por Nível

### Nível 1 - Estrutura Base

```bash
cd Nivel1_Estrutura_Base
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Nível 2 - Modelos

```bash
cd Nivel2_Modelos
python manage.py makemigrations pessoas
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Nível 3 - Views e Templates

```bash
cd Nivel3_Views_Templates
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Nível 4 - Formulários e CRUD

```bash
cd Nivel4_Formularios_CRUD
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Nível 5 - Admin Personalizado

```bash
cd Nivel5_Admin_Personalizado
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Nível 6 - API REST

```bash
cd Nivel6_API_REST
pip install djangorestframework
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Nível 7 - Autenticação

```bash
cd Nivel7_Autenticacao
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Nível 8 - Testes e Deploy

```bash
cd Nivel8_Testes_Deploy
python manage.py test
python manage.py check --deploy
```

## 📦 Instalação de Pacotes Adicionais

### Django REST Framework (Nível 6)

```bash
pip install djangorestframework
```

### Autenticação JWT (Nível 7)

```bash
pip install djangorestframework-simplejwt
```

### Testes (Nível 8)

```bash
pip install pytest pytest-django
pip install coverage
```

### Deploy (Nível 8)

```bash
pip install gunicorn
pip install whitenoise
pip install dj-database-url
pip install python-decouple
```

## 🐛 Debug e Troubleshooting

```bash
# Verificar versão do Django
python -m django --version

# Verificar Python
python --version

# Verificar pacotes instalados
pip list

# Verificar dependências
pip freeze > requirements.txt

# Limpar cache do Python
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

## 📝 Dicas Importantes

1. **Sempre ative o ambiente virtual** antes de trabalhar no projeto
2. **Faça migrations** sempre que modificar modelos
3. **Use `python manage.py check`** antes de fazer deploy
4. **Mantenha o `requirements.txt` atualizado**
5. **Use variáveis de ambiente** para configurações sensíveis em produção
