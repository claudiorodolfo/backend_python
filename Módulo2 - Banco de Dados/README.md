# Módulo 2 - Banco de Dados

Este módulo apresenta o trabalho com bancos de dados relacionais utilizando Python, abordando três dos principais sistemas de gerenciamento de banco de dados (SGBD): SQLite, MySQL e PostgreSQL. Você aprenderá a conectar aplicações Python a diferentes bancos de dados, executar operações CRUD, gerenciar transações e implementar práticas de segurança.

## 📚 Conteúdo do Módulo

Este módulo está dividido em três seções principais, cada uma focada em um SGBD específico, permitindo que você compreenda as diferenças, semelhanças e casos de uso ideais para cada um:

### 1. SQLite
Banco de dados embutido, leve e sem necessidade de servidor separado, ideal para desenvolvimento e aplicações pequenas.

**Características principais:**
- Zero-configuração: não requer instalação ou configuração de servidor
- Baseado em arquivo: todo o banco está em um único arquivo
- Perfeito para protótipos e desenvolvimento local
- Incluído por padrão no Python (biblioteca `sqlite3`)
- Transações ACID completas

**Conceitos abordados:**
- Conexão com SQLite através da biblioteca `sqlite3`
- Criação e gerenciamento de tabelas
- Operações CRUD (Create, Read, Update, Delete)
- Gerenciamento de transações
- Context managers para fechamento seguro de conexões
- Comandos PRAGMA para configuração e otimização

**Arquivos incluídos:**
- `sqlite_bd.py`: Script principal demonstrando operações com SQLite
- `exemplo_bd.db`: Banco de dados de exemplo (gerado automaticamente)
- `README.md`: Documentação específica com comandos úteis e troubleshooting

**Quando usar SQLite:**
- Desenvolvimento local e testes
- Aplicações desktop
- Prototipagem rápida
- Aplicações com poucos usuários simultâneos
- Sistemas embarcados
- Cache local

### 2. MySQL
Um dos SGBDs mais populares do mundo, amplamente utilizado em aplicações web de médio a grande porte.

**Características principais:**
- Alto desempenho e escalabilidade
- Suporte a grandes volumes de dados
- Amplamente usado em aplicações web
- Suporte completo a transações ACID
- Comunidade ativa e grande ecossistema

**Conceitos abordados:**
- Instalação e configuração do MySQL Server
- Conexão usando `mysql.connector` ou `pymysql`
- Configuração segura com variáveis de ambiente
- Gerenciamento de conexões e pools de conexão
- Prepared statements para segurança (prevenção de SQL injection)
- Backup e restore de bancos
- Otimização e monitoramento de performance
- Gerenciamento de usuários e permissões

**Arquivos incluídos:**
- `mysql_bd.py`: Script principal com exemplos de operações
- `config.env.example`: Template de configuração segura
- `config.env`: Arquivo de configuração local (não commitado)
- `requirements.txt`: Dependências Python necessárias
- `README.md`: Guia completo com troubleshooting e comandos úteis

**Quando usar MySQL:**
- Aplicações web de médio a grande porte
- Sistemas que precisam de alta disponibilidade
- Ambientes onde MySQL já está estabelecido
- Aplicações que precisam de recursos específicos do MySQL

### 3. PostgreSQL
SGBD de código aberto avançado, conhecido por sua robustez, conformidade com padrões SQL e recursos avançados.

**Características principais:**
- Conformidade extensiva com padrões SQL
- Recursos avançados (JSON, arrays, full-text search)
- Robusto sistema de tipos de dados
- ACID completo e consistência de dados
- Extensibilidade através de extensões

**Conceitos abordados:**
- Instalação e configuração do PostgreSQL Server
- Conexão usando `psycopg2`
- Configuração segura com variáveis de ambiente
- Gerenciamento avançado de conexões
- Uso de context managers para recursos
- Preparação de queries para performance e segurança
- Backup e restore com `pg_dump` e `psql`
- Monitoramento e análise de performance
- Gerenciamento de schemas, roles e permissões

**Arquivos incluídos:**
- `postgresql_bd.py`: Script principal com exemplos de operações
- `config.env.example`: Template de configuração segura
- `config.env`: Arquivo de configuração local (não commitado)
- `requirements.txt`: Dependências Python necessárias
- `README.md`: Guia completo com troubleshooting e comandos úteis

**Quando usar PostgreSQL:**
- Aplicações enterprise que precisam de robustez
- Sistemas que exigem conformidade com padrões SQL
- Aplicações que precisam de tipos de dados avançados
- Sistemas complexos com relacionamentos complexos
- Quando se precisa de recursos como JSON nativo, full-text search, etc.

## 🎯 Objetivos de Aprendizado

Ao final deste módulo, você será capaz de:
- Entender as diferenças entre SQLite, MySQL e PostgreSQL e quando usar cada um
- Conectar aplicações Python a bancos de dados relacionais
- Executar operações CRUD (Create, Read, Update, Delete) com segurança
- Gerenciar transações e garantir integridade de dados
- Trabalhar com variáveis de ambiente para configurações seguras
- Implementar conexões seguras e gerenciamento adequado de recursos
- Usar prepared statements para prevenir SQL injection
- Gerenciar backups e restauração de bancos de dados
- Otimizar queries e entender planos de execução
- Monitorar e diagnosticar problemas em bancos de dados

