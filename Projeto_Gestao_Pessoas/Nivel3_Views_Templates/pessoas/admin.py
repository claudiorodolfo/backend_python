from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Pessoa.
    """
    list_display = ['nome', 'cpf', 'email', 'telefone', 'data_nascimento', 'idade', 'ativo']
    list_filter = ['sexo', 'estado_civil', 'ativo', 'cidade', 'estado']
    search_fields = ['nome', 'cpf', 'email', 'telefone']
    readonly_fields = ['data_cadastro', 'data_atualizacao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'cpf', 'email', 'telefone')
        }),
        ('Dados Pessoais', {
            'fields': ('data_nascimento', 'sexo', 'estado_civil')
        }),
        ('Endereço', {
            'fields': ('endereco', 'cidade', 'estado', 'cep')
        }),
        ('Controle', {
            'fields': ('ativo', 'observacoes', 'data_cadastro', 'data_atualizacao')
        }),
    )
