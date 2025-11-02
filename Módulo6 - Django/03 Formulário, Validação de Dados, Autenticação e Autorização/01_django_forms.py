"""
01 - Formulários via Django Forms
===================================

Este arquivo demonstra como criar e usar formulários no Django.
"""

from django import forms
from django.core.exceptions import ValidationError


# ============================================================================
# FORM BÁSICO
# ============================================================================

class ContatoForm(forms.Form):
    """
    Formulário básico usando Django Forms.
    """
    nome = forms.CharField(
        max_length=100,
        label='Nome Completo',
        help_text='Digite seu nome completo',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu nome'
        })
    )
    
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com'
        })
    )
    
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Sua mensagem aqui...'
        })
    )
    
    telefone = forms.CharField(
        max_length=20,
        required=False,  # Campo opcional
        label='Telefone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '(00) 00000-0000'
        })
    )


# ============================================================================
# FORM COM VALIDAÇÃO CUSTOMIZADA
# ============================================================================

def validar_cpf(value):
    """Validador customizado"""
    if len(value.replace('.', '').replace('-', '')) != 11:
        raise ValidationError('CPF deve ter 11 dígitos')


class ClienteForm(forms.Form):
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=14, validators=[validar_cpf])
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    salario = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0
    )
    
    def clean_cpf(self):
        """Validação em nível de campo"""
        cpf = self.cleaned_data.get('cpf')
        # Remover pontos e traços
        cpf = cpf.replace('.', '').replace('-', '')
        
        # Verificar se todos são números
        if not cpf.isdigit():
            raise ValidationError('CPF deve conter apenas números')
        
        return cpf
    
    def clean(self):
        """Validação em nível de formulário"""
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        data_nascimento = cleaned_data.get('data_nascimento')
        
        # Exemplo: verificar se nome não contém números
        if nome and any(char.isdigit() for char in nome):
            raise ValidationError({
                'nome': 'Nome não pode conter números'
            })
        
        # Exemplo: verificar idade mínima
        if data_nascimento:
            from datetime import date
            idade = (date.today() - data_nascimento).days // 365
            if idade < 18:
                raise ValidationError({
                    'data_nascimento': 'É necessário ser maior de 18 anos'
                })
        
        return cleaned_data


# ============================================================================
# MODEL FORM
# ============================================================================

"""
# Form baseado em Model

from django import forms
from .models import Produto, Categoria

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'categoria', 'ativo']
        # Ou: fields = '__all__'  # Todos os campos
        # Ou: exclude = ['data_criacao']  # Todos exceto...
        
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço (R$)',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do produto'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
    
    def clean_preco(self):
        """Validação customizada"""
        preco = self.cleaned_data.get('preco')
        if preco and preco <= 0:
            raise ValidationError('Preço deve ser maior que zero')
        return preco
"""


# ============================================================================
# FORM COM ESCOLHAS (CHOICES)
# ============================================================================

class TipoContatoForm(forms.Form):
    TIPOS = [
        ('duvida', 'Dúvida'),
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação'),
        ('elogio', 'Elogio'),
    ]
    
    tipo = forms.ChoiceField(
        choices=TIPOS,
        widget=forms.RadioSelect  # Botões de rádio
    )
    
    assunto = forms.CharField(max_length=200)
    mensagem = forms.CharField(widget=forms.Textarea)


class PreferenciasForm(forms.Form):
    """Form com múltiplas escolhas"""
    LINGUAGENS = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('java', 'Java'),
        ('cpp', 'C++'),
    ]
    
    linguagens = forms.MultipleChoiceField(
        choices=LINGUAGENS,
        widget=forms.CheckboxSelectMultiple,
        label='Linguagens de Programação'
    )
    
    notificacoes = forms.BooleanField(
        required=False,
        label='Receber notificações por e-mail'
    )


# ============================================================================
# FORM COM ARQUIVOS
# ============================================================================

class UploadForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    arquivo = forms.FileField(
        label='Selecione um arquivo',
        help_text='Tamanho máximo: 5MB'
    )
    
    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        if arquivo:
            # Verificar tamanho (5MB)
            if arquivo.size > 5 * 1024 * 1024:
                raise ValidationError('Arquivo muito grande. Máximo: 5MB')
            
            # Verificar extensão
            extensoes_permitidas = ['.pdf', '.doc', '.docx', '.txt']
            if not any(arquivo.name.lower().endswith(ext) for ext in extensoes_permitidas):
                raise ValidationError('Extensão não permitida')
        
        return arquivo


