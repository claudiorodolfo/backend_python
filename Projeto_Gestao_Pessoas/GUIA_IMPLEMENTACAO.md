# Guia de Implementação - Projeto Gestão de Pessoas

Este guia descreve como implementar cada nível do projeto Django de Gestão de Pessoas.

## 📚 Estrutura dos Níveis

### Nível 1: Estrutura Base ✅
**Status**: Completo
- Projeto Django básico criado
- Configurações iniciais
- Admin do Django configurado

### Nível 2: Modelos ✅
**Status**: Completo
- App `pessoas` criado
- Modelo `Pessoa` completo
- Admin configurado para o modelo

### Nível 3: Views e Templates ✅
**Status**: Completo
- Views para listar e detalhar pessoas
- Templates HTML com design moderno
- Sistema de busca

### Nível 4: Formulários e CRUD
**Arquivos a criar/atualizar**:

1. **pessoas/forms.py** - Formulários Django
```python
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 4}),
        }
```

2. **pessoas/views.py** - Adicionar views de CRUD
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Pessoa
from .forms import PessoaForm

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa cadastrada com sucesso!')
            return redirect('pessoas:lista')
    else:
        form = PessoaForm()
    return render(request, 'pessoas/form.html', {'form': form})

def editar_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa atualizada com sucesso!')
            return redirect('pessoas:detalhe', pessoa_id=pessoa.id)
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoas/form.html', {'form': form, 'pessoa': pessoa})

def excluir_pessoa(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    if request.method == 'POST':
        pessoa.delete()
        messages.success(request, 'Pessoa excluída com sucesso!')
        return redirect('pessoas:lista')
    return render(request, 'pessoas/confirmar_exclusao.html', {'pessoa': pessoa})
```

3. **pessoas/urls.py** - Adicionar rotas
```python
urlpatterns = [
    path('', views.lista_pessoas, name='lista'),
    path('criar/', views.criar_pessoa, name='criar'),
    path('<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe'),
    path('<int:pessoa_id>/editar/', views.editar_pessoa, name='editar'),
    path('<int:pessoa_id>/excluir/', views.excluir_pessoa, name='excluir'),
]
```

4. **templates/pessoas/form.html** - Template de formulário
5. **templates/pessoas/confirmar_exclusao.html** - Template de confirmação

### Nível 5: Admin Personalizado
**Arquivos a atualizar**:

1. **pessoas/admin.py** - Melhorar configuração do admin
   - Adicionar actions customizadas
   - Melhorar list_display
   - Adicionar filtros avançados
   - Customizar formulários do admin

### Nível 6: API REST com DRF
**Arquivos a criar**:

1. **requirements.txt** - Adicionar `djangorestframework`
2. **gestao_pessoas/settings.py** - Adicionar `rest_framework` em INSTALLED_APPS
3. **pessoas/serializers.py** - Serializers DRF
4. **pessoas/views_api.py** - ViewSets ou APIViews
5. **pessoas/urls_api.py** - URLs da API
6. **gestao_pessoas/urls.py** - Incluir URLs da API

### Nível 7: Autenticação e Permissões
**Arquivos a criar/atualizar**:

1. **pessoas/permissions.py** - Permissões customizadas
2. **pessoas/views.py** - Adicionar decoradores de autenticação
3. **templates/registration/** - Templates de login/logout
4. **gestao_pessoas/settings.py** - Configurar LOGIN_URL, LOGIN_REDIRECT_URL

### Nível 8: Testes e Deploy
**Arquivos a criar**:

1. **pessoas/tests.py** - Testes unitários e de integração
2. **requirements.txt** - Adicionar dependências de produção
3. **Procfile** - Para deploy no Heroku
4. **runtime.txt** - Versão do Python
5. **.env.example** - Exemplo de variáveis de ambiente

## 🚀 Como Implementar Cada Nível

### Passo 1: Copiar estrutura anterior
```bash
cp -r Nivel3_Views_Templates/* Nivel4_Formularios_CRUD/
```

### Passo 2: Adicionar novos arquivos
Criar os arquivos listados acima para cada nível.

### Passo 3: Atualizar configurações
Atualizar `settings.py`, `urls.py` conforme necessário.

### Passo 4: Testar
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 📝 Notas Importantes

1. Cada nível é independente e pode ser executado separadamente
2. Os níveis são incrementais - cada um adiciona funcionalidades ao anterior
3. Sempre teste após cada modificação
4. Mantenha o código organizado e documentado

## 🔗 Recursos Úteis

- [Documentação Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django Admin](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
