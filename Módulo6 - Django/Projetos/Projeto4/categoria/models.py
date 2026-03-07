from django.db import models


class Categoria(models.Model):
    """
    Model para representar uma Categoria de produtos.
    Uma categoria pode ter N produtos.
    """
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    ativa = models.BooleanField(default=True, verbose_name='Status')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome
