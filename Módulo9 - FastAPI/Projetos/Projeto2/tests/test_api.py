from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_filter() -> None:
    payload = {'nome': 'Bruno Silva', 'email': 'bruno@email.com', 'telefone': '11999999999', 'ativa': True}
    assert client.post('/pessoas', json=payload).status_code == 201
    filtered = client.get('/pessoas', params={'nome': 'Bruno'})
    assert filtered.status_code == 200
    assert len(filtered.json()) >= 1
