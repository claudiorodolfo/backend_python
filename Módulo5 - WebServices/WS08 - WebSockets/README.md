# WS8 - WebSockets

Este projeto demonstra a implementação de um servidor e cliente WebSocket.

## 📋 Descrição

O projeto consiste em:
- **ws_provider.py**: Servidor WebSocket que recebe mensagens e envia echo das respostas
- **ws_client.py**: Cliente WebSocket que conecta ao servidor e envia mensagens de teste

O servidor implementa o protocolo WebSocket completo usando a biblioteca `websockets`, incluindo:
1. Handshake HTTP inicial (upgrade para WebSocket)
2. Codificação/decodificação de frames WebSocket
3. Comunicação bidirecional em tempo real
4. Echo de mensagens recebidas
5. Suporte a múltiplas conexões simultâneas (assíncrono)

## 🔧 Requisitos

- **Python 3.7 ou superior** (requer suporte a `asyncio`)
- **Biblioteca `websockets`** - Biblioteca para trabalhar com WebSockets

### Verificação da versão do Python

```bash
python --version
# ou
python3 --version
```

### Instalação da biblioteca websockets

Instale a biblioteca `websockets` usando pip:

```bash
pip install websockets
# ou
pip3 install websockets
```

### Bibliotecas utilizadas

- `websockets` - Biblioteca para implementação de servidor e cliente WebSocket
- `asyncio` - Biblioteca padrão do Python para programação assíncrona

## 🚀 Como Executar

### 1. Iniciar o Servidor

Execute o servidor em um terminal:

```bash
cd "Módulo5 - WebServices/WS8 - WebSockets"
python ws_provider.py
```

Ou usando Python 3 explicitamente:

```bash
python3 ws_provider.py
```

O servidor será iniciado em `0.0.0.0:8765` e ficará aguardando conexões.

Você verá a mensagem:
```
WebSocket ouvindo em 0.0.0.0:8765
```

Quando um cliente conectar, você verá:
```
Conexão de ('127.0.0.1', 54321)
Handshake WebSocket concluído!
Aguardando mensagens... (Ctrl+C para encerrar)
```

### 2. Executar o Cliente

Em **outro terminal**, execute o cliente:

```bash
cd "Módulo5 - WebServices/WS8 - WebSockets"
python ws_client.py
```

O cliente fará:
1. Conectar ao servidor via TCP
2. Realizar o handshake WebSocket
3. Enviar 3 mensagens de teste
4. Receber e exibir as respostas (echo) do servidor
5. Fechar a conexão

### 3. Executar em Paralelo

Para testar corretamente, você precisa ter **dois terminais abertos**:

**Terminal 1 (Servidor):**
```bash
python ws_provider.py
```

**Terminal 2 (Cliente):**
```bash
python ws_client.py
```

## 📖 Como Funciona

### Protocolo WebSocket

O WebSocket é um protocolo de comunicação bidirecional que permite comunicação em tempo real entre cliente e servidor. O processo envolve:

#### 1. Handshake Inicial (HTTP)

O cliente envia uma requisição HTTP especial:

```
GET / HTTP/1.1
Host: localhost:8765
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: <chave-aleatória>
Sec-WebSocket-Version: 13
```

O servidor responde com:

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: <chave-aceita>
```

#### 2. Comunicação via Frames

Após o handshake, a comunicação ocorre através de **frames WebSocket**:

- **Frame de Texto**: Contém dados de texto codificados em UTF-8
- **Frame de Fechamento**: Indica que a conexão será fechada
- **Masking**: Clientes devem mascarar os dados enviados (servidores não)

> **Nota**: A biblioteca `websockets` gerencia automaticamente toda a codificação/decodificação de frames, então você não precisa se preocupar com os detalhes técnicos de baixo nível.

### Servidor (ws_provider.py)

#### Funções Principais

1. **`handler(websocket, path)`**: Função assíncrona que gerencia cada conexão WebSocket
   - Recebe mensagens do cliente usando `async for`
   - Envia respostas usando `await websocket.send()`
   - Trata desconexões e erros automaticamente

2. **`main()`**: Função assíncrona principal que inicia o servidor
   - Cria o servidor WebSocket usando `websockets.serve()`
   - Fica aguardando conexões indefinidamente

#### Fluxo de Execução

1. Inicia o servidor WebSocket na porta 8765 usando `websockets.serve()`
2. Para cada nova conexão, cria uma tarefa assíncrona executando o `handler`
3. O handler recebe mensagens do cliente automaticamente
4. Para cada mensagem recebida, envia um echo de volta
5. A biblioteca `websockets` gerencia automaticamente:
   - Handshake HTTP inicial
   - Codificação/decodificação de frames
   - Tratamento de erros e desconexões

### Cliente (ws_client.py)

#### Funções Principais

1. **`main()`**: Função assíncrona principal do cliente
   - Conecta ao servidor usando `websockets.connect()`
   - Envia mensagens usando `await websocket.send()`
   - Recebe mensagens usando `await websocket.recv()`

#### Fluxo de Execução

1. Conecta ao servidor usando `websockets.connect()` (gerencia handshake automaticamente)
2. Envia 3 mensagens de teste usando `await websocket.send()`
3. Recebe e exibe as respostas usando `await websocket.recv()`
4. A biblioteca `websockets` gerencia automaticamente:
   - Handshake HTTP inicial
   - Codificação/decodificação de frames
   - Masking de frames (requisito do protocolo)
   - Fechamento da conexão

## 🧪 Testando com Outras Ferramentas

### Usando wscat (Node.js)

Se você tiver Node.js instalado, pode usar `wscat`:

```bash
# Instalar wscat globalmente
npm install -g wscat

