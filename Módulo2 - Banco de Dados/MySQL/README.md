# 🐬 Configuração do Banco MySQL

Este projeto utiliza MySQL com configurações seguras através de variáveis de ambiente.

## 🚀 Quick Start

```bash
# 1. Instalar MySQL
sudo apt install mysql-server mysql-client  # Ubuntu/Debian
brew install mysql                          # macOS

# 2. Configurar segurança
sudo mysql_secure_installation

# 3. Criar banco
mysql -u root -p -e "CREATE DATABASE exemplo_bd;"

# 4. Instalar dependências Python (--break-system-packages é específico de algumas distros, ou seja, não é necessário em todos os sistemas)
pip3 install --break-system-packages -r requirements.txt

# 5. Configurar credenciais
cp config.env.example config.env
# Editar config.env com suas credenciais

# 6. Executar
python3 mysql_bd.py
```

## 📋 Pré-requisitos

### 1. Instalar MySQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install mysql-server mysql-client
sudo systemctl start mysql
sudo systemctl enable mysql
```

**macOS (com Homebrew):**
```bash
brew install mysql
brew services start mysql
```

**Windows:**
- Baixe o instalador do [site oficial do MySQL](https://dev.mysql.com/downloads/mysql/)
- Siga o instalador gráfico
- Ou use o MySQL Installer

### 2. Configurar MySQL

1. **Configurar segurança inicial:**
```bash
# Ubuntu/Debian
sudo mysql_secure_installation

# macOS/Windows - executar após instalação
mysql_secure_installation
```

2. **Criar um banco de dados:**
```bash
# Conectar ao MySQL
mysql -u root -p

# Criar banco de dados
CREATE DATABASE exemplo_bd;

# Criar usuário (opcional)
CREATE USER 'meu_usuario'@'localhost' IDENTIFIED BY 'minha_senha';
GRANT ALL PRIVILEGES ON exemplo_bd.* TO 'meu_usuario'@'localhost';
FLUSH PRIVILEGES;

# Sair do MySQL
EXIT;
```

3. **Verificar se o MySQL está rodando:**
```bash
# Linux/Mac
sudo systemctl status mysql
# ou
brew services list | grep mysql

# Windows - verificar no Services (services.msc)
```

## 📁 Estrutura do Projeto

```
MySQL/
├── mysql_bd.py             # Script principal do banco
├── requirements.txt        # Dependências Python
├── config.env.example      # Template de configuração
├── config.env              # Suas credenciais (não commitado)
├── README.md               # Este arquivo
└── .gitignore              # Ignora arquivos sensíveis
```

## ⚙️ Configuração do Projeto

### 1. Instalar dependências Python

```bash
# Instalar dependências do Python (--break-system-packages é específico de algumas distros, ou seja, não é necessário em todos os sistemas)
pip3 install --break-system-packages -r requirements.txt
```

### 2. Configurar credenciais do banco

Copie o arquivo de exemplo e edite com suas credenciais:
```bash
cp config.env.example config.env
```

Edite o arquivo `config.env`:
```env
DB_HOST=localhost
DB_NAME=exemplo_bd
DB_USER=root
DB_PASSWORD=sua_senha_do_mysql
DB_PORT=3306
```

### 3. Executar o programa

```bash
python3 mysql_bd.py
```

## 🔧 Troubleshooting

### 🚨 Problemas Comuns

#### 1. **Erro de Conexão**
```
mysql.connector.errors.DatabaseError: 2003 (HY000): Can't connect to MySQL server
```

**Possíveis causas e soluções:**
- ✅ **MySQL não está rodando**: `sudo systemctl start mysql` (Linux) ou `brew services start mysql` (macOS)
- ✅ **Porta incorreta**: Verifique se a porta 3306 está correta no `config.env`
- ✅ **Firewall bloqueando**: Desabilite firewall temporariamente ou libere a porta 3306
- ✅ **Host incorreto**: Use `localhost` para conexão local ou IP correto para remota

**Teste de conectividade:**
```bash
# Testar se a porta está aberta
telnet localhost 3306
# ou
nc -zv localhost 3306

# Testar conexão MySQL
mysql -h localhost -u root -p -e "SELECT 1;"
```

#### 2. **Erro de Autenticação**
```
mysql.connector.errors.ProgrammingError: 1045 (28000): Access denied for user
```

**Soluções:**
- ✅ **Senha incorreta**: Verifique a senha no `config.env`
- ✅ **Usuário não existe**: Crie o usuário ou use `root`
- ✅ **Host incorreto**: Use `localhost` ou `127.0.0.1`

**Reset de senha (se necessário):**
```bash
# Parar MySQL
sudo systemctl stop mysql

