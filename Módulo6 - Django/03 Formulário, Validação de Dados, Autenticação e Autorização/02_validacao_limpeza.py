"""
02 - Validação e Limpeza de Dados
==================================

Este arquivo demonstra como validar e limpar dados em formulários Django.
"""

from django import forms
from django.core.exceptions import ValidationError


# ============================================================================
# VALIDAÇÃO EM NÍVEL DE CAMPO
# ============================================================================

class FormValidacaoCampo(forms.Form):
    """Form com validação em nível de campo"""
    
    email = forms.EmailField()
    
    def clean_email(self):
        """Validação customizada para o campo email"""
        email = self.cleaned_data.get('email')
        
        # Verificar se email já existe (exemplo)
        # if User.objects.filter(email=email).exists():
        #     raise ValidationError('Este email já está cadastrado')
        
        # Verificar domínios não permitidos
        dominios_bloqueados = ['spam.com', 'teste.com']
        dominio = email.split('@')[1] if '@' in email else ''
        
        if dominio in dominios_bloqueados:
            raise ValidationError(f'Emails do domínio {dominio} não são aceitos')
        
        return email.lower()  # Normalizar para minúsculas
    
    telefone = forms.CharField(max_length=20)
    
    def clean_telefone(self):
        """Limpar e validar telefone"""
        telefone = self.cleaned_data.get('telefone')
        
        # Remover caracteres não numéricos
        telefone_limpo = ''.join(filter(str.isdigit, telefone))
        
        # Validar formato (exemplo: 10 ou 11 dígitos)
        if len(telefone_limpo) not in [10, 11]:
            raise ValidationError('Telefone deve ter 10 ou 11 dígitos')
        
        # Formatar telefone (exemplo)
        if len(telefone_limpo) == 11:
            return f"({telefone_limpo[:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}"
        else:
            return f"({telefone_limpo[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"
    
    senha = forms.CharField(widget=forms.PasswordInput)
    confirmar_senha = forms.CharField(widget=forms.PasswordInput)
    
    def clean_senha(self):
        """Validar força da senha"""
        senha = self.cleaned_data.get('senha')
        
        if len(senha) < 8:
            raise ValidationError('Senha deve ter pelo menos 8 caracteres')
        
        if not any(char.isdigit() for char in senha):
            raise ValidationError('Senha deve conter pelo menos um número')
        
        if not any(char.isupper() for char in senha):
            raise ValidationError('Senha deve conter pelo menos uma letra maiúscula')
        
        return senha
    
    def clean_confirmar_senha(self):
        """Validar confirmação de senha"""
        senha = self.cleaned_data.get('senha')
        confirmar_senha = self.cleaned_data.get('confirmar_senha')
        
        if senha and confirmar_senha and senha != confirmar_senha:
            raise ValidationError('As senhas não coincidem')
        
        return confirmar_senha


# ============================================================================
# VALIDAÇÃO EM NÍVEL DE FORMULÁRIO
# ============================================================================

class FormValidacaoCompleta(forms.Form):
    """Form com validação que envolve múltiplos campos"""
    
    data_inicio = forms.DateField()
    data_fim = forms.DateField()
    quantidade = forms.IntegerField(min_value=1)
    desconto = forms.DecimalField(max_digits=5, decimal_places=2)
    
    def clean(self):
        """Validação em nível de formulário"""
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')
        quantidade = cleaned_data.get('quantidade')
        desconto = cleaned_data.get('desconto')
        
        erros = {}
        
        # Validar datas
        if data_inicio and data_fim:
            if data_fim < data_inicio:
                erros['data_fim'] = ValidationError(
                    'Data de fim deve ser posterior à data de início'
                )
            
            # Validar intervalo máximo (exemplo: máximo 30 dias)
            dias = (data_fim - data_inicio).days
            if dias > 30:
                erros['data_fim'] = ValidationError(
                    'O intervalo não pode ser maior que 30 dias'
                )
        
        # Validar quantidade e desconto juntos
        if quantidade and desconto:
            # Desconto maior que 50% requer quantidade mínima
            if desconto > 50 and quantidade < 10:
                erros['quantidade'] = ValidationError(
                    'Para descontos acima de 50%, quantidade mínima é 10 unidades'
                )
        
        # Lançar erros se houver
        if erros:
            raise ValidationError(erros)
        
        return cleaned_data


# ============================================================================
# VALIDADORES CUSTOMIZADOS (REUTILIZÁVEIS)
# ============================================================================

def validar_cpf(value):
    """Validador reutilizável para CPF"""
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, value))
    
    if len(cpf) != 11:
        raise ValidationError('CPF deve ter 11 dígitos')
    
    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')
    
    # Algoritmo de validação do CPF
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto
    
    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf, 11)
    
    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        raise ValidationError('CPF inválido')
    
    return cpf


def validar_cnpj(value):
    """Validador reutilizável para CNPJ"""
    cnpj = ''.join(filter(str.isdigit, value))
    
    if len(cnpj) != 14:
        raise ValidationError('CNPJ deve ter 14 dígitos')
    
    # Implementar algoritmo de validação do CNPJ
    # (similar ao CPF, mas com 14 dígitos)
    
    return cnpj


class FormComValidadores(forms.Form):
    """Form usando validadores customizados"""
    
    cpf = forms.CharField(
        max_length=14,
        validators=[validar_cpf],
        label='CPF',
        help_text='Digite apenas números ou no formato: 000.000.000-00'
    )
    
    cnpj = forms.CharField(
        max_length=18,
        validators=[validar_cnpj],
        required=False,
        label='CNPJ'
    )


# ============================================================================
# LIMPEZA DE DADOS
# ============================================================================

