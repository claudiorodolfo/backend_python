"""
02 - EXEMPLOS PRÁTICOS DO DECORATOR
=====================================

Casos de uso reais:
1. Sistema de permissões e autenticação
2. Pipeline de processamento de dados
3. Sistema de notificações com diferentes canais
4. Wrapper para APIs externas
5. Sistema de cache e otimização
"""

from abc import ABC, abstractmethod
from functools import wraps
import time

# EXEMPLO 1: Sistema de Permissões
# ==================================

class Operacao(ABC):
    """Interface para operações que podem ter permissões"""
    
    @abstractmethod
    def executar(self):
        pass


class OperacaoBasica(Operacao):
    """Operação básica sem proteção"""
    
    def __init__(self, nome):
        self.nome = nome
    
    def executar(self):
        return f"Executando operação: {self.nome}"


class OperacaoDecorator(Operacao):
    """Base para decoradores de operação"""
    
    def __init__(self, operacao: Operacao):
        self._operacao = operacao
    
    def executar(self):
        return self._operacao.executar()


class RequerAutenticacao(OperacaoDecorator):
    """Decorator que requer autenticação"""
    
    def __init__(self, operacao: Operacao, usuario_autenticado=False):
        super().__init__(operacao)
        self.usuario_autenticado = usuario_autenticado
    
    def executar(self):
        if not self.usuario_autenticado:
            raise PermissionError("Usuário não autenticado")
        return self._operacao.executar()


class RequerPermissao(OperacaoDecorator):
    """Decorator que requer permissão específica"""
    
    def __init__(self, operacao: Operacao, permissao_requerida, permissoes_usuario=None):
        super().__init__(operacao)
        self.permissao_requerida = permissao_requerida
        self.permissoes_usuario = permissoes_usuario or []
    
    def executar(self):
        if self.permissao_requerida not in self.permissoes_usuario:
            raise PermissionError(f"Permissão '{self.permissao_requerida}' necessária")
        return self._operacao.executar()


class RequerLog(OperacaoDecorator):
    """Decorator que registra operação em log"""
    
    def executar(self):
        resultado = self._operacao.executar()
        print(f"[LOG] Operação executada: {resultado}")
        return resultado


# EXEMPLO 2: Pipeline de Processamento de Dados
# ===============================================

class Processador(ABC):
    """Interface para processadores de dados"""
    
    @abstractmethod
    def processar(self, dados):
        pass


class ProcessadorBasico(Processador):
    """Processador básico"""
    
    def processar(self, dados):
        return dados


class ProcessadorDecorator(Processador):
    """Base para decoradores de processamento"""
    
    def __init__(self, processador: Processador):
        self._processador = processador
    
    def processar(self, dados):
        return self._processador.processar(dados)


class ValidacaoDados(ProcessadorDecorator):
    """Adiciona validação de dados"""
    
    def processar(self, dados):
        if not dados:
            raise ValueError("Dados não podem ser vazios")
        if not isinstance(dados, (list, dict, str)):
            raise TypeError("Dados devem ser lista, dict ou string")
        return self._processador.processar(dados)


class LimpezaDados(ProcessadorDecorator):
    """Adiciona limpeza de dados"""
    
    def processar(self, dados):
        if isinstance(dados, str):
            dados = dados.strip().lower()
        elif isinstance(dados, list):
            dados = [item for item in dados if item]
        return self._processador.processar(dados)


class TransformacaoDados(ProcessadorDecorator):
    """Adiciona transformação"""
    
    def processar(self, dados):
        dados_processados = self._processador.processar(dados)
        if isinstance(dados_processados, list):
            return [str(item).upper() for item in dados_processados]
        return str(dados_processados).upper()


class CacheDados(ProcessadorDecorator):
    """Adiciona cache"""
    
    def __init__(self, processador: Processador):
        super().__init__(processador)
        self.cache = {}
    
    def processar(self, dados):
        chave = str(dados)
        if chave in self.cache:
            print("[CACHE] Retornando dados do cache")
            return self.cache[chave]
        
        resultado = self._processador.processar(dados)
        self.cache[chave] = resultado
        return resultado


# EXEMPLO 3: Decorators Funcionais - Performance e Monitoramento
# ===============================================================

