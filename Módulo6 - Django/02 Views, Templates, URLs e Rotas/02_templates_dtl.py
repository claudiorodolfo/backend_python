"""
02 - Templates HTML com Django Template Language (DTL)
======================================================

Este arquivo demonstra como usar Django Template Language nos templates.
"""

# ============================================================================
# CONFIGURAÇÃO DE TEMPLATES NO SETTINGS.PY
# ============================================================================

"""
# No settings.py:

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Diretório global de templates
        ],
        'APP_DIRS': True,  # Buscar templates em cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.auth',
                'django.template.context.processors.messages',
            ],
        },
    },
]

Estrutura de pastas:
projeto/
├── templates/           # Templates globais
│   └── base.html
└── app/
    └── templates/      # Templates do app
        └── app/
            └── lista.html
"""

# ============================================================================
# TEMPLATE BASE COM HERANÇA
# ============================================================================

"""
# templates/base.html

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Meu Site{% endblock %}</title>
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a>
            <a href="/produtos/">Produtos</a>
            <a href="/contato/">Contato</a>
        </nav>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Meu Site</p>
    </footer>
    
    {% block extra_js %}{% endblock %}
</body>
</html>
"""

# ============================================================================
# TEMPLATE QUE HERDA DO BASE
# ============================================================================

"""
# templates/home.html

{% extends "base.html" %}

{% block title %}Página Inicial - Meu Site{% endblock %}

{% block content %}
    <h1>Bem-vindo ao Meu Site!</h1>
    <p>Esta é a página inicial.</p>
{% endblock %}
"""

# ============================================================================
# VARIÁVEIS E FILTROS
# ============================================================================

"""
# Template com variáveis do contexto

{% extends "base.html" %}

{% block content %}
    <h1>{{ titulo }}</h1>
    <p>{{ mensagem }}</p>
    
    <!-- Filtros -->
    <p>Nome em maiúsculas: {{ nome|upper }}</p>
    <p>Nome em minúsculas: {{ nome|lower }}</p>
    <p>Primeiras letras maiúsculas: {{ nome|title }}</p>
    
    <!-- Filtros de data -->
    <p>Data: {{ data_criacao|date:"d/m/Y" }}</p>
    <p>Data e hora: {{ data_criacao|date:"d/m/Y H:i" }}</p>
    
    <!-- Filtros numéricos -->
    <p>Preço: R$ {{ preco|floatformat:2 }}</p>
    <p>Quantidade: {{ quantidade|default:"Indisponível" }}</p>
    
    <!-- Filtros de texto -->
    <p>Texto truncado: {{ descricao|truncatewords:20 }}</p>
    <p>Primeiras palavras: {{ descricao|truncatewords:10 }}</p>
    
    <!-- Verificar se variável existe -->
    {% if usuario %}
        <p>Usuário: {{ usuario.username }}</p>
    {% endif %}
{% endblock %}
"""

# ============================================================================
# TAGS DE CONTROLE (IF, FOR)
# ============================================================================

"""
# templates/produtos/lista.html

{% extends "base.html" %}

{% block content %}
    <h1>Lista de Produtos</h1>
    
    <!-- IF/ELIF/ELSE -->
    {% if produtos %}
        <p>Total de produtos: {{ produtos|length }}</p>
    {% else %}
        <p>Nenhum produto encontrado.</p>
    {% endif %}
    
    <!-- FOR loop -->
    <ul>
        {% for produto in produtos %}
            <li>
                {{ produto.nome }} - R$ {{ produto.preco|floatformat:2 }}
                {% if produto.desconto %}
                    <span style="color: red;">
                        Desconto: {{ produto.desconto }}%
                    </span>
                {% endif %}
            </li>
        {% empty %}
            <li>Nenhum produto disponível.</li>
        {% endfor %}
    </ul>
    
    <!-- FOR com índice -->
    <ol>
        {% for produto in produtos %}
            <li>
                #{{ forloop.counter }} - {{ produto.nome }}
                {% if forloop.first %}
                    <strong>(Primeiro)</strong>
                {% endif %}
                {% if forloop.last %}
                    <strong>(Último)</strong>
                {% endif %}
            </li>
        {% endfor %}
    </ol>
    
    <!-- Variáveis do loop -->
    <ul>
        {% for item in lista %}
            <li>
                Índice: {{ forloop.counter0 }}
                Reverso: {{ forloop.revcounter }}
                Total: {{ forloop.counter }} de {{ forloop.parentloop.counter }}
            </li>
        {% endfor %}
    </ul>
{% endblock %}
"""

