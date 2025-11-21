# Padrão Builder (Builder Pattern)

## Descrição

O padrão **Builder** é um padrão de projeto criacional que permite construir objetos complexos passo a passo. Ele separa a construção de um objeto complexo da sua representação, permitindo que o mesmo processo de construção possa criar diferentes representações. Este padrão é especialmente útil quando um objeto precisa ser construído com muitos parâmetros opcionais ou quando o processo de construção envolve múltiplas etapas.

## Estrutura

O padrão Builder consiste em:

- **Product (Computador)**: O objeto complexo que está sendo construído
- **Builder (ComputadorBuilder)**: Interface abstrata que define os métodos para construir o produto
- **ConcreteBuilder (PCGamerBuilder, EscritorioBuilder, NotebookBuilder)**: Implementações concretas do builder que constroem diferentes variações do produto
- **Director (Diretor)**: Classe opcional que orquestra a construção usando um builder, definindo a ordem dos passos

## Vantagens

1. **Construção passo a passo**: Permite construir objetos complexos de forma incremental
2. **Reutilização de código**: O mesmo código de construção pode ser reutilizado para diferentes representações
3. **Isolamento de código**: Isola o código de construção da representação do objeto
4. **Flexibilidade**: Permite criar diferentes variações de um objeto usando o mesmo processo de construção
5. **Código mais limpo**: Evita construtores com muitos parâmetros (telescoping constructor anti-pattern)
6. **Validação**: Permite validar o objeto antes de finalizar a construção

## Estrutura do Código

### 1. Product - Computador

A classe `Computador` representa o objeto complexo que será construído:

```python
class Computador:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.armazenamento = None
        self.gpu = None
        self.monitor = None
        self.bateria = None  # Específico para notebooks
        self.peso = None     # Específico para notebooks
```

### 2. Builder Abstrato - ComputadorBuilder

Define a interface para construção de computadores:

```python
class ComputadorBuilder(ABC):
    @abstractmethod
    def setCpu(self, cpu): 
        pass
    
    @abstractmethod
    def setRam(self, ram): 
        pass
    
    @abstractmethod
    def setArmazenamento(self, armazenamento): 
        pass
    
    @abstractmethod
    def setGpu(self, gpu): 
        pass
    
    @abstractmethod
    def getResultado(self) -> Computador: 
        pass
```

### 3. Builders Concretos

#### PCGamerBuilder
Builder específico para PCs Gamer com validação de GPU dedicada:

```python
class PCGamerBuilder(ComputadorBuilder):
    def getResultado(self) -> Computador:
        # Validação: PC Gamer deve ter GPU dedicada
        if not self.computador.gpu:
            raise ValueError("PC Gamer deve ter uma GPU dedicada!")
        return self.computador
```

#### EscritorioBuilder
Builder para computadores de escritório com GPU integrada padrão:

```python
class EscritorioBuilder(ComputadorBuilder):
    def getResultado(self) -> Computador:
        # Validação: Computador de escritório pode usar GPU integrada
        if not self.computador.gpu:
            self.computador.gpu = "GPU Integrada"
        return self.computador
```

#### NotebookBuilder
Builder para notebooks com métodos específicos (bateria e peso):

```python
class NotebookBuilder(ComputadorBuilder):
    def setBateria(self, bateria):
        """Método específico para notebooks"""
        self.computador.bateria = bateria
        return self
    
    def setPeso(self, peso):
        """Método específico para notebooks"""
        self.computador.peso = peso
        return self
```

### 4. Director - Diretor

Orquestra a construção usando builders, definindo configurações pré-definidas:

```python
class Diretor:
    def __init__(self, builder: ComputadorBuilder):
        self.builder = builder
    
    def construir(self, tipo: TipoComputador = None):
        match tipo:
            case TipoComputador.PC_GAMER:
                # Configuração pré-definida para PC Gamer
                ...
            case TipoComputador.ESCRITORIO:
                # Configuração pré-definida para Escritório
                ...
            case TipoComputador.NOTEBOOK:
                # Configuração pré-definida para Notebook
                ...
```

## Exemplo de Uso

### Uso com Director (Configurações Pré-definidas)

