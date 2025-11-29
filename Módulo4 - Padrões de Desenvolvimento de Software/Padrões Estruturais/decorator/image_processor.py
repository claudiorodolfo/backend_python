from abc import ABC, abstractmethod

class ImageProcessor(ABC):

    @abstractmethod
    def process(self, imagePath: str) -> str:
        pass
