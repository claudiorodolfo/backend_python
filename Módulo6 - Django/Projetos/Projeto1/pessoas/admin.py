from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o model Pessoa.
    """
    list_display = ['nome', 'email', 'telefone', 'cpf', 'ativo', 'data_criacao']
    list_display_links = ['nome']
    list_filter = ['ativo', 'data_criacao', 'data_nascimento']
    search_fields = ['nome', 'email', 'cpf', 'telefone']
    list_per_page = 25
    list_editable = ['ativo']
    ordering = ['-data_criacao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'email', 'telefone')
        }),
        ('Documentos', {
            'fields': ('cpf', 'data_nascimento')
        }),
        ('Endereço', {
            'fields': ('endereco',)
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['data_criacao', 'data_atualizacao']
