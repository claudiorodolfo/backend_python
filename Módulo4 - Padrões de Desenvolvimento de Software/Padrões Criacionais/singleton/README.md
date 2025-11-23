# Padrão Singleton (Singleton Pattern)

## Descrição

O padrão **Singleton** é um padrão de projeto criacional que garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global para essa instância. Isso é especialmente útil quando você precisa de exatamente um objeto para coordenar ações em todo o sistema, como conexões de banco de dados, gerenciadores de configuração ou pools de recursos.

## Estrutura

O padrão Singleton consiste em:

- **Singleton (Singleton)**: Classe que garante a existência de apenas uma instância
- **Método `__new__`**: Controla a criação de instâncias, retornando sempre a mesma instância
- **Método `getInstancia`**: Fornece acesso controlado à instância única e permite configurá-la
- **Atributo de classe `_instancia`**: Armazena a referência à única instância criada

## Vantagens

1. **Instância única**: Garante que existe apenas uma instância da classe
2. **Acesso global**: Fornece um ponto de acesso global à instância
3. **Controle de criação**: Controla quando e como a instância é criada
4. **Economia de recursos**: Evita a criação de múltiplas instâncias desnecessárias
5. **Lazy initialization**: Permite criar a instância apenas quando necessário

## Exemplo de Uso

Neste exemplo, a classe `BDManager` implementa o padrão Singleton para garantir que exista apenas uma conexão com o banco de dados em toda a aplicação.

### Código

```python
import random

class BDManager:
    _instancia = None  # atributo de classe: armazena a instância única

    def __new__(cls):
        # __new__ é chamado **antes** de __init__, quando Python vai "criar" um objeto
        if cls._instancia is None:
            # Se ainda não existe uma instância, cria uma nova
            cls._instancia = super().__new__(cls)
            # Inicializa atributos "singleton" (só uma vez)
            cls._instancia._path = None
        return cls._instancia  # retorna a instância única

    def getInstancia(self, path):
        # Aqui self já é a instância única
        self._path = path
        # Inicializa só uma vez
        if not hasattr(self, "inicializado"):
            self._id = random.randint(1, 1000000)
            # self.inicializado = True
        return self
```

### Execução

```python
from singleton import BDManager

print("=== Teste do Padrão Singleton ===\n")

# Obtém duas "instâncias"
print("1. Criando primeira instância:")
bd1 = BDManager()
conector1 = bd1.getInstancia("Conexão Principal")
print(f"   Path da conexão 1: {conector1._path}")
print(f"   ID da conexão 1: {conector1._id}")

print("\n2. Criando segunda instância:")
bd2 = BDManager()
conector2 = bd2.getInstancia("Conexão Secundária")
print(f"   Path da conexão 2: {conector2._path}")
print(f"   ID da conexão 2: {conector2._id}")

# Verificações
print("\n=== Verificações ===")
print(f"3. São a mesma instância? {conector1 is conector2}")
print(f"4. Paths são iguais? {conector1._path == conector2._path}")
print(f"5. Mesmo objeto na memória? {id(conector1) == id(conector2)}")

# Teste adicional: modificação em uma reflete na outra
print("\n6. Teste de modificação:")
conector1._path = "Conexão Terciária"
print(f"   conector1._path = '{conector1._path}'")
print(f"   conector1._id = '{conector1._id}'")
print(f"   conector2._path = '{conector2._path}'")
print(f"   conector2._id = '{conector2._id}'")
print(f"   Modificação refletiu? {conector1._path == conector2._path}")

print("\n✅ Singleton está funcionando corretamente!")
```

## Observações Importantes

- **Método `__new__`**: 
  - É chamado antes de `__init__` e controla a criação do objeto
  - Verifica se já existe uma instância antes de criar uma nova
  - Retorna sempre a mesma instância
  - Inicializa atributos básicos da instância única

- **Método `getInstancia`**: 
  - É um método de instância (não mais um método de classe)
  - Recebe um parâmetro `path` para configurar a conexão
  - Permite configurar a instância única após sua criação
  - Garante que atributos como `_id` sejam inicializados apenas uma vez (usando `hasattr` para verificar)
  - Retorna `self` (a própria instância única)

- **Comportamento do Singleton**: 
  - Todas as chamadas a `BDManager()` retornam a mesma instância
  - Modificações em qualquer referência refletem em todas as outras
  - O último `path` configurado via `getInstancia` será o valor atual

- **Thread Safety**: 
  - A implementação atual não é thread-safe
  - Para uso em ambientes multi-thread, é necessário adicionar locks

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

