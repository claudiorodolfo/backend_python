# Padrão Builder - Construção de Computadores

Este projeto demonstra a implementação do **Padrão Builder** (Construtor) em Python, utilizando a construção de computadores como exemplo prático.

## 📋 Sobre o Padrão Builder

O **Builder** é um padrão de projeto criacional que permite construir objetos complexos passo a passo. Ele separa a construção de um objeto complexo de sua representação, permitindo que o mesmo processo de construção possa criar diferentes representações.

### Vantagens

- ✅ Permite construir objetos passo a passo
- ✅ Reutiliza código de construção
- ✅ Isola código complexo de construção
- ✅ Permite diferentes representações do mesmo objeto
- ✅ Facilita a criação de objetos com muitos parâmetros opcionais

## 🏗️ Estrutura do Projeto

O projeto está organizado nos seguintes componentes:

```
buider/
├── product.py              # Produto (Computador)
├── builder.py              # Builder abstrato (ConstrutorComputador)
├── concret_builders.py     # Builders concretos (Gamer e Escritório)
├── director.py             # Diretor (DiretorComputador)
└── main.py                 # Exemplo de uso
```

## 📦 Componentes

### 1. Product (`product.py`)
A classe `Computador` representa o produto final que será construído. Ela possui os seguintes atributos:
- `cpu`: Processador
- `memoria`: Memória RAM
- `armazenamento`: Disco de armazenamento
- `gpu`: Placa de vídeo (opcional)
- `sistema_operacional`: Sistema operacional (opcional)

### 2. Builder (`builder.py`)
A classe abstrata `ConstrutorComputador` define a interface para construir um computador. Ela especifica métodos para:
- `construirCpu()`: Construir o processador
- `construirMemoria()`: Construir a memória
- `construirArmazenamento()`: Construir o armazenamento
- `construirGpu()`: Construir a GPU (opcional)
- `instalarSistema()`: Instalar sistema operacional (opcional)
- `getResultado()`: Retornar o produto final

### 3. Concrete Builders (`concret_builders.py`)
Implementações concretas do builder:

- **`ConstrutorComputadorGamer`**: Constrói computadores de alta performance
  - CPU: Intel i9-13900K
  - Memória: 32GB DDR5
  - Armazenamento: 1TB SSD NVMe
  - GPU: NVIDIA RTX 4080
  - Sistema: Ubuntu 22.04

- **`ConstrutorComputadorEscritorio`**: Constrói computadores básicos para escritório
  - CPU: Intel i5-12400
  - Memória: 16GB DDR4
  - Armazenamento: 500GB SSD
  - Sistema: Windows 11
  - Sem GPU

### 4. Director (`director.py`)
A classe `DiretorComputador` orquestra o processo de construção. Ela define receitas de construção:
- `fabricarBasico()`: Constrói configuração básica (CPU + Memória + Armazenamento)
- `fabricarCompleto()`: Constrói configuração completa (todos os componentes)
- `construir()`: Retorna o produto final

## 🚀 Como Usar

### Executando o Exemplo

```bash
python main.py
```

### Exemplo de Uso

```python
from concret_builders import ConstrutorComputadorGamer, ConstrutorComputadorEscritorio
from director import DiretorComputador

# Construir um PC Gamer completo
builder_gamer = ConstrutorComputadorGamer()
diretor = DiretorComputador(builder_gamer)
diretor.fabricarCompleto()
pc_gamer = diretor.construir()
print("PC Gamer:", pc_gamer)

# Construir um PC de Escritório básico
builder_office = ConstrutorComputadorEscritorio()
diretor = DiretorComputador(builder_office)
diretor.fabricarBasico()
pc_office = diretor.construir()
print("PC Escritório:", pc_office)
```

### Saída Esperada

```
PC Gamer: CPU: Intel i9-13900K, Memória: 32GB DDR5, Armazenamento: 1TB SSD NVMe, GPU: NVIDIA RTX 4080, Sistema Operacional: Ubuntu 22.04
PC Escritório: CPU: Intel i5-12400, Memória: 16GB DDR4, Armazenamento: 500GB SSD, Sistema Operacional: Windows 11
```

## 🔄 Fluxo de Construção

1. **Cliente** cria um builder concreto (ex: `ConstrutorComputadorGamer`)
2. **Cliente** passa o builder para o diretor (`DiretorComputador`)
3. **Diretor** chama métodos do builder na ordem correta (ex: `fabricarCompleto()`)
4. **Builder** constrói o produto passo a passo
5. **Cliente** obtém o produto final através do diretor (`construir()`)

## 🎯 Casos de Uso

O padrão Builder é útil quando:
- Você precisa construir objetos complexos com muitos parâmetros
- Diferentes representações do mesmo objeto são necessárias
- O processo de construção deve ser independente das partes que compõem o objeto
- Você quer evitar construtores com muitos parâmetros (telescoping constructor)

## 📚 Referências

- [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) - Gang of Four
- [Refactoring Guru - Builder Pattern](https://refactoring.guru/design-patterns/builder)

## 📝 Notas

- O diretor é opcional; você pode usar o builder diretamente se preferir
- Métodos opcionais no builder (como `construirGpu()`) podem ser sobrescritos ou ignorados
- Cada builder concreto pode ter sua própria lógica de construção

