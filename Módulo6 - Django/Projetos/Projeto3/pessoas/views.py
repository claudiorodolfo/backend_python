from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Pessoa
from .forms import PessoaForm


def lista_pessoas(request):
    """
    View para listar todas as pessoas com paginação.
    """
    pessoas_list = Pessoa.objects.all()
    
    # Busca
    busca = request.GET.get('busca', '')
    if busca:
        pessoas_list = pessoas_list.filter(
            nome__icontains=busca
        ) | pessoas_list.filter(
            email__icontains=busca
        ) | pessoas_list.filter(
            cpf__icontains=busca
        )
    
    # Filtro por status
    filtro_ativo = request.GET.get('ativo', '')
    if filtro_ativo == '1':
        pessoas_list = pessoas_list.filter(ativo=True)
    elif filtro_ativo == '0':
        pessoas_list = pessoas_list.filter(ativo=False)
    
    # Paginação
    paginator = Paginator(pessoas_list, 10)  # 10 pessoas por página
    page_number = request.GET.get('page')
    pessoas = paginator.get_page(page_number)
    
    context = {
        'pessoas': pessoas,
        'busca': busca,
        'filtro_ativo': filtro_ativo,
    }
    
    return render(request, 'pessoas/lista.html', context)


def detalhe_pessoa(request, pk):
    """
    View para exibir detalhes de uma pessoa específica.
    """
    pessoa = get_object_or_404(Pessoa, pk=pk)
    context = {
        'pessoa': pessoa,
    }
    return render(request, 'pessoas/detalhe.html', context)


def criar_pessoa(request):
    """
    View para criar uma nova pessoa.
    """
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            pessoa = form.save()
            messages.success(request, f'Pessoa "{pessoa.nome}" criada com sucesso!')
            return redirect('pessoas:detalhe', pk=pessoa.pk)
    else:
        form = PessoaForm()
    
    context = {
        'form': form,
        'titulo': 'Nova Pessoa',
    }
    return render(request, 'pessoas/form.html', context)


def editar_pessoa(request, pk):
    """
    View para editar uma pessoa existente.
    """
    pessoa = get_object_or_404(Pessoa, pk=pk)
    
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            pessoa = form.save()
            messages.success(request, f'Pessoa "{pessoa.nome}" atualizada com sucesso!')
            return redirect('pessoas:detalhe', pk=pessoa.pk)
    else:
        form = PessoaForm(instance=pessoa)
    
    context = {
        'form': form,
        'pessoa': pessoa,
        'titulo': f'Editar Pessoa: {pessoa.nome}',
    }
    return render(request, 'pessoas/form.html', context)


def deletar_pessoa(request, pk):
    """
    View para deletar uma pessoa.
    """
    pessoa = get_object_or_404(Pessoa, pk=pk)
    
    if request.method == 'POST':
        nome = pessoa.nome
        pessoa.delete()
        messages.success(request, f'Pessoa "{nome}" deletada com sucesso!')
        return redirect('pessoas:lista')
    
    context = {
        'pessoa': pessoa,
    }
    return render(request, 'pessoas/deletar.html', context)
