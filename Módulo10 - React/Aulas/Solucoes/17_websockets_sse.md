# Soluções — Aula 17

## Exercício 1 — WS que ecoa (FastAPI)

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def ws_echo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(data)
    except Exception:
        pass
```

## Exercício 2 — Chat mínimo no React

```jsx
import { useEffect, useRef, useState } from "react";

const WS_URL = "ws://127.0.0.1:8000/ws";

export default function ChatBasico() {
  const [msgs, setMsgs] = useState([]);
  const [input, setInput] = useState("");
  const wsRef = useRef(null);

  useEffect(() => {
    const ws = new WebSocket(WS_URL);
    wsRef.current = ws;
    ws.onmessage = (ev) => {
      setMsgs((m) => [...m, ev.data]);
    };
    return () => ws.close();
  }, []);

  function enviar() {
    const t = input.trim();
    if (!t || wsRef.current?.readyState !== WebSocket.OPEN) return;
    wsRef.current.send(t);
    setInput("");
  }

  return (
    <div>
      <ul>
        {msgs.map((m, i) => (
          <li key={i}>{m}</li>
        ))}
      </ul>
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button type="button" onClick={enviar}>
        Enviar
      </button>
    </div>
  );
}
```

> Em produção use `wss://` e trate reconexão.

## Exercício 3 — Limites do SSE atrás de proxy

Pontos para pesquisar e anotar:

- Proxies podem **bufferizar** o corpo; é preciso desativar buffering (ex.: `X-Accel-Buffering: no` no Nginx).
- Timeouts de **idle** no load balancer podem cortar conexões longas — ajuste keep-alive ou heartbeat de comentários SSE.
- Alguns intermediários não suportam `text/event-stream` bem; WebSocket pode ser preferível para bidirecional.

## Desafio — Auth no WebSocket

- **Query string:** `wss://api.example.com/ws?token=...` — funciona, mas tokens podem vazar em **logs de servidor e de proxy**; evite logar URLs completas.
- **Cookie HttpOnly:** não acessível pelo JS; o handshake envia o cookie se `SameSite`/domínio estiver correto — melhor para reduzir vazamento no cliente.
- **Primeira mensagem:** aceitar conexão e exigir JSON `{ "type": "auth", "token": "..." }` antes de entrar na sala — token não fica na URL.
