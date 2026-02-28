from django import forms
from .models import Pessoa


class PessoaForm(forms.ModelForm):
    """
    Formulário para criar e editar Pessoas.
    """
    class Meta:
        model = Pessoa
        fields = ['nome', 'email', 'telefone', 'data_nascimento', 'cpf', 'endereco', 'ativo']
        
        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
            'cpf': 'CPF',
            'endereco': 'Endereço',
            'ativo': 'Ativo',
        }
        
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemplo@email.com'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),
            'data_nascimento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'cpf': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '000.000.000-00'
            }),
            'endereco': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Digite o endereço completo'
            }),
            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    
    def clean_email(self):
        """Validação customizada para email"""
        email = self.cleaned_data.get('email')
        if email:
            # Verifica se já existe outro registro com o mesmo email (exceto o atual)
            pessoa_existente = Pessoa.objects.filter(email=email)
            if self.instance.pk:  # Se estiver editando
                pessoa_existente = pessoa_existente.exclude(pk=self.instance.pk)
            if pessoa_existente.exists():
                raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email
    
    def clean_cpf(self):
        """Validação customizada para CPF"""
        cpf = self.cleaned_data.get('cpf')
        if cpf:
            # Remove caracteres não numéricos
            cpf_limpo = ''.join(filter(str.isdigit, cpf))
            # Verifica se já existe outro registro com o mesmo CPF (exceto o atual)
            pessoa_existente = Pessoa.objects.filter(cpf=cpf)
            if self.instance.pk:  # Se estiver editando
                pessoa_existente = pessoa_existente.exclude(pk=self.instance.pk)
            if pessoa_existente.exists():
                raise forms.ValidationError('Este CPF já está cadastrado.')
        return cpf
