from image_processor import ImageProcessor

class BasicImageProcessor(ImageProcessor):
    """Processador de imagem básico"""

    def process(self, imagePath: str) -> str:
        print("Implementação do processamento de imagem básico.")
        newImagePath = "/uploads/file_processed.jpg"    
        print(f"Processa a imagem de {imagePath} para {newImagePath}")

        return newImagePath