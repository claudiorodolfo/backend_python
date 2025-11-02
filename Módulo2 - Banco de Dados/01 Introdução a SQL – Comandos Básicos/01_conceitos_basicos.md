# 01 - Conceitos Básicos de Banco de Dados
## Módulo 01 - Introdução a SQL – Comandos Básicos

Este documento apresenta os conceitos fundamentais de bancos de dados relacionais.

## 📚 O que é um Banco de Dados?

Um **banco de dados** é uma coleção organizada e estruturada de dados que pode ser facilmente armazenada, gerenciada, atualizada e consultada. Em essência, é um sistema eletrônico que permite armazenar grandes volumes de informações de forma organizada.

### Características Principais

1. **Persistência**: Os dados são mantidos mesmo quando o sistema é desligado
2. **Organização**: Dados estruturados de forma lógica e consistente
3. **Eficiência**: Acesso rápido e eficiente aos dados
4. **Integridade**: Regras que garantem a consistência e confiabilidade dos dados
5. **Segurança**: Controle de acesso e proteção dos dados
6. **Concorrência**: Múltiplos usuários podem acessar simultaneamente
7. **Backup e Recuperação**: Capacidade de fazer backup e restaurar dados

### Exemplos de Uso

- **Sistemas de E-commerce**: Produtos, clientes, pedidos, estoque
- **Redes Sociais**: Usuários, posts, comentários, curtidas
- **Sistemas Bancários**: Contas, transações, clientes
- **Hospitais**: Pacientes, médicos, consultas, exames
- **Escolas**: Alunos, professores, disciplinas, notas

---

## 🔄 Banco de Dados Relacional vs Não Relacional

### Banco de Dados Relacional (SQL)

**Características:**
- Dados organizados em **tabelas** (relações)
- Cada tabela contém **linhas** (registros) e **colunas** (atributos)
- Relacionamentos entre tabelas através de **chaves**
- Usa **SQL (Structured Query Language)** para manipulação
- Garante **integridade referencial** e **normalização**
- Esquema **rigoroso** e **estruturado**

**Estrutura:**
```
┌─────────────┬──────────────┬─────────────┐
│ id_cliente  │ nome         │ email       │
├─────────────┼──────────────┼─────────────┤
│ 1           │ João         │ joao@...    │
│ 2           │ Maria        │ maria@...   │
└─────────────┴──────────────┴─────────────┘
```

**Vantagens:**
- ✅ Estrutura organizada e previsível
- ✅ Integridade de dados garantida
- ✅ Consultas complexas facilitadas (JOINs)
- ✅ Padrão consolidado (SQL)
- ✅ Transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade)

**Desvantagens:**
- ❌ Pode ser menos flexível para dados não estruturados
- ❌ Pode ter dificuldades de escalabilidade horizontal
- ❌ Esquema fixo pode ser limitante

**Quando usar:**
- Aplicações tradicionais (CRUD)
- Dados estruturados e bem definidos
- Integridade de dados crítica
- Relacionamentos complexos entre dados

**Exemplos:** MySQL, PostgreSQL, SQLite, Oracle, SQL Server

---

### Banco de Dados Não Relacional (NoSQL)

**Características:**
- Dados em formatos flexíveis (documentos, chave-valor, grafos, colunas)
- **Sem esquema fixo** (schema-less)
- Pode ser mais rápido para casos específicos
- **Alta escalabilidade horizontal**
- Consultas podem ser diferentes (não sempre SQL)

**Tipos principais:**

1. **Documentos** (MongoDB): Dados em formato JSON/BSON
   ```json
   {
     "id": 1,
     "nome": "João",
     "enderecos": [
       {"tipo": "casa", "rua": "Rua A"},
       {"tipo": "trabalho", "rua": "Rua B"}
     ]
   }
   ```

2. **Chave-Valor** (Redis): Armazena pares chave-valor simples
   ```
   chave: "usuario:123"
   valor: "João Silva"
   ```

3. **Grafos** (Neo4j): Focado em relacionamentos
   ```
   (Pessoa)-[:AMIGO]->(Pessoa)
   ```

4. **Colunas** (Cassandra): Dados organizados por colunas