# Iniciar em modo seguro
sudo mysqld_safe --skip-grant-tables &

# Conectar sem senha
mysql -u root

# Alterar senha
ALTER USER 'root'@'localhost' IDENTIFIED BY 'nova_senha';
FLUSH PRIVILEGES;
EXIT;

# Reiniciar MySQL normalmente
sudo systemctl restart mysql
```

#### 3. **Banco Não Existe**
```
mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'exemplo_bd'
```

**Solução:**
```sql
-- Conectar ao MySQL
mysql -u root -p

-- Criar o banco
CREATE DATABASE exemplo_bd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verificar se foi criado
SHOW DATABASES;
```

#### 4. **Erro de Permissão**
```
mysql.connector.errors.ProgrammingError: 1142 (42000): INSERT command denied to user
```

**Solução:**
```sql
-- Dar permissões completas
GRANT ALL PRIVILEGES ON exemplo_bd.* TO 'seu_usuario'@'localhost';
FLUSH PRIVILEGES;

-- Verificar permissões
SHOW GRANTS FOR 'seu_usuario'@'localhost';
```

#### 5. **Erro de Charset/Encoding**
```
mysql.connector.errors.ProgrammingError: 1366 (HY000): Incorrect string value
```

**Solução:**
```sql
-- Alterar charset do banco
ALTER DATABASE exemplo_bd CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alterar charset da tabela
ALTER TABLE pessoa CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

#### 6. **Erro de Timeout**
```
mysql.connector.errors.OperationalError: 2013 (HY000): Lost connection to MySQL server
```

**Soluções:**
- ✅ **Aumentar timeout**: Adicione `?connect_timeout=60` na string de conexão
- ✅ **Verificar memória**: `SHOW VARIABLES LIKE 'max_connections';`
- ✅ **Reiniciar MySQL**: `sudo systemctl restart mysql`

#### 7. **Erro de SSL**
```
mysql.connector.errors.ProgrammingError: 2026 (HY000): SSL connection error
```

**Solução:**
```python
# Adicionar na string de conexão
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senha',
    'database': 'exemplo_bd',
    'ssl_disabled': True  # Desabilitar SSL se necessário
}
```

### 🔍 Diagnóstico Avançado

#### Verificar Status do MySQL
```bash
# Status do serviço
sudo systemctl status mysql

# Processos MySQL
ps aux | grep mysql

# Portas em uso
netstat -tlnp | grep 3306
```

#### Logs do MySQL
```bash
# Ver logs de erro
sudo tail -f /var/log/mysql/error.log

# Ver logs de queries lentas
sudo tail -f /var/log/mysql/slow.log
```

#### Comandos de Diagnóstico SQL
```sql
-- Ver status geral
SHOW STATUS;

-- Ver variáveis importantes
SHOW VARIABLES LIKE 'max_connections';
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';

-- Ver processos ativos
SHOW PROCESSLIST;

-- Ver locks
SHOW ENGINE INNODB STATUS;
```

### Comandos Úteis

#### 🔗 Conexão e Autenticação
```bash
# Conectar ao MySQL (métodos diferentes)
mysql -h localhost -u root -p                    # Conexão local
mysql -h 192.168.1.100 -u usuario -p             # Conexão remota
mysql -h localhost -u root -p --port=3306         # Especificar porta
mysql -u root -p exemplo_bd                       # Conectar direto ao banco

# Testar conexão sem entrar no shell
mysql -h localhost -u root -p -e "SELECT 1;"

# Conectar com timeout
mysql -h localhost -u root -p --connect-timeout=10
```

#### 📊 Gerenciamento de Bancos de Dados
```sql
-- Listar todos os bancos
SHOW DATABASES;

-- Criar banco com charset específico
CREATE DATABASE novo_banco CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Usar um banco específico
USE exemplo_bd;

-- Ver banco atual
SELECT DATABASE();

-- Renomear banco (MySQL 8.0+)
ALTER DATABASE exemplo_bd RENAME TO novo_nome;

-- Deletar banco
DROP DATABASE IF EXISTS banco_antigo;

-- Verificar tamanho dos bancos
SELECT 
    table_schema AS 'Database',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)'
FROM information_schema.tables 
GROUP BY table_schema;
```

