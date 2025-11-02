"""
01 - PADRÃO DECORATOR
=====================

Definição e Motivação
---------------------
O Decorator é um padrão estrutural que permite adicionar novos comportamentos 
a objetos dinamicamente, colocando-os dentro de objetos wrapper que contêm 
esses comportamentos.

Motivação:
- Adicionar funcionalidades sem modificar código existente
- Compor objetos dinamicamente
- Seguir princípio aberto/fechado (OCP)
- Evitar explosão de subclasses

Diferença entre Herança e Composição via Decorator
---------------------------------------------------
HERANÇA:
- Estática: comportamento definido em tempo de compilação
- Criar múltiplas subclasses para cada combinação
- Pode causar explosão de classes
- Exemplo: TextoBold, TextoItalic, TextoBoldItalic, TextoBoldItalicUnderline...

COMPOSIÇÃO (Decorator):
- Dinâmica: comportamento pode ser adicionado em runtime
- Composição flexível de decoradores
- Sempre uma interface comum
- Exemplo: Decorator compõe objetos e adiciona funcionalidades

Vantagens
---------
✓ Adiciona responsabilidades dinamicamente
✓ Remove responsabilidades facilmente
✓ Mais flexível que herança
✓ Evita explosão de subclasses
✓ Permite combinar decoradores

Desvantagens
------------
✗ Pode ser difícil depurar código decorado
✗ Ordem dos decoradores pode importar
✗ Pode criar objetos complexos difíceis de entender
"""

from abc import ABC, abstractmethod

# EXEMPLO 1: Decorator Clássico (Estrutural)
# ============================================

class Component(ABC):
    """Interface para componentes que podem ser decorados"""
    
    @abstractmethod
    def operacao(self):
        pass


class ComponentConcreto(Component):
    """Componente concreto básico"""
    
    def operacao(self):
        return "ComponenteConcreto"


class Decorator(Component):
    """Classe base para decoradores"""
    
    def __init__(self, component: Component):
        self._component = component
    
    @abstractmethod
    def operacao(self):
        pass


class DecoratorA(Decorator):
    """Decorator que adiciona funcionalidade A"""
    
    def operacao(self):
        resultado_base = self._component.operacao()
        return f"DecoratorA({resultado_base})"


class DecoratorB(Decorator):
    """Decorator que adiciona funcionalidade B"""
    
    def operacao(self):
        resultado_base = self._component.operacao()
        return f"DecoratorB({resultado_base})"


# EXEMPLO 2: Decorator para Processamento de Texto
# ==================================================

class Texto(ABC):
    """Interface para texto"""
    
    @abstractmethod
    def renderizar(self):
        pass


class TextoSimples(Texto):
    """Texto básico sem formatação"""
    
    def __init__(self, conteudo):
        self.conteudo = conteudo
    
    def renderizar(self):
        return self.conteudo


class TextoDecorator(Texto):
    """Base para decoradores de texto"""
    
    def __init__(self, texto: Texto):
        self._texto = texto
    
    @abstractmethod
    def renderizar(self):
        pass


class TextoBold(TextoDecorator):
    """Adiciona negrito"""
    
    def renderizar(self):
        return f"<b>{self._texto.renderizar()}</b>"


class TextoItalic(TextoDecorator):
    """Adiciona itálico"""
    
    def renderizar(self):
        return f"<i>{self._texto.renderizar()}</i>"


class TextoUnderline(TextoDecorator):
    """Adiciona sublinhado"""
    
    def renderizar(self):
        return f"<u>{self._texto.renderizar()}</u>"


class TextoColorido(TextoDecorator):
    """Adiciona cor"""
    
    def __init__(self, texto: Texto, cor):
        super().__init__(texto)
        self.cor = cor
    
    def renderizar(self):
        return f'<span style="color:{self.cor}">{self._texto.renderizar()}</span>'


# EXEMPLO 3: Decorator para Funcionalidades de Funções
# =====================================================

