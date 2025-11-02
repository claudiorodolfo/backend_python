"""
04 - Admin Automático do Django
=================================

Este arquivo demonstra como configurar e customizar o Django Admin.
"""

from django.contrib import admin
from django.utils.html import format_html


# ============================================================================
# REGISTRAR MODEL NO ADMIN (BÁSICO)
# ============================================================================

"""
# No arquivo admin.py do seu app

from django.contrib import admin
from .models import Produto, Categoria

# Registro básico
admin.site.register(Produto)
admin.site.register(Categoria)
"""

# ============================================================================
# CUSTOMIZAÇÃO BÁSICA DO ADMIN
# ============================================================================

# Exemplo de model para demonstrar customizações
class Produto:
    pass


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    """
    Classe para customizar o admin do model Produto.
    """
    # Campos exibidos na listagem
    list_display = ['nome', 'preco', 'categoria', 'ativo', 'data_criacao']
    
    # Campos clicáveis para edição
    list_display_links = ['nome']
    
    # Filtros laterais
    list_filter = ['categoria', 'ativo', 'data_criacao']
    
    # Campo de busca
    search_fields = ['nome', 'descricao']
    
    # Paginação
    list_per_page = 25
    
    # Campos editáveis diretamente na listagem
    list_editable = ['ativo', 'preco']
    
    # Ordenação padrão
    ordering = ['-data_criacao']
    
    # Agrupamento de campos no formulário
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'slug', 'categoria')
        }),
        ('Preço e Estoque', {
            'fields': ('preco', 'quantidade', 'desconto')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )
    
    # Campos somente leitura
    readonly_fields = ['data_criacao', 'data_atualizacao']


# ============================================================================
# ADMIN COM MÉTODOS CUSTOMIZADOS
# ============================================================================

@admin.register(Produto)
class ProdutoAdminAvancado(admin.ModelAdmin):
    list_display = ['nome', 'preco_formatado', 'status_estoque', 'categoria_link']
    list_filter = ['categoria', 'ativo']
    search_fields = ['nome']
    
    def preco_formatado(self, obj):
        """Método customizado para formatar preço"""
        return f"R$ {obj.preco:.2f}"
    preco_formatado.short_description = "Preço"
    
    def status_estoque(self, obj):
        """Método customizado com cores"""
        if obj.quantidade > 10:
            color = 'green'
            status = 'Em Estoque'
        elif obj.quantidade > 0:
            color = 'orange'
            status = 'Estoque Baixo'
        else:
            color = 'red'
            status = 'Sem Estoque'
        
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            status
        )
    status_estoque.short_description = "Status do Estoque"
    
    def categoria_link(self, obj):
        """Link para categoria"""
        if obj.categoria:
            return format_html(
                '<a href="/admin/app/categoria/{}/change/">{}</a>',
                obj.categoria.id,
                obj.categoria.nome
            )
        return "-"
    categoria_link.short_description = "Categoria"


# ============================================================================
# INLINE ADMIN (RELACIONAMENTOS)
# ============================================================================

"""
Para exibir objetos relacionados na mesma página:

from django.contrib import admin
from .models import Categoria, Produto


class ProdutoInline(admin.TabularInline):  # Ou admin.StackedInline
    model = Produto
    extra = 1  # Quantos formulários vazios mostrar
    fields = ['nome', 'preco', 'ativo']
    readonly_fields = ['data_criacao']


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'total_produtos']
    inlines = [ProdutoInline]  # Mostrar produtos dentro da categoria
    
    def total_produtos(self, obj):
        return obj.produtos.count()
    total_produtos.short_description = "Total de Produtos"
"""


# ============================================================================
# ACTIONS PERSONALIZADAS
# ============================================================================

@admin.register(Produto)
class ProdutoAdminComActions(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'ativo']
    actions = ['ativar_produtos', 'desativar_produtos', 'aplicar_desconto']
    
    @admin.action(description='Ativar produtos selecionados')
    def ativar_produtos(self, request, queryset):
        """Action para ativar múltiplos produtos"""
        atualizados = queryset.update(ativo=True)
        self.message_user(
            request,
            f'{atualizados} produto(s) foram ativados.'
        )
    
    @admin.action(description='Desativar produtos selecionados')
    def desativar_produtos(self, request, queryset):
        """Action para desativar múltiplos produtos"""
        atualizados = queryset.update(ativo=False)
        self.message_user(
            request,
            f'{atualizados} produto(s) foram desativados.'
        )
    
    @admin.action(description='Aplicar 10% de desconto')
    def aplicar_desconto(self, request, queryset):
        """Action para aplicar desconto"""
        for produto in queryset:
            produto.preco = produto.preco * 0.9
            produto.save()
        self.message_user(
            request,
            f'Desconto aplicado em {queryset.count()} produto(s).'
        )


