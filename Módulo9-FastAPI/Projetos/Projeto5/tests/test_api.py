from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fluxo_catalogo_completo() -> None:
    categoria = client.post('/categorias', json={'nome': 'Informática', 'ativa': True})
    assert categoria.status_code == 201
    categoria_id = categoria.json()['id']
    produto = client.post('/produtos', json={'nome': 'Teclado', 'preco': 200.0, 'estoque': 5, 'ativo': True, 'categoria_id': categoria_id})
    assert produto.status_code == 201
    produto_id = produto.json()['id']
    filtro = client.get('/produtos', params={'nome': 'Teclado', 'preco_min': 100, 'preco_max': 300})
    assert filtro.status_code == 200
    assert len(filtro.json()) >= 1
    atualiza = client.patch(f'/produtos/{produto_id}', json={'estoque': 8})
    assert atualiza.status_code == 200
    assert atualiza.json()['estoque'] == 8
    assert client.delete(f'/produtos/{produto_id}').status_code == 204