def decorador_logging(func):
    """Decorator que adiciona logging a uma função"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Chamando {func.__name__} com args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} retornou: {resultado}")
        return resultado
    return wrapper


def decorador_cache(func):
    """Decorator que adiciona cache a uma função"""
    cache = {}
    
    def wrapper(*args, **kwargs):
        chave = str(args) + str(kwargs)
        if chave in cache:
            print(f"[CACHE] Retornando resultado em cache para {func.__name__}")
            return cache[chave]
        
        resultado = func(*args, **kwargs)
        cache[chave] = resultado
        print(f"[CACHE] Armazenando resultado em cache para {func.__name__}")
        return resultado
    
    return wrapper


def decorador_validacao(tipo_esperado):
    """Decorator que valida tipo de entrada"""
    def decorador(func):
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, tipo_esperado):
                    raise TypeError(f"Argumento deve ser {tipo_esperado.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorador


# Funções de exemplo
@decorador_logging
def calcular_soma(a, b):
    return a + b


@decorador_cache
@decorador_logging
def calcular_fatorial(n):
    if n <= 1:
        return 1
    return n * calcular_fatorial(n - 1)


@decorador_validacao(int)
def multiplicar(a, b):
    return a * b


# EXEMPLO 4: Decorator para Streaming de Dados
# ===============================================

class Stream(ABC):
    """Interface para streams de dados"""
    
    @abstractmethod
    def ler(self):
        pass
    
    @abstractmethod
    def escrever(self, dados):
        pass


class FileStream(Stream):
    """Stream básico de arquivo"""
    
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.conteudo = ""
    
    def ler(self):
        return f"Lendo de {self.nome_arquivo}: {self.conteudo}"
    
    def escrever(self, dados):
        self.conteudo = dados
        return f"Escrevendo em {self.nome_arquivo}"


class StreamDecorator(Stream):
    """Base para decoradores de stream"""
    
    def __init__(self, stream: Stream):
        self._stream = stream
    
    def ler(self):
        return self._stream.ler()
    
    def escrever(self, dados):
        return self._stream.escrever(dados)


class CompressaoStream(StreamDecorator):
    """Adiciona compressão ao stream"""
    
    def escrever(self, dados):
        dados_comprimidos = f"[COMPRESSO]{dados}[COMPRESSO]"
        return self._stream.escrever(dados_comprimidos)
    
    def ler(self):
        resultado = self._stream.ler()
        return resultado.replace("[COMPRESSO]", "")


class CriptografiaStream(StreamDecorator):
    """Adiciona criptografia ao stream"""
    
    def escrever(self, dados):
        dados_criptografados = f"[CRIPTOGRAFADO]{dados}[CRIPTOGRAFADO]"
        return self._stream.escrever(dados_criptografados)
    
    def ler(self):
        resultado = self._stream.ler()
        return resultado.replace("[CRIPTOGRAFADO]", "")


class LoggingStream(StreamDecorator):
    """Adiciona logging ao stream"""
    
    def escrever(self, dados):
        print(f"[LOG STREAM] Escrevendo: {dados}")
        return self._stream.escrever(dados)
    
    def ler(self):
        resultado = self._stream.ler()
        print(f"[LOG STREAM] Lendo: {resultado}")
        return resultado


# EXEMPLO 5: Decorator em Python (Sintaxe Nativa)
# =================================================

class Contador:
    """Classe simples para demonstrar decorators Python"""
    
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1
        return self.contador


def decorador_contador(func):
    """Decorator que conta chamadas de função"""
    contador = {"count": 0}
    
    def wrapper(*args, **kwargs):
        contador["count"] += 1
        print(f"[CONTADOR] {func.__name__} chamada {contador['count']} vezes")
        return func(*args, **kwargs)
    
    wrapper.contador = lambda: contador["count"]
    return wrapper


@decorador_contador
def funcao_exemplo():
    return "Resultado exemplo"


if __name__ == "__main__":
    print("=" * 60)
    print("PADRÃO DECORATOR")
    print("=" * 60)
    
    # TESTE 1: Decorator Clássico
    print("\n1. Decorator Clássico:")
    componente = ComponentConcreto()
    decorado1 = DecoratorA(componente)
    decorado2 = DecoratorB(decorado1)
    decorado3 = DecoratorA(decorado2)
    
    print(f"   Original: {componente.operacao()}")
    print(f"   Decorado: {decorado3.operacao()}")
    
    # TESTE 2: Decorator de Texto
    print("\n2. Decorator de Texto:")
    texto = TextoSimples("Hello World")
    texto_bold = TextoBold(texto)
    texto_italic_bold = TextoItalic(texto_bold)
    texto_completo = TextoUnderline(TextoColorido(texto_italic_bold, "red"))
    
    print(f"   Original: {texto.renderizar()}")
    print(f"   Decorado: {texto_completo.renderizar()}")
    
    # TESTE 3: Decorator de Funções
    print("\n3. Decorator de Funções:")
    resultado = calcular_soma(5, 3)
    print(f"   Resultado: {resultado}")
    
    resultado_fat = calcular_fatorial(5)
    print(f"   Fatorial de 5: {resultado_fat}")
    
    try:
        multiplicar(5, "3")  # Deve falhar
    except TypeError as e:
        print(f"   Validação funcionando: {e}")
    
    # TESTE 4: Decorator de Stream
    print("\n4. Decorator de Stream:")
    stream_base = FileStream("dados.txt")
    stream_comprimido = CompressaoStream(stream_base)
    stream_cripto = CriptografiaStream(stream_comprimido)
    stream_log = LoggingStream(stream_cripto)
    
    stream_log.escrever("Dados importantes")
    resultado = stream_log.ler()
    print(f"   Resultado: {resultado}")
    
    # TESTE 5: Decorator Python Nativo
    print("\n5. Decorator Python Nativo:")
    funcao_exemplo()
    funcao_exemplo()
    print(f"   Total de chamadas: {funcao_exemplo.contador()}")

