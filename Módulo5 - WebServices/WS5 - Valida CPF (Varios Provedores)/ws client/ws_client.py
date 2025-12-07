import requests
import sys

class CPFCliente:
    def __init__(self, port: int):
        self.base_url = f"http://localhost:{port}"

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
    if len(sys.argv) < 2:
        print("Uso: python ws_client.py <porta>")
        sys.exit(1)
    
    porta = int(sys.argv[1])  
    cliente = CPFCliente(porta)
    cliente.validar("11144477735")