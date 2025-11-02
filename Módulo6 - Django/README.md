# Módulo 6 - Django

Este módulo apresenta o Django, um dos frameworks web mais populares e completos para Python, ideal para desenvolvimento de aplicações backend robustas, escaláveis e com muitas funcionalidades inclusas. Django segue a filosofia "batteries included" (pilhas incluídas), oferecendo uma solução completa para desenvolvimento web.

## 📚 Conteúdo do Módulo

Este módulo aborda o framework Django em profundidade, desde conceitos fundamentais até funcionalidades avançadas para desenvolvimento de aplicações web completas. Você aprenderá a criar aplicações backend profissionais usando um framework maduro e amplamente utilizado na indústria.

### 1. Fundamentos do Django

Conceitos base e filosofia do framework Django.

**História e Filosofia**: Entendendo o "batteries included"
- Framework criado em 2005, maduro e estável
- Filosofia de incluir muitas funcionalidades por padrão
- Foco em desenvolvimento rápido e boas práticas
- Convenção sobre configuração (CoC)
- DRY (Don't Repeat Yourself) como princípio central

**Estrutura de Projeto**: Organização de pastas e arquivos
- `manage.py`: Script de gerenciamento do projeto
- Diretório do projeto: configurações principais
- Apps: módulos da aplicação (separação de funcionalidades)
- `settings.py`: Configurações do projeto
- `urls.py`: Roteamento de URLs
- `wsgi.py` / `asgi.py`: Interfaces para servidores web

**MVC/MVT Pattern**: Model-View-Template architecture
- **MVT vs MVC**: Django usa MVT (Model-View-Template) ao invés de MVC tradicional
- **Model**: Camada de dados (banco de dados)
- **View**: Lógica de negócio e processamento
- **Template**: Camada de apresentação (HTML)
- **URLs**: Mapeamento de URLs para views

**Settings e Configuração**: Gerenciamento de configurações
- `settings.py`: Arquivo central de configuração
- Variáveis de ambiente para configurações sensíveis
- Settings para desenvolvimento vs produção
- `DEBUG`, `SECRET_KEY`, `DATABASES`, `INSTALLED_APPS`
- Configuração de middlewares

### 2. Models e ORM

Criação e gerenciamento de modelos de dados com Django ORM.

**Definição de Models**: Criando modelos de dados
- Classes que representam tabelas no banco
- Campos e tipos de dados disponíveis
- Relacionamentos: ForeignKey, ManyToMany, OneToOne
- Meta classes para configurações avançadas
- Métodos personalizados em models

**ORM (Object-Relational Mapping)**: Abstração do banco de dados
- Django ORM permite trabalhar com banco sem SQL direto
- API de queries intuitiva e Pythonica
- Queries lazy (avaliadas apenas quando necessário)
- Queries eficientes com `select_related` e `prefetch_related`

**Migrations**: Sistema de migrações de banco
- Criação automática de migrations
- Aplicação de migrations (`migrate`)
- Reversão de migrations (`migrate app_name migration_number`)
- Migrations customizadas para mudanças complexas
- Nunca edite migrations manualmente após commitadas

**Relacionamentos**: ForeignKey, ManyToMany, OneToOne
- **ForeignKey**: Relacionamento muitos-para-um
- **ManyToMany**: Relacionamento muitos-para-muitos
- **OneToOne**: Relacionamento um-para-um
- Related names e related queries
- Cascatas (on_delete: CASCADE, PROTECT, SET_NULL, etc.)

**Queries**: API de consultas do Django ORM
- `filter()`, `exclude()`: Filtragem de objetos
- `get()`, `first()`, `last()`: Obtenção de objetos
- `all()`: Todos os objetos
- Queries complexas com Q objects
- Annotate e aggregate para cálculos
- `select_related()` e `prefetch_related()` para otimização

**Admin Interface**: Interface administrativa automática
- Admin automático do Django
- Customização do admin
- Permissões e grupos
- Actions personalizadas no admin

### 3. Views e Templates

Processamento de requisições e renderização de respostas.

**Function-Based Views**: Views baseadas em funções
- Views simples como funções Python
- Recebem `request` como parâmetro
- Retornam objetos `HttpResponse`
- Decoradores úteis (`@login_required`, `@csrf_exempt`)

**Class-Based Views**: Views baseadas em classes
- Views reutilizáveis e organizadas
- ListView, DetailView, CreateView, UpdateView, DeleteView
- Generic views para operações CRUD comuns
- Mixins para funcionalidades compartilhadas

**Templates**: Sistema de templates Django
- Templates usando Django Template Language (DTL)
- Herança de templates (`{% extends %}`)
- Inclusão de templates (`{% include %}`)
- Tags e filters personalizados

**Template Tags e Filters**: Extensão de templates
- Tags: `{% if %}`, `{% for %}`, `{% url %}`, etc.
- Filters: `{{ value|upper }}`, `{{ value|date }}`, etc.
- Criar tags e filters customizados

**Context**: Passando dados para templates
- Context dictionary nas views
- `render()`: Atalho para renderizar template com context
- `get_context_data()`: Em class-based views

### 4. URLs e Roteamento

Configuração de URLs e roteamento de requisições.

**URLconf**: Configuração de URLs
- Arquivo `urls.py` em cada app
- `urlpatterns`: Lista de padrões de URL
- `path()` e `re_path()`: Funções para definir rotas

**URL Patterns**: Padrões e expressões regulares
- Parâmetros nomeados: `<int:id>`, `<str:slug>`
- Tipos de conversores: `int`, `str`, `slug`, `uuid`, `path`
- Expressões regulares com `re_path()`

**Namespaces**: Organização de URLs
- `app_name`: Namespace para URLs de um app
- URLs namespaced: `app_name:view_name`
- Evita conflitos de nomes entre apps

**Reverse URLs**: Geração reversa de URLs
- `reverse()`: Gerar URLs a partir de nomes
- `{% url %}`: Tag de template para URLs
- Evita hardcoding de URLs no código

### 5. Forms

Criação e processamento de formulários.

**Django Forms**: Sistema de formulários
- `forms.Form`: Formulários simples
- `forms.ModelForm`: Formulários baseados em models
- Validação automática de campos
- Renderização de formulários em templates

**Form Validation**: Validação de dados
- Validação em nível de campo
- Validação em nível de formulário (`clean()`)
- Mensagens de erro personalizadas
- Validação customizada

**Model Forms**: Formulários baseados em models
- Criação automática de campos baseados no model
- Salvamento direto em banco de dados
- Relacionamentos em formulários

**CSRF Protection**: Proteção contra CSRF
- Token CSRF automático em formulários
- `{% csrf_token %}`: Tag de template
- Proteção automática do Django
- Exceções quando necessário (`@csrf_exempt`)

### 6. Autenticação e Autorização

Sistema de usuários, login e controle de acesso.

**User Model**: Sistema de usuários do Django
- Model `User` padrão do Django
- Campos: `username`, `email`, `password`, `is_active`, `is_staff`, `is_superuser`
- Custom User Model: Criar modelo de usuário personalizado

**Authentication**: Login, logout, registro
- `authenticate()`: Autenticar usuário
- `login()`: Fazer login
- `logout()`: Fazer logout
- Views de autenticação: `LoginView`, `LogoutView`
- URLs de autenticação padrão

**Permissions**: Sistema de permissões
- Permissões padrão: add, change, delete, view
- Permissões customizadas
- Verificação de permissões em views e templates

**Groups**: Grupos de usuários
- Agrupar usuários com permissões similares
- Atribuição de permissões a grupos
- Usuários podem pertencer a múltiplos grupos

**Custom User Model**: Personalização do modelo de usuário
- Criar model de usuário personalizado
- Configurar `AUTH_USER_MODEL` nas settings
- Importante fazer no início do projeto

### 7. Django REST Framework

Criação de APIs RESTful com Django.

**Serializers**: Serialização de dados
- `serializers.Serializer`: Serializers básicos
- `serializers.ModelSerializer`: Serializers baseados em models
- Serialização e deserialização
- Validação de dados

**ViewSets e Routers**: Organização de APIs
- ViewSets para operações CRUD
- Routers para URLs automáticas
- `ModelViewSet`: CRUD completo baseado em model
- ViewSets customizados

**Permissions**: Permissões em APIs
- Permissões padrão do DRF
- Permissões customizadas
- `IsAuthenticated`, `IsAdminUser`, etc.

**Authentication**: Autenticação em APIs
- Autenticação por sessão
- Autenticação por token
- JWT com `djangorestframework-simplejwt`

**Pagination**: Paginação de resultados
- Paginação padrão
- Paginação customizada
- Configuração global vs por view

### 8. Funcionalidades Avançadas

Recursos avançados do Django para aplicações profissionais.

**Middleware**: Processamento de requisições
- Middleware do Django
- Criar middleware customizado
- Processamento antes/depois da view
- Ordem de execução importante

**Signals**: Sistema de sinais
- Sinais pré-definidos do Django
- Criar sinais customizados
- Conectores de sinais
- Uso: `pre_save`, `post_save`, `pre_delete`, etc.

**Caching**: Sistema de cache
- Backends de cache (Memcached, Redis, etc.)
- Cache por view (`@cache_page`)
- Cache de template
- Cache de query

**Sessions**: Gerenciamento de sessões
- Armazenamento de sessões
- Backends de sessão (database, cache, file)
- Acesso a sessão em views
- Expiração de sessão

**Static Files**: Arquivos estáticos
- `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_DIRS`
- `collectstatic`: Coletar arquivos estáticos
- Servindo arquivos estáticos em produção
- `{% static %}`: Tag de template

**Media Files**: Upload e gerenciamento de mídia
- `MEDIA_URL`, `MEDIA_ROOT`
- Upload de arquivos
- `FileField`, `ImageField` em models
- Servindo arquivos de mídia

### 9. Testes

Framework de testes do Django para garantir qualidade.

**Test Framework**: Framework de testes do Django
- Baseado em `unittest` do Python
- `TestCase`: Classe base para testes
- `django.test.Client`: Cliente de teste HTTP

**TestCase**: Classe base para testes
- `setUp()` e `tearDown()`: Preparação e limpeza
- Fixtures para dados de teste
- Testes de models, views, forms

**Fixtures**: Dados de teste
- Arquivos JSON/YAML com dados
- Carregamento de fixtures
- Factories (usando `factory_boy`)

**Client Testing**: Testes de client HTTP
- `client.get()`, `client.post()`: Simular requisições
- Testar respostas e status codes
- Testar templates renderizados

**Coverage**: Análise de cobertura
- `coverage.py`: Ferramenta de cobertura
- Relatórios de cobertura
- Metas de cobertura

### 10. Deploy e Produção

Preparação e deploy de aplicações Django em produção.

**Settings de Produção**: Configurações para produção
- `DEBUG = False`: Desabilitar debug
- `ALLOWED_HOSTS`: Hosts permitidos
- `SECRET_KEY`: Chave secreta segura
- Variáveis de ambiente para configurações

**Static Files Serving**: Servindo arquivos estáticos
- `whitenoise`: Middleware para arquivos estáticos
- CDN para arquivos estáticos
- `collectstatic` em produção

**Database Optimization**: Otimização de banco
- Índices em models
- `select_related()` e `prefetch_related()`
- Análise de queries (`django-debug-toolbar`)
- Database connection pooling

**Security**: Boas práticas de segurança
- `SECURE_SSL_REDIRECT`: Redirecionar para HTTPS
- `SESSION_COOKIE_SECURE`: Cookies seguros
- `CSRF_COOKIE_SECURE`: Cookies CSRF seguros
- Headers de segurança

**Deployment**: Processo de deploy
- Servidores WSGI: Gunicorn, uWSGI
- Servidores ASGI: Daphne, Uvicorn
- Reverse proxy: Nginx
- Plataformas: Heroku, AWS, DigitalOcean, etc.

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Criar aplicações web completas com Django
- Utilizar o ORM do Django eficientemente para operações de banco
- Implementar autenticação e autorização robustas
- Criar APIs REST com Django REST Framework
- Desenvolver e aplicar templates dinâmicos
- Gerenciar arquivos estáticos e de mídia
- Realizar deploy de aplicações Django em produção
- Aplicar boas práticas de segurança
- Otimizar performance de aplicações Django
- Escrever testes automatizados para aplicações Django
- Organizar projetos Django em múltiplos apps
- Configurar Django para diferentes ambientes (dev/prod)

## 📋 Pré-requisitos

- Conhecimento avançado de Python
  - Classes e objetos
  - Decoradores
  - Context managers
  - Módulos e pacotes
- Compreensão de bancos de dados relacionais
  - SQL básico
  - Relacionamentos entre tabelas
  - Índices e otimização
- Familiaridade com HTTP e web development
  - Como funcionam requisições HTTP
  - Métodos HTTP
  - Status codes
- Experiência com desenvolvimento de APIs (Módulo 5)
  - Conceitos de REST
  - JSON e serialização
- Conhecimento de POO (Módulo 3)
  - Classes e herança
  - Padrões de projeto básicos
- Conhecimento básico de HTML, CSS e JavaScript
  - Para trabalhar com templates
  - Entender estrutura de páginas web

## 🔧 Stack Tecnológica

### Core Django
- **Django Framework**: Framework web completo
- **Django ORM**: Abstração de banco de dados
- **Django Admin**: Interface administrativa automática
- **Django Templates**: Sistema de templates
- **Django REST Framework**: Framework para APIs REST

### Extensões Comuns
- **Django CORS Headers**: CORS para APIs
- **Django Extensions**: Extensões úteis (`shell_plus`, etc.)
- **Django Crispy Forms**: Formulários estilizados
- **Django Debug Toolbar**: Debugging e análise de queries

### Banco de Dados
- **PostgreSQL**: Recomendado para produção
- **MySQL**: Alternativa comum
- **SQLite**: Desenvolvimento e testes

### Outras Ferramentas
- **Gunicorn**: Servidor WSGI para produção
- **Nginx**: Reverse proxy e servidor web
- **Celery**: Tarefas assíncronas
- **Redis**: Cache e broker para Celery
- **PostgreSQL**: Banco de dados recomendado

## 🚀 Estrutura de um Projeto Django

```
projeto_django/
├── manage.py                 # Script de gerenciamento
├── projeto/                  # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py           # Configurações
│   ├── urls.py               # URLs principais
│   ├── wsgi.py               # WSGI config
│   └── asgi.py               # ASGI config
├── app1/                     # App da aplicação
│   ├── migrations/           # Migrations do banco
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py             # Models
│   ├── views.py              # Views
│   ├── urls.py               # URLs do app
│   ├── admin.py              # Configuração do admin
│   ├── forms.py              # Formulários
│   ├── serializers.py        # Serializers (DRF)
│   ├── templates/            # Templates do app
│   └── tests.py              # Testes
├── static/                   # Arquivos estáticos
├── media/                    # Arquivos de mídia
├── requirements.txt          # Dependências
└── .env                      # Variáveis de ambiente
```

## 📖 Recursos de Referência

### Documentação Oficial
- [Django Documentation](https://docs.djangoproject.com/) - Documentação oficial completa
- [Django REST Framework](https://www.django-rest-framework.org/) - Documentação do DRF
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) - Tutorial oficial
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/design-philosophies/) - Filosofia e boas práticas

### Livros Recomendados
- **"Two Scoops of Django"** - Boas práticas Django (atualizado regularmente)
- **"Django for Beginners"** - Guia para iniciantes
- **"Django for APIs"** - Django REST Framework

### Comunidade
- [Django Forum](https://forum.djangoproject.com/) - Fórum oficial
- [Django Users](https://groups.google.com/forum/#!forum/django-users) - Lista de discussão
- [Stack Overflow - Django](https://stackoverflow.com/questions/tagged/django) - Perguntas e respostas

## 🔐 Boas Práticas

### 1. Separation of Concerns
Separe lógica de negócio, apresentação e dados:
- Models: Apenas dados e lógica relacionada
- Views: Lógica de processamento
- Templates: Apenas apresentação

### 2. DRY (Don't Repeat Yourself)
Reutilize código:
- Templates: Herança e inclusão
- Views: Class-based views e mixins
- Models: Relacionamentos e métodos

### 3. Security
- Sempre valide e sanitize entrada
- Use forms para validação
- Nunca confie em dados do cliente
- Use HTTPS em produção
- Configure `SECRET_KEY` e `DEBUG` adequadamente

### 4. Migrations
- Nunca edite migrations manualmente após commitadas
- Crie migrations para todas as mudanças em models
- Teste migrations em ambiente de desenvolvimento
- Faça backup antes de migrations em produção

### 5. Settings
- Use variáveis de ambiente para configurações sensíveis
- Separe settings para desenvolvimento e produção
- Nunca commite `SECRET_KEY` ou senhas
- Use `python-decouple` ou `django-environ`

### 6. Tests
- Escreva testes para funcionalidades críticas
- Teste models, views e forms
- Use fixtures ou factories para dados de teste
- Mantenha boa cobertura de testes

### 7. Documentation
- Documente código complexo
- Use docstrings em models e views
- Mantenha README atualizado
- Documente APIs com DRF

### 8. Performance
- Use `select_related()` e `prefetch_related()` para otimizar queries
- Índices em campos frequentemente consultados
- Cache quando apropriado
- Use `django-debug-toolbar` para identificar problemas de performance

## 💡 Por que Django?

### Batteries Included
- Muitas funcionalidades já inclusas
- Não precisa instalar muitas dependências extras
- Solução completa para desenvolvimento web

### Admin Interface
- Interface administrativa automática
- Customizável e extensível
- Útil para gerenciamento de dados

### ORM Poderoso
- Abstração completa do banco de dados
- Migrations automáticas
- Queries Pythonicas e intuitivas

### Segurança
- Proteções contra vulnerabilidades comuns
- CSRF protection automático
- SQL injection protection via ORM
- XSS protection em templates

### Escalabilidade
- Usado por empresas grandes (Instagram, Spotify, Pinterest, NASA)
- Suporta milhões de usuários
- Arquitetura que suporta crescimento

### Comunidade
- Grande comunidade e ecossistema
- Muitos pacotes disponíveis
- Documentação excelente
- Suporte ativo

## 🏗️ Aplicações Práticas

Django é usado para:
- **Sistemas de gerenciamento de conteúdo**: Blogs, CMS
- **E-commerce**: Lojas online, marketplaces
- **Redes sociais**: Plataformas sociais
- **Plataformas de API**: Backend para aplicações
- **Sistemas de gestão empresarial**: ERP, CRM
- **Aplicações web complexas**: Qualquer aplicação web robusta

## 🎓 Estrutura Pedagógica

Este módulo segue uma abordagem prática:
1. **Fundamentos primeiro**: Entenda a filosofia e estrutura do Django
2. **Projeto guiado**: Construa uma aplicação completa passo a passo
3. **Aprofundamento progressivo**: Adicione complexidade gradualmente
4. **Boas práticas desde o início**: Aprenda da forma correta
5. **Exercícios práticos**: Aplique conhecimento em projetos reais

## ⚠️ Importante

### Curva de Aprendizado
Django tem uma curva de aprendizado, mas oferece muita funcionalidade pronta:
- Comece pelo tutorial oficial antes de criar projetos complexos
- Entenda a estrutura antes de customizar
- Use o admin para entender models e relacionamentos

### Não Pule o Básico
- Entenda models e migrations antes de avançar
- Domine o ORM antes de escrever SQL direto
- Compreenda a arquitetura MVT

### Use a Documentação
- A documentação do Django é excelente
- Consulte regularmente durante desenvolvimento
- Use a documentação como referência principal

### Prática é Essencial
- Django é melhor aprendido fazendo
- Crie projetos próprios além dos exemplos
- Experimente e explore funcionalidades

## 🏆 Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Entender a estrutura de um projeto Django
- [ ] Ser capaz de criar models com relacionamentos
- [ ] Compreender e usar migrations
- [ ] Criar views (function-based e class-based)
- [ ] Trabalhar com templates e herança
- [ ] Implementar autenticação e autorização
- [ ] Criar APIs básicas com DRF
- [ ] Gerenciar arquivos estáticos e de mídia
- [ ] Escrever testes básicos
- [ ] Configurar Django para diferentes ambientes
- [ ] Entender quando usar Django vs outros frameworks

## 💻 Comandos Essenciais

### Gerenciamento de Projeto
```bash
# Criar projeto
django-admin startproject nome_projeto

# Criar app
python manage.py startapp nome_app

# Rodar servidor de desenvolvimento
python manage.py runserver

# Criar superusuário
python manage.py createsuperuser
```

### Banco de Dados
```bash
# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Reverter migration
python manage.py migrate app_name migration_number

# Shell interativo com Django
python manage.py shell
```

### Outros
```bash
# Coletar arquivos estáticos
python manage.py collectstatic

# Executar testes
python manage.py test

# Listar URLs
python manage.py show_urls
```

Este módulo está em desenvolvimento. Conteúdo adicional será adicionado conforme o curso progride, incluindo tutoriais passo a passo, projetos práticos completos e exemplos avançados de uso do Django.

**Dica**: Django tem uma curva de aprendizado, mas oferece muita funcionalidade pronta. Comece pelo tutorial oficial antes de criar projetos complexos.
