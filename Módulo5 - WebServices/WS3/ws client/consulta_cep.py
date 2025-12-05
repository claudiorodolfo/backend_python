import requests

def consulta_cep(cep: str):
    # limpa formatação
    cep = ''.join(c for c in cep if c.isdigit())
    if len(cep) != 8:
        raise ValueError("CEP deve ter 8 dígitos")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()  # levanta erro se status ≠ 200

    dados = resp.json()
    if "erro" in dados:
        return None  # CEP não encontrado
    return dados

if __name__ == "__main__":
    cep = "01001000"
    endereco = consulta_cep(cep)
    if endereco:
        print("CEP:", endereco.get("cep"))
        print("Logradouro:", endereco.get("logradouro"))
        print("Bairro:", endereco.get("bairro"))
        print("Cidade/UF:", endereco.get("localidade"), "/", endereco.get("uf"))
    else:
        print("CEP não encontrado.")
