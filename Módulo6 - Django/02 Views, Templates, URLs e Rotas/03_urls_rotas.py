"""
03 - Configuração de URLConf, Namespaces e Reverse URLs
========================================================

Este arquivo demonstra como configurar URLs no Django.
"""

from django.urls import path, re_path, include
from django.contrib import admin
from . import views

# ============================================================================
# URLCONF PRINCIPAL (projeto/urls.py)
# ============================================================================

"""
# projeto/urls.py - URLConf principal

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Incluir URLs do app
    path('produtos/', include('produtos.urls', namespace='produtos')),
]
"""

# ============================================================================
# URLCONF BÁSICO (app/urls.py)
# ============================================================================

"""
# app/urls.py - URLs do app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]
"""

# ============================================================================
# URLs COM PARÂMETROS
# ============================================================================

"""
# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Parâmetro inteiro
    path('produto/<int:produto_id>/', views.detalhe_produto, name='detalhe'),
    
    # Parâmetro string
    path('usuario/<str:username>/', views.perfil_usuario, name='perfil'),
    
    # Parâmetro slug (aceita letras, números, hífens e underscores)
    path('artigo/<slug:slug>/', views.artigo, name='artigo'),
    
    # Parâmetro UUID
    path('pedido/<uuid:pedido_id>/', views.detalhe_pedido, name='pedido'),
    
    # Parâmetro path (captura toda a URL restante)
    path('arquivo/<path:file_path>/', views.servir_arquivo, name='arquivo'),
    
    # Múltiplos parâmetros
    path('categoria/<int:categoria_id>/produto/<int:produto_id>/', 
         views.produto_por_categoria, name='produto_categoria'),
]
"""

# ============================================================================
# URLs COM PARÂMETROS OPCIONAIS
# ============================================================================

"""
# URLs com parâmetros opcionais (usando múltiplas rotas)

urlpatterns = [
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:ano>/', views.lista_produtos_ano, name='lista_ano'),
    path('produtos/<int:ano>/<int:mes>/', views.lista_produtos_mes, name='lista_mes'),
]
"""

# ============================================================================
# URLs COM EXPRESSÕES REGULARES (re_path)
# ============================================================================

"""
# Usar re_path para mais controle

from django.urls import re_path

urlpatterns = [
    # Aceita apenas números
    re_path(r'^produto/(?P<produto_id>[0-9]+)/$', views.detalhe_produto, name='detalhe'),
    
    # Aceita apenas letras
    re_path(r'^usuario/(?P<username>[a-zA-Z]+)/$', views.perfil_usuario, name='perfil'),
    
    # Aceita números e letras
    re_path(r'^artigo/(?P<slug>[a-zA-Z0-9_-]+)/$', views.artigo, name='artigo'),
    
    # Ano e mês (4 dígitos e 2 dígitos)
    re_path(r'^blog/(?P<ano>[0-9]{4})/(?P<mes>[0-9]{2})/$', views.posts_mes, name='posts'),
]
"""

# ============================================================================
# NAMESPACES E INCLUDE
# ============================================================================

"""
# projeto/urls.py - Definir namespace ao incluir

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contas/', include('contas.urls', namespace='contas')),
]


# produtos/urls.py - Definir app_name para namespace

from django.urls import path
from . import views

app_name = 'produtos'  # Define o namespace

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('criar/', views.criar, name='criar'),
]


# Uso nos templates (com namespace):
{% url 'produtos:lista' %}
{% url 'produtos:detalhe' produto_id=1 %}

# Uso em Python (views):
from django.urls import reverse
url = reverse('produtos:lista')
url = reverse('produtos:detalhe', args=[1])
url = reverse('produtos:detalhe', kwargs={'produto_id': 1})
"""

# ============================================================================
# REVERSE URLs EM VIEWS E TEMPLATES
# ============================================================================

"""
# Em views.py

from django.shortcuts import redirect
from django.urls import reverse

def minha_view(request):
    # Redirecionar usando reverse
    return redirect(reverse('produtos:lista'))
    
    # Com parâmetros posicionais
    return redirect(reverse('produtos:detalhe', args=[1]))
    
    # Com parâmetros nomeados
    return redirect(reverse('produtos:detalhe', kwargs={'produto_id': 1}))


# Em templates (template.html)

<!-- URL simples -->
<a href="{% url 'home' %}">Home</a>

<!-- URL com namespace -->
<a href="{% url 'produtos:lista' %}">Produtos</a>

<!-- URL com parâmetro -->
<a href="{% url 'produtos:detalhe' produto_id=1 %}">Produto 1</a>
<a href="{% url 'produtos:detalhe' 1 %}">Produto 1 (alternativo)</a>

<!-- URL com múltiplos parâmetros -->
<a href="{% url 'blog:post' ano=2024 mes=3 %}">Posts de Março</a>
"""

# ============================================================================
# EXEMPLO COMPLETO: MÚLTIPLOS APPS
# ============================================================================

