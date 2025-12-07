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

    def do_POST(self):
        pass
    
    def somar(self, numero1, numero2):
        return numero1 + numero2

def main():
    servidor = HTTPServer(('127.0.0.1', 8081), Provider)
    print("Servidor iniciado em http://127.0.0.1:8081")
    servidor.serve_forever()

if __name__ == "__main__":
    main()