# ============================================================================
# ADMIN COM FILTROS PERSONALIZADOS
# ============================================================================

from django.contrib.admin import SimpleListFilter


class ProdutoDisponivelFilter(SimpleListFilter):
    """Filtro customizado para produtos disponíveis"""
    title = 'Disponibilidade'
    parameter_name = 'disponivel'
    
    def lookups(self, request, model_admin):
        return (
            ('sim', 'Disponível'),
            ('nao', 'Indisponível'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'sim':
            return queryset.filter(quantidade__gt=0, ativo=True)
        elif self.value() == 'nao':
            return queryset.filter(
                models.Q(quantidade=0) | models.Q(ativo=False)
            )


@admin.register(Produto)
class ProdutoAdminComFiltro(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'quantidade', 'ativo']
    list_filter = [ProdutoDisponivelFilter, 'categoria']


# ============================================================================
# PERMISSÕES NO ADMIN
# ============================================================================

"""
# No model, definir permissões customizadas

class Produto(models.Model):
    # ... campos ...
    
    class Meta:
        permissions = [
            ('pode_publicar', 'Pode publicar produtos'),
            ('pode_moderar', 'Pode moderar produtos'),
        ]


# No admin, usar has_add_permission, has_change_permission, etc.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.has_perm('app.pode_publicar')
    
    def has_change_permission(self, request, obj=None):
        if obj and not obj.ativo:
            return request.user.has_perm('app.pode_moderar')
        return True
"""


# ============================================================================
# CUSTOMIZAÇÃO VISUAL DO ADMIN
# ============================================================================

"""
# Criar arquivo admin/base_site.html em templates/admin/

{% extends "admin/base.html" %}
{% load static %}

{% block branding %}
<h1 id="site-name">
    <a href="{% url 'admin:index' %}">
        Minha Aplicação - Admin
    </a>
</h1>
{% endblock %}

{% block extrastyle %}
<style>
    #header {
        background-color: #2c3e50;
    }
    .module h2, .module caption {
        background-color: #34495e;
    }
</style>
{% endblock %}


# No settings.py, garantir que o diretório templates está configurado:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Adicionar esta linha
        ...
    },
]
"""


# ============================================================================
# EXEMPLO COMPLETO DE ADMIN CONFIGURADO
# ============================================================================

"""
# admin.py completo

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Produto, Categoria, Cliente, Pedido


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'total_produtos']
    search_fields = ['nome']
    
    def total_produtos(self, obj):
        return obj.produtos.count()
    total_produtos.short_description = "Total de Produtos"


class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 0
    fields = ['nome', 'preco', 'quantidade']
    readonly_fields = ['nome']


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'categoria_link',
        'preco_formatado',
        'quantidade',
        'status',
        'data_criacao'
    ]
    list_filter = ['categoria', 'ativo', 'data_criacao']
    search_fields = ['nome', 'descricao']
    list_editable = ['quantidade']
    readonly_fields = ['data_criacao', 'data_atualizacao', 'imagem_preview']
    
    fieldsets = (
        ('Informações', {
            'fields': ('nome', 'slug', 'categoria')
        }),
        ('Preço', {
            'fields': ('preco', 'desconto')
        }),
        ('Estoque', {
            'fields': ('quantidade', 'ativo')
        }),
        ('Imagem', {
            'fields': ('imagem', 'imagem_preview')
        }),
    )
    
    actions = ['ativar_produtos', 'desativar_produtos']
    
    def categoria_link(self, obj):
        if obj.categoria:
            url = reverse('admin:app_categoria_change', args=[obj.categoria.id])
            return format_html('<a href="{}">{}</a>', url, obj.categoria.nome)
        return "-"
    categoria_link.short_description = "Categoria"
    
    def preco_formatado(self, obj):
        return f"R$ {obj.preco:.2f}"
    preco_formatado.short_description = "Preço"
    
    def status(self, obj):
        if obj.ativo and obj.quantidade > 0:
            return format_html('<span style="color: green;">✓ Ativo</span>')
        return format_html('<span style="color: red;">✗ Inativo</span>')
    
    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html(
                '<img src="{}" style="max-height: 200px;" />',
                obj.imagem.url
            )
        return "Sem imagem"
    imagem_preview.short_description = "Preview"
    
    @admin.action(description='Ativar produtos selecionados')
    def ativar_produtos(self, request, queryset):
        queryset.update(ativo=True)
        self.message_user(request, f'{queryset.count()} produtos ativados.')
    
    @admin.action(description='Desativar produtos selecionados')
    def desativar_produtos(self, request, queryset):
        queryset.update(ativo=False)
        self.message_user(request, f'{queryset.count()} produtos desativados.')
"""

print("Arquivo de referência: Django Admin")
print("Registre seus models no admin.py e acesse /admin após criar superusuário")
print("Execute: python manage.py createsuperuser")