## 🔧 Conceitos Abordados

### Operações com Banco de Dados
- **Conexão**: Estabelecer e gerenciar conexões com diferentes SGBDs
- **Queries**: Executar comandos SQL (SELECT, INSERT, UPDATE, DELETE)
- **Transações**: Garantir consistência dos dados através de transações ACID
- **Gestão de Recursos**: Fechar conexões adequadamente usando context managers
- **Pool de Conexões**: Gerenciar múltiplas conexões eficientemente

### Segurança
- **Variáveis de Ambiente**: Armazenar credenciais de forma segura (nunca no código)
- **Prepared Statements**: Prevenir SQL injection usando placeholders
- **Gestão de Credenciais**: Práticas seguras para gerenciamento de senhas e usuários
- **Permissões**: Configurar permissões adequadas para usuários de banco de dados

### Bibliotecas Utilizadas
- **sqlite3**: Biblioteca padrão do Python para SQLite (incluída)
- **mysql-connector-python** ou **pymysql**: Conectores para MySQL
- **psycopg2**: Conector para PostgreSQL
- **python-dotenv**: Gerenciamento de variáveis de ambiente (.env)

### Conceitos de Banco de Dados
- **Tipos de Dados**: Diferenças entre tipos nos diferentes SGBDs
- **Índices**: Criação e otimização de índices para performance
- **Constraints**: Chaves primárias, estrangeiras e outras restrições
- **Normalização**: Estruturação adequada de dados
- **Backup e Restore**: Estratégias de backup e recuperação

## 🚀 Como Utilizar Este Módulo

### Ordem Recomendada de Estudo

1. **SQLite** → Comece aqui para entender os fundamentos sem configuração complexa
2. **MySQL** → Aprenda a trabalhar com servidor de banco de dados
3. **PostgreSQL** → Explore recursos avançados e conformidade com padrões

### Para SQLite

SQLite não requer configuração especial, pois já vem incluído no Python:

```bash
# Navegue até o diretório SQLite
cd "Módulo2 - Banco de Dados/SQLite"

# Execute o script principal
python3 sqlite_bd.py
```

O arquivo `exemplo_bd.db` será criado automaticamente.

### Para MySQL

1. **Instale o MySQL Server**:
   ```bash
   # Ubuntu/Debian
   sudo apt install mysql-server mysql-client
   sudo systemctl start mysql
   
   # macOS
   brew install mysql
   brew services start mysql
   ```

2. **Configure o banco de dados**:
   ```bash
   mysql -u root -p -e "CREATE DATABASE exemplo_bd;"
   ```

3. **Configure as variáveis de ambiente**:
   ```bash
   cd "Módulo2 - Banco de Dados/MySQL"
   cp config.env.example config.env
   # Edite config.env com suas credenciais
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o script**:
   ```bash
   python3 mysql_bd.py
   ```

Para mais detalhes, consulte o [README.md do MySQL](./MySQL/README.md).

### Para PostgreSQL

1. **Instale o PostgreSQL Server**:
   ```bash
   # Ubuntu/Debian
   sudo apt install postgresql postgresql-contrib
   sudo systemctl start postgresql
   
   # macOS
   brew install postgresql
   brew services start postgresql
   ```

2. **Configure o banco de dados**:
   ```bash
   sudo -u postgres psql -c "CREATE DATABASE exemplo_bd;"
   ```

3. **Configure as variáveis de ambiente**:
   ```bash
   cd "Módulo2 - Banco de Dados/PostgreSQL"
   cp config.env.example config.env
   # Edite config.env com suas credenciais
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o script**:
   ```bash
   python3 postgresql_bd.py
   ```

Para mais detalhes, consulte o [README.md do PostgreSQL](./PostgreSQL/README.md).

## 📋 Pré-requisitos

- Python 3.7 ou superior instalado
- Conhecimento básico de SQL (SELECT, INSERT, UPDATE, DELETE)
- Entendimento dos conceitos do Módulo 1 (Lógica de Programação), especialmente:
  - Funções
  - Tratamento de exceções
  - Manipulação de strings
  - Trabalho com arquivos e contexto (context managers)
- Para MySQL/PostgreSQL: SGBD instalado e configurado localmente (ou acesso remoto)

## 💻 Estrutura dos Projetos

Cada subdiretório (SQLite, MySQL, PostgreSQL) contém:

- **Script principal**: Demonstra operações básicas e avançadas
- **README.md específico**: Documentação detalhada com comandos, troubleshooting e boas práticas
- **Configurações**: Arquivos de configuração e exemplos de ambiente
- **Dependências**: `requirements.txt` quando necessário

## 📖 Recursos Adicionais

