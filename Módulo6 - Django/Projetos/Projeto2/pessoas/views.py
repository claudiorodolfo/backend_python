from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pessoa


def lista_pessoas(request):
    """
    View para listar todas as pessoas.
    """
    pessoas = Pessoa.objects.all()
    
    context = {
        'pessoas': pessoas,
    }
    
    return render(request, 'pessoas/lista.html', context)


def detalhe_pessoa(request, pessoa_id):
    """
    View para exibir detalhes de uma pessoa específica.
    """
    pessoa = Pessoa.objects.get(id=pessoa_id)
    context = {
        'pessoa': pessoa,
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
        
        # Verificar se email já existe
        if Pessoa.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa'})
        
        # Verificar se CPF já existe (se fornecido)
        if cpf and Pessoa.objects.filter(cpf=cpf).exists():
            messages.error(request, 'Este CPF já está cadastrado.')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa'})
        
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
            return redirect('pessoas:detalhe', id=pessoa.id)
        except Exception as e:
            messages.error(request, f'Erro ao criar pessoa: {str(e)}')
            return render(request, 'pessoas/form.html', {'titulo': 'Nova Pessoa'})
    
    context = {
        'titulo': 'Nova Pessoa',
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
        
        # Verificar se email já existe (exceto o atual)
        if Pessoa.objects.filter(email=email).exclude(id=pessoa.id).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return render(request, 'pessoas/form.html', {
                'pessoa': pessoa,
                'titulo': f'Editar Pessoa: {pessoa.nome}'
            })
        
        # Verificar se CPF já existe (se fornecido, exceto o atual)
        if cpf and Pessoa.objects.filter(cpf=cpf).exclude(id=pessoa.id).exists():
            messages.error(request, 'Este CPF já está cadastrado.')
            return render(request, 'pessoas/form.html', {
                'pessoa': pessoa,
                'titulo': f'Editar Pessoa: {pessoa.nome}'
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
            return redirect('pessoas:detalhe', id=pessoa.id)
        except Exception as e:
            messages.error(request, f'Erro ao atualizar pessoa: {str(e)}')
            return render(request, 'pessoas/form.html', {
                'pessoa': pessoa,
                'titulo': f'Editar Pessoa: {pessoa.nome}'
            })
    
    context = {
        'pessoa': pessoa,
        'titulo': f'Editar Pessoa: {pessoa.nome}',
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
    
    context = {
        'pessoa': pessoa,
    }
    return render(request, 'pessoas/deletar.html', context)
