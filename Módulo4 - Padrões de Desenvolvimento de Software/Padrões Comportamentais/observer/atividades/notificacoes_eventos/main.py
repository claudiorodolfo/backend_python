from event_manager import EventManager
from console_observer import ConsoleAlertObserver
from logger_observer import LoggerObserver

if __name__ == "__main__":
    event_manager = EventManager()
    logger = LoggerObserver()
    alert = ConsoleAlertObserver()

    event_manager.registerObserver(logger)
    event_manager.registerObserver(alert)

    print("\n--- Disparando Evento 1 ---")
    event_manager.notifyObservers("Usuário fez login")

    print("\n--- Disparando Evento 2 ---")
    event_manager.notifyObservers("Arquivo carregado com sucesso")

    event_manager.unregisterObserver(alert)

    print("\n--- Disparando Evento 3 ---")
    event_manager.notifyObservers("Processo finalizado")