```python
from pc_gamer_builder import PCGamerBuilder
from diretor import Diretor, TipoComputador

# Construir PC Gamer usando configuração pré-definida
builderGamer = PCGamerBuilder()
diretor = Diretor(builderGamer)
pcGamer = diretor.construir(TipoComputador.PC_GAMER)
print(pcGamer)
# Output: Computador(cpu=Intel i9-13900K, ram=32GB DDR5, ...)
```

### Uso Direto do Builder (Construção Customizada)

```python
from notebook_builder import NotebookBuilder

# Construção customizada usando fluent interface
notebook = (NotebookBuilder()
            .setCpu("Apple M2 Pro")
            .setRam("32GB")
            .setArmazenamento("1TB SSD")
            .setGpu("GPU Integrada M2")
            .setMonitor("16\" Retina")
            .setBateria("100Wh")
            .setPeso("2.0kg")
            .construir())
```

### Uso Híbrido (Director + Customização)

```python
from notebook_builder import NotebookBuilder
from diretor import Diretor

# Usar director para iniciar, depois customizar
builder = NotebookBuilder()
diretor = Diretor(builder)
builder = diretor.construir()  # Retorna o builder para customização

notebook = (builder
            .setCpu("Intel i7-13700H")
            .setRam("32GB DDR5")
            .setArmazenamento("2TB SSD")
            .setGpu("RTX 4070")
            .setMonitor("17\" 4K")
            .setBateria("99Wh")
            .setPeso("2.5kg")
            .construir())
```

## Executando o Exemplo

Para executar a demonstração completa do padrão Builder:

```bash
python3 builder.py
```

O script demonstra:
1. Construção de PC Gamer usando Director
2. Construção de Computador de Escritório usando Director
3. Construção de Notebook usando Director
4. Construção customizada sem Director
5. Construção híbrida (Director + customização)

## Características Importantes

### Fluent Interface

Todos os builders implementam uma interface fluente, permitindo encadear chamadas de métodos:

```python
builder.setCpu("Intel i9").setRam("32GB").setGpu("RTX 4080")
```

### Validação

Cada builder pode implementar validações específicas no método `getResultado()`:

- **PCGamerBuilder**: Valida se tem GPU dedicada
- **EscritorioBuilder**: Define GPU integrada como padrão se não especificada
- **NotebookBuilder**: Define bateria padrão se não especificada

### Extensibilidade

O padrão permite adicionar novos tipos de computadores facilmente:

1. Criar um novo builder concreto que estende `ComputadorBuilder`
2. Adicionar métodos específicos se necessário
3. Opcionalmente, adicionar um novo tipo no `Diretor`

## Quando Usar

- Quando um objeto precisa ser construído com muitos parâmetros opcionais
- Quando o processo de construção é complexo e envolve múltiplas etapas
- Quando você precisa criar diferentes representações do mesmo objeto
- Quando você quer isolar o código de construção da representação
- Quando você precisa validar o objeto durante a construção
- Quando você quer permitir construção passo a passo

## Quando NÃO Usar

- Quando o objeto é simples e não requer muitos parâmetros
- Quando a construção é direta e não envolve lógica complexa
- Quando você tem apenas uma representação do objeto
- Quando o overhead do padrão não justifica sua complexidade

## Variações do Padrão

### Builder com Director
- Usa uma classe Director para orquestrar a construção
- Útil quando há configurações pré-definidas comuns
- Implementação atual usa esta abordagem

### Builder sem Director
- O cliente usa o builder diretamente
- Mais flexível, mas requer conhecimento dos passos de construção
- Útil para construções altamente customizadas

### Builder com Validação
- Inclui validação no método `getResultado()`
- Garante que o objeto construído está em um estado válido
- Todos os builders concretos implementam validação

## Diferenças de Outros Padrões

### Builder vs Factory

- **Factory**: Foca em criar objetos de diferentes tipos
- **Builder**: Foca em construir objetos complexos passo a passo

### Builder vs Prototype

- **Prototype**: Cria objetos clonando uma instância existente
- **Builder**: Constrói objetos do zero usando um processo passo a passo

## Referências

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) - Gang of Four
- [Refactoring Guru - Builder Pattern](https://refactoring.guru/design-patterns/builder)

