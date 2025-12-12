# WS9 - Logging

Este projeto demonstra a implementação de logging em um servidor REST simples usando Python. O servidor registra todas as requisições, respostas, erros e eventos importantes em arquivo e no console.

## 📋 Descrição

O projeto consiste em:
- **ws_provider.py**: Servidor HTTP REST que implementa logging completo de todas as operações
- **ws_client.py**: Cliente que faz requisições ao servidor para demonstrar o funcionamento
- **server.log**: Arquivo de log gerado automaticamente pelo servidor

O servidor implementa uma API REST simples para gerenciamento de tarefas (CRUD completo) e registra todos os eventos usando o módulo `logging` do Python.

## 🔧 Requisitos

- Python 3.6 ou superior
- Biblioteca `requests` (para o cliente)

### Instalação das dependências

```bash
pip install requests
```

## 🚀 Como Executar

### 1. Iniciar o Servidor

Execute o servidor em um terminal:

```bash
python ws_provider.py
```

O servidor será iniciado em `http://127.0.0.1:8082` e ficará aguardando requisições.

Você verá mensagens como:
```
2024-01-15 10:30:45 - WSProvider - INFO - ============================================================
2024-01-15 10:30:45 - WSProvider - INFO - Servidor REST com Logging iniciado
2024-01-15 10:30:45 - WSProvider - INFO - URL: http://127.0.0.1:8082
...
```

### 2. Executar o Cliente

Em outro terminal, execute o cliente:

```bash
python ws_client.py
```

O cliente fará várias requisições ao servidor demonstrando todas as operações CRUD e você verá os logs sendo gerados tanto no console quanto no arquivo `server.log`.

## 📡 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/tarefas` | Lista todas as tarefas |
| GET | `/tarefa/{id}` | Busca uma tarefa específica |
| GET | `/status` | Verifica o status do servidor |
| POST | `/tarefa` | Cria uma nova tarefa |
| PUT | `/tarefa/{id}` | Atualiza uma tarefa existente |
| DELETE | `/tarefa/{id}` | Deleta uma tarefa |

### Exemplos de Requisições

#### Listar todas as tarefas
```bash
curl http://127.0.0.1:8082/tarefas
```

#### Buscar uma tarefa
```bash
curl http://127.0.0.1:8082/tarefa/1
```

#### Criar uma nova tarefa
```bash
curl -X POST http://127.0.0.1:8082/tarefa \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Nova tarefa"}'
```

#### Atualizar uma tarefa
```bash
curl -X PUT http://127.0.0.1:8082/tarefa/1 \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Tarefa atualizada", "concluida": true}'
```

#### Deletar uma tarefa
```bash
curl -X DELETE http://127.0.0.1:8082/tarefa/1
```

#### Verificar status
```bash
curl http://127.0.0.1:8082/status
```

## 📝 Logging

### Níveis de Log Utilizados

O servidor utiliza diferentes níveis de log conforme a importância do evento:

- **INFO**: Requisições recebidas, operações bem-sucedidas, início do servidor
- **DEBUG**: Detalhes de parâmetros, corpo das requisições, respostas enviadas
- **WARNING**: Rotas não encontradas, tentativas de operações inválidas
- **ERROR**: Erros ao processar requisições, exceções capturadas

### Formato dos Logs

Os logs são formatados com:
- Timestamp (data e hora)
- Nome do logger
- Nível do log
- Mensagem descritiva

Exemplo:
```
2024-01-15 10:30:45 - WSProvider - INFO - Requisição GET recebida: /tarefas - IP: 127.0.0.1
2024-01-15 10:30:45 - WSProvider - INFO - Listando todas as tarefas
2024-01-15 10:30:45 - WSProvider - DEBUG - Resposta enviada: Status 200 - {'tarefas': [...], 'total': 2}
```

### O que é Registrado

O servidor registra:

✓ **Requisições recebidas**
- Método HTTP (GET, POST, PUT, DELETE)
- Caminho da requisição
- IP do cliente
- Parâmetros de query (em nível DEBUG)

✓ **Operações realizadas**
- Criação de tarefas
- Atualização de tarefas
- Deleção de tarefas
- Busca de tarefas

✓ **Respostas enviadas**
- Status code HTTP
- Dados da resposta (em nível DEBUG)

✓ **Erros e exceções**
- Erros ao processar requisições
- Erros de validação
- Exceções não tratadas (com stack trace)

✓ **Avisos**
- Rotas não encontradas
- Tentativas de operações inválidas

### Localização dos Logs

Os logs são salvos em dois lugares:

1. **Console**: Logs são exibidos no terminal onde o servidor está rodando
2. **Arquivo**: Todos os logs são salvos no arquivo `server.log` na mesma pasta do servidor

## 📖 Como Funciona

### Servidor (ws_provider.py)

1. **Configuração de Logging**:
   - Configura o módulo `logging` com nível INFO
   - Cria handlers para console e arquivo
   - Define formato personalizado para os logs

2. **Processamento de Requisições**:
   - Cada método HTTP (GET, POST, PUT, DELETE) registra a requisição recebida
   - Processa a requisição e registra o resultado
   - Envia resposta e registra o status

