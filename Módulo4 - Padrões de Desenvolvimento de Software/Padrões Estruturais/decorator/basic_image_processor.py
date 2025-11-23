from image_processor_interface import ImageProcessorInterface

class BasicImageProcessor(ImageProcessorInterface):
    """Processador de imagem básico"""
        
    def process(self, imagePath: str) -> str:
        newImagePath = "/uploads/file_processed.jpg"  
        #TODO: Implement the basic image processing logic
        print(f"Processa a imagem de {imagePath} para {newImagePath}")
        
        return newImagePath