**Vantagens:**
- ✅ Alta flexibilidade (schema-less)
- ✅ Escalabilidade horizontal
- ✅ Performance para casos específicos
- ✅ Bom para big data
- ✅ Suporta dados não estruturados

**Desvantagens:**
- ❌ Menos garantias de integridade
- ❌ Consultas complexas podem ser mais difíceis
- ❌ Padrões menos consolidados
- ❌ Pode haver inconsistências temporárias

**Quando usar:**
- Big data e análise de dados
- Dados não estruturados ou semi-estruturados
- Alta necessidade de escalabilidade
- Aplicações que precisam de performance extrema
- Dados que mudam frequentemente de estrutura

**Exemplos:** MongoDB, Redis, Cassandra, Neo4j, DynamoDB

---

## 🏗️ Conceitos Básicos de Tabelas

### Tabela (Table)

Uma **tabela** é uma estrutura bidimensional que organiza dados em linhas e colunas. É a unidade fundamental de armazenamento em bancos relacionais.

**Analogia**: Pense em uma planilha do Excel, onde:
- Cada **coluna** representa um tipo de informação (nome, idade, email)
- Cada **linha** representa um registro completo

**Exemplo de tabela `clientes`:**
```
┌────┬──────────────┬───────────────────┬───────┬──────────────┐
│ id │ nome         │ email             │ idade │ cidade       │
├────┼──────────────┼───────────────────┼───────┼──────────────┤
│ 1  │ João Silva   │ joao@email.com    │ 25    │ São Paulo    │
│ 2  │ Maria Santos │ maria@email.com   │ 30    │ Rio de Janeiro│
│ 3  │ Pedro Costa  │ pedro@email.com   │ 22    │ Belo Horizonte│
└────┴──────────────┴───────────────────┴───────┴──────────────┘
```

### Linha (Row/Record/Tupla)

Uma **linha** representa um registro completo na tabela. Cada linha contém dados relacionados a uma entidade específica (um cliente, um produto, etc.).

**Características:**
- Cada linha é única (pelo menos teoricamente)
- Representa uma instância de uma entidade
- Contém valores para cada coluna (ou NULL)

**Exemplo:** A linha com id=1 representa o cliente "João Silva"

### Coluna (Column/Field/Attribute)

Uma **coluna** define um tipo específico de informação armazenada na tabela.

**Características:**
- Tem um **nome** único na tabela
- Tem um **tipo de dados** (INTEGER, VARCHAR, DATE, etc.)
- Pode ter **restrições** (NOT NULL, UNIQUE, etc.)

**Exemplo:** A coluna `nome` armazena o nome de cada cliente

**Tipos de dados comuns:**
- `INTEGER`: Números inteiros
- `VARCHAR(n)`: Texto com tamanho máximo
- `DECIMAL(p,s)`: Números decimais
- `DATE`: Data
- `BOOLEAN`: Verdadeiro/Falso
- `BLOB`: Dados binários

---

## 🔑 Chaves Primárias e Estrangeiras

### Chave Primária (Primary Key - PK)

A **chave primária** é um campo (ou conjunto de campos) que identifica **unicamente** cada registro em uma tabela.

**Características:**
- ✅ Deve ser **única** (não pode haver duplicatas)
- ✅ Não pode ser **NULL** (obrigatória)
- ✅ Uma tabela pode ter apenas **uma** chave primária
- ✅ Pode ser simples (um campo) ou composta (múltiplos campos)
- ✅ Geralmente é um campo numérico auto-incremento (ID)

**Exemplo:**
```sql
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100)
);
```

Neste exemplo, `id` é a chave primária. Cada cliente terá um ID único: 1, 2, 3, etc.

**Por que usar?**
- Identificação única de registros
- Base para relacionamentos com outras tabelas
- Performance (índices automáticos)
- Integridade dos dados

### Chave Estrangeira (Foreign Key - FK)

A **chave estrangeira** é um campo em uma tabela que referencia a chave primária de outra tabela, estabelecendo um relacionamento entre as tabelas.

**Características:**
- ✅ Mantém a **integridade referencial**
- ✅ Previne inserção de registros órfãos
- ✅ Permite consultas com JOIN entre tabelas
- ✅ Pode ser NULL (se o relacionamento for opcional)
- ✅ Pode ter o mesmo nome da chave primária ou diferente

