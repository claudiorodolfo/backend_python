"""
Cliente REST para Consulta de CEP
Consome o serviço ViaCEP para buscar informações de endereço via requisições HTTP
"""

import requests

class ConsultaCepCliente:
    """Cliente para consumir o serviço de consulta de CEP"""
    
    def __init__(self):
        """Inicializa o cliente com a URL base do servidor ViaCEP"""
        self.base_url = "https://viacep.com.br"
    
    def consultar(self, cep):
        """Realiza uma consulta de CEP"""
        
        # Remove hífens e espaços do CEP
        cep_limpo = cep.replace("-", "").replace(" ", "")
        
        # Verifica se o CEP tem exatamente 8 dígitos após a limpeza
        if len(cep_limpo) != 8 or not cep_limpo.isdigit():
            return {"erro": "CEP deve ter 8 dígitos"}
        
        url = f"{self.base_url}/ws/{cep_limpo}/json/"
        
        try:
            response = requests.get(url, timeout=5)
            dados = response.json()
            return dados
        except Exception as e:
            return {"erro": f"Erro na requisição: {str(e)}"}

if __name__ == '__main__':

    cep_ifba = "45078900"
    
    cliente = ConsultaCepCliente()
    resposta = cliente.consultar(cep_ifba)

    print("=" * 30)
    print("WS Cliente para Consulta de CEP")
    print("=" * 30)
    
    if "erro" in resposta and resposta["erro"] is not False:
        if isinstance(resposta["erro"], bool):
            print("Erro: CEP não encontrado")
        else:
            print(f"Erro: {resposta['erro']}")
    else:
        print(f"CEP: {resposta['cep']}")
        print(f"Logradouro: {resposta['logradouro']}")
        print(f"Bairro: {resposta['bairro']}")
        print(f"Cidade/UF: {resposta['localidade']} / {resposta['uf']}")
    
    print("=" * 30)