#### 📋 Gerenciamento de Tabelas
```sql
-- Listar tabelas
SHOW TABLES;

-- Listar tabelas com informações
SHOW TABLE STATUS;

-- Descrever estrutura de uma tabela
DESCRIBE pessoa;
-- ou
SHOW COLUMNS FROM pessoa;

-- Ver estrutura completa da tabela
SHOW CREATE TABLE pessoa;

-- Ver índices da tabela
SHOW INDEX FROM pessoa;

-- Ver estatísticas da tabela
SHOW TABLE STATUS LIKE 'pessoa';

-- Renomear tabela
RENAME TABLE pessoa TO usuarios;

-- Copiar estrutura de tabela
CREATE TABLE nova_tabela LIKE pessoa;
```

#### 👥 Gerenciamento de Usuários e Permissões
```sql
-- Listar usuários
SELECT user, host FROM mysql.user;

-- Criar usuário
CREATE USER 'novo_usuario'@'localhost' IDENTIFIED BY 'senha_forte';

-- Dar permissões específicas
GRANT SELECT, INSERT ON exemplo_bd.* TO 'usuario'@'localhost';
GRANT ALL PRIVILEGES ON exemplo_bd.* TO 'admin'@'localhost';

-- Remover permissões
REVOKE INSERT ON exemplo_bd.* FROM 'usuario'@'localhost';

-- Aplicar mudanças de permissões
FLUSH PRIVILEGES;

-- Alterar senha
ALTER USER 'usuario'@'localhost' IDENTIFIED BY 'nova_senha';

-- Deletar usuário
DROP USER 'usuario_antigo'@'localhost';

-- Ver permissões do usuário atual
SHOW GRANTS;
SHOW GRANTS FOR 'usuario'@'localhost';
```

#### 🔍 Consultas e Análise
```sql
-- Ver processos ativos
SHOW PROCESSLIST;

-- Ver status do servidor
SHOW STATUS;

-- Ver variáveis de configuração
SHOW VARIABLES;
SHOW VARIABLES LIKE 'max_connections';

-- Ver logs de erro
SHOW VARIABLES LIKE 'log_error';

-- Análise de performance
EXPLAIN SELECT * FROM pessoa WHERE nome = 'João';

-- Ver queries lentas
SHOW VARIABLES LIKE 'slow_query_log';
SHOW VARIABLES LIKE 'long_query_time';

-- Verificar charset e collation
SHOW VARIABLES LIKE 'character_set%';
SHOW VARIABLES LIKE 'collation%';
```

#### 🛠️ Manutenção e Diagnóstico
```sql
-- Verificar integridade da tabela
CHECK TABLE pessoa;

-- Otimizar tabela
OPTIMIZE TABLE pessoa;

-- Reparar tabela (se necessário)
REPAIR TABLE pessoa;

-- Analisar tabela (atualiza estatísticas)
ANALYZE TABLE pessoa;

-- Verificar espaço usado
SELECT 
    table_name,
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size (MB)'
FROM information_schema.tables 
WHERE table_schema = 'exemplo_bd';

-- Ver locks ativos
SHOW ENGINE INNODB STATUS;
```

#### 📤 Backup e Restore (Linha de Comando)
```bash
# Backup completo
mysqldump -u root -p exemplo_bd > backup_completo.sql

# Backup apenas estrutura
mysqldump -u root -p --no-data exemplo_bd > estrutura.sql

# Backup apenas dados
mysqldump -u root -p --no-create-info exemplo_bd > dados.sql

# Backup com compressão
mysqldump -u root -p exemplo_bd | gzip > backup.sql.gz

# Backup de múltiplos bancos
mysqldump -u root -p --databases banco1 banco2 > multiplos_bancos.sql

# Backup de todas as bases
mysqldump -u root -p --all-databases > backup_todos.sql

# Restore
mysql -u root -p exemplo_bd < backup_completo.sql

# Restore com compressão
gunzip -c backup.sql.gz | mysql -u root -p exemplo_bd
```

#### 🚀 Comandos de Sistema
```bash
# Verificar status do MySQL
sudo systemctl status mysql          # Linux
brew services list | grep mysql      # macOS

# Iniciar/parar MySQL
sudo systemctl start mysql          # Linux
sudo systemctl stop mysql
brew services start mysql           # macOS
brew services stop mysql

# Ver logs do MySQL
sudo tail -f /var/log/mysql/error.log    # Linux
tail -f /usr/local/var/mysql/*.err       # macOS

# Verificar porta em uso
netstat -tlnp | grep 3306           # Linux
lsof -i :3306                       # macOS/Linux

# Testar conectividade
telnet localhost 3306
nc -zv localhost 3306
```

