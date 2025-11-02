"""
02 - Testes com Pytest
=======================

Este arquivo demonstra como usar Pytest para testes no Django.
"""

# ============================================================================
# INSTALAÇÃO DO PYTEST
# ============================================================================

"""
# Instalar pytest e plugins para Django
pip install pytest pytest-django pytest-cov

# Ou adicionar ao requirements.txt:
pytest>=7.0.0
pytest-django>=4.5.0
pytest-cov>=4.0.0
"""

# ============================================================================
# CONFIGURAÇÃO DO PYTEST
# ============================================================================

"""
# Criar arquivo pytest.ini na raiz do projeto

[pytest]
DJANGO_SETTINGS_MODULE = projeto.settings
python_files = tests.py test_*.py *_tests.py
python_classes = Test*
python_functions = test_*
addopts = 
    --reuse-db
    --nomigrations
    --cov=.
    --cov-report=html
    --cov-report=term-missing
"""

# ============================================================================
# TESTE BÁSICO COM PYTEST
# ============================================================================

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

@pytest.mark.django_db
def test_criar_usuario():
    """Teste simples com pytest"""
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.check_password('testpass123')


@pytest.mark.django_db
def test_login_view(client):
    """Teste de view com pytest"""
    url = reverse('login')
    response = client.get(url)
    
    assert response.status_code == 200
    assert 'login' in response.content.decode().lower()


# ============================================================================
# FIXTURES DO PYTEST
# ============================================================================

@pytest.fixture
def usuario():
    """Fixture para criar usuário"""
    User = get_user_model()
    return User.objects.create_user(
        username='testuser',
        password='testpass123'
    )


@pytest.fixture
def produto():
    """Fixture para criar produto"""
    from app.models import Produto
    return Produto.objects.create(
        nome='Produto Teste',
        preco=100.00,
        quantidade=10
    )


@pytest.fixture
def cliente_autenticado(client, usuario):
    """Fixture para cliente autenticado"""
    client.force_login(usuario)
    return client


@pytest.mark.django_db
def test_com_fixture(produto):
    """Teste usando fixture"""
    assert produto.nome == 'Produto Teste'
    assert produto.preco == 100.00


@pytest.mark.django_db
def test_view_autenticada(cliente_autenticado):
    """Teste de view que requer autenticação"""
    url = reverse('produtos:criar')
    response = cliente_autenticado.get(url)
    
    assert response.status_code == 200


# ============================================================================
# PARAMETRIZAÇÃO DE TESTES
# ============================================================================

@pytest.mark.django_db
@pytest.mark.parametrize("nome,preco,esperado", [
    ("Produto 1", 100.00, 100.00),
    ("Produto 2", 200.00, 200.00),
    ("Produto 3", 0.00, 0.00),
])
def test_criar_produtos(nome, preco, esperado):
    """Teste parametrizado"""
    from app.models import Produto
    
    produto = Produto.objects.create(
        nome=nome,
        preco=preco
    )
    
    assert produto.preco == esperado


# ============================================================================
# MARCADORES (MARKERS)
# ============================================================================

@pytest.mark.slow
@pytest.mark.django_db
def test_lento():
    """Teste marcado como lento"""
    # Simular teste que demora
    import time
    time.sleep(2)
    assert True


@pytest.mark.skip(reason="Ainda não implementado")
def test_nao_implementado():
    """Teste que será pulado"""
    assert False


@pytest.mark.skipif(True, reason="Pular se condição for verdadeira")
def test_condicional():
    """Teste condicionalmente pulado"""
    assert True


# ============================================================================
# TESTE DE PERFORMANCE
# ============================================================================

@pytest.mark.django_db
def test_performance_query(client):
    """Teste de performance de queries"""
    from django.test.utils import CaptureQueriesContext
    from django.db import connection
    from app.models import Produto
    
    # Criar produtos
    for i in range(100):
        Produto.objects.create(nome=f'Produto {i}', preco=100.00)
    
    # Capturar queries
    with CaptureQueriesContext(connection) as context:
        list(Produto.objects.all())
    
    # Verificar número de queries
    assert len(context.captured_queries) == 1


# ============================================================================
# TESTE DE COBERTURA
# ============================================================================

"""
# Executar testes com cobertura
pytest --cov=app --cov-report=html

# Ver relatório HTML
open htmlcov/index.html

# Executar com threshold mínimo
pytest --cov=app --cov-fail-under=80
"""

# ============================================================================
# FIXTURES CONFTEST.PY
# ============================================================================

"""
# Criar arquivo conftest.py na raiz ou no app

import pytest
from django.contrib.auth import get_user_model

@pytest.fixture
def usuario(db):
    User = get_user_model()
    return User.objects.create_user(
        username='testuser',
        password='testpass123'
    )

@pytest.fixture
def cliente_autenticado(client, usuario):
    client.force_login(usuario)
    return client

# Estas fixtures estarão disponíveis em todos os testes
"""

# ============================================================================
# EXECUTAR TESTES COM PYTEST
# ============================================================================

"""
# Executar todos os testes
pytest

# Executar testes de um arquivo específico
pytest app/tests/test_models.py

# Executar testes de uma classe
pytest app/tests/test_models.py::TestProduto

# Executar um teste específico
pytest app/tests/test_models.py::TestProduto::test_criar_produto

# Executar com verbose
pytest -v

# Executar mostrando prints
pytest -s

# Executar apenas testes marcados
pytest -m slow

# Executar com cobertura
pytest --cov=app --cov-report=term-missing

# Executar em paralelo
pytest -n auto

# Executar e parar no primeiro erro
pytest -x

# Executar último teste que falhou
pytest --lf
"""

# ============================================================================
# EXEMPLO COMPLETO: TESTE COM PYTEST
# ============================================================================

"""
# tests/test_produtos.py

import pytest
from django.urls import reverse
from app.models import Produto, Categoria

@pytest.mark.django_db
class TestProdutos:
    """Testes para produtos"""
    
    @pytest.fixture
    def categoria(self):
        return Categoria.objects.create(nome='Eletrônicos')
    
    @pytest.fixture
    def produto(self, categoria):
        return Produto.objects.create(
            nome='Notebook',
            preco=2500.00,
            categoria=categoria
        )
    
    def test_criar_produto(self, categoria):
        produto = Produto.objects.create(
            nome='Mouse',
            preco=50.00,
            categoria=categoria
        )
        assert produto.nome == 'Mouse'
    
    def test_lista_produtos(self, client, produto):
        url = reverse('produtos:lista')
        response = client.get(url)
        
        assert response.status_code == 200
        assert produto.nome in response.content.decode()
    
    @pytest.mark.parametrize("preco", [100.00, 200.00, 300.00])
    def test_produto_preco(self, categoria, preco):
        produto = Produto.objects.create(
            nome='Produto',
            preco=preco,
            categoria=categoria
        )
        assert produto.preco == preco
"""

print("Arquivo de referência: Testes com Pytest")
print("Pytest oferece sintaxe mais limpa e recursos avançados para testes")

