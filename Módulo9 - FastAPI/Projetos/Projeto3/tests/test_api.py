from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_list_pessoa() -> None:
    payload = {'nome': 'Carlos', 'email': 'carlos@email.com', 'telefone': '11999999999', 'ativa': True}
    assert client.post('/pessoas', json=payload).status_code == 201
    listed = client.get('/pessoas')
    assert listed.status_code == 200
    assert len(listed.json()) >= 1
