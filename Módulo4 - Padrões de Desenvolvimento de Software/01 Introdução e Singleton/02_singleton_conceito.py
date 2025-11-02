"""
02 - PADRÃO SINGLETON
=====================

Conceito e Finalidade
---------------------
O Singleton garante que uma classe tenha apenas UMA instância durante todo 
o ciclo de vida da aplicação e fornece um ponto global de acesso a essa instância.

Por que usar Singleton?
- Recursos compartilhados (conexão de banco, logger)
- Configurações globais
- Cache único
- Pools de objetos

Vantagens
---------
✓ Garante uma única instância
✓ Acesso global controlado
✓ Inicialização preguiçosa (lazy initialization)
✓ Controle sobre recursos compartilhados

Armadilhas e Desvantagens
--------------------------
✗ Pode esconder dependências
✗ Dificulta testes (hard to mock)
✗ Pode violar princípio de responsabilidade única
✗ Problemas em ambientes multi-thread
✗ Pode se tornar um "God Object"
✗ Viola princípio de inversão de dependência

Quando NÃO usar Singleton
--------------------------
- Quando não precisa garantir única instância
- Quando precisa de múltiplas instâncias configuradas diferentemente
- Quando testabilidade é crucial
- Quando trabalha com threads (precisa thread-safety)
"""

# IMPLEMENTAÇÃO 1: Singleton Básico (Pythonic Way)
# ==================================================

class SingletonBasico:
    """
    Singleton usando atributo de classe.
    Esta é a forma mais simples em Python.
    """
    _instance = None
    
    def __new__(cls):
        """Construtor que garante única instância"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inicializado = False
        return cls._instance
    
    def __init__(self):
        """Inicialização (executado apenas na primeira vez)"""
        if not self._inicializado:
            self.valor = 0
            self._inicializado = True
    
    def incrementar(self):
        self.valor += 1
        return self.valor


# IMPLEMENTAÇÃO 2: Singleton com Decorator
# =========================================

def singleton(classe):
    """
    Decorator que transforma qualquer classe em Singleton.
    Vantagem: reutilizável e não modifica a classe original.
    """
    instances = {}
    
    def get_instance(*args, **kwargs):
        if classe not in instances:
            instances[classe] = classe(*args, **kwargs)
        return instances[classe]
    
    return get_instance


@singleton
class Configuracao:
    """Classe transformada em Singleton via decorator"""
    
    def __init__(self):
        self.settings = {}
    
    def set_config(self, chave, valor):
        self.settings[chave] = valor
    
    def get_config(self, chave):
        return self.settings.get(chave)


# IMPLEMENTAÇÃO 3: Singleton com Metaclass
# =========================================

class SingletonMeta(type):
    """
    Metaclass que garante comportamento Singleton.
    Mais Pythonic e permite herança controlada.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    """
    Logger como Singleton - garante que toda aplicação usa o mesmo logger.
    """
    
    def __init__(self):
        self.logs = []
        self.nivel = "INFO"
    
    def log(self, mensagem, nivel="INFO"):
        log_entry = f"[{nivel}] {mensagem}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        return self.logs


# IMPLEMENTAÇÃO 4: Singleton Thread-Safe
# =======================================

import threading

class ThreadSafeSingleton:
    """
    Singleton thread-safe usando lock.
    Necessário quando múltiplas threads podem criar instâncias.
    """
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-check locking pattern
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializado = False
        return cls._instance
    
    def __init__(self):
        if not self._inicializado:
            self.dados = {}
            self._inicializado = True
    
    def set_dado(self, chave, valor):
        with self._lock:
            self.dados[chave] = valor
    
    def get_dado(self, chave):
        return self.dados.get(chave)


if __name__ == "__main__":
    print("=" * 60)
    print("PADRÃO SINGLETON - EXEMPLOS PRÁTICOS")
    print("=" * 60)
    
    # TESTE 1: Singleton Básico
    print("\n1. Singleton Básico:")
    s1 = SingletonBasico()
    s2 = SingletonBasico()
    print(f"   s1 == s2: {s1 is s2}")  # True - mesma instância
    s1.incrementar()
    s2.incrementar()
    print(f"   Valor após incrementos: {s1.valor}")  # 2
    
    # TESTE 2: Singleton com Decorator
    print("\n2. Singleton com Decorator:")
    config1 = Configuracao()
    config2 = Configuracao()
    print(f"   config1 == config2: {config1 is config2}")  # True
    config1.set_config("database", "postgresql")
    print(f"   Config via config2: {config2.get_config('database')}")
    
    # TESTE 3: Singleton com Metaclass (Logger)
    print("\n3. Singleton Logger (Metaclass):")
    logger1 = Logger()
    logger2 = Logger()
    print(f"   logger1 == logger2: {logger1 is logger2}")  # True
    logger1.log("Primeira mensagem")
    logger2.log("Segunda mensagem")
    print(f"   Total de logs: {len(logger1.get_logs())}")
    
    # TESTE 4: Thread-Safe Singleton
    print("\n4. Thread-Safe Singleton:")
    ts1 = ThreadSafeSingleton()
    ts2 = ThreadSafeSingleton()
    print(f"   ts1 == ts2: {ts1 is ts2}")  # True
    ts1.set_dado("usuario", "admin")
    print(f"   Dado via ts2: {ts2.get_dado('usuario')}")

