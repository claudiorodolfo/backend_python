import json
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('server.log'),  # Log em arquivo
        logging.StreamHandler()  # Log no console
    ]
)

# Criar logger específico para o servidor
logger = logging.getLogger('WSProvider')

# Dados em memória (simulando um banco de dados simples)
tarefas = [
    {"id": 1, "titulo": "Aprender REST", "concluida": False},
    {"id": 2, "titulo": "Implementar logging", "concluida": True}
]
contador_id = 3

# Classe Provider para lidar com as requisições HTTP
class WSProvider(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        """Sobrescreve o método padrão de log para usar nosso logger"""
        logger.info(f"{self.address_string()} - {format % args}")

    def do_GET(self):
        """Processa requisições GET"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)

        # Log da requisição recebida
        logger.info(f"Requisição GET recebida: {path} - IP: {self.client_address[0]}")
        logger.debug(f"Query params: {query_params}")

        try:
            if path == "/tarefas":
                # Lista todas as tarefas
                logger.info("Listando todas as tarefas")
                self._enviar_resposta(200, {"tarefas": tarefas, "total": len(tarefas)})
                
            elif path.startswith("/tarefa/"):
                # Busca uma tarefa específica
                tarefa_id = int(path.split("/")[-1])
                logger.info(f"Buscando tarefa ID: {tarefa_id}")
                tarefa = self._buscar_tarefa(tarefa_id)
                
                if tarefa:
                    logger.info(f"Tarefa {tarefa_id} encontrada")
                    self._enviar_resposta(200, tarefa)
                else:
                    logger.warning(f"Tarefa {tarefa_id} não encontrada")
                    self._enviar_resposta(404, {"erro": "Tarefa não encontrada"})
                    
            elif path == "/status":
                # Endpoint de status do servidor
                logger.info("Verificando status do servidor")
                self._enviar_resposta(200, {
                    "status": "online",
                    "timestamp": datetime.now().isoformat(),
                    "total_tarefas": len(tarefas)
                })
            else:
                logger.warning(f"Rota não encontrada: {path}")
                self._enviar_resposta(404, {"erro": "Rota não encontrada"})
                
        except Exception as e:
            logger.error(f"Erro ao processar requisição GET: {str(e)}", exc_info=True)
            self._enviar_resposta(500, {"erro": "Erro interno do servidor"})

    def do_POST(self):
        """Processa requisições POST"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        # Log da requisição recebida
        logger.info(f"Requisição POST recebida: {path} - IP: {self.client_address[0]}")

        try:
            if path == "/tarefa":
                # Cria uma nova tarefa
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                
                logger.debug(f"Body recebido: {body}")
                
                dados = json.loads(body)
                titulo = dados.get('titulo')
                
                if not titulo:
                    logger.warning("Tentativa de criar tarefa sem título")
                    self._enviar_resposta(400, {"erro": "Campo 'titulo' é obrigatório"})
                    return
                
                global contador_id
                nova_tarefa = {
                    "id": contador_id,
                    "titulo": titulo,
                    "concluida": False
                }
                tarefas.append(nova_tarefa)
                contador_id += 1
                
                logger.info(f"Tarefa criada com sucesso: ID {nova_tarefa['id']} - {titulo}")
                self._enviar_resposta(201, nova_tarefa)
                
            else:
                logger.warning(f"Rota POST não encontrada: {path}")
                self._enviar_resposta(404, {"erro": "Rota não encontrada"})
                
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar JSON: {str(e)}")
            self._enviar_resposta(400, {"erro": "JSON inválido"})
        except Exception as e:
            logger.error(f"Erro ao processar requisição POST: {str(e)}", exc_info=True)
            self._enviar_resposta(500, {"erro": "Erro interno do servidor"})

    def do_PUT(self):
        """Processa requisições PUT"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        logger.info(f"Requisição PUT recebida: {path} - IP: {self.client_address[0]}")

        try:
            if path.startswith("/tarefa/"):
                tarefa_id = int(path.split("/")[-1])
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                
                logger.debug(f"Body recebido: {body}")
                
                dados = json.loads(body)
                tarefa = self._buscar_tarefa(tarefa_id)
                
                if not tarefa:
                    logger.warning(f"Tentativa de atualizar tarefa inexistente: {tarefa_id}")
                    self._enviar_resposta(404, {"erro": "Tarefa não encontrada"})
                    return
                
                # Atualiza os campos fornecidos
                if 'titulo' in dados:
                    tarefa['titulo'] = dados['titulo']
                if 'concluida' in dados:
                    tarefa['concluida'] = dados['concluida']
                
                logger.info(f"Tarefa {tarefa_id} atualizada com sucesso")
                self._enviar_resposta(200, tarefa)
            else:
                logger.warning(f"Rota PUT não encontrada: {path}")
                self._enviar_resposta(404, {"erro": "Rota não encontrada"})
                
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar JSON: {str(e)}")
            self._enviar_resposta(400, {"erro": "JSON inválido"})
        except Exception as e:
            logger.error(f"Erro ao processar requisição PUT: {str(e)}", exc_info=True)
            self._enviar_resposta(500, {"erro": "Erro interno do servidor"})

    def do_DELETE(self):
        """Processa requisições DELETE"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        logger.info(f"Requisição DELETE recebida: {path} - IP: {self.client_address[0]}")

        try:
            if path.startswith("/tarefa/"):
                tarefa_id = int(path.split("/")[-1])
                tarefa = self._buscar_tarefa(tarefa_id)
                
                if not tarefa:
                    logger.warning(f"Tentativa de deletar tarefa inexistente: {tarefa_id}")
                    self._enviar_resposta(404, {"erro": "Tarefa não encontrada"})
                    return
                
                tarefas.remove(tarefa)
                logger.info(f"Tarefa {tarefa_id} deletada com sucesso")
                self._enviar_resposta(200, {"mensagem": "Tarefa deletada com sucesso"})
            else:
                logger.warning(f"Rota DELETE não encontrada: {path}")
                self._enviar_resposta(404, {"erro": "Rota não encontrada"})
                
        except Exception as e:
            logger.error(f"Erro ao processar requisição DELETE: {str(e)}", exc_info=True)
            self._enviar_resposta(500, {"erro": "Erro interno do servidor"})

    def _buscar_tarefa(self, tarefa_id):
        """Busca uma tarefa pelo ID"""
        for tarefa in tarefas:
            if tarefa['id'] == tarefa_id:
                return tarefa
        return None

    def _enviar_resposta(self, status_code, dados):
        """Envia resposta JSON para o cliente"""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        resposta = json.dumps(dados, ensure_ascii=False).encode('utf-8')
        self.wfile.write(resposta)
        
        # Log da resposta enviada
        logger.debug(f"Resposta enviada: Status {status_code} - {dados}")

def main():
    """Inicia o servidor HTTP"""
    servidor = HTTPServer(('127.0.0.1', 8082), WSProvider)
    
    logger.info("=" * 60)
    logger.info("Servidor REST com Logging iniciado")
    logger.info("URL: http://127.0.0.1:8082")
    logger.info("Endpoints disponíveis:")
    logger.info("  GET    /tarefas          - Lista todas as tarefas")
    logger.info("  GET    /tarefa/{id}      - Busca uma tarefa")
    logger.info("  GET    /status           - Status do servidor")
    logger.info("  POST   /tarefa           - Cria uma nova tarefa")
    logger.info("  PUT    /tarefa/{id}      - Atualiza uma tarefa")
    logger.info("  DELETE /tarefa/{id}      - Deleta uma tarefa")
    logger.info("=" * 60)
    logger.info("Logs sendo salvos em: server.log")
    logger.info("=" * 60)
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        logger.info("Servidor encerrado pelo usuário")
        servidor.shutdown()

if __name__ == "__main__":
    main()

