"""
03 - PADRÃO OBSERVER
====================

Conceito do Observer
--------------------
O Observer é um padrão comportamental que permite definir um mecanismo de 
assinatura para notificar múltiplos objetos sobre eventos que acontecem 
no objeto que estão observando.

Também conhecido como:
- Publisher-Subscriber (Pub-Sub)
- Model-View Pattern
- Dependents Pattern

Componentes:
- Subject (Sujeito): objeto que mantém lista de observers
- Observer (Observador): interface para objetos que devem ser notificados
- ConcreteObserver: implementação concreta do observer

Quando Utilizar Observer
-------------------------
✓ Quando mudanças em um objeto precisam notificar outros objetos
✓ Quando o número de objetos a notificar é desconhecido ou dinâmico
✓ Quando objetos precisam ser desacoplados
✓ Em sistemas de eventos e notificações
✓ Em arquitetura MVC (Model notifica View)

Uso em Eventos e Notificações
------------------------------
- Sistemas de notificação em tempo real
- Atualização de interfaces quando dados mudam
- Logging e auditoria
- Cache invalidation
- Implementação de callbacks

Vantagens
---------
✓ Acoplamento fraco entre Subject e Observers
✓ Princípio aberto/fechado: fácil adicionar novos observers
✓ Comunicação dinâmica: observers podem ser adicionados/removidos
✓ Suporta broadcasting (um evento para muitos listeners)

Desvantagens
------------
✗ Pode causar updates desnecessários
✗ Ordem de notificação pode ser importante e difícil de controlar
✗ Pode gerar cadeias de notificações não intencionais
"""

from abc import ABC, abstractmethod
from typing import List

# IMPLEMENTAÇÃO 1: Observer Básico
# =================================

class Observer(ABC):
    """Interface para observadores"""
    
    @abstractmethod
    def update(self, mensagem):
        """Chamado quando o subject notifica mudanças"""
        pass


class Subject:
    """Sujeito que mantém lista de observadores"""
    
    def __init__(self):
        self._observers: List[Observer] = []
    
    def adicionar_observer(self, observer: Observer):
        """Adiciona um observador à lista"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer adicionado: {observer.__class__.__name__}")
    
    def remover_observer(self, observer: Observer):
        """Remove um observador da lista"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer removido: {observer.__class__.__name__}")
    
    def notificar(self, mensagem):
        """Notifica todos os observadores"""
        for observer in self._observers:
            observer.update(mensagem)


class ObserverEmail(Observer):
    """Observador que envia emails"""
    
    def __init__(self, email):
        self.email = email
    
    def update(self, mensagem):
        print(f"[EMAIL para {self.email}] {mensagem}")

class ObserverSMS(Observer):
    """Observador que envia SMS"""
    
    def __init__(self, telefone):
        self.telefone = telefone
    
    def update(self, mensagem):
        print(f"[SMS para {self.telefone}] {mensagem}")

class ObserverLog(Observer):
    """Observador que registra em log"""
    
    def __init__(self):
        self.logs = []
    
    def update(self, mensagem):
        log_entry = f"LOG: {mensagem}"
        self.logs.append(log_entry)
        print(f"[LOG] {mensagem}")
    
    def get_logs(self):
        return self.logs


# IMPLEMENTAÇÃO 2: Observer com Dados Específicos
# =================================================

class EventoObserver(ABC):
    """Observer que recebe eventos tipados"""
    
    @abstractmethod
    def on_event(self, evento_tipo, dados):
        pass