# Conectar ao servidor
wscat -c ws://localhost:8765
```

Depois de conectar, você pode digitar mensagens e ver as respostas.

### Usando curl (HTTP/1.1 Handshake apenas)

O `curl` pode fazer o handshake inicial, mas não suporta frames WebSocket completos:

```bash
curl -i -N \
  -H "Connection: Upgrade" \
  -H "Upgrade: websocket" \
  -H "Sec-WebSocket-Key: SGVsbG8sIHdvcmxkIQ==" \
  -H "Sec-WebSocket-Version: 13" \
  http://localhost:8765/
```

Isso mostrará apenas a resposta do handshake (101 Switching Protocols), mas não permitirá comunicação bidirecional completa.

### Usando Python Interativo

Você pode criar um cliente simples no Python interativo usando a biblioteca `websockets`:

```python
import asyncio
import websockets

async def testar():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Enviar mensagem
        await websocket.send("Teste")
        
        # Receber resposta
        resposta = await websocket.recv()
        print(f"Resposta: {resposta}")

# Executar
asyncio.run(testar())
```

## 🔍 Exemplo de Saída

### Saída do Servidor

```
WebSocket ouvindo em 0.0.0.0:8765
Conexão de ('127.0.0.1', 54321)
Handshake WebSocket concluído!
Aguardando mensagens... (Ctrl+C para encerrar)
Mensagem recebida: Olá, servidor!
Resposta enviada: Echo: Olá, servidor!
Mensagem recebida: Esta é uma mensagem de teste
Resposta enviada: Echo: Esta é uma mensagem de teste
Mensagem recebida: WebSocket funcionando!
Resposta enviada: Echo: WebSocket funcionando!
Conexão fechada pelo cliente
Conexão encerrada
```

### Saída do Cliente

```
============================================================
Cliente WebSocket - Testando Conexão
============================================================

Conectando ao servidor ws://localhost:8765...
✓ Conexão WebSocket estabelecida!
✓ Handshake WebSocket concluído com sucesso!

1. Enviando mensagem: Olá, servidor!
   Resposta recebida: Echo: Olá, servidor!

2. Enviando mensagem: Esta é uma mensagem de teste
   Resposta recebida: Echo: Esta é uma mensagem de teste

3. Enviando mensagem: WebSocket funcionando!
   Resposta recebida: Echo: WebSocket funcionando!

============================================================
Teste concluído com sucesso!
============================================================

Conexão fechada.
```

## ⚠️ Observações Importantes

1. **Porta**: O servidor usa a porta `8765` por padrão. Certifique-se de que ela está disponível.

2. **Múltiplas conexões**: A implementação usa `asyncio` e suporta múltiplas conexões simultâneas. Cada conexão é gerenciada de forma assíncrona.

3. **Mensagens grandes**: A biblioteca `websockets` gerencia automaticamente mensagens de qualquer tamanho, incluindo frames fragmentados.

4. **Segurança**: Esta é uma implementação educacional. Para produção, considere:
   - Autenticação/autorização
   - WSS (WebSocket Secure) com TLS/SSL
   - Validação de origem (Origin header)
   - Rate limiting
   - Tratamento de erros mais robusto

5. **Encerramento**: Para encerrar o servidor, use `Ctrl+C` no terminal onde ele está rodando.

## 🐛 Solução de Problemas

### Erro: "Address already in use"

A porta 8765 já está em uso. Soluções:
- Feche outros processos usando a porta
- Altere a porta no código: modifique a constante `PORT` nos arquivos `ws_provider.py` e `ws_client.py`

### Erro: "Connection refused"

O servidor não está rodando. Certifique-se de:
- Ter iniciado o servidor primeiro (`python ws_provider.py`)
- Estar usando o host e porta corretos

### Erro: "ModuleNotFoundError: No module named 'websockets'"

A biblioteca `websockets` não está instalada. Instale usando:
```bash
pip install websockets
```

### Erro: "RuntimeError: This event loop is already running"

Isso pode ocorrer em alguns ambientes (como Jupyter). Use `nest_asyncio` ou execute o código em um script Python normal.

### Mensagens não aparecem

- Verifique se ambos os programas estão rodando
- Confirme que o handshake foi concluído com sucesso (mensagem "101 Switching Protocols")
- Verifique se há erros no console

## 📚 Referências

- [RFC 6455 - The WebSocket Protocol](https://tools.ietf.org/html/rfc6455)
- [MDN Web Docs - WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [websockets library documentation](https://websockets.readthedocs.io/)
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html)

## 📝 Licença

Este é um projeto educacional para demonstração do protocolo WebSocket.

