from django.contrib import admin
from .models import Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativa']
    list_display_links = ['nome']
    list_filter = ['ativa']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativa']
    ordering = ['nome']
