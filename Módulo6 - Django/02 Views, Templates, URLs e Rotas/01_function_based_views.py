"""
01 - Function-Based Views
==========================

Este arquivo demonstra como criar views baseadas em funções no Django.
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# ============================================================================
# VIEW BÁSICA
# ============================================================================

def minha_view(request):
    """
    View mais simples possível.
    Sempre recebe 'request' como primeiro parâmetro.
    """
    return HttpResponse("Olá, esta é minha primeira view!")


def view_com_html(request):
    """View que retorna HTML"""
    html = """
    <html>
        <head><title>Minha View</title></head>
        <body>
            <h1>Bem-vindo!</h1>
            <p>Esta é uma view Django simples.</p>
        </body>
    </html>
    """
    return HttpResponse(html)


# ============================================================================
# VIEW COM PARÂMETROS DA URL
# ============================================================================

def exibir_produto(request, produto_id):
    """
    View que recebe parâmetro da URL.
    URL: /produtos/<produto_id>/
    """
    # Exemplo: buscar produto (simulado)
    # produto = Produto.objects.get(id=produto_id)
    
    return HttpResponse(f"Produto ID: {produto_id}")


def exibir_usuario(request, username, ano=None):
    """
    View com múltiplos parâmetros (um opcional).
    URL: /usuarios/<username>/ ou /usuarios/<username>/<ano>/
    """
    resposta = f"Usuário: {username}"
    if ano:
        resposta += f" | Ano: {ano}"
    return HttpResponse(resposta)


# ============================================================================
# VIEW COM MÉTODOS HTTP
# ============================================================================

def produto_view(request):
    """
    View que trata diferentes métodos HTTP.
    """
    if request.method == 'GET':
        # Exibir formulário ou dados
        return HttpResponse("Formulário para criar produto")
    
    elif request.method == 'POST':
        # Processar dados do formulário
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        # Salvar produto...
        return HttpResponse(f"Produto {nome} criado com sucesso!")
    
    else:
        return HttpResponse("Método não permitido", status=405)


@require_http_methods(["GET", "POST"])
def produto_seguro(request):
    """
    Decorator que restringe métodos HTTP permitidos.
    """
    if request.method == 'POST':
        return HttpResponse("POST processado")
    return HttpResponse("GET recebido")


# ============================================================================
# VIEW COM CONTEXT E RENDER
# ============================================================================

def home(request):
    """
    View que renderiza template com contexto.
    """
    # Preparar dados para o template
    context = {
        'titulo': 'Página Inicial',
        'mensagem': 'Bem-vindo ao nosso site!',
        'produtos': [
            {'nome': 'Produto 1', 'preco': 100},
            {'nome': 'Produto 2', 'preco': 200},
        ],
    }
    
    # Renderizar template com contexto
    return render(request, 'home.html', context)


def lista_produtos(request):
    """
    View que busca dados do banco e passa para template.
    """
    # Simulação: buscar produtos do banco
    # produtos = Produto.objects.filter(ativo=True)
    
    produtos_simulados = [
        {'id': 1, 'nome': 'Notebook', 'preco': 2500.00},
        {'id': 2, 'nome': 'Mouse', 'preco': 50.00},
        {'id': 3, 'nome': 'Teclado', 'preco': 150.00},
    ]
    
    context = {
        'produtos': produtos_simulados,
        'titulo': 'Lista de Produtos',
    }
    
    return render(request, 'produtos/lista.html', context)


# ============================================================================
# VIEW COM get_object_or_404
# ============================================================================

def detalhe_produto(request, produto_id):
    """
    View que busca objeto ou retorna 404.
    """
    # get_object_or_404 busca o objeto ou retorna 404 automaticamente
    # produto = get_object_or_404(Produto, id=produto_id)
    
    # Exemplo manual de tratamento de erro:
    try:
        # produto = Produto.objects.get(id=produto_id)
        produto_simulado = {'id': produto_id, 'nome': 'Produto Exemplo', 'preco': 100.00}
    except:
        raise Http404("Produto não encontrado")
    
    context = {
        'produto': produto_simulado,
    }
    
    return render(request, 'produtos/detalhe.html', context)


# ============================================================================
# VIEW COM REDIRECT
# ============================================================================

def criar_produto(request):
    """
    View que processa POST e redireciona após sucesso.
    """
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        
        # Criar produto no banco
        # produto = Produto.objects.create(nome=nome, preco=preco)
        
        # Redirecionar após criação
        return redirect('produtos:lista')  # Usando namespace
        # Ou: return redirect('/produtos/')
        # Ou: return redirect('detalhe_produto', produto_id=1)
    
    # Se GET, exibir formulário
    return render(request, 'produtos/criar.html')


# ============================================================================
# VIEW COM JSON
# ============================================================================

def api_produtos(request):
    """
    View que retorna JSON (útil para APIs).
    """
    produtos = [
        {'id': 1, 'nome': 'Notebook', 'preco': 2500.00},
        {'id': 2, 'nome': 'Mouse', 'preco': 50.00},
    ]
    
    return JsonResponse({'produtos': produtos})


def api_produto_detalhe(request, produto_id):
    """
    API que retorna detalhe de um produto.
    """
    produto = {
        'id': produto_id,
        'nome': 'Produto Exemplo',
        'preco': 100.00,
        'descricao': 'Descrição do produto',
    }
    
    return JsonResponse(produto)


# ============================================================================
# VIEW COM PAGINAÇÃO
# ============================================================================

def produtos_paginados(request):
    """
    View que implementa paginação.
    """
    # Simulação: todos os produtos
    # todos_produtos = Produto.objects.all()
    
    todos_produtos = [f'Produto {i}' for i in range(1, 101)]  # 100 produtos
    
    # Criar paginador (25 itens por página)
    paginator = Paginator(todos_produtos, 25)
    
    # Obter número da página da URL (?page=2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'produtos': page_obj,
    }
    
    return render(request, 'produtos/lista_paginada.html', context)


# ============================================================================
# VIEW COM DECORATORS DE AUTENTICAÇÃO
# ============================================================================

@login_required
def area_restrita(request):
    """
    View que requer login.
    Usuário não logado será redirecionado para login.
    """
    return render(request, 'area_restrita.html', {
        'usuario': request.user,
    })


@login_required(login_url='/login/')
def area_restrita_customizada(request):
    """
    View com URL de login customizada.
    """
    return HttpResponse(f"Olá, {request.user.username}!")


# ============================================================================
# VIEW COM TRATAMENTO DE ERROS
# ============================================================================

def processar_formulario(request):
    """
    View com tratamento de erros.
    """
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        
        # Validação
        erros = []
        
        if not nome:
            erros.append('Nome é obrigatório')
        
        if not email or '@' not in email:
            erros.append('Email inválido')
        
        if erros:
            # Retornar formulário com erros
            context = {
                'erros': erros,
                'nome': nome,
                'email': email,
            }
            return render(request, 'formulario.html', context)
        
        # Se sem erros, processar
        # salvar_dados(nome, email)
        return redirect('sucesso')
    
    return render(request, 'formulario.html')


# ============================================================================
# VIEW COM QUERY PARAMETERS
# ============================================================================

def buscar_produtos(request):
    """
    View que processa query parameters (?q=termo&categoria=eletronico).
    """
    # Obter parâmetros da URL
    termo = request.GET.get('q', '')  # Valor padrão: string vazia
    categoria = request.GET.get('categoria', '')
    
    # Buscar produtos (simulado)
    # produtos = Produto.objects.filter(nome__icontains=termo)
    # if categoria:
    #     produtos = produtos.filter(categoria__nome=categoria)
    
    produtos = [
        {'nome': f'Produto com {termo}', 'categoria': categoria or 'geral'}
    ]
    
    context = {
        'produtos': produtos,
        'termo': termo,
        'categoria': categoria,
    }
    
    return render(request, 'produtos/busca.html', context)


# ============================================================================
# VIEW COM MENSAGENS
# ============================================================================

from django.contrib import messages


def criar_produto_com_mensagem(request):
    """
    View que usa sistema de mensagens do Django.
    """
    if request.method == 'POST':
        nome = request.POST.get('nome')
        
        if nome:
            # Criar produto...
            messages.success(request, f'Produto {nome} criado com sucesso!')
            return redirect('produtos:lista')
        else:
            messages.error(request, 'Nome é obrigatório')
    
    return render(request, 'produtos/criar.html')


# ============================================================================
# EXEMPLO COMPLETO: CRUD DE PRODUTOS
# ============================================================================

def lista_produtos_view(request):
    """Listar todos os produtos"""
    # produtos = Produto.objects.all()
    produtos = []
    return render(request, 'produtos/lista.html', {'produtos': produtos})


def criar_produto_view(request):
    """Criar novo produto"""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        
        # produto = Produto.objects.create(nome=nome, preco=preco)
        messages.success(request, 'Produto criado!')
        return redirect('produtos:lista')
    
    return render(request, 'produtos/form.html')


def atualizar_produto_view(request, produto_id):
    """Atualizar produto existente"""
    # produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        
        # produto.nome = nome
        # produto.preco = preco
        # produto.save()
        
        messages.success(request, 'Produto atualizado!')
        return redirect('produtos:detalhe', produto_id=produto_id)
    
    # produto = {'id': produto_id, 'nome': 'Exemplo', 'preco': 100}
    context = {'produto': {}}
    return render(request, 'produtos/form.html', context)


def deletar_produto_view(request, produto_id):
    """Deletar produto"""
    # produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        # produto.delete()
        messages.success(request, 'Produto deletado!')
        return redirect('produtos:lista')
    
    # context = {'produto': produto}
    return render(request, 'produtos/confirmar_delete.html', {'produto_id': produto_id})


print("Arquivo de exemplo: Function-Based Views")
print("Estas views devem ser conectadas através de URLs para funcionar")

