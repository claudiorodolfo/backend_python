import requests

class CalculadoraCliente:
    def __init__(self):
        self.base_url = "http://localhost:8081"

    def calcular(self, numero1, numero2):
        #endpoints para as operações aritméticas
        endpoint_get_somar = f"{self.base_url}/somar"
        endpoint_get_subtrair = f"{self.base_url}/subtrair"
        endpoint_post_multiplicar = f"{self.base_url}/multiplicar"
        endpoint_post_dividir = f"{self.base_url}/dividir"

        #dados a serem anexados ao cabeçalho da requisição HTTP
        dados_post = {
            "numero1": numero1,
            "numero2": numero2
        }
        #dados vão na URL como parâmetros da requisição GET
        dados_get = f"?numero1={numero1}&numero2={numero2}"

        response_get_somar = requests.get(endpoint_get_somar + dados_get)
        response_get_subtrair = requests.get(endpoint_get_subtrair + dados_get)

        response_post_multiplicar = requests.post(endpoint_post_multiplicar, dados_post)
        response_post_dividir = requests.post(endpoint_post_dividir, dados_post)


        print("=" * 30)
        print(f"SOMAR: {response_get_somar.json()["resultado"]}")
        print(f"SUBTRAIR: {response_get_subtrair.json()["resultado"]}")
        print("=" * 30)
        print(f"MULTIPLICAR: {response_post_multiplicar.json()["resultado"]}")
        print(f"DIVIDIR: {response_post_dividir.json()["resultado"]}")
        print("=" * 30)

if __name__ == "__main__":
    cliente = CalculadoraCliente()
    cliente.calcular(20, 10)