import requests

class CalculadoraCliente:
    def __init__(self):
        self.base_url = "http://localhost:8081"

    def somar(self, numero1, numero2):
        #endpoint para a operações de somar
        endpoint_somar = f"{self.base_url}/somar"

        #dados vão na URL como parâmetros da requisição GET
        dados = f"?numero1={numero1}&numero2={numero2}"
        
         # Faz uma requisição HTTP GET usando a biblioteca requests
        response_somar = requests.get(endpoint_somar + dados)
        # Converte a resposta JSON para dicionário Python
        dados_json = response_somar.json()

        print("=" * 30)
        print(f"RESULTADO SOMAR: {dados_json['resultado']}")
        print("=" * 30)

if __name__ == "__main__":
    cliente = CalculadoraCliente()
    cliente.somar(20, 10)