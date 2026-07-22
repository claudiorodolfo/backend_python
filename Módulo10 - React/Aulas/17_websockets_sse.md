## Aula 17 — WebSockets e SSE (opcional)

### Objetivos

- Saber quando usar HTTP comum vs push em tempo real
- Introdução a **WebSocket** no FastAPI + consumo no React
- Introdução a **Server-Sent Events (SSE)**

### Quando usar

- **Polling**/`refetch`: simples, funciona atrás de proxies, porém menos eficiente.
- **SSE**: servidor → cliente, one-way, boa opção via HTTP.
- **WebSocket**: canal bidirecional (chat, colaboração, jogos).

### WebSocket (FastAPI) — esboço

```python
@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"ok": True})
    await websocket.close()
```

### Cliente (browser)

```js
const ws = new WebSocket("ws://localhost:8000/ws");
ws.onmessage = (ev) => console.log(JSON.parse(ev.data));
```

### SSE (ideia)

Endpoint que retorna `text/event-stream`; no React use `EventSource` (com reconnection built-in no browser).

### Exercícios

1. Crie um endpoint WS que ecoa mensagens.
2. Monte um chat mínimo (1 sala) no React.
3. Pesquisar limites de SSE atrás de proxies/load balancers.

### Desafio

Adicione autenticação ao WebSocket (token na query string ou cookie) — atenção a vazamento em logs.
