from http.server import BaseHTTPRequestHandler, HTTPServer
import json

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, peso):
        s = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = (s * 10) % 11
        return 0 if resto == 10 else resto

    dig1 = calc_digito(cpf, 10)
    dig2 = calc_digito(cpf, 11)

    return cpf[-2:] == f"{dig1}{dig2}"


class CPFService(BaseHTTPRequestHandler):

    # ------------------------------
    # GET /cpf?cpf=XXXXXXXXXXX
    # ------------------------------
    def do_GET(self):
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(self.path)

        if parsed.path == "/cpf":
            params = parse_qs(parsed.query)
            cpf = params.get("cpf", [""])[0]

            valido = validar_cpf(cpf)
            self._send_json(200, {"cpf": cpf, "valid": valido})
            return

        self._send_json(404, {"error": "rota não encontrada"})

    # ------------------------------
    # POST /cpf
    # Body: { "cpf": "11144477735" }
    # ------------------------------
    def do_POST(self):
        if self.path == "/cpf":
            tamanho = int(self.headers.get('Content-Length', 0))
            corpo = self.rfile.read(tamanho).decode("utf-8")

            try:
                dados = json.loads(corpo)
                cpf = dados.get("cpf", "")
            except:
                self._send_json(400, {"error": "JSON inválido"})
                return

            valido = validar_cpf(cpf)
            self._send_json(200, {"cpf": cpf, "valid": valido})
            return

        self._send_json(404, {"error": "rota não encontrada"})

    # ------------------------------
    # Helper para JSON
    # ------------------------------
    def _send_json(self, status, data):
        resposta = json.dumps(data).encode()

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resposta)))
        self.end_headers()
        self.wfile.write(resposta)


def run():
    servidor = HTTPServer(("localhost", 8000), CPFService)
    print("Servidor rodando em http://localhost:8000 ...")
    servidor.serve_forever()


if __name__ == "__main__":
    run()
