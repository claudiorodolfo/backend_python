import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# Classe Provider para lidar com as requisições HTTP
class WSProvider(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)    
        # Obtém os parâmetros da requisição GET
        query_params = parse_qs(parsed_path.query)
        
        # Verifica se o parâmetro cpf está presente
        if query_params["cpf"]:
            cpf = query_params["cpf"][0]
        else:
            self.send_response(400)  # Bad Request
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"error": "Parâmetro 'cpf' não fornecido"}).encode('utf-8')
            self.wfile.write(resposta)
            return
        

        if self.path.startswith("/validar"):           
            print("Requisição GET recebida - Validar CPF")
            # Realiza a operação de validação
            valida = CPFService()
            resultado = valida.validarCpf(cpf)
        else:
            # Retorna erro 404 quando o endpoint não é /validar
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            resposta = json.dumps({"error": "Endpoint não encontrado"}).encode('utf-8')
            self.wfile.write(resposta)
            return

        # Envia a resposta para o cliente
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        msg_retorno = {"cpf": cpf, "valido": resultado}
        resposta = json.dumps(msg_retorno).encode('utf-8')
        self.wfile.write(resposta)

    def do_POST(self):
        # Este provider só aceita requisições GET
        self.send_response(405)  # 405 Method Not Allowed
        self.send_header('Content-type', 'application/json')
        self.send_header('Allow', 'GET')  # Informa que apenas GET é permitido
        self.end_headers()
        resposta = json.dumps({"error": "Método HTTP 'POST' não é permitido. Apenas o método GET é suportado para este endpoint."}).encode('utf-8')
        self.wfile.write(resposta)
    
# Serviço fornecido pelo Web Service Provider
class CPFService:
    def validarCpf(self, cpf: str) -> bool:
        # Remove todos os caracteres não numéricos do CPF, mantendo apenas dígitos
        cpf_limpo = cpf.replace(".", "").replace("-", "") 
        # Verifica se o CPF tem exatamente 11 dígitos após a limpeza
        if len(cpf_limpo) != 11:
            return False
        # Verifica se todos os dígitos são iguais (ex: 11111111111, 22222222222)
        if cpf_limpo == cpf_limpo[0] * 11:
            return False

        # Calcula os dígitos verificadores
        dig1 = self.__calcDigito(cpf_limpo, 10)
        dig2 = self.__calcDigito(cpf_limpo, 11)

        # Compara os dois últimos dígitos do CPF com os dígitos calculados
        return cpf_limpo[-2:] == f"{dig1}{dig2}"

    # Define função interna para calcular um dígito verificador do CPF
    def __calcDigito(self, cpf, peso):
        s = 0
        for i in range(peso - 1):
            s += int(cpf[i]) * (peso - i)
        resto = (s * 10) % 11
        if resto == 10:
            return 0
        else:
            return resto

def main():
    # Inicia o servidor HTTP na porta 8080
    servidor = HTTPServer(('127.0.0.1', 8080), WSProvider)
    print("Servidor iniciado em http://127.0.0.1:8080")
    servidor.serve_forever()

if __name__ == "__main__":
    main()
