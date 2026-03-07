from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Categoria


def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias,
        'label_nome': Categoria._meta.get_field('nome').verbose_name,
        'label_descricao': Categoria._meta.get_field('descricao').verbose_name,
        'label_ativa': Categoria._meta.get_field('ativa').verbose_name,
    }
    return render(request, 'categoria/lista.html', context)


def detalhe_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    context = {
        'categoria': categoria,
        'label_nome': Categoria._meta.get_field('nome').verbose_name,
        'label_descricao': Categoria._meta.get_field('descricao').verbose_name,
        'label_ativa': Categoria._meta.get_field('ativa').verbose_name,
    }
    return render(request, 'categoria/detalhe.html', context)


def criar_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip() or None
        ativa = request.POST.get('ativa') == 'on'
        if Categoria.objects.filter(nome=nome).exists():
            messages.error(request, 'Já existe uma categoria com este nome.')
            return render(request, 'categoria/form.html', {'titulo': 'Nova Categoria'})
        try:
            cat = Categoria.objects.create(nome=nome, descricao=descricao, ativa=ativa)
            messages.success(request, f'Categoria "{cat.nome}" criada com sucesso!')
            return redirect('categoria:detalhe', id=cat.id)
        except Exception as e:
            messages.error(request, f'Erro ao criar categoria: {str(e)}')
            return render(request, 'categoria/form.html', {'titulo': 'Nova Categoria'})
    return render(request, 'categoria/form.html', {'titulo': 'Nova Categoria'})


def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        descricao = request.POST.get('descricao', '').strip() or None
        ativa = request.POST.get('ativa') == 'on'
        if Categoria.objects.filter(nome=nome).exclude(id=id).exists():
            messages.error(request, 'Já existe outra categoria com este nome.')
            return render(request, 'categoria/form.html', {'categoria': categoria, 'titulo': f'Editar Categoria: {categoria.nome}'})
        try:
            categoria.nome = nome
            categoria.descricao = descricao
            categoria.ativa = ativa
            categoria.save()
            messages.success(request, f'Categoria "{categoria.nome}" atualizada com sucesso!')
            return redirect('categoria:detalhe', id=categoria.id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar: {str(e)}')
            return render(request, 'categoria/form.html', {'categoria': categoria, 'titulo': f'Editar Categoria: {categoria.nome}'})
    return render(request, 'categoria/form.html', {'categoria': categoria, 'titulo': f'Editar Categoria: {categoria.nome}'})


def deletar_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        nome = categoria.nome
        categoria.delete()
        messages.success(request, f'Categoria "{nome}" deletada com sucesso!')
        return redirect('categoria:lista')
    context = {
        'categoria': categoria,
        'label_nome': Categoria._meta.get_field('nome').verbose_name,
    }
    return render(request, 'categoria/deletar.html', context)
