from observer import Observer

class LoggerObserver(Observer):
    """Observador que registra logs no console."""

    def update(self, event):
        print(f"[LOG] Evento recebido: {event}")
