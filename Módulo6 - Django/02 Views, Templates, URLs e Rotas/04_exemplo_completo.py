"""
04 - Exemplo Completo: Views, Templates e URLs Integrados
==========================================================

Este arquivo demonstra um exemplo completo integrando views, templates e URLs.
"""

# ============================================================================
# ESTRUTURA DO PROJETO
# ============================================================================

"""
projeto/
├── projeto/
│   ├── settings.py
│   └── urls.py
├── produtos/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── produtos/
│   │       ├── base.html
│   │       ├── lista.html
│   │       ├── detalhe.html
│   │       └── form.html
│   └── ...
└── manage.py
"""

# ============================================================================
# 1. MODELS (produtos/models.py)
# ============================================================================

"""
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.nome
"""

# ============================================================================
# 2. VIEWS (produtos/views.py)
# ============================================================================

"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Produto, Categoria

def lista_produtos(request):
    # Buscar produtos
    produtos = Produto.objects.filter(ativo=True)
    
    # Filtro por categoria (query parameter)
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)
    
    # Busca por nome
    busca = request.GET.get('q')
    if busca:
        produtos = produtos.filter(nome__icontains=busca)
    
    # Paginação
    paginator = Paginator(produtos, 12)  # 12 por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Contexto
    context = {
        'page_obj': page_obj,
        'produtos': page_obj,
        'categorias': Categoria.objects.all(),
        'categoria_atual': int(categoria_id) if categoria_id else None,
        'busca': busca,
    }
    
    return render(request, 'produtos/lista.html', context)


def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id, ativo=True)
    
    context = {
        'produto': produto,
    }
    
    return render(request, 'produtos/detalhe.html', context)


def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        
        # Validação básica
        if not nome or not preco:
            messages.error(request, 'Nome e preço são obrigatórios')
            return render(request, 'produtos/form.html', {
                'categorias': Categoria.objects.all()
            })
        
        # Criar produto
        categoria = get_object_or_404(Categoria, id=categoria_id)
        produto = Produto.objects.create(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria=categoria
        )
        
        messages.success(request, f'Produto {produto.nome} criado com sucesso!')
        return redirect('produtos:detalhe', produto_id=produto.id)
    
    context = {
        'categorias': Categoria.objects.all(),
    }
    
    return render(request, 'produtos/form.html', context)


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.descricao = request.POST.get('descricao')
        produto.categoria_id = request.POST.get('categoria')
        produto.save()
        
        messages.success(request, 'Produto atualizado!')
        return redirect('produtos:detalhe', produto_id=produto.id)
    
    context = {
        'produto': produto,
        'categorias': Categoria.objects.all(),
    }
    
    return render(request, 'produtos/form.html', context)


def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        nome = produto.nome
        produto.delete()
        messages.success(request, f'Produto {nome} deletado!')
        return redirect('produtos:lista')
    
    context = {
        'produto': produto,
    }
    
    return render(request, 'produtos/confirmar_delete.html', context)
"""

# ============================================================================
# 3. URLs (produtos/urls.py)
# ============================================================================

"""
from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista'),
    path('criar/', views.criar_produto, name='criar'),
    path('<int:produto_id>/', views.detalhe_produto, name='detalhe'),
    path('<int:produto_id>/editar/', views.editar_produto, name='editar'),
    path('<int:produto_id>/deletar/', views.deletar_produto, name='deletar'),
]
"""

# ============================================================================
# 4. URLS PRINCIPAL (projeto/urls.py)
# ============================================================================

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls', namespace='produtos')),
]
"""

# ============================================================================
# 5. TEMPLATE BASE (produtos/templates/produtos/base.html)
# ============================================================================