#### 🎯 Comandos de Desenvolvimento
```sql
-- Ver versão do MySQL
SELECT VERSION();

-- Ver data/hora atual
SELECT NOW();

-- Ver usuário atual
SELECT USER();

-- Limpar tela (no MySQL shell)
\! clear

-- Executar comando do sistema
\! ls -la

-- Ver histórico de comandos
\! history

-- Sair do MySQL
EXIT;
-- ou
QUIT;
```

## Diferenças entre MySQL e PostgreSQL

### Tipos de Dados
- **MySQL**: `AUTO_INCREMENT` vs PostgreSQL `SERIAL`
- **MySQL**: `INT` vs PostgreSQL `INTEGER`
- **MySQL**: `VARCHAR` vs PostgreSQL `VARCHAR` (similar)
- **MySQL**: `TIMESTAMP` vs PostgreSQL `TIMESTAMP` (similar)

### Sintaxe SQL
- **MySQL**: `AUTO_INCREMENT PRIMARY KEY`
- **PostgreSQL**: `SERIAL PRIMARY KEY`
- **MySQL**: `ENGINE=InnoDB` (opcional)
- **PostgreSQL**: Não usa engines

### Conexão
- **MySQL**: Porta padrão 3306
- **PostgreSQL**: Porta padrão 5432
- **MySQL**: `mysql.connector`
- **PostgreSQL**: `psycopg2`

## Segurança

- O arquivo `config.env` está no `.gitignore` e não será commitado
- Use o arquivo `config.env.example` como template para outros desenvolvedores
- Nunca commite credenciais reais no repositório
- Para produção, use variáveis de ambiente do sistema ou serviços de gerenciamento de secrets
- Configure o MySQL com senhas fortes e usuários específicos para cada aplicação

## ⚡ Performance

### 🚀 Dicas de Otimização MySQL

#### 1. **Índices Estratégicos**
```sql
-- Índices simples
CREATE INDEX idx_nome ON pessoa(nome);
CREATE INDEX idx_categoria ON pessoa(categoria_id);

-- Índices compostos
CREATE INDEX idx_nome_categoria ON pessoa(nome, categoria_id);

-- Índices únicos
CREATE UNIQUE INDEX idx_email ON pessoa(email);

-- Verificar uso de índices
EXPLAIN SELECT * FROM pessoa WHERE nome = 'João';
```

#### 2. **Configuração do MySQL**
```sql
-- Verificar configurações importantes
SHOW VARIABLES LIKE 'innodb_buffer_pool_size';    -- Cache de dados
SHOW VARIABLES LIKE 'max_connections';            -- Conexões simultâneas
SHOW VARIABLES LIKE 'query_cache_size';           -- Cache de queries (depreciado a partir do MySQL 8.0+)
SHOW VARIABLES LIKE 'have_query_cache';           -- Cache de queries
SHOW VARIABLES LIKE 'innodb_log_file_size';       -- Tamanho do log

-- Configurações recomendadas para desenvolvimento
SET GLOBAL innodb_buffer_pool_size = 128M;
SET GLOBAL max_connections = 100;
SET GLOBAL query_cache_size = 32M;
```

#### 3. **Análise de Performance**
```sql
-- Ativar log de queries lentas
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 2;
SET GLOBAL log_queries_not_using_indexes = 'ON';

-- Ver queries mais lentas
SELECT * FROM mysql.slow_log ORDER BY start_time DESC LIMIT 10;

-- Análise de performance de uma query
EXPLAIN FORMAT=JSON SELECT * FROM pessoa WHERE nome LIKE 'João%';
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
```

### 📊 Monitoramento

#### Comandos de Monitoramento
```sql
-- Status geral do servidor
SHOW STATUS;

-- Conexões ativas
SHOW PROCESSLIST;

-- Performance de queries
SHOW STATUS LIKE 'Slow_queries';
SHOW STATUS LIKE 'Questions';

-- Uso de memória
SHOW STATUS LIKE 'Innodb_buffer_pool%';

-- Locks e deadlocks
SHOW ENGINE INNODB STATUS;
```

