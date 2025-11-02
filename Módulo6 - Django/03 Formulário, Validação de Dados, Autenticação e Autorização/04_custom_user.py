"""
04 - Customização de Usuários
=============================

Este arquivo demonstra como criar modelos de usuário customizados no Django.
"""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# ============================================================================
# IMPORTANTE: Custom User Model deve ser criado ANTES das migrations iniciais
# ============================================================================

"""
PASSO 1: Criar o modelo ANTES de executar migrate pela primeira vez
PASSO 2: Configurar AUTH_USER_MODEL no settings.py
PASSO 3: Criar e aplicar migrations
"""


# ============================================================================
# USER MANAGER CUSTOMIZADO
# ============================================================================

class CustomUserManager(BaseUserManager):
    """
    Manager customizado para o modelo de usuário.
    Define como criar usuários normais e superusuários.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva um usuário comum.
        """
        if not email:
            raise ValueError('O email é obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e salva um superusuário.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True')
        
        return self.create_user(email, password, **extra_fields)


# ============================================================================
# MODEL DE USUÁRIO CUSTOMIZADO (HERDANDO DE AbstractUser)
# ============================================================================

class CustomUser(AbstractUser):
    """
    Modelo de usuário customizado que herda de AbstractUser.
    Usa email como campo de login ao invés de username.
    """
    
    # Remover username, usar email como identificador único
    username = None
    email = models.EmailField(unique=True)
    
    # Campos adicionais
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    endereco = models.TextField(blank=True)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)
    
    # Campos de timestamp
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    # Definir campo de login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Campos obrigatórios além do USERNAME_FIELD
    
    # Usar manager customizado
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        """Retorna nome completo ou email"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email


# ============================================================================
# MODEL DE USUÁRIO CUSTOMIZADO (HERDANDO DE AbstractBaseUser)
# ============================================================================

"""
# Opção mais customizada: herdar de AbstractBaseUser
# Dá controle total sobre os campos

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['primeiro_nome', 'ultimo_nome']
    
    objects = CustomUserManager()
    
    def get_full_name(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"
    
    def get_short_name(self):
        return self.primeiro_nome
"""


# ============================================================================
# PERFIL DE USUÁRIO (RELACIONAMENTO ONE-TO-ONE)
# ============================================================================

class PerfilUsuario(models.Model):
    """
    Modelo de perfil separado com relacionamento OneToOne.
    Útil quando você quer manter compatibilidade com o User padrão.
    """
    usuario = models.OneToOneField(
        'auth.User',  # Ou seu CustomUser
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    
    # Informações adicionais
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    website = models.URLField(blank=True)
    
    # Endereço
    rua = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    
    # Preferências
    receber_emails = models.BooleanField(default=True)
    tema_escuro = models.BooleanField(default=False)
    
    # Timestamps
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"


# ============================================================================
# CONFIGURAÇÃO NO SETTINGS.PY
# ============================================================================

"""
# settings.py

# Importar o modelo ANTES de criar migrations
AUTH_USER_MODEL = 'contas.CustomUser'  # app.Modelo

# Não use:
# from contas.models import CustomUser
# Isso causará problemas em migrations

# IMPORTANTE: Faça isso ANTES de executar migrate pela primeira vez!
"""


# ============================================================================
# CRIAR PERFIL AUTOMATICAMENTE (SIGNALS)
# ============================================================================

"""
# signals.py no seu app

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    '''
    Cria perfil automaticamente quando um usuário é criado.
    '''
    if created:
        PerfilUsuario.objects.create(usuario=instance)


# No apps.py do seu app, garantir que signals são carregados:

from django.apps import AppConfig

class ContasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contas'
    
    def ready(self):
        import contas.signals  # Importar signals
"""


# ============================================================================
# REFERENCIAR USER MODEL EM OUTROS MODELS
# ============================================================================

"""
# Sempre use get_user_model() ou settings.AUTH_USER_MODEL

from django.conf import settings
from django.contrib.auth import get_user_model

# Método 1: Usando get_user_model()
User = get_user_model()

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    # ...

# Método 2: Usando settings.AUTH_USER_MODEL (recomendado em ForeignKey)
class Comentario(models.Model):
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    # ...
"""


# ============================================================================
# FORMS CUSTOMIZADOS PARA CUSTOM USER
# ============================================================================

"""
# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'primeiro_nome', 'ultimo_nome')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remover campos de username se necessário
        if 'username' in self.fields:
            del self.fields['username']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


# views.py - Usar forms customizados

from django.contrib.auth import login
from .forms import CustomUserCreationForm

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registro.html', {'form': form})
"""


# ============================================================================
# ADMIN CUSTOMIZADO PARA CUSTOM USER
# ============================================================================

"""
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'primeiro_nome', 'ultimo_nome', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('primeiro_nome', 'ultimo_nome', 'telefone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email', 'primeiro_nome', 'ultimo_nome')
    ordering = ('email',)
"""


# ============================================================================
# EXEMPLO COMPLETO: MIGRATION PARA CUSTOM USER
# ============================================================================

"""
# 1. Criar app de contas/usuários
python manage.py startapp contas

# 2. Criar modelo CustomUser em contas/models.py
# (ver exemplo acima)

# 3. Configurar settings.py
AUTH_USER_MODEL = 'contas.CustomUser'

# 4. Adicionar app ao INSTALLED_APPS
INSTALLED_APPS = [
    ...
    'contas',
]

# 5. Criar migrations (ANTES de qualquer migrate!)
python manage.py makemigrations

# 6. Aplicar migrations
python manage.py migrate

# 7. Criar superusuário
python manage.py createsuperuser
# (usará email ao invés de username)
"""


# ============================================================================
# MIGRAR DE USER PADRÃO PARA CUSTOM USER
# ============================================================================

"""
⚠️ ATENÇÃO: Migrar de User padrão para Custom User é complexo!

Se você já tem dados no banco, precisa:
1. Criar CustomUser com os mesmos campos necessários
2. Criar migration customizada para copiar dados
3. Atualizar todas as ForeignKeys

RECOMENDAÇÃO: 
- Use Custom User desde o início do projeto
- Se já tem projeto em produção, considere manter User padrão
- Ou faça migração cuidadosamente com backups
"""

print("Arquivo de referência: Customização de Usuários")
print("IMPORTANTE: Configure AUTH_USER_MODEL antes de criar migrations iniciais!")

