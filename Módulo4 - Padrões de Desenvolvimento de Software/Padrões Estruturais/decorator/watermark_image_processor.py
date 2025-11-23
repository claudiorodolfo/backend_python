from re import I
from image_processor_interface import ImageProcessorInterface

class WatermarkImageProcessor(ImageProcessorInterface):
    """Processador de imagem com marca d'água"""

    def __init__(self, imageProcessor: ImageProcessorInterface):
        self._imageProcessor = imageProcessor

    def process(self, imagePath: str) -> str:
        ImageProcessedPath = self._imageProcessor.process(imagePath)
        
        #TODO: Implementa a lógica da marca d'água
        newImagePath = "/uploads/watermark_file.jpg"
         
        print(f"Processa a imagem de {ImageProcessedPath} para {newImagePath}")
        
        return newImagePath