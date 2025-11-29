from observer import Observer

class ConsoleAlertObserver(Observer):
    """Observador que simula envio de alerta."""

    def update(self, event):
        print(f"[ALERTA] Algo aconteceu: {event}")