#### Scripts de Monitoramento
```bash
# Monitorar conexões em tempo real
watch -n 1 "mysql -u root -p -e 'SHOW PROCESSLIST;'"

# Verificar uso de disco
du -sh /var/lib/mysql/

# Monitorar logs
tail -f /var/log/mysql/slow.log
```

## 💡 Dicas de Desenvolvimento

### 🐍 Boas Práticas Python + MySQL

#### 1. **Conexão Eficiente**
```python
import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='senha',
        database='exemplo_bd',
        autocommit=True,
        charset='utf8mb4'
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
    conn.start_transaction()
    cursor.execute("INSERT INTO pessoa (nome) VALUES (%s)", ("João",))
    cursor.execute("UPDATE categoria SET total = total + 1 WHERE id = %s", (1,))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Erro: {e}")
```

#### 4. **Pool de Conexões**
```python
from mysql.connector import pooling

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senha',
    'database': 'exemplo_bd',
    'pool_name': 'mypool',
    'pool_size': 5,
    'pool_reset_session': True
}

# Criar pool
connection_pool = pooling.MySQLConnectionPool(**config)

# Usar pool
conn = connection_pool.get_connection()
cursor = conn.cursor()
# ... usar conexão
conn.close()  # Retorna para o pool
```

### 🔧 Ferramentas Úteis

#### 1. **MySQL Workbench**
- Interface gráfica para MySQL
- Designer de banco de dados
- Query builder visual
- Monitor de performance

#### 2. **phpMyAdmin** (Web)
```bash
# Instalar phpMyAdmin
sudo apt install phpmyadmin

# Acessar: http://localhost/phpmyadmin
```

#### 3. **Comandos Úteis para Desenvolvimento**
```bash
# Backup automático
mysqldump -u root -p exemplo_bd | gzip > backup_$(date +%Y%m%d).sql.gz

# Restore rápido
gunzip -c backup_20231201.sql.gz | mysql -u root -p exemplo_bd

# Verificar integridade
mysqlcheck -u root -p exemplo_bd

# Otimizar tabelas
mysql -u root -p -e "OPTIMIZE TABLE exemplo_bd.pessoa;"
```

## Backup e Restore

### Backup
```bash
# Backup completo do banco
mysqldump -u root -p exemplo_bd > backup_exemplo_bd.sql

# Backup apenas estrutura
mysqldump -u root -p --no-data exemplo_bd > estrutura_exemplo_bd.sql
```

### Restore
```bash
# Restaurar banco
mysql -u root -p exemplo_bd < backup_exemplo_bd.sql

# Restaurar com compressão
gunzip -c backup_exemplo_bd.sql.gz | mysql -u root -p exemplo_bd

# Restaurar apenas estrutura
mysql -u root -p exemplo_bd < estrutura_exemplo_bd.sql
```

## 📚 Recursos Adicionais

### 🔗 Links Úteis
- [Documentação Oficial MySQL](https://dev.mysql.com/doc/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [MySQL Workbench Download](https://dev.mysql.com/downloads/workbench/)
- [phpMyAdmin](https://www.phpmyadmin.net/)

### 📖 Tutoriais Recomendados
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [Python MySQL Tutorial](https://www.w3schools.com/python/python_mysql.asp)
- [SQL Tutorial](https://www.w3schools.com/sql/)

### 🛠️ Extensões VS Code
- **MySQL**: Syntax highlighting e autocomplete
- **SQLTools**: Interface para bancos de dados
- **Database Client**: Gerenciamento visual de bancos

### 📝 Checklist de Configuração
- [ ] MySQL instalado e rodando
- [ ] Banco de dados criado
- [ ] Usuário com permissões configurado
- [ ] Arquivo `config.env` configurado
- [ ] Dependências Python instaladas
- [ ] Script `mysql_bd.py` executando sem erros

### 🆘 Suporte
Se encontrar problemas:
1. Verifique a seção [Troubleshooting](#-troubleshooting)
2. Consulte os logs do MySQL
3. Teste a conectividade manual
4. Verifique as permissões do usuário

---

## Segurança

- O arquivo `config.env` está no `.gitignore` e não será commitado
- Use o arquivo `config.env.example` como template para outros desenvolvedores
- Nunca commite credenciais reais no repositório
- Para produção, use variáveis de ambiente do sistema ou serviços de gerenciamento de secrets
- Configure o MySQL com senhas fortes e usuários específicos para cada aplicação

**🎉 Parabéns!** Seu ambiente MySQL está configurado e pronto para desenvolvimento!
