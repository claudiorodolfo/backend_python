# Importa BaseHTTPRequestHandler para criar um handler HTTP personalizado
from http.server import BaseHTTPRequestHandler, HTTPServer
# Importa o módulo json para trabalhar com dados JSON
import json

# Função para validar CPF usando o algoritmo oficial da Receita Federal
def validar_cpf(cpf):
    # Remove todos os caracteres que não são dígitos, mantendo apenas números
    cpf = ''.join(filter(str.isdigit, cpf))
    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11:
        return False
    # Verifica se todos os dígitos são iguais (ex: 11111111111), o que é inválido
    if cpf == cpf[0] * 11:
        return False

    # Função auxiliar para calcular um dígito verificador do CPF
    # cpf: string com os dígitos do CPF
    # peso: peso inicial para o cálculo (10 para o primeiro dígito, 11 para o segundo)
    def calc_digito(cpf, peso):
        # Calcula a soma ponderada: multiplica cada dígito pela posição (peso - i)
        # range(peso - 1) itera sobre os dígitos necessários (9 para primeiro, 10 para segundo)
        s = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        # Calcula o resto da divisão por 11 e multiplica por 10
        resto = (s * 10) % 11
        # Se o resto for 10, retorna 0, caso contrário retorna o resto
        return 0 if resto == 10 else resto

    # Calcula o primeiro dígito verificador (peso 10)
    dig1 = calc_digito(cpf, 10)
    # Calcula o segundo dígito verificador (peso 11)
    dig2 = calc_digito(cpf, 11)

    # Compara os dois últimos dígitos do CPF com os dígitos calculados
    # cpf[-2:] pega os dois últimos caracteres do CPF (dígitos verificadores)
    # f"{dig1}{dig2}" formata os dígitos calculados como string
    return cpf[-2:] == f"{dig1}{dig2}"


# Classe que herda de BaseHTTPRequestHandler para processar requisições HTTP
class CPFService(BaseHTTPRequestHandler):

    # ------------------------------
    # GET /cpf?cpf=XXXXXXXXXXX
    # ------------------------------
    # Método chamado automaticamente quando uma requisição GET é recebida
    def do_GET(self):
        # Importa funções para fazer parse da URL e query string
        from urllib.parse import urlparse, parse_qs
        # Faz parse da URL completa da requisição
        parsed = urlparse(self.path)

        # Verifica se o caminho da requisição é /cpf
        # parsed.path contém apenas o caminho da URL, sem query string
        if parsed.path == "/cpf":
            # Faz parse dos parâmetros da query string (ex: ?cpf=11144477735)
            # parse_qs() retorna um dicionário onde cada valor é uma lista (pode haver múltiplos valores)
            params = parse_qs(parsed.query)
            # Extrai o valor do parâmetro "cpf" (retorna lista, pega o primeiro elemento [0])
            # Se "cpf" não existir, usa lista vazia [""] como padrão
            cpf = params.get("cpf", [""])[0]

            # Valida o CPF usando a função validar_cpf
            # A função retorna True se o CPF for válido, False caso contrário
            valido = validar_cpf(cpf)
            # Envia resposta JSON com status 200 (OK) contendo o CPF e se é válido
            # _send_json é um método auxiliar que formata e envia a resposta JSON
            self._send_json(200, {"cpf": cpf, "valid": valido})
            # Retorna para evitar processar mais código
            return

        # Se a rota não for /cpf, retorna erro 404 (não encontrado)
        self._send_json(404, {"error": "rota não encontrada"})

    # ------------------------------
    # POST /cpf
    # Body: { "cpf": "11144477735" }
    # ------------------------------
    # Método chamado automaticamente quando uma requisição POST é recebida
    def do_POST(self):
        # Verifica se o caminho da requisição é /cpf
        if self.path == "/cpf":
            # Obtém o tamanho do corpo da requisição do header Content-Length (ou 0 se não existir)
            tamanho = int(self.headers.get('Content-Length', 0))
            # Lê o corpo da requisição (bytes) e decodifica para string UTF-8
            corpo = self.rfile.read(tamanho).decode("utf-8")

            # Tenta fazer parse do JSON do corpo da requisição
            try:
                # Converte a string JSON em dicionário Python
                # json.loads() faz o parse da string JSON
                dados = json.loads(corpo)
                # Extrai o valor da chave "cpf" do dicionário (ou string vazia se não existir)
                # get() retorna o valor da chave ou o valor padrão (string vazia) se não existir
                cpf = dados.get("cpf", "")
            # Se houver erro ao fazer parse do JSON (except sem especificar exceção captura qualquer erro)
            except:
                # Retorna erro 400 (Bad Request) com mensagem de JSON inválido
                # 400 indica que a requisição está malformada
                self._send_json(400, {"error": "JSON inválido"})
                # Retorna para evitar processar mais código
                return

            # Valida o CPF usando a função validar_cpf
            # A função retorna True se o CPF for válido, False caso contrário
            valido = validar_cpf(cpf)
            # Envia resposta JSON com status 200 (OK) contendo o CPF e se é válido
            # _send_json é um método auxiliar que formata e envia a resposta JSON
            self._send_json(200, {"cpf": cpf, "valid": valido})
            # Retorna para evitar processar mais código
            return

        # Se a rota não for /cpf, retorna erro 404 (não encontrado)
        # 404 indica que o recurso solicitado não foi encontrado no servidor
        self._send_json(404, {"error": "rota não encontrada"})

    # ------------------------------
    # Helper para JSON
    # ------------------------------
    # Método auxiliar para enviar respostas JSON de forma padronizada
    # status: código de status HTTP (200, 404, 400, etc.)
    # data: dicionário Python que será convertido para JSON
    def _send_json(self, status, data):
        # Converte o dicionário Python em string JSON e depois em bytes
        resposta = json.dumps(data).encode()

        # Define o código de status HTTP da resposta (200, 404, 400, etc.)
        self.send_response(status)
        # Define o header Content-Type como application/json
        # Indica ao cliente que a resposta está em formato JSON
        self.send_header("Content-Type", "application/json")
        # Define o header Content-Length com o tamanho da resposta em bytes
        # len(resposta) retorna o tamanho em bytes, str() converte para string
        self.send_header("Content-Length", str(len(resposta)))
        # Finaliza o envio dos headers (obrigatório antes de escrever o corpo)
        self.end_headers()
        # Escreve o corpo da resposta (os bytes do JSON)
        # wfile é um arquivo-like object para escrever a resposta HTTP
        self.wfile.write(resposta)


# Função para iniciar o servidor HTTP
def run():
    # Cria uma instância de HTTPServer escutando em localhost na porta 8000
    # Tupla ("localhost", 8000) define o endereço e porta
    # CPFService é a classe que vai processar as requisições
    servidor = HTTPServer(("localhost", 8000), CPFService)
    # Imprime mensagem informando que o servidor está rodando
    print("Servidor rodando em http://localhost:8000 ...")
    # Inicia o servidor e fica escutando requisições indefinidamente
    servidor.serve_forever()


# Verifica se o script está sendo executado diretamente (não importado como módulo)
if __name__ == "__main__":
    # Chama a função run() para iniciar o servidor
    run()
