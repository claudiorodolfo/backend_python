from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from categoria.models import Categoria
from .models import Produto


def lista_produtos(request):
    produtos = Produto.objects.select_related('categoria').all()
    context = {
        'produtos': produtos,
        'label_nome': Produto._meta.get_field('nome').verbose_name,
        'label_preco': Produto._meta.get_field('preco').verbose_name,
        'label_estoque': Produto._meta.get_field('estoque').verbose_name,
        'label_categoria': Produto._meta.get_field('categoria').verbose_name,
        'label_ativo': Produto._meta.get_field('ativo').verbose_name,
    }
    return render(request, 'produto/lista.html', context)


def detalhe_produto(request, id):
    produto = get_object_or_404(Produto.objects.select_related('categoria'), pk=id)
    meta = Produto._meta
    context = {
        'produto': produto,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_descricao': meta.get_field('descricao').verbose_name,
        'label_preco': meta.get_field('preco').verbose_name,
        'label_estoque': meta.get_field('estoque').verbose_name,
        'label_categoria': meta.get_field('categoria').verbose_name,
        'label_ativo': meta.get_field('ativo').verbose_name,
        'label_data_criacao': meta.get_field('data_criacao').verbose_name,
    }
    return render(request, 'produto/detalhe.html', context)


def criar_produto(request):
    categorias = Categoria.objects.filter(ativa=True).order_by('nome')
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip() or None
        try:
            preco = Decimal(request.POST.get('preco', '0').replace(',', '.'))
        except (InvalidOperation, ValueError):
            preco = None
        try:
            estoque = int(request.POST.get('estoque', 0))
        except ValueError:
            estoque = 0
        categoria_id = request.POST.get('categoria')
        ativo = request.POST.get('ativo') == 'on'
        if not nome:
            messages.error(request, 'Nome é obrigatório.')
            return render(request, 'produto/form.html', {'titulo': 'Novo Produto', 'categorias': categorias})
        if not categoria_id:
            messages.error(request, 'Selecione uma categoria.')
            return render(request, 'produto/form.html', {'titulo': 'Novo Produto', 'categorias': categorias})
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        if preco is None or preco < 0:
            messages.error(request, 'Preço inválido.')
            return render(request, 'produto/form.html', {'titulo': 'Novo Produto', 'categorias': categorias})
        try:
            prod = Produto.objects.create(
                nome=nome, descricao=descricao, preco=preco, estoque=estoque,
                categoria=categoria, ativo=ativo
            )
            messages.success(request, f'Produto "{prod.nome}" criado com sucesso!')
            return redirect('produto:detalhe', id=prod.id)
        except Exception as e:
            messages.error(request, f'Erro ao criar produto: {str(e)}')
            return render(request, 'produto/form.html', {'titulo': 'Novo Produto', 'categorias': categorias})
    return render(request, 'produto/form.html', {'titulo': 'Novo Produto', 'categorias': categorias})


def editar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    categorias = Categoria.objects.filter(ativa=True).order_by('nome')
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip() or None
        try:
            preco = Decimal(request.POST.get('preco', '0').replace(',', '.'))
        except (InvalidOperation, ValueError):
            preco = None
        try:
            estoque = int(request.POST.get('estoque', 0))
        except ValueError:
            estoque = produto.estoque
        categoria_id = request.POST.get('categoria')
        ativo = request.POST.get('ativo') == 'on'
        if not nome:
            messages.error(request, 'Nome é obrigatório.')
            return render(request, 'produto/form.html', {'produto': produto, 'titulo': f'Editar Produto: {produto.nome}', 'categorias': categorias})
        if not categoria_id:
            messages.error(request, 'Selecione uma categoria.')
            return render(request, 'produto/form.html', {'produto': produto, 'titulo': f'Editar Produto: {produto.nome}', 'categorias': categorias})
        categoria = get_object_or_404(Categoria, pk=categoria_id)
        if preco is None or preco < 0:
            messages.error(request, 'Preço inválido.')
            return render(request, 'produto/form.html', {'produto': produto, 'titulo': f'Editar Produto: {produto.nome}', 'categorias': categorias})
        try:
            produto.nome = nome
            produto.descricao = descricao
            produto.preco = preco
            produto.estoque = estoque
            produto.categoria = categoria
            produto.ativo = ativo
            produto.save()
            messages.success(request, f'Produto "{produto.nome}" atualizado com sucesso!')
            return redirect('produto:detalhe', id=produto.id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar: {str(e)}')
            return render(request, 'produto/form.html', {'produto': produto, 'titulo': f'Editar Produto: {produto.nome}', 'categorias': categorias})
    return render(request, 'produto/form.html', {'produto': produto, 'titulo': f'Editar Produto: {produto.nome}', 'categorias': categorias})


def deletar_produto(request, id):
    produto = get_object_or_404(Produto, pk=id)
    if request.method == 'POST':
        nome = produto.nome
        produto.delete()
        messages.success(request, f'Produto "{nome}" deletado com sucesso!')
        return redirect('produto:lista')
    context = {
        'produto': produto,
        'label_nome': Produto._meta.get_field('nome').verbose_name,
        'label_categoria': Produto._meta.get_field('categoria').verbose_name,
    }
    return render(request, 'produto/deletar.html', context)
