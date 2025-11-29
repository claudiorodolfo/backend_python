from image_processor_decorator import ImageProcessorDecorator

class ResizeImageProcessor(ImageProcessorDecorator):
    """Processador de imagem com redimensionamento"""

    def process(self, imagePath: str) -> str:
        ProcessedImagePath = self._imageProcessor.process(imagePath)
        
        print("Implementação a lógica do redimensionamento.")
        newImagePath = "/uploads/resized_file.jpg"     
        print(f"Processa a imagem de {ProcessedImagePath} para {newImagePath}")
        
        return newImagePath