#Definir os endpoint para cada operação do CRUD

#USAR este endpoint para retornar todas as pessoas do servidor
#GET http://localhost:8080/pessoas
# ipconfig para ver ip da maquina no windows
# ifconfig para ver ip da maquina no linux

import requests

class CalculadoraCliente:
    def __init__(self):
        self.base_url = "http://localhost:8081"

    def add(self, numero1, numero2):
        #endpoint para a operação de somar
        endpoint_somar = f"{self.base_url}/somar"

        #dados vão na URL como parâmetros da requisição GET
        dados = f"?numero1={numero1}&numero2={numero2}"
        url_completa = endpoint_somar + dados

         # Faz uma requisição HTTP GET usando a biblioteca requests
        response_somar = requests.get(url_completa)
        # Converte a resposta JSON para dicionário Python
        dados_json = response_somar.json()

        print("=" * 30)
        print(f"RESULTADO SOMAR: {dados_json['resultado']}")
        print("=" * 30)

if __name__ == "__main__":
    cliente = CalculadoraCliente()
    cliente.add(20, 10)
