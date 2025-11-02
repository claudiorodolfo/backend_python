"""
02 - Definição de Models
=========================

Este arquivo demonstra como definir models no Django, incluindo diferentes
tipos de campos e relacionamentos.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# ============================================================================
# MODEL BÁSICO
# ============================================================================

class Produto(models.Model):
    """
    Model básico de um Produto.
    Demonstra tipos de campos comuns.
    """
    # Campos de texto
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)  # blank=True permite vazio
    slug = models.SlugField(unique=True)  # URL amigável
    
    # Campos numéricos
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    desconto = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        default=0.0
    )
    
    # Campos booleanos
    ativo = models.BooleanField(default=True)
    
    # Campos de data/hora
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_expiracao = models.DateField(null=True, blank=True)
    
    # Campos de escolha (choice field)
    CATEGORIAS = [
        ('ELETRONICO', 'Eletrônico'),
        ('ROUPA', 'Roupa'),
        ('COMIDA', 'Comida'),
        ('LIVRO', 'Livro'),
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='ELETRONICO')
    
    # Campos de arquivo/imagem
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    documento = models.FileField(upload_to='documentos/', null=True, blank=True)
    
    class Meta:
        # Metadados do model
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-data_criacao']  # Ordenação padrão
        indexes = [
            models.Index(fields=['nome']),
            models.Index(fields=['categoria', 'ativo']),
        ]
    
    def __str__(self):
        return self.nome
    
    def get_preco_com_desconto(self):
        """Método personalizado do model"""
        return self.preco * (1 - self.desconto / 100)
    
    @property
    def em_estoque(self):
        """Propriedade do model"""
        return self.quantidade > 0


# ============================================================================
# RELACIONAMENTOS - FOREIGN KEY (Muitos-para-Um)
# ============================================================================

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome


class ProdutoComCategoria(models.Model):
    """
    Exemplo de relacionamento ForeignKey.
    Muitos produtos podem pertencer a uma categoria.
    """
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,  # Se categoria for deletada, produtos também
        related_name='produtos'  # Permite acessar: categoria.produtos.all()
    )
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Outras opções de on_delete:
    # models.PROTECT - Impede deletar categoria se tiver produtos
    # models.SET_NULL - Define como NULL (precisa null=True)
    # models.SET_DEFAULT - Define valor padrão
    # models.DO_NOTHING - Não faz nada (cuidado!)
    
    def __str__(self):
        return f"{self.nome} ({self.categoria})"


# ============================================================================
# RELACIONAMENTOS - ONE TO ONE (Um-para-Um)
# ============================================================================

class PerfilUsuario(models.Model):
    """
    Exemplo de relacionamento OneToOne.
    Um usuário tem um perfil, um perfil pertence a um usuário.
    """
    usuario = models.OneToOneField(
        'auth.User',  # Referência ao model User do Django
        on_delete=models.CASCADE,
        related_name='perfil'
    )
    telefone = models.CharField(max_length=20, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"


# ============================================================================
# RELACIONAMENTOS - MANY TO MANY (Muitos-para-Muitos)
# ============================================================================

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome


class Artigo(models.Model):
    """
    Exemplo de relacionamentos ManyToMany.
    Um artigo pode ter vários autores e várias tags.
    """
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    
    # ManyToMany simples
    tags = models.ManyToManyField(Tag, blank=True, related_name='artigos')
    
    # ManyToMany com through (tabela intermediária customizada)
    autores = models.ManyToManyField(
        Autor,
        through='AutoriaArtigo',  # Tabela intermediária customizada
        related_name='artigos'
    )
    
    def __str__(self):
        return self.titulo


class AutoriaArtigo(models.Model):
    """
    Tabela intermediária customizada para ManyToMany.
    Permite adicionar campos extras no relacionamento.
    """
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ordem = models.IntegerField(default=1)  # Campo extra
    porcentagem_contribuicao = models.FloatField(default=100.0)
    
    class Meta:
        unique_together = [['artigo', 'autor']]
        ordering = ['ordem']


# ============================================================================
# MODEL COM VALIDAÇÕES CUSTOMIZADAS
# ============================================================================

def validar_cpf(value):
    """Validador customizado"""
    if len(value) != 11:
        raise models.ValidationError('CPF deve ter 11 dígitos')
    # Adicionar mais validações aqui


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, validators=[validar_cpf], unique=True)
    email = models.EmailField()
    
    def clean(self):
        """Validação em nível de model"""
        super().clean()
        if self.email.endswith('@spam.com'):
            raise models.ValidationError('Emails deste domínio não são aceitos')
    
    def __str__(self):
        return self.nome


# ============================================================================
# MODEL COM QUERYSET CUSTOMIZADO E MANAGER
# ============================================================================

class ProdutoQuerySet(models.QuerySet):
    """QuerySet customizado com métodos úteis"""
    
    def ativos(self):
        return self.filter(ativo=True)
    
    def em_estoque(self):
        return self.filter(quantidade__gt=0)
    
    def por_categoria(self, categoria):
        return self.filter(categoria=categoria)


class ProdutoManager(models.Manager):
    """Manager customizado"""
    
    def get_queryset(self):
        return ProdutoQuerySet(self.model, using=self._db)
    
    def ativos(self):
        return self.get_queryset().ativos()
    
    def em_estoque(self):
        return self.get_queryset().em_estoque()


class ProdutoAvancado(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    
    objects = ProdutoManager()  # Usar manager customizado
    
    class Meta:
        ordering = ['nome']
    
    def __str__(self):
        return self.nome


# ============================================================================
# USO DOS MODELS (exemplos comentados)
# ============================================================================

"""
# No shell do Django ou em views:

# Criar objetos
produto = Produto.objects.create(
    nome="Notebook",
    slug="notebook-gamer",
    preco=2500.00,
    categoria="ELETRONICO"
)

categoria = Categoria.objects.create(nome="Eletrônicos")
produto_cat = ProdutoComCategoria.objects.create(
    nome="Smartphone",
    categoria=categoria,
    preco=1500.00
)

# Consultas
Produto.objects.all()
Produto.objects.filter(ativo=True)
Produto.objects.get(slug="notebook-gamer")
Produto.objects.filter(preco__gte=1000)  # Preço >= 1000
Produto.objects.filter(nome__icontains="notebook")  # Case-insensitive

# Acessar relacionamentos
categoria.produtos.all()  # Todos produtos da categoria (usando related_name)
produto_cat.categoria.nome  # Acessar categoria do produto

# ManyToMany
artigo = Artigo.objects.create(titulo="Python Django")
autor = Autor.objects.create(nome="João Silva", email="joao@email.com")
artigo.autores.add(autor)
artigo.tags.add(Tag.objects.create(nome="Python"))

# Queries com relacionamentos
Artigo.objects.filter(autores__nome="João Silva")
Artigo.objects.filter(tags__nome="Python")
ProdutoComCategoria.objects.filter(categoria__nome="Eletrônicos")
"""

print("Models definidos com sucesso!")
print("Lembre-se de criar e aplicar migrations após definir seus models:")
print("python manage.py makemigrations")
print("python manage.py migrate")