**Exemplo:**
```sql
-- Tabela clientes
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100)
);

-- Tabela pedidos (referencia clientes)
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    valor DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

Neste exemplo:
- `clientes.id` é a chave primária
- `pedidos.cliente_id` é a chave estrangeira que referencia `clientes.id`

**Benefícios:**
- Garante que só existam pedidos de clientes válidos
- Previne exclusão acidental de clientes com pedidos
- Facilita consultas que combinam dados de múltiplas tabelas

**Tipos de relacionamento:**
- **1:1** (Um para Um): Um registro de A se relaciona com um de B
- **1:N** (Um para Muitos): Um registro de A se relaciona com muitos de B
- **N:N** (Muitos para Muitos): Muitos de A se relacionam com muitos de B (requer tabela intermediária)

---

## 📊 Modelo Entidade-Relacionamento (ER)

O **Modelo Entidade-Relacionamento (ER)** é uma representação gráfica e conceitual dos dados e seus relacionamentos. É usado na fase de modelagem de banco de dados.

### Componentes do Modelo ER

#### 1. Entidade (Entity)

Uma **entidade** representa uma "coisa" do mundo real que pode ser identificada e possui características (atributos).

**Exemplos:**
- Cliente
- Produto
- Pedido
- Funcionário

**Representação gráfica:**
```
┌─────────┐
│ Cliente │
└─────────┘
```

#### 2. Atributo (Attribute)

Um **atributo** é uma propriedade ou característica de uma entidade.

**Tipos:**
- **Simples**: Não pode ser dividido (ex: idade)
- **Composto**: Pode ser dividido (ex: endereço → rua, cidade, CEP)
- **Chave**: Identifica unicamente a entidade (ex: id)
- **Derivado**: Pode ser calculado (ex: idade a partir de data_nascimento)

**Exemplo de entidade Cliente com atributos:**
```
┌─────────┐
│ Cliente │
├─────────┤
│ id (PK) │
│ nome    │
│ email   │
│ idade   │
└─────────┘
```

#### 3. Relacionamento (Relationship)

Um **relacionamento** é uma associação entre duas ou mais entidades.

**Tipos:**

**1:1 (Um para Um)**
```
┌─────────┐     1    1    ┌──────────┐
│ Pessoa │─────possui────│ Passaporte│
└─────────┘               └──────────┘
```
Cada pessoa tem um passaporte, cada passaporte pertence a uma pessoa.

**1:N (Um para Muitos)**
```
┌─────────┐     1    N    ┌──────────┐
│ Cliente │─────faz───────│ Pedido   │
└─────────┘               └──────────┘
```
Um cliente pode fazer muitos pedidos, mas cada pedido pertence a um cliente.

**N:N (Muitos para Muitos)**
```
┌─────────┐     N    N    ┌──────────┐
│ Aluno   │─────cursa─────│ Disciplina│
└─────────┘               └──────────┘
```
Um aluno cursa muitas disciplinas, uma disciplina é cursada por muitos alunos.

*Nota: N:N geralmente requer uma tabela intermediária no banco físico.*

---

## 🗄️ Sistema Gerenciador de Banco de Dados (SGBD)

Um **Sistema Gerenciador de Banco de Dados (SGBD)** ou **Database Management System (DBMS)** é um software que gerencia bancos de dados, permitindo criar, modificar, consultar e gerenciar dados.

### Funções Principais

1. **Gerenciamento de Dados**
   - Criar, ler, atualizar e deletar dados (CRUD)
   - Gerenciar estrutura de tabelas

2. **Controle de Acesso e Segurança**
   - Autenticação de usuários
   - Controle de permissões
   - Criptografia de dados

3. **Garantia de Integridade**
   - Validação de dados
   - Constraints (restrições)
   - Integridade referencial

4. **Gerenciamento de Transações**
   - Garantir operações atômicas
   - Controle de concorrência
   - Rollback e commit

5. **Otimização de Consultas**
   - Otimizador de queries
   - Índices para performance
   - Cache de consultas

6. **Backup e Recuperação**
   - Criação de backups
   - Restauração de dados
   - Recuperação de falhas

### Arquitetura

```
┌─────────────┐
│ Aplicação   │
│  (Python)   │
└──────┬──────┘
       │
       │ SQL
       │
