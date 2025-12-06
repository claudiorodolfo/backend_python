import requests
import json

class GestaoCEP:
    def __init__(self, url: str):
        self.url = url

    def consultaCEP(self):
        cep = int(input("Digite o CEP: "))
        url_completa = f"{self.url}/{cep}/json/"

        retorno = requests.get(url_completa)

        dados = retorno.json()
        print("=" * 30)
        print(dados)
        print("=" * 30)
        print(f"O logradouro é {dados["logradouro"]}")

gestao = GestaoCEP("https://viacep.com.br/ws/")
gestao.consultaCEP()
 