# Padrão Decorator - Processador de Imagens

Este projeto demonstra a implementação do **Padrão Decorator** (Decorator Pattern) através de um sistema de processamento de imagens. O padrão permite adicionar funcionalidades dinamicamente a objetos sem alterar sua estrutura.

## 📋 Sobre o Padrão Decorator

O **Decorator Pattern** é um padrão estrutural que permite adicionar novos comportamentos a objetos de forma dinâmica, envolvendo-os com objetos decoradores. Isso oferece uma alternativa flexível à herança para estender funcionalidades.

### Vantagens
- ✅ Adiciona responsabilidades de forma dinâmica
- ✅ Permite combinar funcionalidades de forma flexível
- ✅ Evita a explosão de classes (subclasses para cada combinação)
- ✅ Segue o princípio Open/Closed (aberto para extensão, fechado para modificação)

## 🏗️ Estrutura do Projeto

```
decorator/
├── image_processor_interface.py    # Interface abstrata
├── basic_image_processor.py         # Implementação base (Componente Concreto)
├── resize_image_processor.py        # Decorator para redimensionamento
├── watermark_image_processor.py    # Decorator para marca d'água
└── run.py                           # Exemplos de uso
```

## 📁 Componentes

### `ImageProcessorInterface`
Interface abstrata que define o contrato para processadores de imagem:
- `process(imagePath: str) -> str`: Método abstrato para processar imagens

### `BasicImageProcessor`
Implementação base do processador de imagens. Representa o componente concreto que será decorado.

### `ResizeImageProcessor`
Decorator que adiciona funcionalidade de redimensionamento à imagem. Envolve um `ImageProcessorInterface` e adiciona o comportamento de resize.

### `WatermarkImageProcessor`
Decorator que adiciona funcionalidade de marca d'água à imagem. Envolve um `ImageProcessorInterface` e adiciona o comportamento de watermark.

## 🚀 Como Usar

### Executando o exemplo

```bash
python run.py
```

### Exemplo de código

```python
from basic_image_processor import BasicImageProcessor
from watermark_image_processor import WatermarkImageProcessor
from resize_image_processor import ResizeImageProcessor

# Composição 1: Básico → Watermark → Resize
imageProcessor = BasicImageProcessor()
imageProcessor = WatermarkImageProcessor(imageProcessor)
imageProcessor = ResizeImageProcessor(imageProcessor)
imageProcessor.process("/temp/file.jpg")

# Composição 2: Básico → Resize → Watermark
imageProcessor = BasicImageProcessor()
imageProcessor = ResizeImageProcessor(imageProcessor)
imageProcessor = WatermarkImageProcessor(imageProcessor)
imageProcessor.process("/temp/file.jpg")

# Composição 3: Apenas Resize
imageProcessor = BasicImageProcessor()
imageProcessor = ResizeImageProcessor(imageProcessor)
imageProcessor.process("/temp/file.jpg")
```

## 🔄 Fluxo de Execução

Quando você compõe decorators, o processamento ocorre em uma cadeia:

1. O decorator mais externo recebe a chamada
2. Ele delega para o decorator interno (ou componente base)
3. Cada decorator adiciona sua funcionalidade antes/depois do processamento base
4. O resultado é retornado através da cadeia

### Exemplo de fluxo (Composição 1):
```
ResizeImageProcessor.process()
  └─> WatermarkImageProcessor.process()
      └─> BasicImageProcessor.process()
          └─> Retorna imagem processada
      └─> Adiciona watermark
  └─> Redimensiona imagem
```

## 🎯 Casos de Uso

Este padrão é útil quando:
- Você precisa adicionar funcionalidades a objetos de forma dinâmica
- A herança não é adequada (muitas combinações possíveis)
- Você quer manter a flexibilidade de combinar funcionalidades
- Precisa adicionar/remover responsabilidades em tempo de execução

## 📝 Notas de Implementação

- Os decorators implementam a mesma interface que o componente base
- Cada decorator mantém uma referência ao componente que decora
- A ordem dos decorators pode afetar o resultado final
- Os TODOs no código indicam onde a lógica real de processamento seria implementada

## 🔧 Requisitos

- Python 3.x
- Nenhuma dependência externa (apenas biblioteca padrão)

## 📚 Referências

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) - Gang of Four
- [Refactoring Guru - Decorator Pattern](https://refactoring.guru/design-patterns/decorator)

