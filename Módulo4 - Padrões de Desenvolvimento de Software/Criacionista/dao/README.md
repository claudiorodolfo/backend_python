# DAO (Data Access Object)

O padrão DAO é um padrão estrutural que abstrai o acesso a dados, separando a lógica de negócio da lógica de persistência.

## 📚 Conceito

O **Data Access Object (DAO)** é um padrão que fornece uma interface abstrata para acessar dados de uma fonte de dados (banco de dados, arquivo, API, etc.). Ele encapsula toda a lógica de acesso a dados e fornece uma interface mais simples para o restante da aplicação.

### Componentes do Padrão DAO

1. **Model/Entity**: Representa a entidade de negócio (ex: `Usuario`)
2. **DAO Interface**: Define o contrato com os métodos de acesso a dados
3. **DAO Concreto**: Implementa a interface com acesso real ao banco de dados
4. **Service Layer**: Usa o DAO para implementar lógica de negócio

### Benefícios

- ✅ **Separação de responsabilidades**: Lógica de negócio separada da persistência
- ✅ **Testabilidade**: Fácil criar mocks do DAO para testes
- ✅ **Flexibilidade**: Permite trocar implementação de persistência facilmente
- ✅ **Manutenibilidade**: Código mais organizado e fácil de entender
- ✅ **Reutilização**: DAO pode ser reutilizado em diferentes partes da aplicação

## 📁 Estrutura dos Arquivos

```
dao/
├── dao.py          # Implementação completa do padrão DAO
├── run.py          # Exemplo prático de uso
└── README.md       # Esta documentação
```

## 🔍 Como Funciona

### 1. Model/Entity (`Usuario`)

Representa a entidade de negócio:

```python
class Usuario:
    def __init__(self, id=None, nome="", email=""):
        self.id = id
        self.nome = nome
        self.email = email
```

### 2. DAO Interface (`UsuarioDAO`)

Define o contrato com métodos abstratos:

```python
class UsuarioDAO(ABC):
    @abstractmethod
    def criar(self, usuario: Usuario) -> Usuario:
        pass
    
    @abstractmethod
    def buscar_por_id(self, id: int) -> Optional[Usuario]:
        pass
    
    # ... outros métodos
```

### 3. DAO Concreto (`UsuarioDAOSQLite`)

Implementa a interface com acesso real ao banco:

```python
class UsuarioDAOSQLite(UsuarioDAO):
    def criar(self, usuario: Usuario) -> Usuario:
        # Implementação com SQLite
        pass
```

### 4. DAO Mock (`UsuarioDAOMock`)

Implementação em memória para testes:

```python
class UsuarioDAOMock(UsuarioDAO):
    def __init__(self):
        self._usuarios = {}
    
    def criar(self, usuario: Usuario) -> Usuario:
        # Implementação em memória
        pass
```

### 5. Service Layer (`UsuarioService`)

Usa o DAO para implementar lógica de negócio:

```python
class UsuarioService:
    def __init__(self, dao: UsuarioDAO):
        self.dao = dao
    
    def cadastrar_usuario(self, nome: str, email: str) -> Usuario:
        # Validações de negócio
        if not nome or not email:
            raise ValueError("Nome e email são obrigatórios")
        
        # Usa o DAO para persistir
        usuario = Usuario(nome=nome, email=email)
        return self.dao.criar(usuario)
```

## 🚀 Como Usar

### Exemplo Básico

```python
from dao import UsuarioDAOSQLite, UsuarioService

# Criar DAO e Service
dao = UsuarioDAOSQLite("usuarios.db")
service = UsuarioService(dao)

# Criar usuário
usuario = service.cadastrar_usuario("João", "joao@email.com")

# Buscar usuário
usuario_encontrado = service.obter_usuario(usuario.id)

# Listar todos
usuarios = service.listar_usuarios()
```

### Para Testes (usando Mock)

```python
from dao import UsuarioDAOMock, UsuarioService

# Usar mock para testes
dao = UsuarioDAOMock()
service = UsuarioService(dao)

# Testar sem banco de dados real
usuario = service.cadastrar_usuario("Teste", "teste@email.com")
```

## 🎯 Quando Usar

Use o padrão DAO quando:

- ✅ Precisa separar lógica de negócio de acesso a dados
- ✅ Quer facilitar testes unitários (mock do DAO)
- ✅ Pode precisar trocar a fonte de dados no futuro
- ✅ Tem múltiplas entidades que precisam de acesso a dados
- ✅ Quer centralizar operações de CRUD

## ⚠️ Quando NÃO Usar

Evite o padrão DAO quando:

- ❌ A aplicação é muito simples e não justifica a abstração
- ❌ Você está usando um ORM completo (como SQLAlchemy, Django ORM)
- ❌ Não há necessidade de trocar a fonte de dados
- ❌ A lógica de acesso a dados é trivial

## 🔗 Relação com Outros Padrões

- **Repository Pattern**: Similar ao DAO, mas mais abstrato. Repository pode agregar múltiplos DAOs
- **Service Layer**: Usa o DAO para implementar lógica de negócio
- **Factory Method**: Pode ser usado para criar diferentes implementações de DAO
- **Singleton**: Pode ser usado para garantir uma única instância de conexão com banco

## 📖 Executando os Exemplos

### Executar exemplo completo:

```bash
python3 dao.py
```

### Executar exemplo prático:

```bash
python3 run.py
```

## 💡 Boas Práticas

1. **Use interfaces abstratas**: Facilita criar mocks e trocar implementações
2. **Trate exceções**: Implemente tratamento de erros adequado
3. **Use context managers**: Para gerenciar conexões com banco de dados
4. **Validações no Service**: Mantenha validações de negócio no Service, não no DAO
5. **Documentação**: Documente métodos e parâmetros do DAO

## 🔄 Próximos Passos

Depois de entender o DAO, explore:

- **Repository Pattern**: Padrão mais abstrato que pode usar DAOs
- **Unit of Work**: Para gerenciar transações
- **Active Record**: Padrão alternativo onde o modelo contém a lógica de acesso

