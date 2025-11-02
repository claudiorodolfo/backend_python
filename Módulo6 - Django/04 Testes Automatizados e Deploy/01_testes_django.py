"""
01 - Testes no Django
======================

Este arquivo demonstra como escrever testes no Django usando o framework de testes.
"""

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone

# ============================================================================
# TESTE DE MODEL
# ============================================================================

class ProdutoTestCase(TestCase):
    """
    Testes para o modelo Produto.
    """
    
    def setUp(self):
        """
        Método executado antes de cada teste.
        Prepara dados para os testes.
        """
        # Criar objetos de teste
        self.produto = Produto.objects.create(
            nome='Notebook',
            preco=2500.00,
            quantidade=10
        )
    
    def test_produto_criacao(self):
        """Testar criação de produto"""
        self.assertEqual(self.produto.nome, 'Notebook')
        self.assertEqual(self.produto.preco, 2500.00)
        self.assertEqual(self.produto.quantidade, 10)
    
    def test_produto_str(self):
        """Testar método __str__"""
        self.assertEqual(str(self.produto), 'Notebook')
    
    def test_produto_em_estoque(self):
        """Testar método de estoque"""
        self.assertTrue(self.produto.em_estoque())
        
        # Produto sem estoque
        produto_sem_estoque = Produto.objects.create(
            nome='Mouse',
            preco=50.00,
            quantidade=0
        )
        self.assertFalse(produto_sem_estoque.em_estoque())
    
    def test_produto_preco_com_desconto(self):
        """Testar cálculo de preço com desconto"""
        self.produto.desconto = 10
        self.produto.save()
        
        preco_esperado = 2500.00 * 0.9  # 10% de desconto
        self.assertEqual(self.produto.get_preco_com_desconto(), preco_esperado)


# ============================================================================
# TESTE DE VIEW
# ============================================================================

class ProdutoViewTestCase(TestCase):
    """
    Testes para views de produtos.
    """
    
    def setUp(self):
        """Preparar dados"""
        self.client = Client()
        self.produto = Produto.objects.create(
            nome='Teste',
            preco=100.00
        )
    
    def test_lista_produtos_view(self):
        """Testar view de listagem"""
        response = self.client.get(reverse('produtos:lista'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Teste')
        self.assertTemplateUsed(response, 'produtos/lista.html')
    
    def test_detalhe_produto_view(self):
        """Testar view de detalhe"""
        url = reverse('produtos:detalhe', args=[self.produto.id])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.produto.nome)
    
    def test_produto_nao_existe(self):
        """Testar produto que não existe"""
        url = reverse('produtos:detalhe', args=[99999])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)
    
    def test_criar_produto_requer_login(self):
        """Testar que criar produto requer login"""
        url = reverse('produtos:criar')
        response = self.client.get(url)
        
        # Deve redirecionar para login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)


# ============================================================================
# TESTE COM AUTENTICAÇÃO
# ============================================================================

class ProdutoAutenticadoTestCase(TestCase):
    """
    Testes que requerem autenticação.
    """
    
    def setUp(self):
        """Preparar dados e usuário"""
        self.client = Client()
        User = get_user_model()
        
        # Criar usuário
        self.usuario = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        # Fazer login
        self.client.login(username='testuser', password='testpass123')
    
    def test_criar_produto_com_login(self):
        """Testar criar produto quando logado"""
        url = reverse('produtos:criar')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
    
    def test_criar_produto_post(self):
        """Testar POST para criar produto"""
        url = reverse('produtos:criar')
        data = {
            'nome': 'Novo Produto',
            'preco': 150.00,
            'descricao': 'Descrição do produto'
        }
        
        response = self.client.post(url, data)
        
        # Deve redirecionar após criar
        self.assertEqual(response.status_code, 302)
        
        # Verificar se produto foi criado
        produto = Produto.objects.get(nome='Novo Produto')
        self.assertEqual(produto.preco, 150.00)


# ============================================================================
# TESTE DE FORMULÁRIO
# ============================================================================

