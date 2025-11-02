"""
01 - PADRÃO FACTORY METHOD
==========================

Conceito do Factory Method
---------------------------
O Factory Method é um padrão criacional que fornece uma interface para criar 
objetos em uma superclasse, mas permite que subclasses alterem o tipo de objetos 
que serão criados.

Problema que resolve:
- Como criar objetos sem especificar suas classes exatas?
- Como delegar a criação de objetos para subclasses?
- Como flexibilizar a criação de objetos?

Diferenças entre Factory Method e Simple Factory
-------------------------------------------------
SIMPLE FACTORY:
- Uma única classe/função cria todos os objetos
- Não usa herança ou polimorfismo
- Mais simples, mas menos flexível

FACTORY METHOD:
- Cada subclasse define seu próprio método de criação
- Usa herança e polimorfismo
- Mais flexível e extensível
- Segue o princípio aberto/fechado (OCP)

Vantagens
---------
✓ Baixo acoplamento entre criador e produto
✓ Princípio de responsabilidade única
✓ Princípio aberto/fechado: fácil adicionar novos tipos
✓ Código mais organizado e manutenível

Desvantagens
------------
✗ Pode complicar código se há poucos tipos de produtos
✗ Requer criar subclasses do criador
"""

# EXEMPLO 1: Simple Factory (para comparação)
# ============================================

class MySQLConnection:
    def connect(self):
        return "Conectado ao MySQL"

class PostgreSQLConnection:
    def connect(self):
        return "Conectado ao PostgreSQL"

class MongoDBConnection:
    def connect(self):
        return "Conectado ao MongoDB"

# Simple Factory - função que cria objetos
def criar_conexao(tipo_banco):
    """Simple Factory: uma função cria todos os tipos"""
    if tipo_banco == "mysql":
        return MySQLConnection()
    elif tipo_banco == "postgresql":
        return PostgreSQLConnection()
    elif tipo_banco == "mongodb":
        return MongoDBConnection()
    else:
        raise ValueError(f"Tipo de banco desconhecido: {tipo_banco}")


# EXEMPLO 2: Factory Method Pattern
# ===================================

from abc import ABC, abstractmethod

# Interface do produto
class Conexao(ABC):
    """Interface para conexões de banco de dados"""
    
    @abstractmethod
    def connect(self):
        """Conecta ao banco de dados"""
        pass
    
    @abstractmethod
    def execute_query(self, query):
        """Executa uma query"""
        pass


# Implementações concretas
class ConexaoMySQL(Conexao):
    def connect(self):
        return "Conectado ao MySQL"
    
    def execute_query(self, query):
        return f"MySQL executando: {query}"

class ConexaoPostgreSQL(Conexao):
    def connect(self):
        return "Conectado ao PostgreSQL"
    
    def execute_query(self, query):
        return f"PostgreSQL executando: {query}"

class ConexaoMongoDB(Conexao):
    def connect(self):
        return "Conectado ao MongoDB"
    
    def execute_query(self, query):
        return f"MongoDB executando: {query}"


# Criador abstrato (Factory Method)
class DatabaseFactory(ABC):
    """Factory abstrato - define método factory"""
    
    @abstractmethod
    def criar_conexao(self) -> Conexao:
        """Factory method - cada subclasse implementa"""
        pass
    
    def testar_conexao(self):
        """Método que usa o produto criado"""
        conexao = self.criar_conexao()
        print(f"Testando: {conexao.connect()}")
        return conexao


# Criadores concretos
class MySQLFactory(DatabaseFactory):
    def criar_conexao(self) -> Conexao:
        return ConexaoMySQL()

class PostgreSQLFactory(DatabaseFactory):
    def criar_conexao(self) -> Conexao:
        return ConexaoPostgreSQL()

class MongoDBFactory(DatabaseFactory):
    def criar_conexao(self) -> Conexao:
        return ConexaoMongoDB()


# EXEMPLO 3: Factory Method com parâmetros
# ==========================================

