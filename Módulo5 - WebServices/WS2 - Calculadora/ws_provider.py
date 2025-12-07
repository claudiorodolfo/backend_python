import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Classe Provider para lidar com as requisições HTTP
class WSProvider(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        # Obtém os parâmetros da requisição GET
        query_params = parse_qs(parsed_path.query)
        numero1 = int(query_params["numero1"][0])
        numero2 = int(query_params["numero2"][0])

        if self.path.startswith("/somar"):
            print("Requisição GET recebida - SOMAR")
            # Realiza a operação de soma
            calc = CalculadoraService()
            resultado = calc.somar(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

        elif self.path.startswith("/subtrair"):
            print("Requisição GET recebida - SUBTRAIR")
            # Realiza a operação de subtração
            calc = CalculadoraService()
            resultado = calc.subtrair(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

    def do_POST(self):
        tamanho = int(self.headers['Content-Length'])
        corpo = self.rfile.read(tamanho).decode('utf-8')
        # Obtém os parâmetros da requisição POST
        dados = parse_qs(corpo)
        numero1 = int(dados["numero1"][0])
        numero2 = int(dados["numero2"][0])

        if self.path == "/multiplicar":
            print("Requisição POST recebida - MULTIPLICAR")
            # Realiza a operação de multiplicação
            calc = CalculadoraService()
            resultado = calc.multiplicar(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

        elif self.path == "/dividir":
            print("Requisição POST recebida - DIVIDIR")
            # Realiza a operação de divisão
            calc = CalculadoraService()
            resultado = calc.dividir(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

# Serviço fornecido pelo Web Service Provider
class CalculadoraService:
    def somar(self, numero1, numero2):
        return numero1 + numero2

    def subtrair(self, numero1, numero2):
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):
        return numero1 * numero2

    def dividir(self, numero1, numero2):
        if numero2 == 0:
            return "Erro: Divisão por zero"
        return numero1 / numero2

def main():
    # Inicia o servidor HTTP na porta 8081
    servidor = HTTPServer(('127.0.0.1', 8081), WSProvider)
    print("Servidor iniciado em http://127.0.0.1:8081")
    servidor.serve_forever()

if __name__ == "__main__":
    main()