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
            calc = SomaService()
            resultado = calc.somar(numero1, numero2)

            # Envia a resposta para o cliente
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg_retorno = {"resultado": resultado}
            resposta = json.dumps(msg_retorno).encode('utf-8')
            self.wfile.write(resposta)

    def do_POST(self):
        pass
    
# Serviço fornecido pelo Web Service Provider
class SomaService:
    def somar(self, numero1, numero2):
        return numero1 + numero2

def main():
    # Inicia o servidor HTTP na porta 8081
    servidor = HTTPServer(('127.0.0.1', 8081), WSProvider)
    print("Servidor iniciado em http://127.0.0.1:8081")
    servidor.serve_forever()

if __name__ == "__main__":
    main()