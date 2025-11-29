from basic_image_processor import BasicImageProcessor
from watermark_image_processor import WatermarkImageProcessor
from resize_image_processor import ResizeImageProcessor

print("=== Teste do Padrão Decorator ===\n")

if __name__ == "__main__":
    imagePath = "/temp/file.jpg"

    #Composicao 1
    print("Composicao 1: Básico -> Marca d'água -> Redimensionado\n")
    imagem = ResizeImageProcessor(WatermarkImageProcessor(BasicImageProcessor()))
    imagem.process(imagePath)

   #Composicao 2
    print("\nComposicao 2: Básico -> Redimensionado -> Marca d'água\n")
    imagem = WatermarkImageProcessor(ResizeImageProcessor(BasicImageProcessor()))
    imagem.process(imagePath)

    # Composicao 3    
    print("\n\nComposicao 3: Básico -> Redimensionado\n ")
    imagem = ResizeImageProcessor(BasicImageProcessor())
    imagem.process(imagePath)