from abc import abstractmethod
from image_processor import ImageProcessor

class ImageProcessorDecorator(ImageProcessor):
    def __init__(self, imageProcessor: ImageProcessor):
        self._imageProcessor = imageProcessor

    @abstractmethod
    def process(self, imagePath: str) -> str:
        pass