# ============================================================================
# TAGS DE URL E REVERSE
# ============================================================================

"""
# templates/nav.html

{% load static %}

<nav>
    <!-- URL hardcoded (não recomendado) -->
    <a href="/">Home</a>
    
    <!-- URL com tag url (recomendado) -->
    <a href="{% url 'home' %}">Home</a>
    
    <!-- URL com namespace -->
    <a href="{% url 'produtos:lista' %}">Produtos</a>
    
    <!-- URL com parâmetros -->
    <a href="{% url 'produtos:detalhe' produto_id=1 %}">Produto 1</a>
    <a href="{% url 'produtos:detalhe' 1 %}">Produto 1 (alternativo)</a>
    
    <!-- URL com múltiplos parâmetros -->
    <a href="{% url 'usuario:perfil' username='joao' ano=2024 %}">Perfil</a>
</nav>
"""

# ============================================================================
# ARQUIVOS ESTÁTICOS (CSS, JS, IMAGENS)
# ============================================================================

"""
# templates/base.html

{% load static %}

<!DOCTYPE html>
<html>
<head>
    <!-- CSS -->
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    
    <!-- JavaScript -->
    <script src="{% static 'js/main.js' %}"></script>
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Imagem estática -->
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    
    {% block content %}{% endblock %}
    
    {% block extra_js %}{% endblock %}
</body>
</html>
"""

# ============================================================================
# INCLUSÃO DE TEMPLATES (INCLUDE)
# ============================================================================

"""
# templates/componentes/header.html

<header>
    <h1>Meu Site</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/produtos/">Produtos</a>
    </nav>
</header>


# templates/base.html

{% extends "base.html" %}

{% block content %}
    {% include "componentes/header.html" %}
    
    <main>
        <!-- Conteúdo específico -->
    </main>
    
    {% include "componentes/footer.html" %}
{% endblock %}


# Include com variáveis
{% include "componentes/card.html" with produto=item %}
{% include "componentes/card.html" with produto=item only %}  # Só passa 'produto'
"""

# ============================================================================
# FORMULÁRIOS EM TEMPLATES
# ============================================================================

"""
# templates/produtos/form.html

{% extends "base.html" %}

{% block content %}
    <h1>{% if produto %}Editar{% else %}Criar{% endif %} Produto</h1>
    
    <form method="post">
        {% csrf_token %}
        
        <div>
            <label for="nome">Nome:</label>
            <input type="text" id="nome" name="nome" 
                   value="{{ produto.nome|default:'' }}" required>
        </div>
        
        <div>
            <label for="preco">Preço:</label>
            <input type="number" id="preco" name="preco" step="0.01"
                   value="{{ produto.preco|default:'' }}" required>
        </div>
        
        <button type="submit">Salvar</button>
        <a href="{% url 'produtos:lista' %}">Cancelar</a>
    </form>
{% endblock %}


# Template com Django Forms
{% extends "base.html" %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}  <!-- Renderiza como parágrafos -->
        <button type="submit">Enviar</button>
    </form>
{% endblock %}

<!-- Outras formas de renderizar forms -->
{{ form.as_table }}  <!-- Como tabela -->
{{ form.as_ul }}     <!-- Como lista -->
{{ form.nome }}      <!-- Campo individual -->
{{ form.errors }}    <!-- Erros do formulário -->
"""

# ============================================================================
# MENSAGENS DO DJANGO
# ============================================================================

"""
# templates/base.html

{% if messages %}
    <ul class="messages">
        {% for message in messages %}
            <li class="{{ message.tags }}">
                {{ message }}
            </li>
        {% endfor %}
    </ul>
{% endif %}


# Template mais completo com estilos
{% if messages %}
    <div class="messages">
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }} alert-dismissible">
                {{ message }}
                <button type="button" class="close" data-dismiss="alert">
                    &times;
                </button>
            </div>
        {% endfor %}
    </div>
{% endif %}
"""

# ============================================================================
# FILTROS CUSTOMIZADOS
# ============================================================================

"""
# Criar arquivo: app/templatetags/meus_filtros.py

from django import template

register = template.Library()

@register.filter(name='moeda')
def moeda(valor):
    return f"R$ {valor:,.2f}".replace(',', '.')

@register.filter(name='plural')
def plural(valor, sufixo='s'):
    if valor == 1:
        return ''
    return sufixo


# Uso no template:
{% load meus_filtros %}

<p>Preço: {{ produto.preco|moeda }}</p>
<p>Produto{{ produtos|length|plural }}</p>
"""

