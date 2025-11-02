# 01 - Introdução a SQL – Comandos Básicos

Este módulo apresenta os conceitos fundamentais de bancos de dados relacionais e os comandos SQL básicos para trabalhar com dados.

## 📚 Conteúdo

### O que é um Banco de Dados

Um **banco de dados** é uma coleção organizada de dados estruturados, armazenados e acessados eletronicamente. Os bancos de dados permitem armazenar, gerenciar, recuperar e manipular informações de forma eficiente.

**Características principais:**
- **Persistência**: Dados são mantidos mesmo após o fechamento do sistema
- **Organização**: Dados estruturados em tabelas e relacionamentos
- **Integridade**: Regras que garantem a consistência dos dados
- **Concorrência**: Múltiplos usuários podem acessar simultaneamente
- **Segurança**: Controle de acesso e permissões

### Diferença entre Banco de Dados Relacional e Não Relacional

#### Banco de Dados Relacional
- Dados organizados em **tabelas** (linhas e colunas)
- Relacionamentos entre tabelas através de **chaves**
- Usa **SQL (Structured Query Language)** para consultas
- Garante **integridade referencial**
- Exemplos: MySQL, PostgreSQL, SQLite, Oracle, SQL Server

**Vantagens:**
- Estrutura organizada e previsível
- Integridade de dados garantida
- Consultas complexas facilitadas
- Padrão consolidado (SQL)

#### Banco de Dados Não Relacional (NoSQL)
- Dados organizados em formatos diferentes (documentos, chave-valor, grafos)
- Mais flexível na estrutura de dados
- Pode ser mais rápido para casos específicos
- Exemplos: MongoDB, Redis, Cassandra, Neo4j

**Quando usar cada um:**
- **Relacional**: Aplicações tradicionais, dados estruturados, integridade crítica
- **NoSQL**: Big data, dados não estruturados, alta escalabilidade horizontal

### Conceitos Básicos

#### Tabela
Uma **tabela** é uma estrutura bidimensional que organiza dados em linhas (registros) e colunas (campos).

```
┌────────────┬─────────────┬──────────┐
│ id         │ nome        │ idade    │
├────────────┼─────────────┼──────────┤
│ 1          │ João        │ 25       │
│ 2          │ Maria       │ 30       │
│ 3          │ Pedro       │ 22       │
└────────────┴─────────────┴──────────┘
```

#### Linha (Registro/Tupla)
Uma **linha** representa um registro completo na tabela. Cada linha contém dados relacionados a uma entidade específica.

#### Coluna (Campo/Atributo)
Uma **coluna** define um tipo específico de informação armazenada. Cada coluna tem um nome e um tipo de dados (INTEGER, VARCHAR, DATE, etc.).

#### Chave Primária (Primary Key)
A **chave primária** é um campo (ou conjunto de campos) que identifica unicamente cada registro em uma tabela.

**Características:**
- Deve ser **única** (não pode haver duplicatas)
- Não pode ser **NULL** (obrigatória)
- Uma tabela pode ter apenas **uma** chave primária

Exemplo: Em uma tabela de alunos, o campo `id` pode ser a chave primária.

#### Chave Estrangeira (Foreign Key)
A **chave estrangeira** é um campo que referencia a chave primária de outra tabela, estabelecendo um relacionamento entre tabelas.

**Características:**
- Mantém a **integridade referencial**
- Previne inserção de registros órfãos
- Permite consultas com JOIN

Exemplo: Em uma tabela de `pedidos`, o campo `cliente_id` pode ser uma chave estrangeira que referencia a tabela `clientes`.

### Modelo Entidade-Relacionamento (ER)

O **Modelo Entidade-Relacionamento** é uma representação gráfica e conceitual dos dados e seus relacionamentos.

**Componentes:**
- **Entidade**: Representa uma "coisa" do mundo real (ex: Cliente, Produto)
- **Atributo**: Propriedades de uma entidade (ex: nome, email)
- **Relacionamento**: Coneção entre entidades (ex: Cliente faz Pedido)

**Tipos de relacionamento:**
- **1:1** (Um para Um): Um registro de uma tabela se relaciona com um registro de outra
- **1:N** (Um para Muitos): Um registro se relaciona com muitos registros
- **N:N** (Muitos para Muitos): Muitos registros se relacionam com muitos registros

### Sistema Gerenciador de Banco de Dados (SGBD)

Um **SGBD** é um software que gerencia bancos de dados, permitindo criar, modificar e consultar dados.

**Funções principais:**
- Gerenciamento de dados (CRUD)
- Controle de acesso e segurança
- Garantia de integridade
- Gerenciamento de transações
- Otimização de consultas
- Backup e recuperação

### SGBDs Populares

#### SQLite
- **Tipo**: Banco embutido (arquivo único)
- **Características**: Leve, sem servidor, zero configuração
- **Uso**: Desenvolvimento, protótipos, aplicações pequenas
- **Incluído**: Por padrão no Python (`sqlite3`)

#### MySQL
- **Tipo**: Servidor cliente-servidor
- **Características**: Popular, performático, amplamente usado
- **Uso**: Aplicações web de médio/grande porte
- **Porta padrão**: 3306