# ============================================================================
# FORM COM DATAS E HORAS
# ============================================================================

class EventoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    
    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Data de Início'
    )
    
    hora_inicio = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Hora de Início'
    )
    
    data_fim = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Data e Hora de Fim',
        required=False
    )
    
    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        
        if data_inicio and data_fim and data_fim < data_inicio:
            raise ValidationError({
                'data_fim': 'Data de fim deve ser posterior à data de início'
            })
        
        return cleaned_data


# ============================================================================
# USO DO FORM EM VIEWS
# ============================================================================

"""
# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        
        if form.is_valid():
            # Dados validados
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            
            # Processar dados (salvar, enviar email, etc.)
            # enviar_email(nome, email, mensagem)
            
            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('contato')
    else:
        form = ContatoForm()
    
    return render(request, 'contato.html', {'form': form})


# Uso com ModelForm

from .forms import ProdutoForm
from .models import Produto

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()  # Salva diretamente no banco
            return redirect('produtos:detalhe', produto_id=produto.id)
    else:
        form = ProdutoForm()
    
    return render(request, 'produtos/form.html', {'form': form})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:detalhe', produto_id=produto.id)
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'produtos/form.html', {'form': form})
"""

# ============================================================================
# RENDERIZAR FORM EM TEMPLATE
# ============================================================================

"""
<!-- Renderização básica -->
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}  <!-- Como parágrafos -->
    <button type="submit">Enviar</button>
</form>

<!-- Outras formas -->
{{ form.as_table }}  <!-- Como tabela -->
{{ form.as_ul }}     <!-- Como lista não ordenada -->

<!-- Renderização manual (mais controle) -->
<form method="post">
    {% csrf_token %}
    
    <div class="form-group">
        {{ form.nome.label_tag }}
        {{ form.nome }}
        {% if form.nome.errors %}
            <div class="error">{{ form.nome.errors }}</div>
        {% endif %}
        {% if form.nome.help_text %}
            <small>{{ form.nome.help_text }}</small>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.email.label_tag }}
        {{ form.email }}
        {{ form.email.errors }}
    </div>
    
    <button type="submit">Enviar</button>
</form>

<!-- Exibir erros gerais do formulário -->
{% if form.non_field_errors %}
    <div class="errors">
        {{ form.non_field_errors }}
    </div>
{% endif %}
"""

# ============================================================================
# FORM COM FORM SETS (Múltiplos forms)
# ============================================================================

"""
# forms.py

from django.forms import formset_factory

TelefoneFormSet = formset_factory(
    forms.CharField,
    extra=2,  # Quantos forms vazios mostrar
    can_delete=True  # Permitir deletar
)

# Uso em view:
def contato(request):
    TelefoneFormSet = formset_factory(TelefoneForm, extra=2)
    
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        formset = TelefoneFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            # Processar
            pass
    else:
        form = ContatoForm()
        formset = TelefoneFormSet()
    
    return render(request, 'contato.html', {
        'form': form,
        'formset': formset
    })
"""

# ============================================================================
# FORM COM INLINE FORMSETS (Model Forms)
# ============================================================================

"""
# Para relacionamentos ForeignKey/ManyToMany

from django.forms import inlineformset_factory
from .models import Pedido, ItemPedido

ItemPedidoFormSet = inlineformset_factory(
    Pedido,
    ItemPedido,
    fields=['produto', 'quantidade', 'preco'],
    extra=1,
    can_delete=True
)

# Uso em view:
def criar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        formset = ItemPedidoFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            pedido = form.save()
            formset.instance = pedido
            formset.save()
            return redirect('pedidos:detalhe', pedido_id=pedido.id)
    else:
        form = PedidoForm()
        formset = ItemPedidoFormSet()
    
    return render(request, 'pedidos/form.html', {
        'form': form,
        'formset': formset
    })
"""

# ============================================================================
# WIDGETS CUSTOMIZADOS
# ============================================================================

class DatePickerWidget(forms.DateInput):
    """Widget customizado para data"""
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {})
        kwargs['attrs'].update({
            'type': 'date',
            'class': 'datepicker'
        })
        super().__init__(*args, **kwargs)


class FormComWidgetCustomizado(forms.Form):
    data = forms.DateField(widget=DatePickerWidget)


print("Arquivo de referência: Django Forms")
print("Use forms.Form para formulários simples e forms.ModelForm para baseados em models")