# ============================================================================
# TAGS CUSTOMIZADAS
# ============================================================================

"""
# app/templatetags/meus_tags.py

from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def data_atual(format_string="%d/%m/%Y"):
    return datetime.now().strftime(format_string)

@register.inclusion_tag('componentes/card.html')
def card_produto(produto):
    return {'produto': produto}


# Uso no template:
{% load meus_tags %}

<p>Data atual: {% data_atual %}</p>
<p>Data: {% data_atual "%d-%m-%Y %H:%M" %}</p>

{% card_produto produto %}
"""

# ============================================================================
# TEMPLATE COMPLEXO - EXEMPLO COMPLETO
# ============================================================================

"""
# templates/produtos/lista.html

{% extends "base.html" %}
{% load static %}
{% load meus_filtros %}

{% block title %}Produtos - Meu Site{% endblock %}

{% block extra_css %}
    <link rel="stylesheet" href="{% static 'css/produtos.css' %}">
{% endblock %}

{% block content %}
    <div class="container">
        <h1>Lista de Produtos</h1>
        
        <!-- Mensagens -->
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        {% endif %}
        
        <!-- Barra de busca -->
        <form method="get" action="{% url 'produtos:busca' %}">
            <input type="text" name="q" value="{{ request.GET.q }}" 
                   placeholder="Buscar produtos...">
            <button type="submit">Buscar</button>
        </form>
        
        <!-- Filtros -->
        <div class="filtros">
            <a href="?categoria=">Todos</a>
            <a href="?categoria=eletronico">Eletrônicos</a>
            <a href="?categoria=roupa">Roupas</a>
        </div>
        
        <!-- Lista de produtos -->
        {% if produtos %}
            <div class="grid-produtos">
                {% for produto in produtos %}
                    <div class="card-produto">
                        <h3>{{ produto.nome|title }}</h3>
                        <p class="preco">{{ produto.preco|moeda }}</p>
                        {% if produto.desconto %}
                            <span class="badge-desconto">
                                -{{ produto.desconto }}%
                            </span>
                        {% endif %}
                        <a href="{% url 'produtos:detalhe' produto.id %}" 
                           class="btn-ver">Ver Detalhes</a>
                    </div>
                {% endfor %}
            </div>
            
            <!-- Paginação -->
            {% if page_obj.has_other_pages %}
                <div class="paginacao">
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
        
        <!-- Link para criar -->
        {% if user.is_authenticated %}
            <a href="{% url 'produtos:criar' %}" class="btn-criar">
                Criar Novo Produto
            </a>
        {% endif %}
    </div>
{% endblock %}

{% block extra_js %}
    <script src="{% static 'js/produtos.js' %}"></script>
{% endblock %}
"""

# ============================================================================
# FILTROS ÚTEIS DO DJANGO
# ============================================================================

"""
# Filtros de string
{{ texto|length }}              # Tamanho da string
{{ texto|upper }}               # Maiúsculas
{{ texto|lower }}               # Minúsculas
{{ texto|title }}               # Primeira letra maiúscula
{{ texto|capfirst }}            # Primeira letra maiúscula
{{ texto|truncatewords:10 }}    # Trunca palavras
{{ texto|truncatechars:50 }}    # Trunca caracteres
{{ texto|linebreaks }}          # Converte quebras de linha em <br>
{{ texto|linebreaksbr }}        # Adiciona <br> antes de quebras
{{ texto|safe }}                # Marca como HTML seguro (cuidado!)

# Filtros de número
{{ numero|floatformat:2 }}      # Formata decimal
{{ numero|intcomma }}           # Adiciona vírgulas (1,000)
{{ numero|default:"N/A" }}      # Valor padrão

# Filtros de data/hora
{{ data|date:"d/m/Y" }}         # Formato de data
{{ data|time:"H:i" }}           # Formato de hora
{{ data|timesince }}            # "há 2 horas"
{{ data|timeuntil }}            # "em 2 horas"

# Filtros de lista
{{ lista|length }}              # Tamanho da lista
{{ lista|first }}               # Primeiro item
{{ lista|last }}                # Último item
{{ lista|join:", " }}           # Junta com separador
{{ lista|random }}              # Item aleatório

# Outros filtros úteis
{{ variavel|default:"padrão" }} # Valor padrão
{{ variavel|yesno:"sim,não" }}  # True/False para sim/não
{{ variavel|filesizeformat }}   # Formata tamanho de arquivo
"""

print("Arquivo de referência: Django Template Language")
print("Crie os templates HTML seguindo os exemplos acima")

