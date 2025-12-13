import base64
from http.server import HTTPServer, BaseHTTPRequestHandler

USUARIOS = {
    "admin": "1234",
    "user": "senha"
}

class SimpleAuthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        auth_header = self.headers.get("Authorization")

        if not auth_header:
            self.send_auth_request()
            return

        # examina header "Basic <base64>"
        method, b64 = auth_header.split()
        if method != "Basic":
            self.send_auth_request()
            return

        try:
            cred = base64.b64decode(b64).decode("utf-8")
            usuario, senha = cred.split(":")
        except Exception:
            self.send_auth_request()
            return

        if USUARIOS.get(usuario) == senha:
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Autenticado com sucesso!")
        else:
            self.send_auth_request()

    def send_auth_request(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Login Required"')
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Autenticacao necessaria")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleAuthHandler)
    print("Servidor HTTP com Basic Auth em http://localhost:8000")
    server.serve_forever()