┌──────▼──────┐
│    SGBD     │
│  (MySQL,    │
│  PostgreSQL)│
└──────┬──────┘
       │
       │ Armazena
       │
┌──────▼──────┐
│    Disco    │
│  (Arquivos) │
└─────────────┘
```

---

## 🛠️ SGBDs Populares

### SQLite

**Características:**
- ✅ **Embarcado**: Banco de dados em arquivo único
- ✅ **Zero configuração**: Não precisa de servidor
- ✅ **Leve**: Pouco uso de recursos
- ✅ **Incluído no Python**: Biblioteca `sqlite3` padrão
- ✅ **Transações ACID**: Garante integridade
- ✅ **Sem rede**: Banco local apenas

**Quando usar:**
- Desenvolvimento e prototipagem
- Aplicações desktop
- Testes automatizados
- Aplicações pequenas/médias
- Sistemas embarcados
- Cache local

**Limitações:**
- Concorrência limitada (escrita única)
- Sem usuários/permissões
- Escalabilidade limitada

**Exemplo de uso:**
```python
import sqlite3

conn = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM clientes')
```

---

### MySQL

**Características:**
- ✅ **Servidor**: Arquitetura cliente-servidor
- ✅ **Popular**: Um dos mais usados no mundo
- ✅ **Performance**: Alta velocidade de consultas
- ✅ **Escalável**: Suporta grandes volumes
- ✅ **Open Source**: Versão community gratuita
- ✅ **Ampla comunidade**: Muito suporte disponível

**Quando usar:**
- Aplicações web de médio/grande porte
- Sistemas que precisam de alta disponibilidade
- Ambientes onde MySQL já está estabelecido
- Aplicações LAMP/LNMP (Linux, Apache/Nginx, MySQL, PHP/Python)

**Recursos:**
- Porta padrão: 3306
- Múltiplos engines (InnoDB, MyISAM)
- Replicação e cluster
- Triggers e stored procedures

**Exemplo de conexão:**
```python
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='meu_banco'
)
```

---

### PostgreSQL

**Características:**
- ✅ **Robusto**: Alta confiabilidade
- ✅ **Padrão SQL**: Excelente conformidade
- ✅ **Recursos avançados**: JSON, arrays, full-text search
- ✅ **Tipos de dados**: Sistema extensível de tipos
- ✅ **ACID completo**: Garantias fortes
- ✅ **Open Source**: Gratuito e open source

**Quando usar:**
- Aplicações enterprise
- Sistemas que exigem conformidade com padrões
- Aplicações com dados complexos
- Quando precisa de recursos avançados (JSON, arrays)
- Sistemas com relacionamentos complexos

**Recursos:**
- Porta padrão: 5432
- Suporte a JSON nativo
- Arrays e tipos compostos
- Full-text search integrado
- Extensões (PostGIS, pg_trgm, etc.)

**Exemplo de conexão:**
```python
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='meu_banco'
)
```

---

### Comparação Rápida

| Aspecto | SQLite | MySQL | PostgreSQL |
|---------|--------|-------|------------|
| **Instalação** | Incluído no Python | Requer servidor | Requer servidor |
| **Tipo** | Arquivo único | Cliente-servidor | Cliente-servidor |
| **Concorrência** | Limitada | Alta | Muito alta |
| **Escalabilidade** | Pequena/Média | Média/Grande | Grande/Enterprise |
| **Uso típico** | Dev/Testes | Apps web | Enterprise |
| **Facilidade** | Muito fácil | Moderada | Moderada |

---

## 📝 Resumo

Neste módulo você aprendeu:
- ✅ O que é um banco de dados e suas características
- ✅ Diferenças entre bancos relacionais e não relacionais
- ✅ Conceitos de tabelas, linhas, colunas
- ✅ Chaves primárias e estrangeiras
- ✅ Modelo Entidade-Relacionamento
- ✅ SGBDs e suas funções
- ✅ Principais SGBDs: SQLite, MySQL, PostgreSQL

No próximo módulo, você aprenderá a usar comandos SELECT, INSERT e outras operações básicas com SQL!