3. **Tratamento de Erros**:
   - Captura exceções e registra com nível ERROR
   - Inclui stack trace para facilitar debug
   - Retorna respostas de erro apropriadas

### Cliente (ws_client.py)

O cliente demonstra todas as operações CRUD:
- Lista tarefas
- Busca tarefas específicas
- Cria novas tarefas
- Atualiza tarefas existentes
- Deleta tarefas
- Verifica status do servidor

## 💡 Exemplos de Uso

### Exemplo 1: Criar e Listar Tarefas

```python
from ws_client import RESTCliente

cliente = RESTCliente()

# Criar tarefas
cliente.criar_tarefa("Estudar Python")
cliente.criar_tarefa("Fazer exercícios")

# Listar todas
cliente.listar_tarefas()
```

### Exemplo 2: Atualizar Tarefa

```python
# Marcar tarefa como concluída
cliente.atualizar_tarefa(1, concluida=True)

# Atualizar título
cliente.atualizar_tarefa(1, titulo="Estudar Python Avançado")
```

### Exemplo 3: Deletar Tarefa

```python
cliente.deletar_tarefa(1)
```

## 🔍 Visualizando os Logs

### No Console

Os logs aparecem em tempo real no terminal onde o servidor está rodando.

### No Arquivo

Para visualizar os logs salvos:

```bash
# Ver todo o arquivo
cat server.log

# Ver últimas 20 linhas
tail -n 20 server.log

# Acompanhar logs em tempo real
tail -f server.log
```

### Exemplo de Logs Gerados

```
2024-01-15 10:30:45 - WSProvider - INFO - ============================================================
2024-01-15 10:30:45 - WSProvider - INFO - Servidor REST com Logging iniciado
2024-01-15 10:30:45 - WSProvider - INFO - URL: http://127.0.0.1:8082
2024-01-15 10:30:50 - WSProvider - INFO - Requisição GET recebida: /status - IP: 127.0.0.1
2024-01-15 10:30:50 - WSProvider - INFO - Verificando status do servidor
2024-01-15 10:30:51 - WSProvider - INFO - Requisição GET recebida: /tarefas - IP: 127.0.0.1
2024-01-15 10:30:51 - WSProvider - INFO - Listando todas as tarefas
2024-01-15 10:30:52 - WSProvider - INFO - Requisição POST recebida: /tarefa - IP: 127.0.0.1
2024-01-15 10:30:52 - WSProvider - INFO - Tarefa criada com sucesso: ID 3 - Estudar Python
```

## 📝 Estrutura do Código

### ws_provider.py

- **Configuração de Logging**: Setup do módulo logging com handlers
- **WSProvider**: Classe principal que herda de `BaseHTTPRequestHandler`
- **Métodos HTTP**: `do_GET()`, `do_POST()`, `do_PUT()`, `do_DELETE()`
- **Métodos auxiliares**: `_buscar_tarefa()`, `_enviar_resposta()`
- **Dados**: Lista `tarefas` em memória (simulando banco de dados)

### ws_client.py

- **RESTCliente**: Classe cliente para fazer requisições
- **Métodos CRUD**: Implementação de todas as operações
- **Tratamento de erros**: Captura e exibe erros de forma amigável

## 🛠️ Personalização

### Alterar Nível de Log

Para ver mais detalhes (incluindo logs DEBUG), altere a linha 10 em `ws_provider.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Mude de INFO para DEBUG
    ...
)
```

### Alterar Porta do Servidor

Modifique a linha 189 em `ws_provider.py`:

```python
servidor = HTTPServer(('127.0.0.1', 8080), WSProvider)  # Porta 8080
```

E atualize a URL no cliente:

```python
cliente = RESTCliente("http://127.0.0.1:8080")
```

### Alterar Nome do Arquivo de Log

Modifique a linha 15 em `ws_provider.py`:

```python
logging.FileHandler('meus_logs.log'),  # Novo nome do arquivo
```

## 📚 Conceitos Demonstrados

Este projeto demonstra:

1. **Configuração de Logging**:
   - Uso do módulo `logging` do Python
   - Configuração de handlers (console e arquivo)
   - Formatação personalizada de logs

2. **Níveis de Log**:
   - Quando usar INFO, DEBUG, WARNING, ERROR
   - Diferença entre níveis de log

3. **Logging em Aplicações Web**:
   - Como registrar requisições HTTP
   - Como registrar respostas
   - Como registrar erros e exceções

4. **Boas Práticas**:
   - Logging estruturado
   - Contexto relevante nos logs
   - Não logar dados sensíveis
   - Uso apropriado de níveis

## 🔐 Segurança

**Nota**: Este é um exemplo educacional. Em produção, considere:

- Usar HTTPS em vez de HTTP
- Implementar autenticação e autorização
- Validar e sanitizar todas as entradas
- Implementar rate limiting
- Rotacionar arquivos de log
- Não logar dados sensíveis (senhas, tokens, etc.)
- Implementar rotação de logs para evitar arquivos muito grandes

## 📊 Benefícios do Logging

- **Debug**: Facilita identificar problemas em produção
- **Monitoramento**: Acompanha o comportamento da aplicação
- **Auditoria**: Registra todas as operações realizadas
- **Análise**: Permite analisar padrões de uso
- **Troubleshooting**: Ajuda a resolver problemas rapidamente