### Documentação Oficial
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Python Database API Specification (PEP 249)](https://www.python.org/dev/peps/pep-0249/)

### Tutoriais e Cursos
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [Real Python - Working with Databases](https://realpython.com/python-sql/)

### Ferramentas Recomendadas
- **SQLite Browser (DB Browser for SQLite)**: Interface gráfica para SQLite
- **MySQL Workbench**: Interface gráfica oficial do MySQL
- **pgAdmin**: Interface gráfica oficial do PostgreSQL
- **DBeaver**: Ferramenta multiplataforma para todos os bancos
- **TablePlus**: Interface moderna para múltiplos bancos (macOS/Windows)

## 🔐 Boas Práticas

### Segurança
1. **Nunca commite arquivos `.env`** com credenciais reais
2. **Use prepared statements** para evitar SQL injection
3. **Valide entrada de dados** antes de inserir no banco
4. **Use conexões seguras** em produção (SSL/TLS quando disponível)
5. **Configure usuários com permissões mínimas necessárias**
6. **Mantenha backups regulares** de dados importantes

### Performance
1. **Feche conexões adequadamente** usando context managers (`with`)
2. **Use índices estratégicos** em colunas frequentemente consultadas
3. **Evite SELECT *** - especifique apenas as colunas necessárias
4. **Use LIMIT** em queries que podem retornar muitos resultados
5. **Analise queries lentas** usando EXPLAIN ou EXPLAIN ANALYZE
6. **Use pool de conexões** em aplicações que recebem muitas requisições

### Manutenibilidade
1. **Documente esquemas de banco** e relacionamentos
2. **Use migrations** para versionar mudanças no schema
3. **Mantenha backups testados** e procedimentos de restore
4. **Versionar scripts SQL** junto com o código da aplicação
5. **Teste queries em ambiente de desenvolvimento** antes de produção

## 📝 Diferenças Principais entre SGBDs

### SQLite vs MySQL vs PostgreSQL

| Aspecto | SQLite | MySQL | PostgreSQL |
|--------|--------|-------|------------|
| **Instalação** | Incluído no Python | Requer servidor | Requer servidor |
| **Tipo** | Arquivo único | Servidor cliente-servidor | Servidor cliente-servidor |
| **Porta padrão** | N/A (arquivo) | 3306 | 5432 |
| **Concorrência** | Limitada | Alta | Muito alta |
| **Escalabilidade** | Pequena/Média | Média/Grande | Grande/Enterprise |
| **Tipos de dados** | Básicos | Amplos | Muito amplos |
| **Conformidade SQL** | Básica | Boa | Excelente |
| **Uso ideal** | Dev, testes, apps pequenas | Apps web médias/grandes | Apps enterprise |

## ⚠️ Importante

### Segurança de Credenciais

- **NUNCA** commite arquivos `config.env` com credenciais reais
- Sempre use o arquivo `config.env.example` como template
- Em produção, use variáveis de ambiente do sistema ou serviços de secrets management
- Configure senhas fortes e usuários específicos para cada aplicação

### Testes e Desenvolvimento

- Sempre teste conexões antes de implementar lógicas mais complexas
- Use SQLite para desenvolvimento rápido e testes
- Migre para MySQL/PostgreSQL quando precisar de recursos de servidor
- Cada subdiretório possui seu próprio README.md com instruções específicas e troubleshooting

### Próximos Passos

Este módulo estabelece a base para:
- **Módulo 3 (POO)**: Integração de bancos de dados com classes e objetos
- **Módulo 5 (WebServices)**: APIs que consomem e fornecem dados de bancos
- **Módulo 6 (Django)**: Uso do ORM do Django para abstrair operações de banco

## 🏆 Checklist de Conclusão

Antes de avançar, certifique-se de:
- [ ] Conseguir conectar e executar queries em SQLite
- [ ] Entender como usar variáveis de ambiente para configurações
- [ ] Conhecer as diferenças principais entre SQLite, MySQL e PostgreSQL
- [ ] Ser capaz de executar operações CRUD básicas em Python
- [ ] Entender o uso de prepared statements e sua importância para segurança
- [ ] Saber gerenciar conexões adequadamente com context managers
- [ ] Entender o conceito de transações e quando usá-las
- [ ] (Opcional) Ter configurado e testado MySQL ou PostgreSQL localmente

## 💡 Dicas de Aprendizado

- **Comece pelo SQLite**: É a forma mais simples de começar sem configuração complexa
- **Experimente os três**: Entenda as diferenças práticas entre os SGBDs
- **Leia os READMEs específicos**: Cada subdiretório tem troubleshooting detalhado
- **Pratique SQL separadamente**: Use ferramentas gráficas para visualizar dados
- **Entenda o plano de execução**: Use EXPLAIN para entender como queries funcionam
- **Faça backups**: Pratique backup e restore regularmente
- **Teste tratamento de erros**: Veja como cada biblioteca trata diferentes erros
- **Compare abordagens**: Veja como a mesma operação é feita em cada SGBD

Este módulo é fundamental para todo desenvolvimento backend, pois praticamente todas as aplicações backend trabalham com persistência de dados.