"""
# Estrutura do projeto:
projeto/
├── projeto/
│   └── urls.py          # URLs principal
├── produtos/
│   ├── urls.py
│   ├── views.py
│   └── ...
├── blog/
│   ├── urls.py
│   ├── views.py
│   └── ...
└── contas/
    ├── urls.py
    ├── views.py
    └── ...


# projeto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),  # Página inicial
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('contas/', include('contas.urls', namespace='contas')),
]


# produtos/urls.py

from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('criar/', views.criar, name='criar'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('<int:id>/editar/', views.editar, name='editar'),
    path('<int:id>/deletar/', views.deletar, name='deletar'),
    path('buscar/', views.buscar, name='buscar'),
    path('categoria/<int:categoria_id>/', views.por_categoria, name='categoria'),
]


# blog/urls.py

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.lista_posts, name='lista'),
    path('<slug:slug>/', views.detalhe_post, name='detalhe'),
    path('categoria/<slug:categoria>/', views.por_categoria, name='categoria'),
    path('autor/<str:autor>/', views.por_autor, name='autor'),
]


# contas/urls.py

from django.urls import path
from . import views

app_name = 'contas'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
]
"""

# ============================================================================
# PREFIXOS DE URL
# ============================================================================

"""
# Adicionar prefixo comum para todas as rotas de um app

# projeto/urls.py
urlpatterns = [
    path('api/v1/', include([
        path('produtos/', include('produtos.urls')),
        path('pedidos/', include('pedidos.urls')),
    ])),
]

# URLs resultantes:
# /api/v1/produtos/
# /api/v1/produtos/<id>/
# /api/v1/pedidos/
"""

# ============================================================================
# REDIRECIONAMENTOS EM URLs
# ============================================================================

"""
# Redirecionar URL antiga para nova

from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # Redirecionar permanente (301)
    path('produto/<int:id>/', RedirectView.as_view(
        url='/produtos/<int:id>/',
        permanent=True
    )),
    
    # Redirecionar temporário (302)
    path('old/', RedirectView.as_view(url='/new/', permanent=False)),
    
    # Redirecionar para view
    path('old-path/', RedirectView.as_view(pattern_name='nova_view')),
]
"""

# ============================================================================
# URLs COM VIEWS INLINE
# ============================================================================

"""
# Definir view diretamente na URL (não recomendado para views complexas)

from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('simples/', lambda request: HttpResponse("Olá!")),
    
    path('exemplo/', lambda request, nome: HttpResponse(f"Olá, {nome}!"), 
         {'nome': 'Mundo'}),
]
"""

# ============================================================================
# ORDEM DAS URLs (IMPORTANTE!)
# ============================================================================

"""
# IMPORTANTE: Django testa URLs na ordem definida!
# URLs mais específicas devem vir antes das genéricas.

# ❌ ERRADO (nunca vai acessar 'criar', sempre vai para 'detalhe')
urlpatterns = [
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('criar/', views.criar, name='criar'),  # Nunca será acessado!
]

# ✅ CORRETO (URLs específicas primeiro)
urlpatterns = [
    path('criar/', views.criar, name='criar'),  # Específico primeiro
    path('<int:id>/', views.detalhe, name='detalhe'),  # Genérico depois
]
"""

# ============================================================================
# DEBUGGING URLs
# ============================================================================

"""
# Comando útil para ver todas as URLs do projeto
python manage.py show_urls

# Ou instalar django-extensions
pip install django-extensions

# Adicionar ao INSTALLED_APPS:
INSTALLED_APPS = [
    ...
    'django_extensions',
]

# Executar:
python manage.py show_urls
"""

# ============================================================================
# EXEMPLO PRÁTICO COMPLETO
# ============================================================================

"""
# projeto/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('produtos/', include('produtos.urls', namespace='produtos')),
    path('pedidos/', include('pedidos.urls', namespace='pedidos')),
    path('contas/', include('contas.urls', namespace='contas')),
]

# Servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# produtos/urls.py

from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    # Listagem
    path('', views.lista, name='lista'),
    path('buscar/', views.buscar, name='buscar'),
    
    # CRUD
    path('criar/', views.criar, name='criar'),
    path('<int:id>/', views.detalhe, name='detalhe'),
    path('<int:id>/editar/', views.editar, name='editar'),
    path('<int:id>/deletar/', views.deletar, name='deletar'),
    
    # Categorias
    path('categoria/<int:categoria_id>/', views.por_categoria, name='categoria'),
    path('categoria/<slug:slug>/', views.por_categoria_slug, name='categoria_slug'),
]


# Uso em views.py (produtos/views.py)

from django.shortcuts import render, redirect
from django.urls import reverse

def criar_produto(request):
    if request.method == 'POST':
        # ... processar formulário ...
        return redirect(reverse('produtos:detalhe', kwargs={'id': produto.id}))
    return render(request, 'produtos/form.html')


# Uso em templates (produtos/lista.html)

{% url 'produtos:lista' %}
{% url 'produtos:criar' %}
{% url 'produtos:detalhe' produto.id %}
{% url 'produtos:editar' produto.id %}
{% url 'produtos:categoria' categoria.id %}
"""

print("Arquivo de referência: URLs e Roteamento")
print("Configure suas URLs seguindo os padrões acima")

