"""
03 - CASOS PRÁTICOS DE USO DO SINGLETON
========================================

Exemplos reais onde Singleton é útil:
1. Gerenciador de Conexão de Banco de Dados
2. Sistema de Logging Global
3. Cache de Aplicação
4. Gerenciador de Configurações
5. Pool de Threads (com cuidado)
"""

# CASO DE USO 1: Gerenciador de Conexão de Banco
# ================================================

class DatabaseConnection:
    """Singleton para gerenciar conexão única com banco de dados"""
    
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'inicializado'):
            self.inicializado = True
    
    def connect(self, database_url):
        """Conecta ao banco de dados (simulado)"""
        if self._connection is None:
            self._connection = f"Conectado a: {database_url}"
            print(f"✓ {self._connection}")
        return self._connection
    
    def execute_query(self, query):
        """Executa query usando conexão única"""
        if self._connection is None:
            raise Exception("Banco não conectado!")
        print(f"Executando: {query}")
        return f"Resultado de: {query}"
    
    def disconnect(self):
        """Desconecta do banco"""
        self._connection = None
        print("Desconectado do banco")


# CASO DE USO 2: Sistema de Logging
# ==================================

class ApplicationLogger:
    """Singleton para logging global da aplicação"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance
    
    def info(self, mensagem):
        self._log("INFO", mensagem)
    
    def error(self, mensagem):
        self._log("ERROR", mensagem)
    
    def warning(self, mensagem):
        self._log("WARNING", mensagem)
    
    def _log(self, nivel, mensagem):
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{nivel}] {mensagem}"
        self.logs.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        return self.logs


# CASO DE USO 3: Cache de Aplicação
# ==================================

class AppCache:
    """Singleton para cache global da aplicação"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cache = {}
            cls._instance._max_size = 100
        return cls._instance
    
    def set(self, chave, valor):
        """Adiciona item ao cache"""
        if len(self.cache) >= self._max_size:
            # Remove item mais antigo (simplificado)
            primeiro_item = next(iter(self.cache))
            del self.cache[primeiro_item]
        
        self.cache[chave] = valor
        print(f"Cache atualizado: {chave}")
    
    def get(self, chave):
        """Recupera item do cache"""
        return self.cache.get(chave)
    
    def clear(self):
        """Limpa cache"""
        self.cache.clear()
        print("Cache limpo")
    
    def stats(self):
        """Retorna estatísticas do cache"""
        return {
            "tamanho": len(self.cache),
            "max_size": self._max_size,
            "chaves": list(self.cache.keys())
        }


# CASO DE USO 4: Gerenciador de Configurações
# =============================================

class ConfigManager:
    """Singleton para gerenciar configurações globais"""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config = {}
        return cls._instance
    
    def load_from_dict(self, config_dict):
        """Carrega configurações de um dicionário"""
        self.config.update(config_dict)
        print(f"Configurações carregadas: {len(config_dict)} itens")
    
    def set(self, chave, valor):
        """Define uma configuração"""
        self.config[chave] = valor
    
    def get(self, chave, default=None):
        """Obtém uma configuração"""
        return self.config.get(chave, default)
    
    def get_all(self):
        """Retorna todas as configurações"""
        return self.config.copy()


# EXEMPLO DE USO COMBINADO
# =========================

def exemplo_aplicacao_completa():
    """
    Demonstra como vários Singletons trabalham juntos em uma aplicação
    """
    print("\n" + "=" * 60)
    print("EXEMPLO: APLICAÇÃO USANDO MÚLTIPLOS SINGLETONS")
    print("=" * 60)
    
    # 1. Configurar aplicação
    config = ConfigManager()
    config.load_from_dict({
        "database_url": "postgresql://localhost:5432/mydb",
        "debug": True,
        "max_connections": 10
    })
    
    # 2. Inicializar logger
    logger = ApplicationLogger()
    logger.info("Aplicação iniciada")
    
    # 3. Conectar ao banco
    db = DatabaseConnection()
    db.connect(config.get("database_url"))
    logger.info("Conexão com banco estabelecida")
    
    # 4. Usar cache
    cache = AppCache()
    cache.set("usuario_atual", {"id": 1, "nome": "João"})
    logger.info("Cache inicializado")
    
    # 5. Executar operação
    resultado = db.execute_query("SELECT * FROM usuarios")
    logger.info("Query executada com sucesso")
    
    # 6. Verificar que são as mesmas instâncias
    logger2 = ApplicationLogger()
    db2 = DatabaseConnection()
    cache2 = AppCache()
    
    print(f"\nVerificando Singleton:")
    print(f"  logger == logger2: {logger is logger2}")
    print(f"  db == db2: {db is db2}")
    print(f"  cache == cache2: {cache is cache2}")
    
    # Logs compartilhados
    print(f"\nTotal de logs (via logger2): {len(logger2.get_logs())}")


if __name__ == "__main__":
    # Testes individuais
    print("=" * 60)
    print("CASOS DE USO PRÁTICOS - SINGLETON")
    print("=" * 60)
    
    print("\n1. Database Connection:")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    db1.connect("postgresql://localhost/db")
    db2.execute_query("SELECT * FROM users")
    
    print("\n2. Application Logger:")
    logger1 = ApplicationLogger()
    logger2 = ApplicationLogger()
    logger1.info("Mensagem 1")
    logger2.error("Mensagem 2")
    print(f"Logs compartilhados: {len(logger1.get_logs())}")
    
    print("\n3. App Cache:")
    cache1 = AppCache()
    cache2 = AppCache()
    cache1.set("item1", "valor1")
    print(f"Item via cache2: {cache2.get('item1')}")
    
    print("\n4. Config Manager:")
    config1 = ConfigManager()
    config2 = ConfigManager()
    config1.set("chave", "valor")
    print(f"Config via config2: {config2.get('chave')}")
    
    # Exemplo combinado
    exemplo_aplicacao_completa()

