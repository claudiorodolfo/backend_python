"""
Cliente REST para Calculadora
Consome o serviço de calculadora via requisições HTTP
"""

# Importa o módulo json para serializar e desserializar dados JSON
import json
# Importa a biblioteca requests para fazer requisições HTTP
import requests


# Define a classe CalculadoraCliente para consumir o serviço REST
class CalculadoraCliente:
    """Cliente para consumir o serviço de calculadora"""
    
    # Define o método construtor __init__ que recebe a URL base do servidor
    def __init__(self, base_url='http://localhost:8000'):
        """Inicializa o cliente com a URL base do servidor"""
        # Remove a barra final da URL base se existir e armazena em self.base_url
        self.base_url = base_url.rstrip('/')
    
    # Define o método calcular que realiza uma requisição HTTP POST para calcular
    def calcular(self, operacao, numero1, numero2):
        """Realiza um cálculo"""
        # Constrói a URL completa do endpoint concatenando a URL base com '/calcular'
        url = f"{self.base_url}/calcular"
        # Cria um dicionário com os dados da requisição (operação e dois números)
        dados = {
            "operacao": operacao,
            "numero1": numero1,
            "numero2": numero2
        }
        
        # Inicia um bloco try para capturar possíveis erros na requisição
        try:
            # Realiza uma requisição POST usando requests, enviando dados como JSON
            # O parâmetro json=dados automaticamente serializa para JSON e define Content-Type
            response = requests.post(url, json=dados)
            
             # Converte a resposta JSON para dicionário e retorna junto com o código HTTP
            return response.json(), response.status_code

        # Captura erros de conexão (ex: servidor não encontrado)
        except Exception as e:
            # Retorna um dicionário com mensagem de erro inesperado e None para o código
            return {"erro": f"Erro inesperado: {str(e)}"}, None


# Define a função main que será executada quando o script for chamado diretamente
def main():
    """Função principal para testar o cliente"""
    # Cria uma instância do cliente CalculadoraCliente com a URL padrão
    cliente = CalculadoraCliente()
    
    # Imprime uma linha de separação com 50 caracteres '='
    print("=" * 50)
    # Imprime o título do cliente
    print("Cliente Calculadora REST")
    # Imprime outra linha de separação com 50 caracteres '='
    print("=" * 50)
    
    # Testa as operações
    # Cria uma lista de tuplas com operações e números para testar
    testes = [
        # Tupla com operação de soma, primeiro número 10 e segundo número 5
        ('soma', 10, 5),
        # Tupla com operação de subtração, primeiro número 10 e segundo número 5
        ('subtracao', 10, 5),
        # Tupla com operação de multiplicação, primeiro número 10 e segundo número 5
        ('multiplicacao', 10, 5),
        # Tupla com operação de divisão, primeiro número 10 e segundo número 5
        ('divisao', 10, 5),
        # Tupla com operação de divisão por zero para testar tratamento de erro
        ('divisao', 10, 0),  # Teste de erro
    ]
    
    # Itera sobre cada tupla na lista de testes
    for operacao, num1, num2 in testes:
        # Imprime o nome da operação em maiúsculas e os números sendo testados
        print(f"\n{operacao.upper()}({num1}, {num2}):")
        # Chama o método calcular do cliente passando a operação e os dois números
        resposta, codigo = cliente.calcular(operacao, num1, num2)
        
        # Verifica se o código HTTP retornado é 200 (sucesso)
        if codigo == 200:
            # Obtém o resultado do dicionário de resposta
            resultado = resposta.get('resultado')
            # Imprime o resultado do cálculo
            print(f"  Resultado: {resultado}")
        else:
            # Se o código não for 200, obtém a mensagem de erro ou usa uma mensagem padrão
            erro = resposta.get('erro', 'Erro desconhecido')
            # Imprime a mensagem de erro
            print(f"  Erro: {erro}")


# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Chama a função main para executar os testes
    main()
