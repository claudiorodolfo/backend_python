"""
04 - EXERCÍCIOS: CRIANDO CLASSES SINGLETON
===========================================

Exercícios práticos para implementar o padrão Singleton.
"""

# EXERCÍCIO 1: Singleton Simples
# ===============================
"""
Crie uma classe Singleton chamada ContadorGlobal que:
- Mantém um contador que pode ser incrementado e decrementado
- Garante que apenas uma instância existe
- Permite obter o valor atual do contador

Teste criando múltiplas "instâncias" e verificando que compartilham o mesmo estado.
"""

# TODO: Implemente aqui
class ContadorGlobal:
    """Implemente o Singleton aqui"""
    pass


# EXERCÍCIO 2: Singleton com Decorator
# =====================================
"""
Crie um decorator @singleton que transforma qualquer classe em Singleton.
Depois, use esse decorator para criar uma classe ConfiguracoesSingleton.

A classe ConfiguracoesSingleton deve:
- Armazenar configurações em um dicionário
- Ter métodos set_config(chave, valor) e get_config(chave)
- Ser um Singleton através do decorator
"""

# TODO: Implemente o decorator aqui
def singleton_decorator(classe):
    """Implemente o decorator Singleton aqui"""
    pass


# TODO: Use o decorator aqui
@singleton_decorator
class ConfiguracoesSingleton:
    """Implemente a classe aqui"""
    pass


# EXERCÍCIO 3: Singleton Thread-Safe
# ===================================
"""
Crie uma classe FileManager Singleton que:
- Gerencia operações de arquivo de forma thread-safe
- Mantém um log de todas as operações realizadas
- Permite ler, escrever e listar arquivos (simulado)

Use locks para garantir thread-safety.
"""

import threading

# TODO: Implemente aqui
class FileManager:
    """Implemente Singleton thread-safe aqui"""
    pass


# EXERCÍCIO 4: Singleton para Gerenciamento de Sessões
# =====================================================
"""
Crie uma classe SessionManager Singleton que:
- Armazena sessões de usuários (simulado com dicionário)
- Permite criar, obter e destruir sessões
- Mantém um registro de todas as sessões ativas
- Tem um método para limpar sessões expiradas (simulado)
"""

# TODO: Implemente aqui
class SessionManager:
    """Implemente Singleton para gerenciamento de sessões"""
    pass


# EXERCÍCIO 5: Análise Crítica
# =============================
"""
Analise os seguintes cenários e determine se Singleton é apropriado:

a) Uma classe que representa um carrinho de compras de um usuário
b) Uma classe que gerencia conexões com múltiplos bancos de dados
c) Uma classe que armazena configurações da aplicação
d) Uma classe que representa um usuário logado
e) Uma classe que faz cache de resultados de queries caras

Para cada caso, explique:
- Singleton é apropriado? Por quê?
- Quais seriam alternativas ao Singleton?
"""

def analisar_casos():
    """
    Complete as respostas abaixo:
    """
    casos = {
        "a) Carrinho de compras": {
            "singleton_apropriado": None,  # True ou False
            "explicacao": "",  # Sua explicação
            "alternativas": []  # Lista de alternativas
        },
        "b) Conexões múltiplas BD": {
            "singleton_apropriado": None,
            "explicacao": "",
            "alternativas": []
        },
        "c) Configurações aplicação": {
            "singleton_apropriado": None,
            "explicacao": "",
            "alternativas": []
        },
        "d) Usuário logado": {
            "singleton_apropriado": None,
            "explicacao": "",
            "alternativas": []
        },
        "e) Cache de queries": {
            "singleton_apropriado": None,
            "explicacao": "",
            "alternativas": []
        }
    }
    return casos


# SOLUÇÕES DOS EXERCÍCIOS
# ========================

class SolucaoExercicio1:
    """Solução do Exercício 1"""
    
    class ContadorGlobal:
        _instance = None
        
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.valor = 0
            return cls._instance
        
        def incrementar(self):
            self.valor += 1
        
        def decrementar(self):
            self.valor -= 1
        
        def obter_valor(self):
            return self.valor


class SolucaoExercicio2:
    """Solução do Exercício 2"""
    
    def singleton_decorator(classe):
        instances = {}
        
        def get_instance(*args, **kwargs):
            if classe not in instances:
                instances[classe] = classe(*args, **kwargs)
            return instances[classe]
        
        return get_instance
    
    @singleton_decorator
    class ConfiguracoesSingleton:
        def __init__(self):
            if not hasattr(self, 'config'):
                self.config = {}
        
        def set_config(self, chave, valor):
            self.config[chave] = valor
        
        def get_config(self, chave):
            return self.config.get(chave)


class SolucaoExercicio3:
    """Solução do Exercício 3"""
    
    class FileManager:
        _instance = None
        _lock = threading.Lock()
        
        def __new__(cls):
            if cls._instance is None:
                with cls._lock:
                    if cls._instance is None:
                        cls._instance = super().__new__(cls)
                        cls._instance.arquivos = {}
                        cls._instance.log = []
            return cls._instance
        
        def escrever(self, nome_arquivo, conteudo):
            with self._lock:
                self.arquivos[nome_arquivo] = conteudo
                self.log.append(f"ESCRITA: {nome_arquivo}")
        
        def ler(self, nome_arquivo):
            with self._lock:
                self.log.append(f"LEITURA: {nome_arquivo}")
                return self.arquivos.get(nome_arquivo)
        
        def listar(self):
            with self._lock:
                self.log.append("LISTAGEM")
                return list(self.arquivos.keys())
        
        def get_log(self):
            return self.log.copy()


class SolucaoExercicio4:
    """Solução do Exercício 4"""
    
    class SessionManager:
        _instance = None
        
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.sessoes = {}
                cls._instance.contador_id = 0
            return cls._instance
        
        def criar_sessao(self, usuario_id):
            self.contador_id += 1
            session_id = f"session_{self.contador_id}"
            self.sessoes[session_id] = {
                "usuario_id": usuario_id,
                "criada_em": "2024-01-01 10:00:00",  # Simplificado
                "ativa": True
            }
            return session_id
        
        def obter_sessao(self, session_id):
            return self.sessoes.get(session_id)
        
        def destruir_sessao(self, session_id):
            if session_id in self.sessoes:
                del self.sessoes[session_id]
        
        def listar_sessoes_ativas(self):
            return {sid: sess for sid, sess in self.sessoes.items() if sess["ativa"]}
        
        def limpar_expiradas(self):
            # Simulação: remove sessões inativas
            self.sessoes = {sid: sess for sid, sess in self.sessoes.items() if sess["ativa"]}


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCÍCIOS - PADRÃO SINGLETON")
    print("=" * 60)
    print("\nComplete os exercícios acima e teste suas implementações!")
    print("\nPara ver as soluções, consulte as classes SolucaoExercicio*")

