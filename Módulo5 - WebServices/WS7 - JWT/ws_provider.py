import jwt
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Chave secreta para assinar tokens
SECRET = "minha_chave_secreta"
USUARIOS = {"admin":"1234", "user":"senha"}

class JWTHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Login
        if self.path == "/login":
            length = int(self.headers.get("Content-Length"))
            body = self.rfile.read(length)
            data = json.loads(body)

            usuario = data.get("usuario")
            senha = data.get("senha")

            # Verifica credenciais
            if USUARIOS.get(usuario) == senha:
                # Cria token com expiração
                payload = {
                    "usuario": usuario,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }
                token = jwt.encode(payload, SECRET, algorithm="HS256")
                
                # Garante que token é string (compatibilidade com diferentes versões do PyJWT)
                if isinstance(token, bytes):
                    token = token.decode('utf-8')

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"token": token}).encode())
            else:
                self.send_response(401)
                self.end_headers()
            return

        self.send_response(404)
        self.end_headers()

    def do_GET(self):
        # Protege rota
        if self.path == "/protegido":
            auth = self.headers.get("Authorization")
            if not auth or not auth.startswith("Bearer "):
                self.send_response(401); self.end_headers(); return

            token = auth.split(" ")[1]
            try:
                # Valida token
                payload = jwt.decode(token, SECRET, algorithms=["HS256"])
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message":f"Acesso liberado: {payload['usuario']}"}).encode())
            except jwt.ExpiredSignatureError:
                self.send_response(401); self.end_headers()
            except jwt.InvalidTokenError:
                self.send_response(401); self.end_headers()
            return

        self.send_response(404)
        self.end_headers()

# Executa
server = HTTPServer(("0.0.0.0", 8000), JWTHandler)
print("Servidor JWT rodando em http://localhost:8000")
server.serve_forever()
