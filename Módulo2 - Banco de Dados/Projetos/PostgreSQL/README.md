# 🐘 Configuração do Banco PostgreSQL

Este projeto utiliza PostgreSQL com configurações seguras através de variáveis de ambiente.

## 🚀 Quick Start

```bash
# 1. Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib  # Ubuntu/Debian
brew install postgresql                         # macOS

# 2. Iniciar serviço
sudo systemctl start postgresql  # Linux
brew services start postgresql   # macOS

# 3. Criar banco
sudo -u postgres psql -c "CREATE DATABASE exemplo_bd;"

# 4. Instalar dependências Python (--break-system-packages é específico de algumas distros, ou seja, não é necessário em todos os sistemas)
pip3 install --break-system-packages -r requirements.txt

# 5. Configurar credenciais
cp config.env.example config.env
# Editar config.env com suas credenciais

# 6. Executar
python3 postgresql_bd.py
```

## 📋 Pré-requisitos

### 1. Instalar PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**macOS (com Homebrew):**
```bash
brew install postgresql
brew services start postgresql
```

**Windows:**
- Baixe o instalador do [site oficial do PostgreSQL](https://www.postgresql.org/download/windows/)
- Siga o instalador gráfico

### 2. Configurar PostgreSQL

1. **Criar um banco de dados:**
```bash
# Conectar ao PostgreSQL
sudo -u postgres psql

# Criar banco de dados
CREATE DATABASE exemplo_bd;

# Criar usuário (opcional)
CREATE USER meu_usuario WITH PASSWORD 'minha_senha';
GRANT ALL PRIVILEGES ON DATABASE exemplo_bd TO meu_usuario;

# Sair do psql
\q
```

2. **Verificar se o PostgreSQL está rodando:**
```bash
# Linux/Mac
sudo systemctl status postgresql
# ou
brew services list | grep postgresql

# Windows - verificar no Services (services.msc)
```

## 📁 Estrutura do Projeto

```
PostgreSQL/
├── postgresql_bd.py        # Script principal do banco
├── requirements.txt        # Dependências Python
├── config.env.example      # Template de configuração
├── config.env              # Suas credenciais (não commitado)
├── README.md               # Este arquivo
└── .gitignore              # Ignora arquivos sensíveis
```

## ⚙️ Configuração do Projeto

### 1. Instalar dependências Python

```bash
# Instalar dependências Python (--break-system-packages é específico de algumas distros, ou seja, não é necessário em todos os sistemas)
pip3 install --break-system-packages -r requirements.txt
```

### 2. Configurar credenciais do banco

1. Copie o arquivo de exemplo:
```bash
cp config.env.example config.env
```

2. Edite o arquivo `config.env` com suas credenciais:
```env
DB_HOST=localhost
DB_NAME=exemplo_bd
DB_USER=postgres
DB_PASSWORD=sua_senha_do_postgres
DB_PORT=5432
```

### 3. Executar o programa

```bash
python3 postgresql_bd.py
```

## 🔧 Troubleshooting

### 🚨 Problemas Comuns

#### 1. **Erro de Conexão**
```
psycopg2.OperationalError: could not connect to server
```

**Possíveis causas e soluções:**
- ✅ **PostgreSQL não está rodando**: `sudo systemctl start postgresql` (Linux) ou `brew services start postgresql` (macOS)
- ✅ **Porta incorreta**: Verifique se a porta 5432 está correta no `config.env`
- ✅ **Firewall bloqueando**: Desabilite firewall temporariamente ou libere a porta 5432
- ✅ **Host incorreto**: Use `localhost` para conexão local ou IP correto para remota

**Teste de conectividade:**
```bash
# Testar se a porta está aberta
telnet localhost 5432
# ou
nc -zv localhost 5432

# Testar conexão PostgreSQL
psql -h localhost -U postgres -d exemplo_bd -c "SELECT 1;"
```

#### 2. **Erro de Autenticação**
```
psycopg2.OperationalError: FATAL: password authentication failed
```

**Soluções:**
- ✅ **Senha incorreta**: Verifique a senha no `config.env`
- ✅ **Usuário não existe**: Crie o usuário ou use `postgres`
- ✅ **Host incorreto**: Use `localhost` ou `127.0.0.1`
- ✅ **Configuração pg_hba.conf**: Verifique o arquivo de configuração

**Reset de senha (se necessário):**
```bash
# Parar PostgreSQL
sudo systemctl stop postgresql

# Iniciar em modo single-user (atenção, este caminho pode variar conforme a distribuição)
sudo -u postgres postgres --single -D /var/lib/postgresql/data

# Conectar e alterar senha
ALTER USER postgres PASSWORD 'nova_senha';
\q

# Reiniciar PostgreSQL normalmente
sudo systemctl start postgresql
```

#### 3. **Banco Não Existe**
```
psycopg2.OperationalError: database "exemplo_bd" does not exist
```

**Solução:**
```sql
-- Conectar ao PostgreSQL
sudo -u postgres psql

-- Criar o banco
CREATE DATABASE exemplo_bd;

-- Verificar se foi criado
\l
```

#### 4. **Erro de Permissão**
```
psycopg2.OperationalError: permission denied for database
```

**Solução:**
```sql
-- Dar permissões completas
GRANT ALL PRIVILEGES ON DATABASE exemplo_bd TO seu_usuario;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO seu_usuario;

-- Verificar permissões
\du
```

#### 5. **Erro de Encoding/Charset**
```
psycopg2.OperationalError: invalid byte sequence for encoding "UTF8"
```

**Solução:**
```sql
-- Alterar encoding do banco
ALTER DATABASE exemplo_bd SET client_encoding = 'UTF8';

-- Verificar encoding
SHOW client_encoding;
```

#### 6. **Erro de Timeout**
```
psycopg2.OperationalError: connection timeout expired
```

**Soluções:**
- ✅ **Aumentar timeout**: Adicione `connect_timeout=60` na string de conexão
- ✅ **Verificar memória**: `SHOW max_connections;`
- ✅ **Reiniciar PostgreSQL**: `sudo systemctl restart postgresql`

#### 7. **Erro de SSL**
```
psycopg2.OperationalError: SSL connection error
```

**Solução:**
```python
# Adicionar na string de conexão
config = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'senha',
    'database': 'exemplo_bd',
    'sslmode': 'disable'  # Desabilitar SSL se necessário
}
```

### 🔍 Diagnóstico Avançado

#### Verificar Status do PostgreSQL
```bash
# Status do serviço
sudo systemctl status postgresql

# Processos PostgreSQL
ps aux | grep postgres

# Portas em uso
netstat -tlnp | grep 5432
```

#### Logs do PostgreSQL
```bash
# Ver logs de erro
sudo tail -f /var/log/postgresql/postgresql-*.log

# Ver logs de queries lentas
sudo tail -f /var/log/postgresql/postgresql-*.log | grep "slow"
```

#### Comandos de Diagnóstico SQL
```sql
-- Ver status geral
SELECT * FROM pg_stat_activity;

-- Ver configurações importantes
SHOW max_connections;
SHOW shared_buffers;

-- Ver processos ativos
SELECT pid, usename, application_name, client_addr, state, query 
FROM pg_stat_activity 
WHERE state = 'active';

-- Ver locks ativos
SELECT * FROM pg_locks;
```

### Comandos Úteis

#### Conectar ao PostgreSQL
```bash
# Conectar como usuário padrão
psql -h localhost -U postgres

# Conectar a um banco específico
psql -h localhost -U postgres -d exemplo_bd

# Conectar com porta específica
psql -h localhost -U postgres -p 5432

# Conectar via socket Unix (Linux/Mac)
psql -U postgres
```

#### Comandos dentro do psql

**Navegação e Informações:**
```sql
-- Listar todos os bancos de dados
\l
\l+

-- Conectar a um banco específico
\c exemplo_bd
\c nome_do_banco

-- Listar tabelas do banco atual
\dt
\dt+

-- Listar todas as tabelas (incluindo system tables)
\dt *

-- Descrever estrutura de uma tabela
\d nome_da_tabela
\d+ nome_da_tabela

-- Listar índices
\di

-- Listar views
\dv

-- Listar funções
\df

-- Listar usuários/roles
\du
\du+

-- Mostrar informações do banco atual
\conninfo

-- Mostrar versão do PostgreSQL
SELECT version();
```

**Consultas e Dados:**
```sql
-- Ver todas as tabelas e suas linhas
SELECT schemaname, tablename, n_tup_ins as "Inserções", n_tup_upd as "Atualizações", n_tup_del as "Deleções" 
FROM pg_stat_user_tables;

-- Ver tamanho das tabelas
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Ver conexões ativas
SELECT pid, usename, application_name, client_addr, state, query 
FROM pg_stat_activity 
WHERE state = 'active';

-- Ver estatísticas do banco
SELECT * FROM pg_stat_database WHERE datname = 'exemplo_bd';
```

**Gerenciamento de Usuários:**
```sql
-- Criar usuário
CREATE USER novo_usuario WITH PASSWORD 'senha_segura';

-- Dar privilégios
GRANT ALL PRIVILEGES ON DATABASE exemplo_bd TO novo_usuario;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO novo_usuario;

-- Alterar senha
ALTER USER nome_usuario WITH PASSWORD 'nova_senha';

-- Remover usuário
DROP USER nome_usuario;
```

**Backup e Restore:**
```bash
# Backup completo do banco
pg_dump -h localhost -U postgres -d exemplo_bd > backup.sql

# Backup apenas estrutura (schema)
pg_dump -h localhost -U postgres -d exemplo_bd --schema-only > schema.sql

# Backup apenas dados
pg_dump -h localhost -U postgres -d exemplo_bd --data-only > dados.sql

# Restaurar backup
psql -h localhost -U postgres -d exemplo_bd < backup.sql

# Backup com compressão
pg_dump -h localhost -U postgres -d exemplo_bd | gzip > backup.sql.gz

# Restaurar backup comprimido
gunzip -c backup.sql.gz | psql -h localhost -U postgres -d exemplo_bd
```

**Configuração e Monitoramento:**
```sql
-- Ver configurações atuais
SHOW ALL;

-- Ver configuração específica
SHOW max_connections;
SHOW shared_buffers;

-- Ver logs de erro recentes (se habilitado)
SELECT * FROM pg_stat_database;

-- Ver queries lentas (se pg_stat_statements estiver habilitado)
SELECT query, calls, total_time, mean_time 
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;
```

**Comandos de Sistema:**
```bash
# Iniciar PostgreSQL
sudo systemctl start postgresql    # Linux
brew services start postgresql     # macOS

# Parar PostgreSQL
sudo systemctl stop postgresql     # Linux
brew services stop postgresql      # macOS

# Reiniciar PostgreSQL
sudo systemctl restart postgresql  # Linux
brew services restart postgresql   # macOS

# Ver status do serviço
sudo systemctl status postgresql   # Linux
brew services list | grep postgresql  # macOS

# Ver logs do PostgreSQL
sudo tail -f /var/log/postgresql/postgresql-*.log  # Linux
tail -f /usr/local/var/log/postgresql.log          # macOS (Homebrew)
```

**Sair do psql:**
```sql
-- Qualquer um destes comandos funciona
\q
exit
quit
```

## ⚡ Performance

### 🚀 Dicas de Otimização PostgreSQL

#### 1. **Índices Estratégicos**
```sql
-- Índices simples
CREATE INDEX idx_nome ON pessoa(nome);
CREATE INDEX idx_categoria ON pessoa(categoria_id);

-- Índices compostos
CREATE INDEX idx_nome_categoria ON pessoa(nome, categoria_id);

-- Índices únicos
CREATE UNIQUE INDEX idx_email ON pessoa(email);

-- Índices parciais
CREATE INDEX idx_ativos ON pessoa(nome) WHERE ativo = true;

-- Verificar uso de índices
EXPLAIN (ANALYZE, BUFFERS) SELECT * FROM pessoa WHERE nome = 'João';
```

#### 2. **Configuração do PostgreSQL**
```sql
-- Verificar configurações importantes
SHOW shared_buffers;           -- Cache de dados
SHOW max_connections;          -- Conexões simultâneas
SHOW work_mem;                 -- Memória para operações
SHOW maintenance_work_mem;      -- Memória para manutenção

-- Configurações recomendadas para desenvolvimento (atenção, em algumas versões pode exige permissões de superusuário)
ALTER SYSTEM SET shared_buffers = '128MB';
ALTER SYSTEM SET work_mem = '4MB';
ALTER SYSTEM SET maintenance_work_mem = '64MB';
SELECT pg_reload_conf();
```

#### 3. **Análise de Performance**
```sql
-- Ativar estatísticas
ALTER SYSTEM SET track_activities = on;
ALTER SYSTEM SET track_counts = on;
ALTER SYSTEM SET track_io_timing = on;
SELECT pg_reload_conf();

-- Ver queries mais lentas
SELECT query, calls, total_time, mean_time, rows
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;

-- Análise de performance de uma query
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) 
SELECT * FROM pessoa WHERE nome LIKE 'João%';
```

#### 4. **Otimização de Queries**
```sql
-- Usar LIMIT para grandes datasets
SELECT * FROM pessoa LIMIT 1000;

-- Usar índices em WHERE
SELECT * FROM pessoa WHERE id = 123;  -- Usa índice primário

-- Evitar SELECT *
SELECT id, nome, email FROM pessoa WHERE categoria_id = 1;

-- Usar JOINs eficientes
SELECT p.nome, c.nome as categoria 
FROM pessoa p 
INNER JOIN categoria c ON p.categoria_id = c.id;

-- Usar EXISTS ao invés de IN para subqueries
SELECT * FROM pessoa p 
WHERE EXISTS (SELECT 1 FROM categoria c WHERE c.id = p.categoria_id);
```

### 📊 Monitoramento

#### Comandos de Monitoramento
```sql
-- Status geral do servidor
SELECT * FROM pg_stat_database WHERE datname = 'exemplo_bd';

-- Conexões ativas
SELECT pid, usename, application_name, client_addr, state, query 
FROM pg_stat_activity 
WHERE state = 'active';

-- Performance de queries
SELECT * FROM pg_stat_statements ORDER BY total_time DESC LIMIT 10;

-- Uso de memória
SELECT * FROM pg_stat_bgwriter;

-- Locks e deadlocks
SELECT * FROM pg_locks WHERE NOT granted;
```

#### Scripts de Monitoramento
```bash
# Monitorar conexões em tempo real
watch -n 1 "psql -h localhost -U postgres -d exemplo_bd -c 'SELECT count(*) FROM pg_stat_activity;'"

# Verificar uso de disco
du -sh /var/lib/postgresql/

# Monitorar logs
tail -f /var/log/postgresql/postgresql-*.log
```

## 💡 Dicas de Desenvolvimento

### 🐍 Boas Práticas Python + PostgreSQL

#### 1. **Conexão Eficiente**
```python
import psycopg2
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='senha',
        database='exemplo_bd',
        autocommit=True
    )
    try:
        yield conn
    finally:
        conn.close()

# Uso
with get_connection() as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pessoa")
    results = cursor.fetchall()
```

#### 2. **Prepared Statements (Segurança)**
```python
# ❌ Vulnerável a SQL Injection
cursor.execute(f"SELECT * FROM pessoa WHERE nome = '{nome}'")

# ✅ Seguro com prepared statements
cursor.execute("SELECT * FROM pessoa WHERE nome = %s", (nome,))
```

#### 3. **Transações**
```python
try:
    conn.autocommit = False
    cursor.execute("INSERT INTO pessoa (nome) VALUES (%s)", ("João",))
    cursor.execute("UPDATE categoria SET total = total + 1 WHERE id = %s", (1,))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Erro: {e}")
```

#### 4. **Pool de Conexões**
```python
from psycopg2 import pool

# Criar pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20,  # min e max conexões
    host='localhost',
    user='postgres',
    password='senha',
    database='exemplo_bd'
)

# Usar pool
conn = connection_pool.getconn()
cursor = conn.cursor()
# ... usar conexão
connection_pool.putconn(conn)  # Retorna para o pool
```

### 🔧 Ferramentas Úteis

#### 1. **pgAdmin**
- Interface gráfica para PostgreSQL
- Designer de banco de dados
- Query builder visual
- Monitor de performance

#### 2. **DBeaver** (Multiplataforma)
```bash
# Download: https://dbeaver.io/
# Suporte nativo ao PostgreSQL
# Interface moderna e intuitiva
```

#### 3. **Comandos Úteis para Desenvolvimento**
```bash
# Backup automático
pg_dump -h localhost -U postgres exemplo_bd | gzip > backup_$(date +%Y%m%d).sql.gz

# Restore rápido
gunzip -c backup_20231201.sql.gz | psql -h localhost -U postgres exemplo_bd

# Verificar integridade
psql -h localhost -U postgres -d exemplo_bd -c "VACUUM ANALYZE;"

# Otimizar tabelas
psql -h localhost -U postgres -d exemplo_bd -c "REINDEX DATABASE exemplo_bd;"
```

## Diferenças entre PostgreSQL e MySQL

### Tipos de Dados
- **PostgreSQL**: `SERIAL` vs MySQL `AUTO_INCREMENT`
- **PostgreSQL**: `INTEGER` vs MySQL `INT`
- **PostgreSQL**: `VARCHAR` vs MySQL `VARCHAR` (similar)
- **PostgreSQL**: `TIMESTAMP` vs MySQL `TIMESTAMP` (similar)

### Sintaxe SQL
- **PostgreSQL**: `SERIAL PRIMARY KEY`
- **MySQL**: `AUTO_INCREMENT PRIMARY KEY`
- **PostgreSQL**: Não usa engines
- **MySQL**: `ENGINE=InnoDB` (opcional)

### Conexão
- **PostgreSQL**: Porta padrão 5432
- **MySQL**: Porta padrão 3306
- **PostgreSQL**: `psycopg2`
- **MySQL**: `mysql.connector`

## 📚 Recursos Adicionais

### 🔗 Links Úteis
- [Documentação Oficial PostgreSQL](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [pgAdmin Download](https://www.pgadmin.org/download/)
- [DBeaver](https://dbeaver.io/)

### 📖 Tutoriais Recomendados
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [Python PostgreSQL Tutorial](https://www.w3schools.com/python/python_postgresql.asp)
- [SQL Tutorial](https://www.w3schools.com/sql/)

### 🛠️ Extensões VS Code
- **PostgreSQL**: Syntax highlighting e autocomplete
- **SQLTools**: Interface para bancos de dados
- **Database Client**: Gerenciamento visual de bancos

### 📝 Checklist de Configuração
- [ ] PostgreSQL instalado e rodando
- [ ] Banco de dados criado
- [ ] Usuário com permissões configurado
- [ ] Arquivo `config.env` configurado
- [ ] Dependências Python instaladas
- [ ] Script `postgresql_bd.py` executando sem erros

### 🆘 Suporte
Se encontrar problemas:
1. Verifique a seção [Troubleshooting](#-troubleshooting)
2. Consulte os logs do PostgreSQL
3. Teste a conectividade manual
4. Verifique as permissões do usuário

---

## Segurança

- O arquivo `config.env` está no `.gitignore` e não será commitado
- Use o arquivo `config.env.example` como template para outros desenvolvedores
- Nunca commite credenciais reais no repositório
- Para produção, use variáveis de ambiente do sistema ou serviços de gerenciamento de secrets
- Configure o PostgreSQL com senhas fortes e usuários específicos para cada aplicação

**🎉 Parabéns!** Seu ambiente PostgreSQL está configurado e pronto para desenvolvimento!