from basic_image_processor import BasicImageProcessor
from watermark_image_processor import WatermarkImageProcessor

print("=== Teste do Padrão Decorator ===\n")

if __name__ == "__main__":
    imagePath = "/temp/file.jpg"
    imageProcessor = BasicImageProcessor()
    imageProcessor = WatermarkImageProcessor(imageProcessor)
    imageProcessor.process(imagePath)