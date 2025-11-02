# Módulo 2 - Banco de Dados

Este módulo apresenta o trabalho com bancos de dados relacionais utilizando Python, abordando três dos principais sistemas de gerenciamento de banco de dados (SGBD): SQLite, MySQL e PostgreSQL.

## 📚 Conteúdo do Módulo

Este módulo está dividido em três seções, cada uma focada em um SGBD específico:

### 1. SQLite
Banco de dados embutido, leve e sem necessidade de servidor separado, ideal para desenvolvimento e aplicações pequenas.
- **Características**: Zero-configuração, baseado em arquivo, perfeito para protótipos
- **Uso recomendado**: Desenvolvimento local, aplicações desktop, testes
- **Arquivos**: `sqlite_bd.py`, `exemplo_bd.db`

### 2. MySQL
Um dos SGBDs mais populares do mundo, amplamente utilizado em aplicações web.
- **Características**: Alto desempenho, suporte a grandes volumes de dados
- **Uso recomendado**: Aplicações web de médio a grande porte
- **Arquivos**: `mysql_bd.py`, `config.env`, `config.env.example`, `requirements.txt`
- **Documentação**: Consulte o [README.md](./MySQL/README.md) para instruções detalhadas

### 3. PostgreSQL
SGBD de código aberto avançado, conhecido por sua robustez e recursos avançados.
- **Características**: ACID completo, suporte extensivo a tipos de dados
- **Uso recomendado**: Aplicações enterprise, sistemas complexos
- **Arquivos**: `postgresql_bd.py`, `config.env`, `config.env.example`, `requirements.txt`
- **Documentação**: Consulte o [README.md](./PostgreSQL/README.md) para instruções detalhadas

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Entender as diferenças entre diferentes SGBDs
- Conectar aplicações Python a bancos de dados relacionais
- Executar operações CRUD (Create, Read, Update, Delete)
- Gerenciar transações e integridade de dados
- Trabalhar com variáveis de ambiente para configurações seguras
- Implementar conexões seguras e gerenciamento de recursos

## 🔧 Conceitos Abordados

### Operações com Banco de Dados
- **Conexão**: Estabelecer e gerenciar conexões com o banco
- **Queries**: Executar comandos SQL (SELECT, INSERT, UPDATE, DELETE)
- **Transações**: Garantir consistência dos dados
- **Gestão de Recursos**: Fechar conexões adequadamente (context managers)

### Segurança
- **Variáveis de Ambiente**: Armazenar credenciais de forma segura
- **Prepared Statements**: Prevenir SQL injection
- **Gestão de Credenciais**: Nunca hardcodear senhas no código

### Bibliotecas Utilizadas
- **sqlite3**: Biblioteca padrão do Python para SQLite
- **mysql-connector-python** ou **pymysql**: Conectores para MySQL
- **psycopg2**: Conector para PostgreSQL
- **python-dotenv**: Gerenciamento de variáveis de ambiente

## 🚀 Como Utilizar Este Módulo

### Para SQLite
```bash
python3 sqlite_bd.py
```

### Para MySQL
1. Instale o MySQL Server
2. Configure as variáveis de ambiente (copie `config.env.example` para `config.env`)
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute: `python3 mysql_bd.py`

### Para PostgreSQL
1. Instale o PostgreSQL Server
2. Configure as variáveis de ambiente (copie `config.env.example` para `config.env`)
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute: `python3 postgresql_bd.py`

## 📋 Pré-requisitos

- Python 3.7 ou superior
- Conhecimento básico de SQL
- Entendimento dos conceitos do Módulo 1 (Lógica de Programação)
- Para MySQL/PostgreSQL: SGBD instalado e configurado localmente

## 📖 Recursos Adicionais

- [Documentação SQLite](https://www.sqlite.org/docs.html)
- [Documentação MySQL](https://dev.mysql.com/doc/)
- [Documentação PostgreSQL](https://www.postgresql.org/docs/)
- [Python Database API Specification](https://www.python.org/dev/peps/pep-0249/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

## 🔐 Boas Práticas

1. **Nunca commite arquivos `.env`** com credenciais reais
2. **Use prepared statements** para evitar SQL injection
3. **Feche conexões adequadamente** usando context managers (`with`)
4. **Trate exceções** relacionadas ao banco de dados
5. **Faça backup regular** dos dados importantes
6. **Use transações** para operações que precisam ser atômicas

## ⚠️ Importante

- Cada subdiretório (SQLite, MySQL, PostgreSQL) possui seu próprio README.md com instruções específicas
- Configure sempre as credenciais através de variáveis de ambiente, nunca diretamente no código
- Teste as conexões antes de implementar lógicas mais complexas