"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Produtos{% endblock %}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; line-height: 1.6; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background: #333; color: white; padding: 1rem; }
        nav a { color: white; text-decoration: none; margin-right: 20px; }
        .messages { padding: 10px; margin: 10px 0; }
        .messages .success { background: #d4edda; color: #155724; }
        .messages .error { background: #f8d7da; color: #721c24; }
        .btn { display: inline-block; padding: 10px 20px; 
               background: #007bff; color: white; text-decoration: none; 
               border-radius: 5px; }
        .btn:hover { background: #0056b3; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); 
                gap: 20px; margin: 20px 0; }
        .card { border: 1px solid #ddd; padding: 15px; border-radius: 5px; }
    </style>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <nav>
            <a href="{% url 'produtos:lista' %}">Home</a>
            <a href="{% url 'produtos:criar' %}">Novo Produto</a>
        </nav>
    </header>
    
    <main class="container">
        {% if messages %}
            <div class="messages">
                {% for message in messages %}
                    <div class="{{ message.tags }}">{{ message }}</div>
                {% endfor %}
            </div>
        {% endif %}
        
        {% block content %}{% endblock %}
    </main>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
"""

# ============================================================================
# 6. TEMPLATE LISTA (produtos/templates/produtos/lista.html)
# ============================================================================

"""
{% extends "produtos/base.html" %}

{% block title %}Lista de Produtos{% endblock %}

{% block content %}
    <h1>Lista de Produtos</h1>
    
    <!-- Busca -->
    <form method="get" style="margin: 20px 0;">
        <input type="text" name="q" value="{{ busca }}" 
               placeholder="Buscar produtos...">
        <button type="submit">Buscar</button>
    </form>
    
    <!-- Filtros de categoria -->
    <div style="margin: 20px 0;">
        <a href="{% url 'produtos:lista' %}" 
           class="btn {% if not categoria_atual %}active{% endif %}">
            Todas
        </a>
        {% for categoria in categorias %}
            <a href="?categoria={{ categoria.id }}" 
               class="btn {% if categoria_atual == categoria.id %}active{% endif %}">
                {{ categoria.nome }}
            </a>
        {% endfor %}
    </div>
    
    <!-- Lista de produtos -->
    {% if produtos %}
        <div class="grid">
            {% for produto in produtos %}
                <div class="card">
                    <h3>{{ produto.nome }}</h3>
                    <p>{{ produto.descricao|truncatewords:15 }}</p>
                    <p><strong>R$ {{ produto.preco|floatformat:2 }}</strong></p>
                    <p>Categoria: {{ produto.categoria.nome }}</p>
                    <a href="{% url 'produtos:detalhe' produto.id %}" class="btn">
                        Ver Detalhes
                    </a>
                </div>
            {% endfor %}
        </div>
        
        <!-- Paginação -->
        {% if page_obj.has_other_pages %}
            <div style="margin: 20px 0; text-align: center;">
                {% if page_obj.has_previous %}
                    <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
                {% endif %}
                
                <span>
                    Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}
                </span>
                
                {% if page_obj.has_next %}
                    <a href="?page={{ page_obj.next_page_number }}">Próxima</a>
                {% endif %}
            </div>
        {% endif %}
    {% else %}
        <p>Nenhum produto encontrado.</p>
    {% endif %}
{% endblock %}
"""

# ============================================================================
# 7. TEMPLATE DETALHE (produtos/templates/produtos/detalhe.html)
# ============================================================================

"""
{% extends "produtos/base.html" %}

{% block title %}{{ produto.nome }}{% endblock %}

{% block content %}
    <div>
        <a href="{% url 'produtos:lista' %}">← Voltar</a>
    </div>
    
    <h1>{{ produto.nome }}</h1>
    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
        <div>
            <p><strong>Preço:</strong> R$ {{ produto.preco|floatformat:2 }}</p>
            <p><strong>Categoria:</strong> {{ produto.categoria.nome }}</p>
            <p><strong>Estoque:</strong> {{ produto.quantidade }} unidades</p>
            <p><strong>Data:</strong> {{ produto.data_criacao|date:"d/m/Y" }}</p>
        </div>
        
        <div>
            <h3>Descrição</h3>
            <p>{{ produto.descricao|linebreaks }}</p>
        </div>
    </div>
    
    <div>
        <a href="{% url 'produtos:editar' produto.id %}" class="btn">Editar</a>
        <a href="{% url 'produtos:deletar' produto.id %}" class="btn" 
           style="background: #dc3545;">Deletar</a>
    </div>
{% endblock %}
"""

# ============================================================================
# 8. TEMPLATE FORMULÁRIO (produtos/templates/produtos/form.html)
# ============================================================================

"""
{% extends "produtos/base.html" %}

{% block title %}
    {% if produto %}Editar{% else %}Criar{% endif %} Produto
{% endblock %}

{% block content %}
    <h1>{% if produto %}Editar{% else %}Criar{% endif %} Produto</h1>
    
    <form method="post" style="max-width: 600px; margin: 20px 0;">
        {% csrf_token %}
        
        <div style="margin: 15px 0;">
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" 
                   value="{{ produto.nome|default:'' }}" 
                   required style="width: 100%; padding: 8px;">
        </div>
        
        <div style="margin: 15px 0;">
            <label for="preco">Preço:</label>
            <input type="number" id="preco" name="preco" step="0.01"
                   value="{{ produto.preco|default:'' }}" 
                   required style="width: 100%; padding: 8px;">
        </div>
        
        <div style="margin: 15px 0;">
            <label for="categoria">Categoria:</label>
            <select id="categoria" name="categoria" 
                    required style="width: 100%; padding: 8px;">
                {% for categoria in categorias %}
                    <option value="{{ categoria.id }}" 
                            {% if produto.categoria.id == categoria.id %}selected{% endif %}>
                        {{ categoria.nome }}
                    </option>
                {% endfor %}
            </select>
        </div>
        
        <div style="margin: 15px 0;">
            <label for="descricao">Descrição:</label>
            <textarea id="descricao" name="descricao" rows="5" 
                      style="width: 100%; padding: 8px;">{{ produto.descricao|default:'' }}</textarea>
        </div>
        
        <div>
            <button type="submit" class="btn">Salvar</button>
            <a href="{% if produto %}{% url 'produtos:detalhe' produto.id %}{% else %}{% url 'produtos:lista' %}{% endif %}" 
               class="btn" style="background: #6c757d;">Cancelar</a>
        </div>
    </form>
{% endblock %}
"""

print("Arquivo de referência: Exemplo Completo Integrado")
print("Este exemplo mostra como integrar Models, Views, Templates e URLs")

