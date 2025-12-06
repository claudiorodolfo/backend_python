# Importa a classe BaseHTTPRequestHandler para criar um handler HTTP personalizado
from http.server import BaseHTTPRequestHandler, HTTPServer
# Importa o módulo json para serializar e deserializar dados JSON
import json

# Define a função para validar um CPF (Cadastro de Pessoa Física)
def validar_cpf(cpf):
    # Remove todos os caracteres não numéricos do CPF, mantendo apenas dígitos
    cpf = ''.join(filter(str.isdigit, cpf))
    # Verifica se o CPF tem exatamente 11 dígitos após a limpeza
    if len(cpf) != 11:
        # Retorna False se o CPF não tiver 11 dígitos
        return False
    # Verifica se todos os dígitos são iguais (ex: 11111111111, 22222222222)
    if cpf == cpf[0] * 11:
        # Retorna False se todos os dígitos forem iguais (CPF inválido)
        return False

    # Define função interna para calcular um dígito verificador do CPF
    def calc_digito(cpf, peso):
        # Calcula a soma ponderada: multiplica cada dígito pela posição (peso - índice)
        # O peso começa em 10 para o primeiro dígito verificador e 11 para o segundo
        s = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        # Calcula o resto da divisão por 11 e multiplica por 10
        resto = (s * 10) % 11
        # Se o resto for 10, o dígito verificador é 0, caso contrário é o próprio resto
        return 0 if resto == 10 else resto

    # Calcula o primeiro dígito verificador (posição 9 do CPF) usando peso 10
    dig1 = calc_digito(cpf, 10)
    # Calcula o segundo dígito verificador (posição 10 do CPF) usando peso 11
    dig2 = calc_digito(cpf, 11)

    # Compara os dois últimos dígitos do CPF com os dígitos calculados
    # Retorna True se forem iguais (CPF válido), False caso contrário
    return cpf[-2:] == f"{dig1}{dig2}"


# Define a classe CPFService que herda de BaseHTTPRequestHandler
# Esta classe processa requisições HTTP para validação de CPF
class CPFService(BaseHTTPRequestHandler):

    # ------------------------------
    # GET /cpf?numero=XXXXXXXXXXX
    # ------------------------------
    # Método que processa requisições HTTP GET
    def do_GET(self):
        # Importa funções para fazer parse da URL e dos parâmetros de query
        from urllib.parse import urlparse, parse_qs
        # Faz o parse da URL da requisição para extrair path e query string
        parsed = urlparse(self.path)

        # Verifica se o caminho da requisição é "/cpf"
        if parsed.path == "/cpf":
            # Extrai os parâmetros da query string (ex: ?numero=11144477735)
            params = parse_qs(parsed.query)
            # Obtém o valor do parâmetro "numero", retornando string vazia se não existir
            # parse_qs retorna uma lista, então pegamos o primeiro elemento [0]
            cpf = params.get("numero", [""])[0]

            # Chama a função validar_cpf para verificar se o CPF é válido
            valido = validar_cpf(cpf)
            # Envia resposta JSON com status 200 (OK), contendo o CPF e se é válido
            self._send_json(200, {"cpf": cpf, "valido": valido})
            # Retorna para encerrar o processamento da requisição
            return

        # Se o caminho não for "/cpf", retorna erro 404 (não encontrado)
        self._send_json(404, {"erro": "rota não encontrada"})

    # ------------------------------
    # POST /cpf
    # Body: { "cpf": "11144477735" }
    # ------------------------------
    # Método que processa requisições HTTP POST
    def do_POST(self):
        # Verifica se o caminho da requisição é "/cpf"
        if self.path == "/cpf":
            # Obtém o tamanho do corpo da requisição do header Content-Length
            # Se não existir, assume 0
            tamanho = int(self.headers.get('Content-Length', 0))
            # Lê o corpo da requisição (bytes) e decodifica para string UTF-8
            corpo = self.rfile.read(tamanho).decode("utf-8")

            # Tenta fazer o parse do JSON do corpo da requisição
            try:
                # Converte a string JSON em um dicionário Python
                dados = json.loads(corpo)
                # Obtém o valor da chave "cpf" do JSON, retornando string vazia se não existir
                cpf = dados.get("cpf", "")
            except:
                # Se houver erro ao fazer parse do JSON, retorna erro 400 (Bad Request)
                self._send_json(400, {"erro": "JSON inválido"})
                # Retorna para encerrar o processamento
                return

            # Chama a função validar_cpf para verificar se o CPF é válido
            valido = validar_cpf(cpf)
            # Envia resposta JSON com status 200 (OK), contendo o CPF e se é válido
            self._send_json(200, {"cpf": cpf, "valido": valido})
            # Retorna para encerrar o processamento da requisição
            return

        # Se o caminho não for "/cpf", retorna erro 404 (não encontrado)
        self._send_json(404, {"erro": "rota não encontrada"})

    # ------------------------------
    # Helper para JSON
    # ------------------------------
    # Método auxiliar privado para enviar respostas JSON
    def _send_json(self, status, data):
        # Converte o dicionário Python em string JSON e depois em bytes
        resposta = json.dumps(data).encode()

        # Envia o código de status HTTP (ex: 200, 404, 400)
        self.send_response(status)
        # Define o header Content-Type como application/json
        self.send_header("Content-Type", "application/json")
        # Define o header Content-Length com o tamanho da resposta em bytes
        self.send_header("Content-Length", str(len(resposta)))
        # Finaliza o envio dos headers HTTP
        self.end_headers()
        # Escreve o corpo da resposta (JSON em bytes) no stream de saída
        self.wfile.write(resposta)


# Define a função run() que inicia o servidor HTTP
def run():
    # Cria uma instância de HTTPServer escutando em localhost na porta 8000
    # CPFService é a classe handler que processará as requisições
    servidor = HTTPServer(("localhost", 8000), CPFService)
    # Imprime mensagem informando que o servidor está rodando
    print("Servidor rodando em http://localhost:8000 ...")
    # Inicia o servidor e fica escutando requisições indefinidamente
    servidor.serve_forever()


# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função run() para iniciar o servidor
    run()
