"""
Servidor REST para Calculadora
Fornece as 4 operações básicas: soma, subtração, multiplicação e divisão
"""

# Importa o módulo json para serializar e desserializar dados JSON
import json
# Importa HTTPServer e BaseHTTPRequestHandler do módulo http.server para criar um servidor HTTP
from http.server import HTTPServer, BaseHTTPRequestHandler


# Define a classe CalculadoraHandler que herda de BaseHTTPRequestHandler
class CalculadoraHandler(BaseHTTPRequestHandler):
    """Handler para processar requisições da calculadora"""
    
    # Define o método do_POST para processar requisições HTTP POST
    def do_POST(self):
        """Processa requisições POST para realizar cálculos"""
        # Verifica se o caminho da requisição é '/calcular'
        if self.path == '/calcular':
            # Inicia um bloco try para capturar possíveis erros
            try:
                # Lê os dados da requisição
                # Obtém o tamanho do conteúdo da requisição do cabeçalho HTTP
                content_length = int(self.headers['Content-Length'])
                # Lê os dados brutos do corpo da requisição usando o tamanho obtido
                post_data = self.rfile.read(content_length)
                # Decodifica os dados de bytes para string UTF-8 e converte de JSON para dicionário Python
                dados = json.loads(post_data.decode('utf-8'))
                
                # Extrai os parâmetros
                # Obtém a operação do dicionário, converte para minúsculas e usa string vazia como padrão
                operacao = dados.get('operacao', '').lower()
                # Obtém o primeiro número do dicionário, converte para float e usa 0 como padrão
                numero1 = float(dados.get('numero1', 0))
                # Obtém o segundo número do dicionário, converte para float e usa 0 como padrão
                numero2 = float(dados.get('numero2', 0))
                
                # Realiza o cálculo
                # Chama o método privado _calcular passando a operação e os dois números
                resultado = self._calcular(operacao, numero1, numero2)
                
                # Verifica se o resultado não é None (ou seja, a operação foi bem-sucedida)
                if resultado is not None:
                    # Sucesso
                    # Envia o código de status HTTP 200 (OK)
                    self.send_response(200)
                    # Define o cabeçalho Content-Type como application/json
                    self.send_header('Content-type', 'application/json')
                    # Finaliza o envio dos cabeçalhos HTTP
                    self.end_headers()
                    
                    # Cria um dicionário com os dados da resposta incluindo operação, números e resultado
                    resposta = {
                        "operacao": operacao,
                        "numero1": numero1,
                        "numero2": numero2,
                        "resultado": resultado
                    }
                    # Converte o dicionário para JSON, codifica para bytes UTF-8 e escreve na resposta
                    self.wfile.write(json.dumps(resposta).encode('utf-8'))
                else:
                    # Erro na operação
                    # Envia o código de status HTTP 400 (Bad Request)
                    self.send_response(400)
                    # Define o cabeçalho Content-Type como application/json
                    self.send_header('Content-type', 'application/json')
                    # Finaliza o envio dos cabeçalhos HTTP
                    self.end_headers()
                    # Cria um dicionário com a mensagem de erro indicando que a operação não é suportada
                    erro = {"erro": f"Operação '{operacao}' não suportada"}
                    # Converte o dicionário de erro para JSON, codifica para bytes UTF-8 e escreve na resposta
                    self.wfile.write(json.dumps(erro).encode('utf-8'))
                    
            # Captura exceções relacionadas a JSON inválido
            except json.JSONDecodeError:
                # Envia o código de status HTTP 400 (Bad Request)
                self.send_response(400)
                # Define o cabeçalho Content-Type como application/json
                self.send_header('Content-type', 'application/json')
                # Finaliza o envio dos cabeçalhos HTTP
                self.end_headers()
                # Cria um dicionário com a mensagem de erro indicando JSON inválido
                erro = {"erro": "JSON inválido"}
                # Converte o dicionário de erro para JSON, codifica para bytes UTF-8 e escreve na resposta
                self.wfile.write(json.dumps(erro).encode('utf-8'))
            # Captura exceções relacionadas a valores inválidos (ex: divisão por zero)
            except ValueError as e:
                # Envia o código de status HTTP 400 (Bad Request)
                self.send_response(400)
                # Define o cabeçalho Content-Type como application/json
                self.send_header('Content-type', 'application/json')
                # Finaliza o envio dos cabeçalhos HTTP
                self.end_headers()
                # Cria um dicionário com a mensagem de erro convertendo a exceção para string
                erro = {"erro": str(e)}
                # Converte o dicionário de erro para JSON, codifica para bytes UTF-8 e escreve na resposta
                self.wfile.write(json.dumps(erro).encode('utf-8'))
        else:
            # Se o caminho não for '/calcular', retorna erro 404 (Not Found)
            # Envia o código de status HTTP 404 (Not Found)
            self.send_response(404)
            # Define o cabeçalho Content-Type como application/json
            self.send_header('Content-type', 'application/json')
            # Finaliza o envio dos cabeçalhos HTTP
            self.end_headers()
            # Cria um dicionário com a mensagem de erro indicando que o endpoint não foi encontrado
            error = {"erro": "Endpoint não encontrado"}
            # Converte o dicionário de erro para JSON, codifica para bytes UTF-8 e escreve na resposta
            self.wfile.write(json.dumps(error).encode('utf-8'))
    
    # Define o método privado _calcular para realizar os cálculos matemáticos
    def _calcular(self, operacao, numero1, numero2):
        """Realiza o cálculo baseado na operação"""
        # Verifica se a operação é 'soma'
        if operacao == 'soma':
            # Retorna a soma dos dois números
            return numero1 + numero2
        # Verifica se a operação é 'subtracao'
        elif operacao == 'subtracao':
            # Retorna a subtração do primeiro número pelo segundo
            return numero1 - numero2
        # Verifica se a operação é 'multiplicacao'
        elif operacao == 'multiplicacao':
            # Retorna a multiplicação dos dois números
            return numero1 * numero2
        # Verifica se a operação é 'divisao'
        elif operacao == 'divisao':
            # Verifica se o divisor (numero2) é zero
            if numero2 == 0:
                # Lança uma exceção ValueError se houver tentativa de divisão por zero
                raise ValueError("Divisão por zero não é permitida")
            # Retorna a divisão do primeiro número pelo segundo
            return numero1 / numero2
        else:
            # Se a operação não for reconhecida, retorna None
            return None


# Define a função main que será executada quando o script for chamado diretamente
def main():
    """Inicia o servidor"""
    # Define a porta onde o servidor irá escutar (8000)
    porta = 8000
    # Cria uma instância de HTTPServer com o endereço localhost, porta definida e handler CalculadoraHandler
    servidor = HTTPServer(('localhost', porta), CalculadoraHandler)
    
    # Imprime uma mensagem informando que o servidor foi iniciado
    print(f"Servidor iniciado em http://localhost:{porta}")
    # Imprime uma mensagem informando o endpoint disponível
    print(f"Endpoint: http://localhost:{porta}/calcular")
    # Imprime uma mensagem informando como parar o servidor
    print("Pressione Ctrl+C para parar o servidor")
    
    # Inicia um bloco try para capturar interrupções do teclado
    try:
        # Inicia o servidor e mantém ele rodando indefinidamente
        servidor.serve_forever()
    # Captura a exceção KeyboardInterrupt quando o usuário pressiona Ctrl+C
    except KeyboardInterrupt:
        # Imprime uma mensagem informando que o servidor foi encerrado
        print("\nServidor encerrado")
        # Fecha a conexão do servidor
        servidor.server_close()


# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Chama a função main para iniciar o servidor
    main()
