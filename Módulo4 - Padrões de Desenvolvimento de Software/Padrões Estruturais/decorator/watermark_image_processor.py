from image_processor_decorator import ImageProcessorDecorator

class WatermarkImageProcessor(ImageProcessorDecorator):
    """Processador de imagem com marca d'água"""

    def process(self, imagePath: str) -> str:
        ProcessedImagePath = self._imageProcessor.process(imagePath)
        
        print("Implementação a lógica da marca d'água.")
        newImagePath = "/uploads/watermark_file.jpg"
        print(f"Processa a imagem de {ProcessedImagePath} para {newImagePath}")
        
        return newImagePath