from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Pessoa


def _get_pessoa_form_labels():
    """Retorna os verbose_name dos campos do formul?rio de Pessoa."""
    meta = Pessoa._meta
    return {
        'label_nome': meta.get_field('nome').verbose_name,
        'label_email': meta.get_field('email').verbose_name,
        'label_telefone': meta.get_field('telefone').verbose_name,
        'label_data_nascimento': meta.get_field('data_nascimento').verbose_name,
        'label_cpf': meta.get_field('cpf').verbose_name,
        'label_endereco': meta.get_field('endereco').verbose_name,
        'label_ativo': meta.get_field('ativo').verbose_name,
    }


def lista_pessoas(request):
    """
    View para listar todas as pessoas.
    """
    pessoas = Pessoa.objects.all()
    busca = request.GET.get('busca', '').strip()
    if busca:
        pessoas = pessoas.filter(
            Q(nome__icontains=busca) |
            Q(email__icontains=busca) |
            Q(cpf__icontains=busca)
        )
    meta = Pessoa._meta
    
    context = {
        'pessoas': pessoas,
        'busca': busca,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_email': meta.get_field('email').verbose_name,
        'label_telefone': meta.get_field('telefone').verbose_name,
        'label_ativo': meta.get_field('ativo').verbose_name,
    }
    
    return render(request, 'pessoas/lista.html', context)


def detalhe_pessoa(request, pessoa_id):
    """
    View para exibir detalhes de uma pessoa espec?fica.
    """
    pessoa = Pessoa.objects.get(id=pessoa_id)
    meta = Pessoa._meta
    context = {
        'pessoa': pessoa,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_email': meta.get_field('email').verbose_name,
        'label_telefone': meta.get_field('telefone').verbose_name,
        'label_data_nascimento': meta.get_field('data_nascimento').verbose_name,
        'label_cpf': meta.get_field('cpf').verbose_name,
        'label_endereco': meta.get_field('endereco').verbose_name,
        'label_ativo': meta.get_field('ativo').verbose_name,
        'label_data_criacao': meta.get_field('data_criacao').verbose_name,
        'label_data_atualizacao': meta.get_field('data_atualizacao').verbose_name,
    }
    return render(request, 'pessoas/detalhe.html', context)


def criar_pessoa(request):
    """
    View para criar uma nova pessoa.
    """
    if request.POST:
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        telefone = request.POST.get('telefone', '').strip() or None
        data_nascimento = request.POST.get('data_nascimento') or None
        cpf = request.POST.get('cpf', '').strip() or None
        endereco = request.POST.get('endereco', '').strip() or None
        ativo = request.POST.get('ativo') == 'on'
        
        # Verificar se email j? existe
        if Pessoa.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail j? est? cadastrado.')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa', **_get_pessoa_form_labels()})
        
        # Verificar se CPF j? existe (se fornecido)
        if cpf and Pessoa.objects.filter(cpf=cpf).exists():
            messages.error(request, 'Este CPF j? est? cadastrado.')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa', **_get_pessoa_form_labels()})
        
        try:
            pessoa = Pessoa.objects.create(
                nome=nome,
                email=email,
                telefone=telefone,
                data_nascimento=data_nascimento,
                cpf=cpf,
                endereco=endereco,
                ativo=ativo
            )
            messages.success(request, f'Pessoa "{pessoa.nome}" criada com sucesso!')
            return redirect('pessoas:detalhe', pessoa_id=pessoa.id)
        except Exception as e:
            messages.error(request, f'Erro ao criar pessoa: {str(e)}')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa', **_get_pessoa_form_labels()})
    
    context = {
        'titulo': 'Nova Pessoa',
        **_get_pessoa_form_labels(),
    }
    return render(request, 'pessoas/form.html', context)


def editar_pessoa(request, pessoa_id):
    """
    View para editar uma pessoa existente.
    """
    pessoa = Pessoa.objects.get(id=pessoa_id)
    
    if request.POST:
        nome = request.POST.get('nome', '').strip()
        email = request.POST.get('email', '').strip()
        telefone = request.POST.get('telefone', '').strip() or None
        data_nascimento = request.POST.get('data_nascimento') or None
        cpf = request.POST.get('cpf', '').strip() or None
        endereco = request.POST.get('endereco', '').strip() or None
        ativo = request.POST.get('ativo') == 'on'
        
        # Verificar se email j? existe (exceto o atual)
        if Pessoa.objects.filter(email=email).exclude(id=pessoa.id).exists():
            messages.error(request, 'Este e-mail j? est? cadastrado.')
            return render(request, 'pessoas/form.html', {
                'pessoa': pessoa,
                'titulo': f'Editar Pessoa: {pessoa.nome}',
                **_get_pessoa_form_labels(),
            })
        
        # Verificar se CPF j? existe (se fornecido, exceto o atual)
        if cpf and Pessoa.objects.filter(cpf=cpf).exclude(id=pessoa.id).exists():
            messages.error(request, 'Este CPF j? est? cadastrado.')
            return render(request, 'pessoas/form.html', {
                'pessoa': pessoa,
                'titulo': f'Editar Pessoa: {pessoa.nome}',
                **_get_pessoa_form_labels(),
            })
        
        try:
            pessoa.nome = nome
            pessoa.email = email
            pessoa.telefone = telefone
            pessoa.data_nascimento = data_nascimento
            pessoa.cpf = cpf
            pessoa.endereco = endereco
            pessoa.ativo = ativo
            pessoa.save()
            messages.success(request, f'Pessoa "{pessoa.nome}" atualizada com sucesso!')
            return redirect('pessoas:detalhe', pessoa_id=pessoa.id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar pessoa: {str(e)}')
            return render(request, 'pessoas/form.html', {
                'pessoa': pessoa,
                'titulo': f'Editar Pessoa: {pessoa.nome}',
                **_get_pessoa_form_labels(),
            })
    
    context = {
        'pessoa': pessoa,
        'titulo': f'Editar Pessoa: {pessoa.nome}',
        **_get_pessoa_form_labels(),
    }
    return render(request, 'pessoas/form.html', context)


def deletar_pessoa(request, pessoa_id):
    """
    View para deletar uma pessoa.
    """
    pessoa = Pessoa.objects.get(id=pessoa_id)
    
    if request.POST:
        nome = pessoa.nome
        pessoa.delete()
        messages.success(request, f'Pessoa "{nome}" deletada com sucesso!')
        return redirect('pessoas:lista')
    
    meta = Pessoa._meta
    context = {
        'pessoa': pessoa,
        'label_nome': meta.get_field('nome').verbose_name,
        'label_email': meta.get_field('email').verbose_name,
    }
    return render(request, 'pessoas/deletar.html', context)
