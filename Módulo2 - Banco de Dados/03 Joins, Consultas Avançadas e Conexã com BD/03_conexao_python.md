# 03 - Conexão Python com Banco de Dados

Este documento apresenta como conectar Python a bancos de dados SQLite usando a biblioteca nativa `sqlite3`.

## 📚 Introdução

A biblioteca **sqlite3** vem incluída no Python e permite trabalhar com bancos de dados SQLite sem instalação adicional.

### O que é SQLite?

SQLite é um banco de dados embarcado que:
- Não requer servidor separado
- Armazena dados em um arquivo único
- É leve e rápido
- Perfeito para desenvolvimento e aplicações pequenas/médias

---

## 🔌 Conceitos Básicos

### Conexão (Connection)

Uma **conexão** representa uma sessão com o banco de dados.

```python
import sqlite3

conn = sqlite3.connect('banco.db')
```

**Métodos importantes:**
- `connect()`: Cria conexão
- `commit()`: Salva mudanças
- `rollback()`: Reverte mudanças
- `close()`: Fecha conexão

### Cursor

Um **cursor** é usado para executar comandos SQL e buscar resultados.

```python
cursor = conn.cursor()
```

**Métodos importantes:**
- `execute()`: Executa um comando SQL
- `executemany()`: Executa múltiplas vezes
- `fetchone()`: Busca um resultado
- `fetchall()`: Busca todos os resultados
- `fetchmany(n)`: Busca n resultados

### Context Manager

Usar `with` garante que a conexão seja fechada automaticamente:

```python
with sqlite3.connect('banco.db') as conn:
    cursor = conn.cursor()
    # Operações aqui
    # Conexão fechada automaticamente
```

---

## 🏗️ Criando Tabelas

### Exemplo Básico

```python
import sqlite3

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE
        )
    ''')
    
    conn.commit()
```

### Criar Múltiplas Tabelas

```python
tabelas = [
    '''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL
    )
    ''',
    '''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    '''
]

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    for tabela in tabelas:
        cursor.execute(tabela)
    conn.commit()
```

---

## ➕ Inserção de Dados

### Inserção Individual

```python
cursor.execute('''
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
''', ('João Silva', 'joao@email.com'))

conn.commit()
```

**⚠️ Importante**: Use `?` (placeholders) para evitar SQL injection!

### Inserção Múltipla

```python
clientes = [
    ('Maria Santos', 'maria@email.com'),
    ('Pedro Costa', 'pedro@email.com'),
    ('Ana Oliveira', 'ana@email.com'),
]

cursor.executemany('''
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
''', clientes)

conn.commit()
```

### Obter ID do Último Registro Inserido

```python
cursor.execute('''
    INSERT INTO clientes (nome, email)
    VALUES (?, ?)
''', ('João Silva', 'joao@email.com'))

cliente_id = cursor.lastrowid
print(f"Cliente inserido com ID: {cliente_id}")
```

---

## 🔍 Consultas de Dados

### Buscar Todos os Resultados

```python
cursor.execute('SELECT * FROM clientes')
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)
```

### Buscar Um Resultado

```python
cursor.execute('SELECT * FROM clientes WHERE id = ?', (1,))
cliente = cursor.fetchone()

if cliente:
    print(cliente)
else:
    print("Cliente não encontrado")
```

### Buscar Vários Resultados

```python
cursor.execute('SELECT * FROM clientes WHERE idade > ?', (25,))
clientes = cursor.fetchmany(5)  # Próximos 5 resultados

for cliente in clientes:
    print(cliente)
```

### Iterar sobre Resultados (Eficiente)

```python
cursor.execute('SELECT * FROM clientes')
for row in cursor:
    print(row)
```

---

## 🔗 JOINs em Python

### INNER JOIN

```python
cursor.execute('''
    SELECT 
        c.nome,
        p.id AS pedido_id,
        p.valor_total
    FROM clientes c
    INNER JOIN pedidos p ON c.id = p.cliente_id
''')

resultados = cursor.fetchall()
for row in resultados:
    print(f"{row[0]}: Pedido {row[1]} - R$ {row[2]}")
```

### LEFT JOIN

```python
cursor.execute('''
    SELECT 
        c.nome,
        p.id AS pedido_id
    FROM clientes c
    LEFT JOIN pedidos p ON c.id = p.cliente_id
''')

resultados = cursor.fetchall()
for row in resultados:
    pedido = row[1] if row[1] else 'Sem pedidos'
    print(f"{row[0]}: {pedido}")
```

---

## 📊 Agregações (GROUP BY)

```python
cursor.execute('''
    SELECT 
        cidade,
        COUNT(*) AS total
    FROM clientes
    GROUP BY cidade
''')

resultados = cursor.fetchall()
for row in resultados:
    print(f"{row[0]}: {row[1]} clientes")
```

---

## ✏️ Atualização e Remoção

### UPDATE

```python
cursor.execute('''
    UPDATE clientes
    SET nome = ?
    WHERE id = ?
''', ('João Silva Santos', 1))

conn.commit()
print(f"Registros atualizados: {cursor.rowcount}")
```

