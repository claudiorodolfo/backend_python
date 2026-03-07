from django.db import models
from categoria.models import Categoria


class Produto(models.Model):
    """
    Model para representar um Produto.
    Cada produto pertence a 1 categoria; uma categoria pode ter N produtos.
    """
    nome = models.CharField(max_length=200, verbose_name='Nome')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    estoque = models.IntegerField(verbose_name='Estoque')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='produtos',
        verbose_name='Categoria'
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-data_criacao']

    def __str__(self):
        return self.nome
