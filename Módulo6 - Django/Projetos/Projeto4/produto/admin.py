from django.contrib import admin
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'preco', 'estoque', 'ativo', 'data_criacao']
    list_display_links = ['nome']
    list_filter = ['ativo', 'categoria', 'data_criacao']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativo']
    ordering = ['-data_criacao']
    readonly_fields = ['data_criacao']
