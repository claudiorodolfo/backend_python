from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fluxo_catalogo() -> None:
    categoria = client.post('/categorias', json={'nome': 'Eletrônicos', 'ativa': True})
    assert categoria.status_code == 201
    categoria_id = categoria.json()['id']
    produto = client.post('/produtos', json={'nome': 'Mouse', 'preco': 99.9, 'estoque': 10, 'ativo': True, 'categoria_id': categoria_id})
    assert produto.status_code == 201
