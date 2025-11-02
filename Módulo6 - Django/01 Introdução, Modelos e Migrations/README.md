# 01 - Introdução, Modelos e Migrations

Este módulo introduz os conceitos fundamentais do Django, focando na arquitetura MTV, instalação, definição de models, migrations e o admin automático.

## 📚 Conteúdo

1. **Conceito de MTV**
2. **Instalação e Ambientação**
3. **Definição de Models**
4. **Criação e Execução de Migrations**
5. **Admin Automático**

## 🎯 Objetivos de Aprendizado

Ao final desta unidade, você será capaz de:
- Entender a arquitetura MTV do Django
- Instalar e configurar um projeto Django
- Definir models com diferentes tipos de campos
- Criar e aplicar migrations
- Configurar e customizar o Django Admin

## 📁 Arquivos

- `01_instalacao_ambientacao.py` - Instalação, configuração e conceitos MTV
- `02_definicao_models.py` - Exemplos de models com campos e relacionamentos
- `03_migrations.py` - Guia completo de migrations
- `04_admin_automatico.py` - Configuração e customização do admin

## 🚀 Prática: Criar um Projeto Django

### Passo 1: Instalação

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar Django
pip install django

# Verificar versão
python -m django --version
```

### Passo 2: Criar Projeto

```bash
# Criar projeto
django-admin startproject meu_projeto

# Entrar no diretório
cd meu_projeto

# Criar app
python manage.py startapp produtos
```

### Passo 3: Configurar Settings

No arquivo `meu_projeto/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produtos',  # Adicionar seu app
]
```

### Passo 4: Criar Models

No arquivo `produtos/models.py`:

```python
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.nome
```

### Passo 5: Criar Migrations

```bash
# Criar migrations
python manage.py makemigrations

# Ver SQL que será executado
python manage.py sqlmigrate produtos 0001

# Aplicar migrations
python manage.py migrate
```

### Passo 6: Configurar Admin

No arquivo `produtos/admin.py`:

```python
from django.contrib import admin
from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']
    search_fields = ['nome']

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'quantidade', 'categoria', 'ativo']
    list_filter = ['categoria', 'ativo']
    search_fields = ['nome']
    list_editable = ['preco', 'ativo']
```

### Passo 7: Criar Superusuário e Acessar Admin

```bash
# Criar superusuário
python manage.py createsuperuser

# Rodar servidor
python manage.py runserver

# Acessar http://127.0.0.1:8000/admin
```

## 🔑 Conceitos Importantes

### MTV (Model-Template-View)

- **Model**: Define a estrutura dos dados (banco de dados)
- **Template**: Define como os dados são apresentados (HTML)
- **View**: Processa requisições e coordena Model e Template

### Models

- Herdam de `models.Model`
- Campos definem estrutura do banco
- Métodos `__str__()` para representação legível
- Meta class para configurações adicionais

### Migrations

- Nunca edite migrations já aplicadas
- Sempre teste antes de aplicar em produção
- Faça backup antes de migrations importantes
- Use migrations customizadas para migração de dados

### Admin

- Interface administrativa automática
- Customizável através de `ModelAdmin`
- Actions para operações em massa
- Permissões granulares

## 📝 Exercícios Práticos

1. **Exercício 1**: Criar um modelo `Autor` e `Livro` com relacionamento ForeignKey
2. **Exercício 2**: Adicionar campos `isbn` e `publicacao` ao modelo `Livro`
3. **Exercício 3**: Criar migration customizada para popular categorias padrão
4. **Exercício 4**: Customizar admin para mostrar resumo de livros por autor
5. **Exercício 5**: Criar action no admin para marcar múltiplos livros como publicados

## 💡 Dicas

- Use `python manage.py shell` para testar queries
- Sempre defina `__str__()` nos models para facilitar debug
- Use `related_name` em ForeignKey para acessar relacionamento reverso
- Configure `list_display` no admin para mostrar informações úteis
- Use migrations customizadas apenas quando necessário

## 📖 Recursos Adicionais

- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Django Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

