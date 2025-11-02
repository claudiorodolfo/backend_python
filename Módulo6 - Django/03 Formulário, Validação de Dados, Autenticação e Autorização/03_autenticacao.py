"""
03 - Sistema de Autenticação Embutido
=======================================

Este arquivo demonstra como usar o sistema de autenticação do Django.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# ============================================================================
# LOGIN MANUAL
# ============================================================================

def login_view(request):
    """
    View de login personalizada.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login bem-sucedido
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            
            # Redirecionar para próxima página ou página padrão
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            # Login falhou
            messages.error(request, 'Usuário ou senha inválidos')
    
    return render(request, 'auth/login.html')


# ============================================================================
# LOGOUT
# ============================================================================

@login_required
def logout_view(request):
    """
    View de logout.
    """
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso')
    return redirect('home')


# ============================================================================
# REGISTRO DE USUÁRIO
# ============================================================================

def registro_view(request):
    """
    View de registro de novo usuário.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            # Fazer login automático após registro
            login(request, user)
            
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/registro.html', {'form': form})


# ============================================================================
# VIEWS DE AUTENTICAÇÃO DO DJANGO (Class-Based)
# ============================================================================

"""
# urls.py - Usar views pré-construídas do Django

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


# Customizar views de autenticação

from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True  # Redireciona se já estiver logado
    
    def form_valid(self, form):
        messages.success(self.request, 'Login realizado com sucesso!')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    next_page = 'home'
    
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'Logout realizado com sucesso!')
        return super().dispatch(request, *args, **kwargs)


# urls.py
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]
"""

# ============================================================================
# DECORATOR @login_required
# ============================================================================

"""
# Decorator básico
from django.contrib.auth.decorators import login_required

@login_required
def area_restrita(request):
    return render(request, 'area_restrita.html')


# Com URL de login customizada
@login_required(login_url='/contas/login/')
def area_restrita(request):
    return render(request, 'area_restrita.html')


# Verificar se usuário está logado em template
{% if user.is_authenticated %}
    <p>Olá, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Sair</a>
{% else %}
    <a href="{% url 'login' %}">Entrar</a>
{% endif %}
"""

# ============================================================================
# VERIFICAÇÕES DE PERMISSÃO
# ============================================================================

"""
# Decorator @permission_required
from django.contrib.auth.decorators import permission_required

@permission_required('app.pode_editar_produto', raise_exception=True)
def editar_produto(request, produto_id):
    # Apenas usuários com permissão específica podem acessar
    pass


# Verificar permissão manualmente
from django.core.exceptions import PermissionDenied

def deletar_produto(request, produto_id):
    if not request.user.has_perm('app.pode_deletar_produto'):
        raise PermissionDenied
    
    # Deletar produto


# Verificar permissão em template
{% if perms.app.pode_editar_produto %}
    <a href="{% url 'produtos:editar' produto.id %}">Editar</a>
{% endif %}

{% if user.is_staff %}
    <a href="/admin/">Admin</a>
{% endif %}
"""

# ============================================================================
# MIDDLEWARE DE AUTENTICAÇÃO
# ============================================================================

"""
# settings.py - Já vem configurado por padrão

MIDDLEWARE = [
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]

# Isso permite usar request.user em todas as views
"""

# ============================================================================
# CRIAR E GERENCIAR USUÁRIOS PROGRAMATICAMENTE
# ============================================================================

"""
from django.contrib.auth.models import User

# Criar usuário
user = User.objects.create_user(
    username='joao',
    email='joao@example.com',
    password='senha_segura_123'
)

# Criar superusuário
admin = User.objects.create_superuser(
    username='admin',
    email='admin@example.com',
    password='admin123'
)

# Verificar senha
if user.check_password('senha_segura_123'):
    print("Senha correta!")

# Alterar senha
user.set_password('nova_senha_123')
user.save()

# Verificar se usuário está ativo
if user.is_active:
    print("Usuário está ativo")

# Verificar permissões
if user.is_staff:
    print("Usuário é staff (pode acessar admin)")

if user.is_superuser:
    print("Usuário é superusuário")
"""

# ============================================================================
# INFORMAÇÕES DO USUÁRIO LOGADO
# ============================================================================

"""
# Em views:
def minha_view(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        nome_completo = request.user.get_full_name()
        primeiro_nome = request.user.first_name
        ultimo_nome = request.user.last_name
        
        # Grupos
        grupos = request.user.groups.all()
        
        # Permissões
        todas_permissoes = request.user.get_all_permissions()
        tem_perm = request.user.has_perm('app.pode_editar')
        
        # Verificar se é staff
        if request.user.is_staff:
            # Usuário pode acessar admin
            pass


# Em templates:
{% if user.is_authenticated %}
    <p>Olá, {{ user.get_full_name|default:user.username }}!</p>
    <p>Email: {{ user.email }}</p>
    <p>Último login: {{ user.last_login|date:"d/m/Y H:i" }}</p>
    
    {% if user.is_staff %}
        <a href="/admin/">Área Administrativa</a>
    {% endif %}
    
    {% for group in user.groups.all %}
        <span>{{ group.name }}</span>
    {% endfor %}
{% endif %}
"""

# ============================================================================
# EXEMPLO COMPLETO: SISTEMA DE LOGIN/LOGOUT
# ============================================================================

"""
# urls.py

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
]


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Credenciais inválidas')
    
    return render(request, 'auth/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta')
    return redirect('home')

def registro_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/registro.html', {'form': form})

@login_required
def perfil_view(request):
    return render(request, 'auth/perfil.html', {'user': request.user})


# templates/auth/login.html

{% extends "base.html" %}

{% block content %}
    <h1>Login</h1>
    
    <form method="post">
        {% csrf_token %}
        
        <div>
            <label for="username">Usuário:</label>
            <input type="text" id="username" name="username" required>
        </div>
        
        <div>
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        
        <button type="submit">Entrar</button>
    </form>
    
    <p>Não tem conta? <a href="{% url 'registro' %}">Registre-se</a></p>
{% endblock %}
"""

# ============================================================================
# CONFIGURAÇÕES DE AUTENTICAÇÃO NO SETTINGS.PY
# ============================================================================

"""
# settings.py

# URL para redirecionar após login
LOGIN_URL = '/contas/login/'

# URL para redirecionar após login bem-sucedido
LOGIN_REDIRECT_URL = '/'

# URL para redirecionar após logout
LOGOUT_REDIRECT_URL = '/'

# Tempo de expiração da sessão (em segundos)
SESSION_COOKIE_AGE = 86400  # 24 horas

# Sessão expira quando navegador fecha
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Usar HTTPS em produção para cookies de sessão
SESSION_COOKIE_SECURE = True  # Apenas em produção
SESSION_COOKIE_HTTPONLY = True
"""

print("Arquivo de referência: Sistema de Autenticação")
print("O Django vem com sistema de autenticação completo pronto para usar")

