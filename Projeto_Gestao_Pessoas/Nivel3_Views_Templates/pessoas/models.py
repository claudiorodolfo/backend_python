"""
Modelos para gestão de pessoas.
"""
from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from django.utils import timezone


class Pessoa(models.Model):
    """
    Modelo que representa uma pessoa no sistema.
    """
    
    # Opções para campos de escolha
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar'),
    ]
    
    ESTADO_CIVIL_CHOICES = [
        ('S', 'Solteiro(a)'),
        ('C', 'Casado(a)'),
        ('D', 'Divorciado(a)'),
        ('V', 'Viúvo(a)'),
        ('U', 'União Estável'),
    ]
    
    # Campos básicos
    nome = models.CharField(
        max_length=100,
        verbose_name='Nome Completo',
        help_text='Nome completo da pessoa'
    )
    
    cpf = models.CharField(
        max_length=14,
        unique=True,
        verbose_name='CPF',
        help_text='CPF no formato XXX.XXX.XXX-XX',
        validators=[
            RegexValidator(
                regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
                message='CPF deve estar no formato XXX.XXX.XXX-XX'
            )
        ]
    )
    
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='E-mail',
        validators=[EmailValidator()]
    )
    
    telefone = models.CharField(
        max_length=15,
        verbose_name='Telefone',
        help_text='Telefone no formato (XX) XXXXX-XXXX',
        validators=[
            RegexValidator(
                regex=r'^\(\d{2}\)\s?\d{4,5}-?\d{4}$',
                message='Telefone deve estar no formato (XX) XXXXX-XXXX'
            )
        ]
    )
    
    data_nascimento = models.DateField(
        verbose_name='Data de Nascimento',
        help_text='Data de nascimento no formato DD/MM/AAAA'
    )
    
    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        verbose_name='Sexo',
        default='N'
    )
    
    estado_civil = models.CharField(
        max_length=1,
        choices=ESTADO_CIVIL_CHOICES,
        verbose_name='Estado Civil',
        default='S'
    )
    
    # Endereço
    endereco = models.CharField(
        max_length=200,
        verbose_name='Endereço',
        blank=True,
        null=True
    )
    
    cidade = models.CharField(
        max_length=100,
        verbose_name='Cidade',
        blank=True,
        null=True
    )
    
    estado = models.CharField(
        max_length=2,
        verbose_name='Estado (UF)',
        blank=True,
        null=True,
        help_text='Sigla do estado (ex: SP, RJ)'
    )
    
    cep = models.CharField(
        max_length=9,
        verbose_name='CEP',
        blank=True,
        null=True,
        help_text='CEP no formato XXXXX-XXX',
        validators=[
            RegexValidator(
                regex=r'^\d{5}-?\d{3}$',
                message='CEP deve estar no formato XXXXX-XXX'
            )
        ]
    )
    
    # Campos de controle
    data_cadastro = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Cadastro'
    )
    
    data_atualizacao = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização'
    )
    
    ativo = models.BooleanField(
        default=True,
        verbose_name='Ativo',
        help_text='Indica se a pessoa está ativa no sistema'
    )
    
    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observações',
        help_text='Observações adicionais sobre a pessoa'
    )
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['cpf']),
            models.Index(fields=['email']),
        ]
    
    def __str__(self):
        return f"{self.nome} ({self.cpf})"
    
    def idade(self):
        """Calcula a idade da pessoa."""
        hoje = timezone.now().date()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )
    
    idade.short_description = 'Idade'
    
    def nome_completo(self):
        """Retorna o nome completo."""
        return self.nome
    
    nome_completo.short_description = 'Nome Completo'
