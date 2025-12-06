"""
Cliente REST para Consulta de CEP
Consome o serviço ViaCEP para buscar informações de endereço via requisições HTTP
"""

# Importa o módulo json para serializar e desserializar dados JSON
import json
# Importa o módulo requests para fazer requisições HTTP
import requests


# Define a classe ConsultaCepCliente para consumir o serviço REST
class ConsultaCepCliente:
    """Cliente para consumir o serviço de consulta de CEP"""
    
    # Define o método construtor __init__ que recebe a URL base do servidor ViaCEP
    def __init__(self, base_url='https://viacep.com.br'):
        """Inicializa o cliente com a URL base do servidor ViaCEP"""
        # Remove a barra final da URL base se existir e armazena em self.base_url
        self.base_url = base_url.rstrip('/')
    
    # Define o método consultar que realiza uma requisição HTTP GET para consultar CEP
    def consultar(self, cep):
        """Realiza uma consulta de CEP"""
        
        # Verifica se o CEP tem exatamente 8 dígitos após a limpeza
        if len(cep) != 8:
            # Retorna um dicionário com mensagem de erro e None para o código
            return {"erro": "CEP deve ter 8 dígitos"}, None
        
        # Constrói a URL completa do endpoint concatenando a URL base com o caminho da API ViaCEP
        url = f"{self.base_url}/ws/{cep}/json/"
        
        # Inicia um bloco try para capturar possíveis erros na requisição
        try:
            # Faz uma requisição HTTP GET usando a biblioteca requests
            response = requests.get(url, timeout=5)
            # Verifica se a requisição foi bem-sucedida (código 200)
            response.raise_for_status()
            # Converte a resposta JSON para dicionário Python
            dados = response.json()
            
            # Verifica se a resposta contém a chave "erro", indicando CEP não encontrado
            if "erro" in dados:
                # Retorna um dicionário com mensagem de erro e código 404
                return {"erro": "CEP não encontrado"}, 404
            
            # Retorna o dicionário com os dados do endereço e o código HTTP 200
            return dados, 200
                
        except Exception as e:
            # Retorna um dicionário com mensagem de erro inesperado e None para o código
            return {"erro": f"Erro inesperado: {str(e)}"}, None


# Define a função main que será executada quando o script for chamado diretamente
def main():
    """Função principal para testar o cliente"""
    # Cria uma instância do cliente ConsultaCepCliente com a URL padrão
    cliente = ConsultaCepCliente()
    
    # Imprime uma linha de separação com 50 caracteres '='
    print("=" * 50)
    # Imprime o título do cliente
    print("Cliente Consulta CEP REST")
    # Imprime outra linha de separação com 50 caracteres '='
    print("=" * 50)
    
    # Testa diferentes CEPs
    # Cria uma lista de CEPs para testar
    ceps_teste = [
        # CEP válido
        "01001000",
        # CEP válido
        "01310100",
        # CEP válido
        "45078900",
        # CEP não encontrado
        "00000000",
        # CEP inválido (menos de 8 dígitos)
        "12345",
    ]
    
    # Itera sobre cada CEP na lista de testes
    for cep in ceps_teste:
        # Imprime o CEP sendo testado
        print(f"\nConsultando CEP: {cep}")
        # Chama o método consultar do cliente passando o CEP
        resposta, codigo = cliente.consultar(cep)
        
        # Verifica se o código HTTP retornado é 200 (sucesso)
        if codigo == 200:
            # Obtém os dados do endereço do dicionário de resposta
            cep_formatado = resposta.get('cep')
            logradouro = resposta.get('logradouro')
            bairro = resposta.get('bairro')
            localidade = resposta.get('localidade')
            uf = resposta.get('uf')
            # Imprime os dados do endereço encontrado
            print(f"  CEP: {cep_formatado}")
            print(f"  Logradouro: {logradouro}")
            print(f"  Bairro: {bairro}")
            print(f"  Cidade/UF: {localidade} / {uf}")
        else:
            # Se o código não for 200, obtém a mensagem de erro ou usa uma mensagem padrão
            erro = resposta.get('erro', 'Erro desconhecido')
            # Imprime a mensagem de erro
            print(f"  Erro: {erro}")
            # Se houver código HTTP, imprime também
            if codigo:
                print(f"  Código HTTP: {codigo}")


# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Chama a função main para executar os testes
    main()