class ProdutoFormTestCase(TestCase):
    """
    Testes para formulários.
    """
    
    def test_form_valido(self):
        """Testar formulário válido"""
        from .forms import ProdutoForm
        
        data = {
            'nome': 'Produto Teste',
            'preco': 100.00,
            'descricao': 'Descrição'
        }
        form = ProdutoForm(data=data)
        
        self.assertTrue(form.is_valid())
    
    def test_form_preco_invalido(self):
        """Testar validação de preço"""
        from .forms import ProdutoForm
        
        data = {
            'nome': 'Produto',
            'preco': -10.00,  # Preço negativo
            'descricao': 'Descrição'
        }
        form = ProdutoForm(data=data)
        
        self.assertFalse(form.is_valid())
        self.assertIn('preco', form.errors)
    
    def test_form_campos_obrigatorios(self):
        """Testar campos obrigatórios"""
        from .forms import ProdutoForm
        
        form = ProdutoForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('preco', form.errors)


# ============================================================================
# TESTE DE INTEGRAÇÃO
# ============================================================================

class FluxoCompletoTestCase(TestCase):
    """
    Teste de integração completo (fluxo de usuário).
    """
    
    def setUp(self):
        """Preparar dados"""
        self.client = Client()
        User = get_user_model()
        self.usuario = User.objects.create_user(
            username='user',
            password='pass123'
        )
    
    def test_fluxo_criar_produto(self):
        """Testar fluxo completo de criar produto"""
        # 1. Login
        self.client.login(username='user', password='pass123')
        
        # 2. Acessar página de criação
        url = reverse('produtos:criar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # 3. Criar produto
        data = {
            'nome': 'Produto Final',
            'preco': 200.00,
            'descricao': 'Teste'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        
        # 4. Verificar se produto foi criado
        produto = Produto.objects.get(nome='Produto Final')
        self.assertIsNotNone(produto)
        
        # 5. Ver detalhe do produto
        url_detalhe = reverse('produtos:detalhe', args=[produto.id])
        response = self.client.get(url_detalhe)
        self.assertContains(response, 'Produto Final')


# ============================================================================
# TESTE COM FIXTURES
# ============================================================================

class TestComFixtures(TestCase):
    """
    Teste usando fixtures (dados pré-carregados).
    """
    fixtures = ['produtos.json', 'categorias.json']
    
    def test_carregar_fixtures(self):
        """Testar se fixtures foram carregadas"""
        # Produtos da fixture devem existir
        produtos = Produto.objects.all()
        self.assertGreater(produtos.count(), 0)


# ============================================================================
# TESTE DE PERFORMANCE (QUERIES)
# ============================================================================

from django.test.utils import override_settings
from django.db import connection
from django.test.utils import CaptureQueriesContext

class ProdutoQueriesTestCase(TestCase):
    """
    Teste para verificar número de queries executadas.
    """
    
    def setUp(self):
        """Criar muitos produtos"""
        for i in range(10):
            Produto.objects.create(
                nome=f'Produto {i}',
                preco=100.00
            )
    
    def test_lista_produtos_otimizada(self):
        """Verificar se lista usa select_related"""
        with CaptureQueriesContext(connection) as context:
            produtos = list(Produto.objects.select_related('categoria').all())
        
        # Verificar número de queries
        self.assertLessEqual(len(context.captured_queries), 2)


# ============================================================================
# TESTE COM MOCK
# ============================================================================

from unittest.mock import patch, MagicMock

class ProdutoComMockTestCase(TestCase):
    """
    Teste usando mocks (simular comportamentos externos).
    """
    
    @patch('app.views.enviar_email')
    def test_criar_produto_envia_email(self, mock_enviar_email):
        """Testar se email é enviado ao criar produto"""
        # Simular criação de produto
        produto = Produto.objects.create(
            nome='Produto',
            preco=100.00
        )
        
        # Chamar função que envia email
        # enviar_email_notificacao(produto)
        
        # Verificar se função foi chamada
        # mock_enviar_email.assert_called_once()


# ============================================================================
# EXECUTAR TESTES
# ============================================================================

"""
# Executar todos os testes
python manage.py test

# Executar testes de um app específico
python manage.py test produtos

# Executar testes de uma classe específica
python manage.py test produtos.tests.ProdutoTestCase

# Executar um teste específico
python manage.py test produtos.tests.ProdutoTestCase.test_produto_criacao

# Executar com verbose
python manage.py test --verbosity=2

# Executar mantendo banco de dados de teste
python manage.py test --keepdb

# Executar testes em paralelo
python manage.py test --parallel
"""

print("Arquivo de referência: Testes no Django")
print("Use TestCase para criar testes automatizados do seu código")

