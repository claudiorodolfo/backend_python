"""
05 - EXERCÍCIOS: FACTORY METHOD E OBSERVER
===========================================

Exercícios práticos para implementar os padrões Factory Method e Observer.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

# ===========================================
# EXERCÍCIOS FACTORY METHOD
# ===========================================

# EXERCÍCIO 1: Factory para Formatos de Arquivo
# ==============================================
"""
Crie um sistema usando Factory Method para processar diferentes formatos de arquivo.

Requisitos:
- Interface Arquivo com métodos: ler(), escrever()
- Implementações: ArquivoTXT, ArquivoCSV, ArquivoJSON
- Factory abstrato ArquivoFactory com método criar_arquivo(tipo)
- Factory concreto ProcessadorArquivoFactory
- Método processar_arquivo(tipo, dados) que usa o factory

Teste criando arquivos de diferentes tipos.
"""

# TODO: Implemente aqui
class Arquivo(ABC):
    """Interface para arquivos"""
    pass

class ArquivoFactory(ABC):
    """Factory abstrato"""
    pass


# EXERCÍCIO 2: Factory para Diferentes Estratégias de Desconto
# ==============================================================
"""
Crie um sistema de descontos usando Factory Method.

Requisitos:
- Interface Desconto com método: calcular(valor_original)
- Tipos: DescontoPercentual (ex: 10%), DescontoFixo (ex: R$ 50), DescontoProgressivo
- Factory que cria o tipo de desconto apropriado
- Método aplicar_desconto(tipo, valor) que usa o factory

Implemente cada tipo de desconto com suas regras específicas.
"""

# TODO: Implemente aqui
class Desconto(ABC):
    """Interface para descontos"""
    pass

class DescontoFactory(ABC):
    """Factory para descontos"""
    pass


# EXERCÍCIO 3: Factory para Conexões de API
# ===========================================
"""
Crie um Factory Method para diferentes tipos de conexão com APIs.

Requisitos:
- Interface APIConnection com métodos: conectar(), fazer_request(endpoint)
- Implementações: RESTAPIConnection, GraphQLAPIConnection, SOAPAPIConnection
- Factory que cria conexão baseada no tipo de API
- Cada implementação simula o comportamento específico do protocolo

Teste fazendo requests com diferentes tipos de API.
"""

# TODO: Implemente aqui
class APIConnection(ABC):
    """Interface para conexões de API"""
    pass

class APIConnectionFactory(ABC):
    """Factory para conexões de API"""
    pass


# ===========================================
# EXERCÍCIOS OBSERVER
# ===========================================

# EXERCÍCIO 4: Sistema de Monitoramento de Temperatura
# ======================================================
"""
Crie um sistema de monitoramento de temperatura usando Observer.

Requisitos:
- Classe SensorTemperatura (Subject) que mantém temperatura atual
- Métodos: set_temperatura(valor), get_temperatura()
- Observers: AlertaObserver (alerta se > 30°C), DisplayObserver (mostra temp), 
             LogObserver (registra mudanças)
- Notifique observers quando temperatura mudar

Implemente todos os observers e teste mudanças de temperatura.
"""

# TODO: Implemente aqui
class TemperaturaObserver(ABC):
    """Observer para temperatura"""
    pass

class SensorTemperatura:
    """Subject que monitora temperatura"""
    pass


# EXERCÍCIO 5: Sistema de Eventos de Chat
# ========================================
"""
Crie um sistema de chat com eventos usando Observer.

Requisitos:
- Classe ChatRoom (Subject) que gerencia mensagens
- Métodos: enviar_mensagem(usuario, mensagem), listar_mensagens()
- Observers: 
  * NotificacaoObserver: notifica usuários sobre novas mensagens
  * ModeracaoObserver: verifica palavras proibidas
  * HistoricoObserver: salva histórico de mensagens
- Notifique observers quando nova mensagem for enviada

Teste enviando mensagens e verificando comportamento dos observers.
"""

# TODO: Implemente aqui
class ChatObserver(ABC):
    """Observer para eventos de chat"""
    pass

class ChatRoom:
    """Subject que gerencia chat"""
    pass


# EXERCÍCIO 6: Sistema de Pedidos com Observer
# ==============================================
"""
Crie um sistema completo de pedidos usando Observer.

Requisitos:
- Classe PedidoOnline (Subject) com: criar_pedido(), atualizar_status(), cancelar()
- Observers:
  * EmailObserver: envia email em cada mudança de status
  * EstoqueObserver: atualiza estoque quando pedido confirmado
  * FinanceiroObserver: registra pagamento quando pedido pago
  * LogisticaObserver: inicia preparação quando pedido confirmado
- Notifique observers em cada mudança de estado do pedido

Implemente estados: pendente -> confirmado -> pago -> enviado -> entregue
"""

# TODO: Implemente aqui
class PedidoObserver(ABC):
    """Observer para eventos de pedido"""
    pass

class PedidoOnline:
    """Subject que gerencia pedido online"""
    pass


# EXERCÍCIO 7: Análise Comparativa
# ==================================
"""
Responda as seguintes questões:

1. Qual a principal diferença entre Simple Factory e Factory Method?

2. Em que situação você usaria Observer ao invés de simplesmente chamar métodos diretamente?

3. Quais são os trade-offs do padrão Observer em relação a performance?

4. Quando não devemos usar Factory Method?

5. Como Observer se relaciona com o padrão MVC que veremos depois?
"""

def analisar_padroes():
    """Complete as respostas abaixo"""
    respostas = {
        "1. Diferença Simple Factory vs Factory Method": "",
        "2. Quando usar Observer": "",
        "3. Trade-offs Observer": "",
        "4. Quando não usar Factory Method": "",
        "5. Observer e MVC": ""
    }
    return respostas


# ===========================================
# SOLUÇÕES DOS EXERCÍCIOS
# ===========================================

class SolucaoExercicio1:
    """Solução do Exercício 1 - Factory para Arquivos"""
    
    class Arquivo(ABC):
        @abstractmethod
        def ler(self):
            pass
        
        @abstractmethod
        def escrever(self, dados):
            pass
    
    class ArquivoTXT(Arquivo):
        def __init__(self, nome):
            self.nome = nome
            self.conteudo = ""
        
        def ler(self):
            return f"Lendo {self.nome}.txt: {self.conteudo}"
        
        def escrever(self, dados):
            self.conteudo = dados
            return f"Escrevendo em {self.nome}.txt"
    
    class ArquivoCSV(Arquivo):
        def __init__(self, nome):
            self.nome = nome
            self.dados = []
        
        def ler(self):
            return f"Lendo {self.nome}.csv: {len(self.dados)} linhas"
        
        def escrever(self, dados):
            self.dados = dados if isinstance(dados, list) else [dados]
            return f"Escrevendo em {self.nome}.csv"
    
    class ArquivoJSON(Arquivo):
        def __init__(self, nome):
            self.nome = nome
            self.json_data = {}
        
        def ler(self):
            return f"Lendo {self.nome}.json: {self.json_data}"
        
        def escrever(self, dados):
            self.json_data = dados
            return f"Escrevendo em {self.nome}.json"
    
    class ArquivoFactory(ABC):
        @abstractmethod
        def criar_arquivo(self, tipo, nome) -> Arquivo:
            pass
    
    class ProcessadorArquivoFactory(ArquivoFactory):
        def criar_arquivo(self, tipo, nome) -> Arquivo:
            if tipo == "txt":
                return SolucaoExercicio1.ArquivoTXT(nome)
            elif tipo == "csv":
                return SolucaoExercicio1.ArquivoCSV(nome)
            elif tipo == "json":
                return SolucaoExercicio1.ArquivoJSON(nome)
            else:
                raise ValueError(f"Tipo não suportado: {tipo}")
        
        def processar_arquivo(self, tipo, nome, dados):
            arquivo = self.criar_arquivo(tipo, nome)
            arquivo.escrever(dados)
            return arquivo.ler()


class SolucaoExercicio4:
    """Solução do Exercício 4 - Monitoramento de Temperatura"""
    
    class TemperaturaObserver(ABC):
        @abstractmethod
        def update(self, temperatura):
            pass
    
    class AlertaObserver(TemperaturaObserver):
        def __init__(self, limite=30):
            self.limite = limite
        
        def update(self, temperatura):
            if temperatura > self.limite:
                print(f"[ALERTA] Temperatura crítica: {temperatura}°C (limite: {self.limite}°C)")
    
    class DisplayObserver(TemperaturaObserver):
        def update(self, temperatura):
            print(f"[DISPLAY] Temperatura atual: {temperatura}°C")
    
    class LogObserver(TemperaturaObserver):
        def __init__(self):
            self.historico = []
        
        def update(self, temperatura):
            self.historico.append(temperatura)
            print(f"[LOG] Temperatura registrada: {temperatura}°C")
    
    class SensorTemperatura:
        def __init__(self):
            self._observers: List[TemperaturaObserver] = []
            self._temperatura = 20
        
        def adicionar_observer(self, observer: TemperaturaObserver):
            if observer not in self._observers:
                self._observers.append(observer)
        
        def remover_observer(self, observer: TemperaturaObserver):
            if observer in self._observers:
                self._observers.remove(observer)
        
        def set_temperatura(self, valor):
            if self._temperatura != valor:
                self._temperatura = valor
                self._notificar()
        
        def get_temperatura(self):
            return self._temperatura
        
        def _notificar(self):
            for observer in self._observers:
                observer.update(self._temperatura)


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCÍCIOS - FACTORY METHOD E OBSERVER")
    print("=" * 60)
    print("\nComplete os exercícios acima e teste suas implementações!")
    print("\nPara ver as soluções, consulte as classes SolucaoExercicio*")