### DELETE

```python
cursor.execute('DELETE FROM clientes WHERE id = ?', (1,))
conn.commit()
print(f"Registros removidos: {cursor.rowcount}")
```

---

## 🛡️ Transações

### Commit e Rollback

```python
try:
    cursor.execute('INSERT INTO clientes (nome) VALUES (?)', ('Teste',))
    cursor.execute('UPDATE clientes SET nome = ? WHERE id = ?', ('Novo Nome', 1))
    conn.commit()
    print("Operações concluídas com sucesso!")
except Exception as e:
    conn.rollback()
    print(f"Erro: {e}. Mudanças revertidas.")
```

### Context Manager para Transações

```python
from contextlib import contextmanager

@contextmanager
def transaction(conn):
    try:
        yield
        conn.commit()
    except Exception:
        conn.rollback()
        raise

with sqlite3.connect('exemplo.db') as conn:
    cursor = conn.cursor()
    with transaction(conn):
        cursor.execute('INSERT INTO clientes (nome) VALUES (?)', ('Teste',))
        # Se algo der errado, rollback automático
```

---

## 🎨 Row Factory

**Row Factory** permite acessar colunas por nome em vez de índice.

### Sem Row Factory (acesso por índice)

```python
cursor.execute('SELECT * FROM clientes WHERE id = ?', (1,))
row = cursor.fetchone()
print(row[0])  # ID
print(row[1])  # Nome
```

### Com Row Factory (acesso por nome)

```python
conn.row_factory = sqlite3.Row

cursor = conn.cursor()
cursor.execute('SELECT * FROM clientes WHERE id = ?', (1,))
row = cursor.fetchone()

print(row['id'])
print(row['nome'])
# Ou ainda por índice
print(row[0])
```

---

## 🔒 Segurança: Prepared Statements

**Sempre use placeholders (`?`)** para evitar SQL injection!

### ❌ ERRADO (Vulnerável a SQL Injection)

```python
nome = "João'; DROP TABLE clientes; --"
query = f"SELECT * FROM clientes WHERE nome = '{nome}'"
cursor.execute(query)  # PERIGOSO!
```

### ✅ CORRETO (Seguro)

```python
nome = "João'; DROP TABLE clientes; --"
cursor.execute('SELECT * FROM clientes WHERE nome = ?', (nome,))  # SEGURO!
```

**O SQLite trata o valor como dado, não como código SQL.**

---

## 🎯 Exemplo Completo

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_connection(db_file):
    """Context manager para gerenciar conexões."""
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row  # Permite acesso por nome
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def criar_banco():
    """Cria o banco de dados."""
    with get_connection('exemplo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE
            )
        ''')

def inserir_cliente(nome, email):
    """Insere um novo cliente."""
    with get_connection('exemplo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO clientes (nome, email)
            VALUES (?, ?)
        ''', (nome, email))
        return cursor.lastrowid

def listar_clientes():
    """Lista todos os clientes."""
    with get_connection('exemplo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        return cursor.fetchall()

# Uso
if __name__ == '__main__':
    criar_banco()
    inserir_cliente('João Silva', 'joao@email.com')
    clientes = listar_clientes()
    for cliente in clientes:
        print(f"{cliente['nome']}: {cliente['email']}")
```

---

## 📋 Boas Práticas

1. ✅ **Use context managers** (`with`) para garantir fechamento
2. ✅ **Use prepared statements** (`?`) para segurança
3. ✅ **Use row_factory** para acesso por nome
4. ✅ **Trate exceções** adequadamente
5. ✅ **Use transações** para operações críticas
6. ✅ **Feche conexões** quando não usar context manager
7. ✅ **Valide dados** antes de inserir/atualizar
8. ✅ **Use commit** apenas quando necessário

---

## ⚠️ Erros Comuns

### Erro 1: Esquecer commit

```python
cursor.execute('INSERT INTO clientes (nome) VALUES (?)', ('João',))
# Faltou conn.commit() - mudanças não foram salvas!
```

### Erro 2: SQL Injection

```python
nome = input("Nome: ")
cursor.execute(f"SELECT * FROM clientes WHERE nome = '{nome}'")  # PERIGOSO!
```

### Erro 3: Não fechar conexão

```python
conn = sqlite3.connect('exemplo.db')
# ... operações ...
# Esqueceu conn.close() - conexão permanece aberta!
```

### Erro 4: Usar fetchone() múltiplas vezes incorretamente

```python
cursor.execute('SELECT * FROM clientes')
primeiro = cursor.fetchone()
segundo = cursor.fetchone()  # Pega o próximo, não o mesmo!
```

---

## 🚀 Próximos Passos

Depois de dominar SQLite com Python, você pode:
- Trabalhar com ORMs (SQLAlchemy, Django ORM)
- Conectar a outros bancos (MySQL, PostgreSQL)
- Criar APIs que interagem com bancos de dados
- Construir aplicações web completas

---

Dominar conexão Python com bancos de dados abre muitas possibilidades! 🎯

