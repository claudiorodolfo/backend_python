import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pessoa_service import PessoaService
from pessoa import Pessoa

# Classe Provider para lidar com as requisições HTTP
class WSProvider(BaseHTTPRequestHandler):
    # Instância compartilhada do serviço para todas as requisições
    _service = PessoaService()

    def do_GET(self):
        if self.path.startswith("/pessoas"):
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            
            # Verifica se há parâmetro email na query string
            if 'email' in query_params:
                print("Requisição GET recebida - BUSCAR POR EMAIL")
                # Realiza a operação de buscar pessoa por email
                email = query_params['email'][0]
                pessoa_busca = Pessoa(email)
                pessoa = self._service.buscarPorEmail(pessoa_busca)
                
                if pessoa:
                    # Converte objeto Pessoa para dicionário
                    pessoa_json = {
                        "email": pessoa.email,
                        "nome": pessoa.nome,
                        "idade": pessoa.idade,
                        "altura": pessoa.altura
                    }
                    # Envia a resposta para o cliente
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    msg_retorno = {"pessoa": pessoa_json}
                    resposta = json.dumps(msg_retorno).encode('utf-8')
                    self.wfile.write(resposta)
                else:
                    # Pessoa não encontrada
                    self.send_response(404)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    msg_retorno = {"erro": "Pessoa não encontrada"}
                    resposta = json.dumps(msg_retorno).encode('utf-8')
                    self.wfile.write(resposta)
            else:
                print("Requisição GET recebida - LISTAR")
                # Realiza a operação de listar pessoas
                pessoas = self._service.listarTodas()
                # Converte lista de objetos Pessoa para lista de dicionários
                pessoas_json = []
                for pessoa in pessoas:
                    pessoas_json.append({
                        "email": pessoa.email,
                        "nome": pessoa.nome,
                        "idade": pessoa.idade,
                        "altura": pessoa.altura
                    })
                # Envia a resposta para o cliente
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"pessoas": pessoas_json}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)

    def do_POST(self):
        if self.path.startswith("/pessoas"):
            print("Requisição POST recebida - CRIAR")
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            
            # Extrai os parâmetros da query string
            email = query_params.get('email', [None])[0]
            nome = query_params.get('nome', [None])[0]
            idade = query_params.get('idade', [None])[0]
            altura = query_params.get('altura', [None])[0]
            
            # Valida se email foi fornecido
            if not email:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"erro": "Email é obrigatório"}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)
                return
            
            # Converte idade e altura se fornecidos
            idade_int = int(idade) if idade else None
            altura_float = float(altura) if altura else None
            
            # Cria o objeto Pessoa
            pessoa = Pessoa(
                email=email,
                nome=nome,
                idade=idade_int,
                altura=altura_float
            )
            
            # Realiza a operação de criar pessoa
            pessoa_criada = self._service.criar(pessoa)
            
            # Converte objeto Pessoa para dicionário
            pessoa_json = {
                "email": pessoa_criada.email,
                "nome": pessoa_criada.nome,
                "idade": pessoa_criada.idade,
                "altura": pessoa_criada.altura
            }
            
            # Envia a resposta para o cliente
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            msg_retorno = {"pessoa": pessoa_json}
            resposta = json.dumps(msg_retorno).encode('utf-8')
            self.wfile.write(resposta)

    def do_PUT(self):
        if self.path.startswith("/pessoas"):
            print("Requisição PUT recebida - ATUALIZAR")
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            
            # Extrai os parâmetros da query string
            email = query_params.get('email', [None])[0]
            nome = query_params.get('nome', [None])[0]
            idade = query_params.get('idade', [None])[0]
            altura = query_params.get('altura', [None])[0]
            
            # Valida se email foi fornecido
            if not email:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"erro": "Email é obrigatório"}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)
                return
            
            # Converte idade e altura se fornecidos
            idade_int = int(idade) if idade else None
            altura_float = float(altura) if altura else None
            
            # Cria o objeto Pessoa
            pessoa = Pessoa(
                email=email,
                nome=nome,
                idade=idade_int,
                altura=altura_float
            )
            
            # Realiza a operação de atualizar pessoa
            pessoa_atualizada = self._service.atualizar(pessoa)
            
            if pessoa_atualizada:
                # Converte objeto Pessoa para dicionário
                pessoa_json = {
                    "email": pessoa_atualizada.email,
                    "nome": pessoa_atualizada.nome,
                    "idade": pessoa_atualizada.idade,
                    "altura": pessoa_atualizada.altura
                }
                # Envia a resposta para o cliente
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"pessoa": pessoa_json}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)
            else:
                # Pessoa não encontrada
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"erro": "Pessoa não encontrada"}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)

    def do_DELETE(self):
        if self.path.startswith("/pessoas"):
            print("Requisição DELETE recebida - APAGAR")
            parsed_url = urlparse(self.path)
            query_params = parse_qs(parsed_url.query)
            
            # Extrai o parâmetro email da query string
            email = query_params.get('email', [None])[0]
            
            # Valida se email foi fornecido
            if not email:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"erro": "Email é obrigatório"}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)
                return
            
            # Cria o objeto Pessoa para busca
            pessoa = Pessoa(email=email)
            
            # Realiza a operação de apagar pessoa
            resultado = self._service.apagar(pessoa)
            
            if resultado:
                # Pessoa apagada com sucesso
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"mensagem": "Pessoa apagada com sucesso"}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)
            else:
                # Pessoa não encontrada
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                msg_retorno = {"erro": "Pessoa não encontrada"}
                resposta = json.dumps(msg_retorno).encode('utf-8')
                self.wfile.write(resposta)

def main():
    # Inicia o servidor HTTP na porta 8080
    servidor = HTTPServer(('127.0.0.1', 8080), WSProvider)
    print("Servidor iniciado em http://127.0.0.1:8080")
    servidor.serve_forever()

if __name__ == "__main__":
    main()