class EventoSubject:
    """Subject que envia eventos tipados"""
    
    def __init__(self):
        self._observers: List[EventoObserver] = []
    
    def adicionar_observer(self, observer: EventoObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remover_observer(self, observer: EventoObserver):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notificar_evento(self, evento_tipo, dados=None):
        """Notifica observers com tipo de evento e dados"""
        for observer in self._observers:
            observer.on_event(evento_tipo, dados)


class ObserverEstoque(EventoObserver):
    """Observer que monitora eventos de estoque"""
    
    def on_event(self, evento_tipo, dados):
        if evento_tipo == "estoque_baixo":
            print(f"[ESTOQUE] Alerta: {dados['produto']} está com estoque baixo!")
        elif evento_tipo == "estoque_zerado":
            print(f"[ESTOQUE] Crítico: {dados['produto']} sem estoque!")

class ObserverFinanceiro(EventoObserver):
    """Observer que monitora eventos financeiros"""
    
    def on_event(self, evento_tipo, dados):
        if evento_tipo == "venda_realizada":
            valor = dados.get('valor', 0)
            print(f"[FINANCEIRO] Venda registrada: R${valor:.2f}")


# IMPLEMENTAÇÃO 3: Observer com Callbacks
# ========================================

class CallbackObserver:
    """Observer simples usando callbacks/funções"""
    
    def __init__(self):
        self.callbacks = []
    
    def adicionar_callback(self, callback):
        """Adiciona uma função callback"""
        self.callbacks.append(callback)
    
    def remover_callback(self, callback):
        """Remove uma função callback"""
        if callback in self.callbacks:
            self.callbacks.remove(callback)
    
    def notificar(self, *args, **kwargs):
        """Chama todos os callbacks"""
        for callback in self.callbacks:
            callback(*args, **kwargs)


# IMPLEMENTAÇÃO 4: Observer com Filtros
# ======================================

class FilteredObserver(ABC):
    """Observer que pode filtrar eventos"""
    
    @abstractmethod
    def deve_processar(self, evento_tipo):
        """Retorna True se deve processar este tipo de evento"""
        pass
    
    @abstractmethod
    def update(self, evento_tipo, dados):
        pass


class FilteredSubject:
    """Subject que permite filtros nos observers"""
    
    def __init__(self):
        self._observers: List[FilteredObserver] = []
    
    def adicionar_observer(self, observer: FilteredObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def notificar(self, evento_tipo, dados):
        """Notifica apenas observers que querem processar este evento"""
        for observer in self._observers:
            if observer.deve_processar(evento_tipo):
                observer.update(evento_tipo, dados)


class ObserverApenasErros(FilteredObserver):
    """Observer que só processa erros"""
    
    def deve_processar(self, evento_tipo):
        return evento_tipo in ["erro", "falha", "exception"]
    
    def update(self, evento_tipo, dados):
        print(f"[ERRO] {evento_tipo}: {dados}")


if __name__ == "__main__":
    print("=" * 60)
    print("PADRÃO OBSERVER")
    print("=" * 60)
    
    # TESTE 1: Observer Básico
    print("\n1. Observer Básico:")
    subject = Subject()
    
    email_observer = ObserverEmail("admin@email.com")
    sms_observer = ObserverSMS("11999999999")
    log_observer = ObserverLog()
    
    subject.adicionar_observer(email_observer)
    subject.adicionar_observer(sms_observer)
    subject.adicionar_observer(log_observer)
    
    subject.notificar("Sistema iniciado com sucesso")
    subject.notificar("Nova atualização disponível")
    
    # TESTE 2: Observer com Eventos Tipados
    print("\n2. Observer com Eventos Tipados:")
    evento_subject = EventoSubject()
    
    estoque_observer = ObserverEstoque()
    financeiro_observer = ObserverFinanceiro()
    
    evento_subject.adicionar_observer(estoque_observer)
    evento_subject.adicionar_observer(financeiro_observer)
    
    evento_subject.notificar_evento("estoque_baixo", {
        "produto": "Notebook",
        "quantidade": 5
    })
    
    evento_subject.notificar_evento("venda_realizada", {
        "produto": "Notebook",
        "valor": 2500.00
    })
    
    # TESTE 3: Observer com Callbacks
    print("\n3. Observer com Callbacks:")
    callback_observer = CallbackObserver()
    
    def callback1(mensagem):
        print(f"Callback 1: {mensagem}")
    
    def callback2(mensagem):
        print(f"Callback 2: {mensagem}")
    
    callback_observer.adicionar_callback(callback1)
    callback_observer.adicionar_callback(callback2)
    callback_observer.notificar("Mensagem importante")
    
    # TESTE 4: Observer com Filtros
    print("\n4. Observer com Filtros:")
    filtered_subject = FilteredSubject()
    erro_observer = ObserverApenasErros()
    
    filtered_subject.adicionar_observer(erro_observer)
    
    filtered_subject.notificar("info", "Sistema funcionando")
    filtered_subject.notificar("erro", "Falha na conexão")
    filtered_subject.notificar("sucesso", "Operação concluída")

