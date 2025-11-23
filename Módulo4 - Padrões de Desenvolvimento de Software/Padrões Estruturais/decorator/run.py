from basic_image_processor import BasicImageProcessor
from watermark_image_processor import WatermarkImageProcessor
from resize_image_processor import ResizeImageProcessor

print("=== Teste do Padrão Decorator ===\n")

if __name__ == "__main__":
    imagePath = "/temp/file.jpg"
    #Composicao 1
    print("Composicao 1:")
    imageProcessor = BasicImageProcessor()
    imageProcessor = WatermarkImageProcessor(imageProcessor)
    imageProcessor = ResizeImageProcessor(imageProcessor)
    imageProcessor.process(imagePath)

   #Composicao 2
    print("\n\nComposicao 2:")
    imageProcessor = BasicImageProcessor()
    imageProcessor = ResizeImageProcessor(imageProcessor)
    imageProcessor = WatermarkImageProcessor(imageProcessor)
    imageProcessor.process(imagePath)

    # Composicao 3    
    print("\n\nComposicao 3:")
    imageProcessor = BasicImageProcessor()
    imageProcessor = ResizeImageProcessor(imageProcessor)
    imageProcessor.process(imagePath)