import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class Provider(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if self.path.startswith("/somar"):
            print("Requisição GET recebida - SOMAR")
            numero1 = int(query_params.get('numero1', [0])[0])
            numero2 = int(query_params.get('numero2', [0])[0])
            resultado = self.somar(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

        elif self.path.startswith("/subtrair"):
            print("Requisição GET recebida - SUBTRAIR")
            numero1 = int(query_params.get('numero1', [0])[0])
            numero2 = int(query_params.get('numero2', [0])[0])
            resultado = self.subtrair(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

    def do_POST(self):
        tamanho = int(self.headers['Content-Length'])
        corpo = self.rfile.read(tamanho).decode('utf-8')
        # O cliente envia dados como form data (application/x-www-form-urlencoded)
        dados = parse_qs(corpo)
        numero1 = int(dados.get('numero1', [0])[0])
        numero2 = int(dados.get('numero2', [0])[0])

        if self.path == "/multiplicar":
            print("Requisição POST recebida - MULTIPLICAR")
            resultado = self.multiplicar(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

        elif self.path == "/dividir":
            print("Requisição POST recebida - DIVIDIR")
            resultado = self.dividir(numero1, numero2)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"resultado": resultado}).encode('utf-8')
            self.wfile.write(resposta)

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
    servidor = HTTPServer(('127.0.0.1', 8081), Provider)
    print("Servidor iniciado em http://127.0.0.1:8081")
    servidor.serve_forever()

if __name__ == "__main__":
    main()