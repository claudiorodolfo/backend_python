# Padrão Singleton (Singleton Pattern)

## Descrição

O padrão **Singleton** é um padrão de projeto criacional que garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global para essa instância. Isso é especialmente útil quando você precisa de exatamente um objeto para coordenar ações em todo o sistema, como conexões de banco de dados, gerenciadores de configuração ou pools de recursos.

## Estrutura

O padrão Singleton consiste em:

- **Singleton (Singleton)**: Classe que garante a existência de apenas uma instância
- **Método `__new__`**: Controla a criação de instâncias, retornando sempre a mesma instância
- **Método `getInstancia`**: Fornece acesso controlado à instância única
- **Atributo de classe `_instancia`**: Armazena a referência à única instância criada

## Vantagens

1. **Instância única**: Garante que existe apenas uma instância da classe
2. **Acesso global**: Fornece um ponto de acesso global à instância
3. **Controle de criação**: Controla quando e como a instância é criada
4. **Economia de recursos**: Evita a criação de múltiplas instâncias desnecessárias
5. **Lazy initialization**: Permite criar a instância apenas quando necessário

## Exemplo de Uso

Neste exemplo, a classe `ConectorBD` implementa o padrão Singleton para garantir que exista apenas uma conexão com o banco de dados em toda a aplicação.

### Código

```python
import random

class ConectorBD:
    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, valor=None):
        # Inicializa só uma vez
        if not hasattr(self, "inicializado"):
            self._id = random.randint(1, 1000000)
            print(f"ID da conexão: {self._id}")
            self.inicializado = True

    @classmethod
    def getInstancia(cls, valor=None):
        """Retorna a instância única do Singleton."""
        if cls._instancia is None:
            cls._instancia = cls(valor)
        return cls._instancia
```

### Execução

```python
from singleton import ConectorBD

conector1 = ConectorBD.getInstancia()
conector2 = ConectorBD.getInstancia()

# Ambas as variáveis referenciam a mesma instância
print(conector1 is conector2)  # True
```

## Observações Importantes

- **Método `__new__`**: 
  - É chamado antes de `__init__` e controla a criação do objeto
  - Verifica se já existe uma instância antes de criar uma nova
  - Retorna sempre a mesma instância

- **Flag `inicializado`**: 
  - Previne que `__init__` seja executado múltiplas vezes
  - Garante que a inicialização aconteça apenas na primeira criação

- **Thread Safety**: 
  - A implementação atual não é thread-safe
  - Para uso em ambientes multi-thread, é necessário adicionar locks

- **Método `getInstancia`**: 
  - Fornece uma interface clara para obter a instância
  - Permite lazy initialization (criação sob demanda)

## Quando Usar

- Quando você precisa de exatamente uma instância de uma classe
- Para gerenciadores de recursos compartilhados (banco de dados, cache, logger)
- Quando o controle de acesso global é necessário
- Para objetos que consomem muitos recursos e devem ser compartilhados
- Em configurações ou estados globais da aplicação

## Quando NÃO Usar

- Quando múltiplas instâncias são necessárias
- Em cenários onde o estado global pode causar problemas
- Quando a classe precisa ser testável e mockável facilmente
- Em aplicações multi-thread sem sincronização adequada
- Quando a dependência global dificulta a manutenção do código

## Variações

- **Eager Singleton**: A instância é criada no momento da importação do módulo
- **Lazy Singleton**: A instância é criada apenas quando solicitada (implementação atual)
- **Thread-Safe Singleton**: Utiliza locks para garantir segurança em ambientes multi-thread
- **Double-Checked Locking**: Otimização para reduzir overhead de locks em ambientes thread-safe