class FormLimpeza(forms.Form):
    """Form que demonstra limpeza de dados"""
    
    nome = forms.CharField(max_length=100)
    
    def clean_nome(self):
        """Limpar nome: remover espaços extras, capitalizar"""
        nome = self.cleaned_data.get('nome')
        
        # Remover espaços extras
        nome = ' '.join(nome.split())
        
        # Capitalizar (primeira letra maiúscula)
        nome = nome.title()
        
        return nome
    
    endereco = forms.CharField(required=False)
    
    def clean_endereco(self):
        """Limpar endereço"""
        endereco = self.cleaned_data.get('endereco')
        
        if endereco:
            # Normalizar espaços e capitalizar
            endereco = ' '.join(endereco.split()).title()
        
        return endereco
    
    url = forms.URLField(required=False)
    
    def clean_url(self):
        """Adicionar http:// se não tiver protocolo"""
        url = self.cleaned_data.get('url')
        
        if url and not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        return url


# ============================================================================
# MENSAGENS DE ERRO PERSONALIZADAS
# ============================================================================

class FormMensagensPersonalizadas(forms.Form):
    """Form com mensagens de erro customizadas"""
    
    email = forms.EmailField(
        error_messages={
            'required': 'O campo email é obrigatório',
            'invalid': 'Por favor, digite um email válido'
        }
    )
    
    idade = forms.IntegerField(
        min_value=18,
        max_value=120,
        error_messages={
            'required': 'Idade é obrigatória',
            'min_value': 'Você deve ter pelo menos 18 anos',
            'max_value': 'Idade inválida',
            'invalid': 'Por favor, digite um número válido'
        }
    )
    
    senha = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={
            'required': 'Senha é obrigatória',
            'min_length': 'Senha deve ter pelo menos %(limit_value)d caracteres'
        }
    )


# ============================================================================
# VALIDAÇÃO EM MODEL FORM
# ============================================================================

"""
# Exemplo com ModelForm

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'quantidade']
    
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        
        # Verificar unicidade (quando criando)
        if not self.instance.pk:  # Novo objeto
            if Produto.objects.filter(nome=nome).exists():
                raise ValidationError('Já existe um produto com este nome')
        
        # Verificar unicidade (quando editando)
        else:
            if Produto.objects.filter(nome=nome).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Já existe um produto com este nome')
        
        return nome
    
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        
        if preco <= 0:
            raise ValidationError('Preço deve ser maior que zero')
        
        return preco
    
    def clean(self):
        cleaned_data = super().clean()
        preco = cleaned_data.get('preco')
        quantidade = cleaned_data.get('quantidade')
        
        # Validar regra de negócio
        if preco and quantidade:
            valor_total = preco * quantidade
            if valor_total > 1000000:
                raise ValidationError(
                    'O valor total do estoque não pode exceder R$ 1.000.000,00'
                )
        
        return cleaned_data
"""

# ============================================================================
# VALIDAÇÃO DE ARQUIVOS
# ============================================================================

class FormUploadArquivo(forms.Form):
    arquivo = forms.FileField()
    
    def clean_arquivo(self):
        arquivo = self.cleaned_data.get('arquivo')
        
        if arquivo:
            # Validar tamanho (5MB)
            tamanho_maximo = 5 * 1024 * 1024
            if arquivo.size > tamanho_maximo:
                raise ValidationError(
                    f'Arquivo muito grande. Tamanho máximo: {tamanho_maximo / (1024*1024):.1f} MB'
                )
            
            # Validar extensão
            extensoes_permitidas = ['.pdf', '.doc', '.docx', '.txt', '.jpg', '.png']
            nome_arquivo = arquivo.name.lower()
            
            if not any(nome_arquivo.endswith(ext) for ext in extensoes_permitidas):
                raise ValidationError(
                    f'Extensão não permitida. Use: {", ".join(extensoes_permitidas)}'
                )
            
            # Validar tipo MIME (básico)
            tipos_permitidos = [
                'application/pdf',
                'application/msword',
                'image/jpeg',
                'image/png',
                'text/plain'
            ]
            
            if hasattr(arquivo, 'content_type'):
                if arquivo.content_type not in tipos_permitidos:
                    raise ValidationError('Tipo de arquivo não permitido')
        
        return arquivo


# ============================================================================
# EXIBIR ERROS EM TEMPLATE
# ============================================================================

"""
<!-- Exibir erros de campo específico -->
<div class="form-group">
    {{ form.nome.label_tag }}
    {{ form.nome }}
    {% if form.nome.errors %}
        <div class="errors">
            {% for error in form.nome.errors %}
                <span class="error">{{ error }}</span>
            {% endfor %}
        </div>
    {% endif %}
</div>

<!-- Exibir erros não relacionados a campos específicos -->
{% if form.non_field_errors %}
    <div class="alert alert-error">
        {% for error in form.non_field_errors %}
            <p>{{ error }}</p>
        {% endfor %}
    </div>
{% endif %}

<!-- Exibir todos os erros -->
{% if form.errors %}
    <div class="alert alert-error">
        <strong>Por favor, corrija os seguintes erros:</strong>
        <ul>
            {% for field in form %}
                {% for error in field.errors %}
                    <li><strong>{{ field.label }}:</strong> {{ error }}</li>
                {% endfor %}
            {% endfor %}
            {% for error in form.non_field_errors %}
                <li>{{ error }}</li>
            {% endfor %}
        </ul>
    </div>
{% endif %}
"""

print("Arquivo de referência: Validação e Limpeza de Dados")
print("Use clean_<campo> para validação de campo e clean() para validação do formulário completo")

