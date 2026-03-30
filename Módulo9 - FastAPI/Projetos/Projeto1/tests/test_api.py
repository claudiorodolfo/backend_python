from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crud_pessoas() -> None:
    created = client.post('/pessoas', json={'nome': 'Ana', 'email': 'ana@email.com'})
    assert created.status_code == 201
    pessoa_id = created.json()['id']
    assert client.get(f'/pessoas/{pessoa_id}').status_code == 200
    assert client.put(f'/pessoas/{pessoa_id}', json={'nome': 'Ana Maria'}).status_code == 200
    assert client.delete(f'/pessoas/{pessoa_id}').status_code == 204
