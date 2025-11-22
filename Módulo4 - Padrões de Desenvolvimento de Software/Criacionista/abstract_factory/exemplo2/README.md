# Abstract Factory - Exemplo 2: Fábrica de Animais

Este projeto demonstra o padrão **Abstract Factory** criando animais de diferentes portes (Pequeno, Médio e Grande) e tipos (Cão, Gato e Pato).

## Estrutura do Projeto

```
exemplo2/
├── interfaces/            # Interfaces abstratas
│   ├── __init__.py
│   ├── cao.py            # Interface Cao
│   ├── gato.py           # Interface Gato
│   └── pato.py           # Interface Pato
├── animais/              # Implementações concretas de animais
│   ├── __init__.py
│   ├── pequenos/         # Animais de pequeno porte
│   │   ├── __init__.py
│   │   ├── cao_pequeno.py
│   │   ├── gato_pequeno.py
│   │   └── pato_pequeno.py
│   ├── medios/           # Animais de médio porte
│   │   ├── __init__.py
│   │   ├── cao_medio.py
│   │   ├── gato_medio.py
│   │   └── pato_medio.py
│   └── grandes/          # Animais de grande porte
│       ├── __init__.py
│       ├── cao_grande.py
│       ├── gato_grande.py
│       └── pato_grande.py
├── factories/            # Fábricas abstratas e concretas
│   ├── __init__.py
│   ├── fabrica_animais.py           # Fábrica abstrata
│   ├── fabrica_animais_pequenos.py  # Fábrica para pequenos
│   ├── fabrica_animais_medios.py    # Fábrica para médios
│   └── fabrica_animais_grandes.py   # Fábrica para grandes
├── main.py               # Exemplo de uso
└── README.md             # Este arquivo
```

## Componentes

### Interfaces Abstratas (`interfaces/`)
Cada interface está em seu próprio arquivo:
- `interfaces/cao.py`: Interface `Cao` com métodos `latir()` e `getPorte()`
- `interfaces/gato.py`: Interface `Gato` com métodos `miar()` e `getPorte()`
- `interfaces/pato.py`: Interface `Pato` com métodos `grasnar()` e `getPorte()`

### Implementações Concretas (`animais/`)
Cada classe de animal está em seu próprio arquivo, organizadas por porte:

**Pequeno Porte** (`animais/pequenos/`):
- `cao_pequeno.py`: Classe `CaoPequeno`
- `gato_pequeno.py`: Classe `GatoPequeno`
- `pato_pequeno.py`: Classe `PatoPequeno`

**Médio Porte** (`animais/medios/`):
- `cao_medio.py`: Classe `CaoMedio`
- `gato_medio.py`: Classe `GatoMedio`
- `pato_medio.py`: Classe `PatoMedio`

**Grande Porte** (`animais/grandes/`):
- `cao_grande.py`: Classe `CaoGrande`
- `gato_grande.py`: Classe `GatoGrande`
- `pato_grande.py`: Classe `PatoGrande`

### Fábricas (`factories/`)
Cada fábrica está em seu próprio arquivo:
- `fabrica_animais.py`: Fábrica abstrata `FabricaAnimais` com métodos para criar cada tipo de animal
- `fabrica_animais_pequenos.py`: Fábrica concreta `FabricaAnimaisPequenos`
- `fabrica_animais_medios.py`: Fábrica concreta `FabricaAnimaisMedios`
- `fabrica_animais_grandes.py`: Fábrica concreta `FabricaAnimaisGrandes`

## Como Usar

Execute o arquivo `main.py`:

```bash
python main.py
```

O programa demonstrará a criação de animais de cada porte usando o padrão Abstract Factory.

## Exemplo de Uso Programático

```python
from factories import FabricaAnimaisPequenos, FabricaAnimaisMedios, FabricaAnimaisGrandes

# Criar fábrica de animais pequenos
fabrica = FabricaAnimaisPequenos()

# Criar animais usando a fábrica
cao = fabrica.criar_cao()
gato = fabrica.criar_gato()
pato = fabrica.criar_pato()

# Usar os animais
print(cao.latir())    # "Au au! (latido agudo de cão pequeno)"
print(gato.miar())    # "Miau! (miado agudo de gato pequeno)"
print(pato.grasnar()) # "Quack! (grasnido agudo de pato pequeno)"
```

## Vantagens do Padrão

1. **Consistência**: Garante que todos os animais criados por uma fábrica sejam do mesmo porte
2. **Flexibilidade**: Fácil adicionar novos portes ou tipos de animais
3. **Desacoplamento**: O código cliente não precisa conhecer as classes concretas
4. **Extensibilidade**: Novos tipos de animais ou portes podem ser adicionados sem modificar código existente

