from observer import Observer
from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def registerObserver(self, observer: Observer):
        pass

    @abstractmethod
    def unregisterObserver(self, observer: Observer):
        pass

    @abstractmethod
    def notifyObservers(self, event):
        pass