#### PostgreSQL
- **Tipo**: Servidor cliente-servidor
- **Características**: Robusto, padrão SQL, recursos avançados
- **Uso**: Aplicações enterprise, sistemas complexos
- **Porta padrão**: 5432

## 📖 Comandos SQL Básicos

### SELECT - Seleção de Dados

O comando **SELECT** é usado para consultar dados de uma tabela.

#### Sintaxe Básica
```sql
SELECT coluna1, coluna2, ...
FROM nome_da_tabela;
```

#### Selecionar Todas as Colunas
```sql
SELECT * FROM clientes;
```

#### Selecionar Colunas Específicas
```sql
SELECT nome, email FROM clientes;
```

### Filtros com WHERE

A cláusula **WHERE** filtra registros baseado em condições.

```sql
SELECT * FROM clientes
WHERE idade > 25;
```

**Operadores comuns:**
- `=` (igual)
- `!=` ou `<>` (diferente)
- `>` (maior que)
- `<` (menor que)
- `>=` (maior ou igual)
- `<=` (menor ou igual)
- `LIKE` (padrão de texto)
- `IN` (valores em lista)
- `AND`, `OR`, `NOT` (lógicos)

**Exemplos:**
```sql
-- Idade maior que 25
SELECT * FROM clientes WHERE idade > 25;

-- Nome que começa com 'J'
SELECT * FROM clientes WHERE nome LIKE 'J%';

-- Idade entre 20 e 30
SELECT * FROM clientes WHERE idade >= 20 AND idade <= 30;

-- Nome em uma lista
SELECT * FROM clientes WHERE nome IN ('João', 'Maria');
```

### ORDER BY - Ordenação

A cláusula **ORDER BY** ordena os resultados.

```sql
SELECT * FROM clientes
ORDER BY nome ASC;  -- ASC (crescente) é o padrão
```

```sql
SELECT * FROM clientes
ORDER BY idade DESC;  -- DESC (decrescente)
```

**Ordenação por múltiplas colunas:**
```sql
SELECT * FROM clientes
ORDER BY cidade ASC, nome ASC;
```

### LIMIT - Limitar Resultados

A cláusula **LIMIT** limita o número de registros retornados.

```sql
SELECT * FROM clientes
LIMIT 10;
```

```sql
-- Pular os primeiros 5 registros e mostrar os próximos 10
SELECT * FROM clientes
LIMIT 10 OFFSET 5;
```

### INSERT INTO - Inserção de Dados

O comando **INSERT INTO** adiciona novos registros a uma tabela.

#### Sintaxe Básica
```sql
INSERT INTO nome_da_tabela (coluna1, coluna2, ...)
VALUES (valor1, valor2, ...);
```

#### Inserir um Registro
```sql
INSERT INTO clientes (nome, email, idade)
VALUES ('João Silva', 'joao@email.com', 25);
```

#### Inserir Múltiplos Registros
```sql
INSERT INTO clientes (nome, email, idade)
VALUES 
    ('Maria Santos', 'maria@email.com', 30),
    ('Pedro Costa', 'pedro@email.com', 22),
    ('Ana Oliveira', 'ana@email.com', 28);
```

#### Inserir em Todas as Colunas (ordem da tabela)
```sql
INSERT INTO clientes
VALUES (NULL, 'João Silva', 'joao@email.com', 25);
-- NULL para coluna auto-incremento
```

## 🎯 Prática

### Arquivos Disponíveis

1. **`01_conceitos_basicos.md`**: Explicações detalhadas dos conceitos
2. **`02_exemplos_sql.sql`**: Scripts SQL práticos para execução
3. **`03_exercicios.md`**: Exercícios práticos com soluções
4. **`04_sqlite_pratico.py`**: Exemplos práticos com Python e SQLite

### Como Usar

#### Usando SQLite via Python
```bash
python 04_sqlite_pratico.py
```

#### Usando SQLite via Linha de Comando
```bash
sqlite3 exemplo.db < 02_exemplos_sql.sql
```

#### Usando DB Browser for SQLite
1. Abra o DB Browser for SQLite
2. Crie um novo banco de dados ou abra `exemplo.db`
3. Execute os scripts SQL da aba "Execute SQL"

## ✅ Objetivos de Aprendizado

Ao final desta seção, você será capaz de:
- [ ] Entender o que é um banco de dados e suas características
- [ ] Diferenciar bancos relacionais de não relacionais
- [ ] Compreender conceitos: tabela, linha, coluna, chave primária, chave estrangeira
- [ ] Entender o modelo ER e seus componentes
- [ ] Conhecer diferentes SGBDs e suas características
- [ ] Usar SELECT para consultar dados
- [ ] Aplicar filtros com WHERE
- [ ] Ordenar resultados com ORDER BY
- [ ] Limitar resultados com LIMIT
- [ ] Inserir dados com INSERT INTO

## 📝 Próximos Passos

Após dominar estes conceitos, avance para:
- **Módulo 02**: Comandos de atualização (UPDATE), remoção (DELETE), modelagem e normalização
- **Módulo 03**: JOINs, consultas avançadas e conexão com Python

