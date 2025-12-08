import requests

class CPFCliente:
    def __init__(self):
        self.base_url = "http://localhost:8080"

    def validar(self, cpf: str):
        #endpoint para a operação de validar CPF
        endpoint_cpf = f"{self.base_url}/validar"

        #dados vão na URL como parâmetros da requisição GET
        dados = f"?cpf={cpf}"
        
         # Faz uma requisição HTTP GET usando a biblioteca requests
        response_validar = requests.get(endpoint_cpf + dados)
        # Converte a resposta JSON para dicionário Python
        dados_json = response_validar.json()

        print("=" * 30)
        print(f"RESULTADO VALIDAR CPF: {dados_json['valido']}")
        print("=" * 30)

if __name__ == "__main__":
    cliente = CPFCliente()
    cliente.validar("11144477735")
    cliente.validar("11111111111")