def medir_tempo(func):
    """Decorator que mede tempo de execução"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"[PERFORMANCE] {func.__name__} executou em {fim - inicio:.4f}s")
        return resultado
    return wrapper


def retry(max_tentativas=3, delay=1):
    """Decorator que tenta novamente em caso de falha"""
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for tentativa in range(max_tentativas):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if tentativa == max_tentativas - 1:
                        raise
                    print(f"[RETRY] Tentativa {tentativa + 1} falhou: {e}. Tentando novamente...")
                    time.sleep(delay)
        return wrapper
    return decorador


def rate_limit(max_chamadas=5, periodo=60):
    """Decorator que limita taxa de chamadas"""
    chamadas = []
    
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            agora = time.time()
            chamadas[:] = [c for c in chamadas if c > agora - periodo]
            
            if len(chamadas) >= max_chamadas:
                raise Exception(f"Rate limit excedido: {max_chamadas} chamadas por {periodo}s")
            
            chamadas.append(agora)
            return func(*args, **kwargs)
        return wrapper
    return decorador


# Exemplos de funções decoradas
@medir_tempo
def operacao_lenta():
    """Função que demora para executar"""
    time.sleep(0.1)
    return "Operação concluída"


@retry(max_tentativas=3, delay=0.1)
def operacao_instavel(tentativa_atual=0):
    """Função que pode falhar"""
    if tentativa_atual < 2:
        raise Exception("Falha temporária")
    return "Sucesso"


@rate_limit(max_chamadas=3, periodo=10)
def api_restrita():
    """API com limite de chamadas"""
    return "Dados da API"


# EXEMPLO 4: Decorator para Sistema de Notificações
# ===================================================

class Notificacao(ABC):
    """Interface para notificações"""
    
    @abstractmethod
    def enviar(self, mensagem):
        pass


class NotificacaoBasica(Notificacao):
    """Notificação básica"""
    
    def enviar(self, mensagem):
        return f"Notificação: {mensagem}"


class NotificacaoDecorator(Notificacao):
    """Base para decoradores de notificação"""
    
    def __init__(self, notificacao: Notificacao):
        self._notificacao = notificacao
    
    def enviar(self, mensagem):
        return self._notificacao.enviar(mensagem)


class PrioridadeAlta(NotificacaoDecorator):
    """Marca notificação como alta prioridade"""
    
    def enviar(self, mensagem):
        mensagem_prioritaria = f"🔴 URGENTE: {mensagem}"
        return self._notificacao.enviar(mensagem_prioritaria)


class FormatarHTML(NotificacaoDecorator):
    """Formata notificação em HTML"""
    
    def enviar(self, mensagem):
        mensagem_formatada = self._notificacao.enviar(mensagem)
        return f"<html><body>{mensagem_formatada}</body></html>"


class AdicionarTimestamp(NotificacaoDecorator):
    """Adiciona timestamp à notificação"""
    
    def enviar(self, mensagem):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensagem_com_timestamp = f"[{timestamp}] {mensagem}"
        return self._notificacao.enviar(mensagem_com_timestamp)


# EXEMPLO 5: Decorator para Wrapper de API
# ==========================================

class APIClient:
    """Cliente básico de API"""
    
    def fazer_request(self, endpoint, dados=None):
        return f"Request para {endpoint}: {dados}"


class APIClientDecorator:
    """Base para decoradores de API"""
    
    def __init__(self, client: APIClient):
        self._client = client
    
    def fazer_request(self, endpoint, dados=None):
        return self._client.fazer_request(endpoint, dados)


class APIAutenticacao(APIClientDecorator):
    """Adiciona autenticação"""
    
    def __init__(self, client: APIClient, api_key):
        super().__init__(client)
        self.api_key = api_key
    
    def fazer_request(self, endpoint, dados=None):
        dados_com_auth = dados or {}
        dados_com_auth["api_key"] = self.api_key
        return self._client.fazer_request(endpoint, dados_com_auth)


class APICache(APIClientDecorator):
    """Adiciona cache"""
    
    def __init__(self, client: APIClient):
        super().__init__(client)
        self.cache = {}
    
    def fazer_request(self, endpoint, dados=None):
        chave = f"{endpoint}:{dados}"
        if chave in self.cache:
            print("[API CACHE] Retornando do cache")
            return self.cache[chave]
        
        resultado = self._client.fazer_request(endpoint, dados)
        self.cache[chave] = resultado
        return resultado


class APILogging(APIClientDecorator):
    """Adiciona logging"""
    
    def fazer_request(self, endpoint, dados=None):
        print(f"[API LOG] Chamando {endpoint} com dados: {dados}")
        resultado = self._client.fazer_request(endpoint, dados)
        print(f"[API LOG] Resposta: {resultado}")
        return resultado


if __name__ == "__main__":
    print("=" * 60)
    print("EXEMPLOS PRÁTICOS - DECORATOR")
    print("=" * 60)
    
    # TESTE 1: Sistema de Permissões
    print("\n1. Sistema de Permissões:")
    op_basica = OperacaoBasica("Criar usuário")
    
    # Sem autenticação - deve falhar
    try:
        op_protegida = RequerAutenticacao(op_basica, usuario_autenticado=False)
        op_protegida.executar()
    except PermissionError as e:
        print(f"   {e}")
    
    # Com autenticação
    op_autenticada = RequerAutenticacao(op_basica, usuario_autenticado=True)
    op_completa = RequerPermissao(op_autenticada, "criar_usuario", ["criar_usuario", "editar_usuario"])
    op_final = RequerLog(op_completa)
    print(f"   {op_final.executar()}")
    
    # TESTE 2: Pipeline de Processamento
    print("\n2. Pipeline de Processamento:")
    processador_base = ProcessadorBasico()
    
    # Construindo pipeline
    processador = CacheDados(
        TransformacaoDados(
            LimpezaDados(
                ValidacaoDados(processador_base)
            )
        )
    )
    
    dados = ["  item1  ", "ITEM2", "", "item3"]
    resultado = processador.processar(dados)
    print(f"   Entrada: {dados}")
    print(f"   Saída: {resultado}")
    
    # Segunda chamada (usa cache)
    processador.processar(dados)
    
    # TESTE 3: Decorators Funcionais
    print("\n3. Decorators Funcionais:")
    operacao_lenta()
    
    resultado_retry = operacao_instavel(tentativa_atual=0)
    print(f"   Resultado após retry: {resultado_retry}")
    
    # TESTE 4: Sistema de Notificações
    print("\n4. Sistema de Notificações:")
    notif_base = NotificacaoBasica()
    notif_decorada = AdicionarTimestamp(
        PrioridadeAlta(
            FormatarHTML(notif_base)
        )
    )
    resultado = notif_decorada.enviar("Nova mensagem importante")
    print(f"   {resultado}")
    
    # TESTE 5: Wrapper de API
    print("\n5. Wrapper de API:")
    api_base = APIClient()
    api_decorada = APILogging(
        APICache(
            APIAutenticacao(api_base, "key123")
        )
    )
    
    resultado1 = api_decorada.fazer_request("/users", {"nome": "João"})
    print(f"   {resultado1}")
    
    # Segunda chamada (usa cache)
    resultado2 = api_decorada.fazer_request("/users", {"nome": "João"})
    print(f"   {resultado2}")

