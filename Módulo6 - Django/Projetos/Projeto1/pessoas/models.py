from django.db import models


class Pessoa(models.Model):
    """
    Model para representar uma Pessoa no sistema.
    """
    nome = models.CharField(max_length=100, verbose_name='Nome')
    email = models.EmailField(max_length=100, unique=True, verbose_name='E-mail')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    data_nascimento = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=14, blank=True, null=True, unique=True, verbose_name='CPF')
    endereco = models.TextField(blank=True, null=True, verbose_name='Endereço')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['-data_criacao']
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return self.nome
