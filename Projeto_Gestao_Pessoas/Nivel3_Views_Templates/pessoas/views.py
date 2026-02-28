"""
Views para gestão de pessoas.
"""
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Pessoa


def lista_pessoas(request):
    """
    View que lista todas as pessoas cadastradas.
    """
    pessoas = Pessoa.objects.filter(ativo=True).order_by('nome')
    
    # Busca por nome ou CPF
    busca = request.GET.get('busca', '')
    if busca:
        pessoas = pessoas.filter(
            nome__icontains=busca
        ) | pessoas.filter(
            cpf__icontains=busca
        )
    
    context = {
        'pessoas': pessoas,
        'busca': busca,
    }
    
    return render(request, 'pessoas/lista.html', context)


def detalhe_pessoa(request, pessoa_id):
    """
    View que exibe os detalhes de uma pessoa específica.
    """
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    
    context = {
        'pessoa': pessoa,
    }
    
    return render(request, 'pessoas/detalhe.html', context)
