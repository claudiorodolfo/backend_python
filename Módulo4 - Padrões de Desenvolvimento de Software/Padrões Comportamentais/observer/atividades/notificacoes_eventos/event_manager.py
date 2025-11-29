from observer import Observer
from subject import Subject

class EventManager(Subject):
    """Gerencia a inscrição e notificação de observadores."""
    def __init__(self):
        self._observers = []

    def registerObserver(self, observer: Observer):
        """Registra um novo observador."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unregisterObserver(self, observer: Observer):
        """Remove um observador existente."""
        if observer in self._observers:
            self._observers.remove(observer)

    def notifyObservers(self, event):
        """Notifica todos os observadores sobre um evento."""
        for observer in self._observers:
            observer.update(event)