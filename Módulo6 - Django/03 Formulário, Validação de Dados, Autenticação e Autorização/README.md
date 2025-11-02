# 03 - Formulário, Validação de Dados, Autenticação e Autorização

Este módulo aborda formulários, validação de dados, e o sistema completo de autenticação e autorização do Django.

## 📚 Conteúdo

1. **Formulários via Django Forms**
2. **Validação e Limpeza de Dados**
3. **Mensagens de Erro**
4. **Sistema de Autenticação Embutido**
5. **Login, Logout e Restrição de Acesso**
6. **Customização de Usuários**

## 🎯 Objetivos de Aprendizado

Ao final desta unidade, você será capaz de:
- Criar formulários usando Django Forms e ModelForms
- Implementar validação em nível de campo e formulário
- Limpar e normalizar dados de entrada
- Implementar sistema completo de autenticação
- Controlar acesso a views com decorators
- Criar modelos de usuário customizados

## 📁 Arquivos

- `01_django_forms.py` - Formulários Django (Form e ModelForm)
- `02_validacao_limpeza.py` - Validação e limpeza de dados
- `03_autenticacao.py` - Sistema de autenticação do Django
- `04_custom_user.py` - Customização de modelos de usuário

## 🚀 Formulários Django

### Form Básico

```python
from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    mensagem = forms.CharField(widget=forms.Textarea)
```

### Model Form

```python
from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao']
```

### Uso em Views

```python
def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            return redirect('produtos:detalhe', produto_id=produto.id)
    else:
        form = ProdutoForm()
    
    return render(request, 'form.html', {'form': form})
```

### Renderização em Templates

```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enviar</button>
</form>
```

## ✅ Validação

### Validação de Campo

```python
def clean_email(self):
    email = self.cleaned_data.get('email')
    if '@spam.com' in email:
        raise ValidationError('Email não permitido')
    return email.lower()
```

### Validação de Formulário

```python
def clean(self):
    cleaned_data = super().clean()
    senha = cleaned_data.get('senha')
    confirmar = cleaned_data.get('confirmar_senha')
    
    if senha != confirmar:
        raise ValidationError({
            'confirmar_senha': 'As senhas não coincidem'
        })
    
    return cleaned_data
```

### Validadores Customizados

```python
def validar_cpf(value):
    if len(value) != 11:
        raise ValidationError('CPF inválido')
    return value

class Form(forms.Form):
    cpf = forms.CharField(validators=[validar_cpf])
```

## 🔐 Autenticação

### Login Manual

```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('home')
```

### Views Pré-construídas

```python
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

### Restrição de Acesso

```python
from django.contrib.auth.decorators import login_required

@login_required
def area_restrita(request):
    return render(request, 'restrita.html')
```

### Verificar Permissões

```python
from django.contrib.auth.decorators import permission_required

@permission_required('app.pode_editar')
def editar_produto(request):
    pass
```

## 👤 Custom User Model

### Criar Custom User

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
```

### Configurar no Settings

```python
# settings.py
AUTH_USER_MODEL = 'contas.CustomUser'
```

⚠️ **IMPORTANTE**: Configure antes de criar migrations iniciais!

## 📝 Exemplos Práticos

### 1. Formulário de Registro

```python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
```

### 2. Form com Validação Customizada

```python
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']
    
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco <= 0:
            raise ValidationError('Preço deve ser maior que zero')
        return preco
```

### 3. Verificar Usuário em Template

```html
{% if user.is_authenticated %}
    <p>Olá, {{ user.username }}!</p>
    <a href="{% url 'logout' %}">Sair</a>
{% else %}
    <a href="{% url 'login' %}">Entrar</a>
{% endif %}
```

## 🔑 Conceitos Importantes

### Form vs ModelForm

- **Form**: Para formulários não relacionados a models
- **ModelForm**: Para formulários baseados em models (CRUD)

### Validação

- **clean_<campo>()**: Validação de campo específico
- **clean()**: Validação que envolve múltiplos campos
- **Validadores**: Funções reutilizáveis de validação

### Autenticação vs Autorização

- **Autenticação**: Verificar quem é o usuário (login)
- **Autorização**: Verificar o que o usuário pode fazer (permissões)

### Custom User

- Use `AbstractUser` para adicionar campos
- Use `AbstractBaseUser` para controle total
- Configure `AUTH_USER_MODEL` antes de migrations

## 💡 Boas Práticas

1. **Sempre valide dados**: Use forms ao invés de processar POST diretamente
2. **Validação em camadas**: Valide no form e no model quando necessário
3. **Mensagens claras**: Forneça mensagens de erro descritivas
4. **Segurança**: Use `{% csrf_token %}` em todos os forms
5. **Custom User**: Planeje antes de começar o projeto

## 📖 Exercícios Práticos

1. **Exercício 1**: Criar formulário de contato com validação
2. **Exercício 2**: Criar ModelForm para criar/editar produtos
3. **Exercício 3**: Implementar validação de CPF customizada
4. **Exercício 4**: Criar sistema de login/logout completo
5. **Exercício 5**: Implementar registro de usuário
6. **Exercício 6**: Criar Custom User com email como username

## 🔧 Configurações de Autenticação

```python
# settings.py

LOGIN_URL = '/contas/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SESSION_COOKIE_AGE = 86400  # 24 horas
```

## 📚 Recursos Adicionais

- [Django Forms Documentation](https://docs.djangoproject.com/en/stable/topics/forms/)
- [Django Authentication](https://docs.djangoproject.com/en/stable/topics/auth/)
- [Custom User Models](https://docs.djangoproject.com/en/stable/topics/auth/customizing/)
- [Form Validation](https://docs.djangoproject.com/en/stable/ref/forms/validation/)

