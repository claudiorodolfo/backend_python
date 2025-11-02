# 02 - Views, Templates, URLs e Rotas

Este módulo aborda como criar views, trabalhar com templates usando Django Template Language (DTL), configurar URLs e implementar roteamento em aplicações Django.

## 📚 Conteúdo

1. **Function-Based Views**
2. **Templates HTML com Django Template Language (DTL)**
3. **Context e Renderização**
4. **Configuração de URLConf**
5. **Namespaces e Reverse URLs**
6. **Incluindo Múltiplos Apps**

## 🎯 Objetivos de Aprendizado

Ao final desta unidade, você será capaz de:
- Criar views baseadas em funções
- Trabalhar com templates e Django Template Language
- Passar contexto das views para templates
- Configurar URLs e roteamento
- Usar namespaces e reverse URLs
- Integrar múltiplos apps em um projeto

## 📁 Arquivos

- `01_function_based_views.py` - Exemplos de function-based views
- `02_templates_dtl.py` - Guia completo de templates e DTL
- `03_urls_rotas.py` - Configuração de URLs, namespaces e reverse
- `04_exemplo_completo.py` - Exemplo completo integrado

## 🚀 Conceitos Fundamentais

### Views (Function-Based)

Views são funções Python que recebem requisições HTTP e retornam respostas HTTP:

```python
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def minha_view(request):
    return HttpResponse("Olá!")

def produto_detalhe(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produto.html', {'produto': produto})
```

### Templates

Templates são arquivos HTML que usam Django Template Language para exibir dados dinamicamente:

```html
{% extends "base.html" %}

{% block content %}
    <h1>{{ titulo }}</h1>
    <ul>
        {% for item in lista %}
            <li>{{ item.nome }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

### URLs

URLs conectam endereços web às views:

```python
# urls.py
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:id>/', views.detalhe, name='detalhe'),
]
```

## 📝 Exemplos Práticos

### 1. View Simples com Template

```python
# views.py
def home(request):
    context = {
        'titulo': 'Página Inicial',
        'mensagem': 'Bem-vindo!'
    }
    return render(request, 'home.html', context)
```

```html
<!-- templates/home.html -->
{% extends "base.html" %}
{% block content %}
    <h1>{{ titulo }}</h1>
    <p>{{ mensagem }}</p>
{% endblock %}
```

### 2. View com Formulário

```python
# views.py
def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        # Processar dados...
        return redirect('produtos:lista')
    return render(request, 'form.html')
```

### 3. View com Paginação

```python
# views.py
from django.core.paginator import Paginator

def lista_produtos(request):
    produtos = Produto.objects.all()
    paginator = Paginator(produtos, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lista.html', {'page_obj': page_obj})
```

### 4. URLs com Namespace

```python
# projeto/urls.py
urlpatterns = [
    path('produtos/', include('produtos.urls', namespace='produtos')),
]

# produtos/urls.py
app_name = 'produtos'
urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:id>/', views.detalhe, name='detalhe'),
]

# No template:
{% url 'produtos:lista' %}
{% url 'produtos:detalhe' produto.id %}
```

## 🔑 Tags e Filtros Comuns do DTL

### Tags

```html
{% if condition %}...{% endif %}
{% for item in lista %}...{% endfor %}
{% extends "base.html" %}
{% include "componente.html" %}
{% url 'view_name' %}
{% csrf_token %}
{% block content %}...{% endblock %}
```

### Filtros

```html
{{ texto|upper }}              <!-- Maiúsculas -->
{{ texto|truncatewords:10 }}   <!-- Truncar palavras -->
{{ numero|floatformat:2 }}     <!-- Formato decimal -->
{{ data|date:"d/m/Y" }}        <!-- Formato data -->
{{ variavel|default:"N/A" }}   <!-- Valor padrão -->
```

## 🎨 Estrutura de Templates

```
projeto/
├── templates/              # Templates globais
│   ├── base.html
│   └── components/
│       ├── header.html
│       └── footer.html
└── app/
    └── templates/         # Templates do app
        └── app/
            ├── lista.html
            └── detalhe.html
```

## 💡 Boas Práticas

1. **Herança de Templates**: Use `{% extends %}` para reutilizar código
2. **Namespaces**: Sempre use namespaces em URLs para evitar conflitos
3. **Reverse URLs**: Use `{% url %}` ao invés de URLs hardcoded
4. **Context Processors**: Use context processors para dados globais
5. **Include**: Use `{% include %}` para componentes reutilizáveis

## 📖 Exercícios Práticos

1. **Exercício 1**: Criar view que lista todos os produtos
2. **Exercício 2**: Criar template base com header e footer
3. **Exercício 3**: Implementar paginação na lista de produtos
4. **Exercício 4**: Criar formulário para adicionar produtos
5. **Exercício 5**: Implementar busca com query parameters
6. **Exercício 6**: Criar múltiplos apps e configurar namespaces

## 🔧 Comandos Úteis

```bash
# Ver todas as URLs do projeto
python manage.py show_urls

# Rodar servidor de desenvolvimento
python manage.py runserver

# Coletar arquivos estáticos
python manage.py collectstatic
```

## 📚 Recursos Adicionais

- [Django Views Documentation](https://docs.djangoproject.com/en/stable/topics/http/views/)
- [Django Templates Documentation](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Django URLs Documentation](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Template Language Reference](https://docs.djangoproject.com/en/stable/ref/templates/language/)