class Documento(ABC):
    """Interface para documentos"""
    
    @abstractmethod
    def criar(self, titulo, conteudo):
        pass
    
    @abstractmethod
    def salvar(self):
        pass

class PDFDocumento(Documento):
    def criar(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        return f"PDF criado: {titulo}"
    
    def salvar(self):
        return f"Salvando PDF: {self.titulo}"

class WordDocumento(Documento):
    def criar(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo
        return f"Word criado: {titulo}"
    
    def salvar(self):
        return f"Salvando Word: {self.titulo}"

class DocumentoFactory(ABC):
    """Factory para documentos"""
    
    @abstractmethod
    def criar_documento(self, tipo) -> Documento:
        """Factory method que pode receber parâmetros"""
        pass

class EditorFactory(DocumentoFactory):
    """Factory que cria diferentes tipos de documentos"""
    
    def criar_documento(self, tipo) -> Documento:
        if tipo == "pdf":
            return PDFDocumento()
        elif tipo == "word":
            return WordDocumento()
        else:
            raise ValueError(f"Tipo desconhecido: {tipo}")


# EXEMPLO 4: Uso Prático - Processamento de Dados
# ================================================

class ProcessadorDados(ABC):
    """Interface para processadores de dados"""
    
    @abstractmethod
    def processar(self, dados):
        pass

class ProcessadorCSV(ProcessadorDados):
    def processar(self, dados):
        return f"Processando CSV: {len(dados)} linhas"

class ProcessadorJSON(ProcessadorDados):
    def processar(self, dados):
        return f"Processando JSON: {len(dados)} objetos"

class ProcessadorXML(ProcessadorDados):
    def processar(self, dados):
        return f"Processando XML: {len(dados)} elementos"

class DataProcessorFactory(ABC):
    """Factory para processadores de dados"""
    
    @abstractmethod
    def criar_processador(self, formato) -> ProcessadorDados:
        pass
    
    def processar_arquivo(self, formato, dados):
        """Método que usa o factory method"""
        processador = self.criar_processador(formato)
        return processador.processar(dados)

class GenericDataProcessorFactory(DataProcessorFactory):
    """Factory genérico que cria qualquer processador"""
    
    def criar_processador(self, formato) -> ProcessadorDados:
        if formato == "csv":
            return ProcessadorCSV()
        elif formato == "json":
            return ProcessadorJSON()
        elif formato == "xml":
            return ProcessadorXML()
        else:
            raise ValueError(f"Formato não suportado: {formato}")


if __name__ == "__main__":
    print("=" * 60)
    print("PADRÃO FACTORY METHOD")
    print("=" * 60)
    
    # Comparação: Simple Factory vs Factory Method
    print("\n1. Simple Factory:")
    conexao1 = criar_conexao("mysql")
    print(f"   {conexao1.connect()}")
    
    print("\n2. Factory Method:")
    mysql_factory = MySQLFactory()
    postgres_factory = PostgreSQLFactory()
    
    conexao2 = mysql_factory.criar_conexao()
    conexao3 = postgres_factory.criar_conexao()
    
    print(f"   {conexao2.connect()}")
    print(f"   {conexao3.connect()}")
    
    print("\n3. Factory Method com uso:")
    mysql_factory.testar_conexao()
    postgres_factory.testar_conexao()
    
    print("\n4. Factory Method com parâmetros:")
    editor_factory = EditorFactory()
    doc1 = editor_factory.criar_documento("pdf")
    doc2 = editor_factory.criar_documento("word")
    
    doc1.criar("Relatório", "Conteúdo...")
    doc2.criar("Apresentação", "Conteúdo...")
    print(f"   {doc1.salvar()}")
    print(f"   {doc2.salvar()}")
    
    print("\n5. Processamento de Dados:")
    processor_factory = GenericDataProcessorFactory()
    resultado = processor_factory.processar_arquivo("json", [1, 2, 3])
    print(f"   {resultado}")

