"""
06 - Introdução a WebSockets
==============================
Diferença entre HTTP e WebSockets, casos de uso
"""

print("=" * 60)
print("INTRODUÇÃO A WEBSOCKETS")
print("=" * 60)


# ============================================
# 1. HTTP vs WEBSOCKETS
# ============================================

print("\n" + "=" * 60)
print("HTTP vs WEBSOCKETS")
print("=" * 60)

comparacao = {
    "HTTP": {
        "conexao": "Stateless - nova conexão para cada requisição",
        "comunicacao": "Request-Response (cliente solicita, servidor responde)",
        "direcao": "Cliente → Servidor (requisições)",
        "overhead": "Headers HTTP em cada requisição",
        "uso": "APIs REST, páginas web, transferência de dados",
        "exemplo": "Cliente faz GET /api/users, recebe resposta, conexão fecha"
    },
    "WebSocket": {
        "conexao": "Persistente - conexão mantida aberta",
        "comunicacao": "Full-duplex (ambos podem enviar a qualquer momento)",
        "direcao": "Bidirecional (cliente ↔ servidor)",
        "overhead": "Baixo após handshake inicial",
        "uso": "Chat, notificações em tempo real, jogos, dashboards",
        "exemplo": "Conexão aberta, servidor pode enviar atualizações instantaneamente"
    }
}

for protocolo, info in comparacao.items():
    print(f"\n{protocolo}:")
    for chave, valor in info.items():
        print(f"  {chave.title()}: {valor}")


# ============================================
# 2. COMO FUNCIONA WEBSOCKET
# ============================================

print("\n" + "=" * 60)
print("COMO FUNCIONA WEBSOCKET")
print("=" * 60)

fluxo_websocket = """
1. Handshake Inicial (HTTP):
   Cliente → GET /ws HTTP/1.1
            Upgrade: websocket
            Connection: Upgrade
   
   Servidor → HTTP/1.1 101 Switching Protocols
              Upgrade: websocket
              Connection: Upgrade

2. Conexão Estabelecida:
   - Conexão TCP mantida aberta
   - Ambos podem enviar dados a qualquer momento

3. Comunicação Bidirecional:
   Cliente → [mensagem 1]
   Servidor → [mensagem 2]
   Cliente → [mensagem 3]
   Servidor → [mensagem 4]
   ...

4. Fechamento:
   - Qualquer lado pode fechar conexão
   - Frame de fechamento enviado
"""

print(fluxo_websocket)


# ============================================
# 3. CASOS DE USO
# ============================================

print("\n" + "=" * 60)
print("CASOS DE USO PARA WEBSOCKETS")
print("=" * 60)

casos_uso = {
    "Chat em Tempo Real": {
        "descricao": "Aplicações de mensagens instantâneas",
        "porque": "Mensagens aparecem instantaneamente sem polling",
        "exemplo": "WhatsApp Web, Slack, Discord"
    },
    "Notificações Push": {
        "descricao": "Alertas e notificações instantâneas",
        "porque": "Servidor pode notificar cliente imediatamente",
        "exemplo": "Notificações de email, likes em redes sociais"
    },
    "Dashboards em Tempo Real": {
        "descricao": "Atualizações de dados ao vivo",
        "porque": "Dados atualizados sem refresh da página",
        "exemplo": "Monitoramento de servidores, analytics ao vivo"
    },
    "Jogos Online": {
        "descricao": "Multiplayer em tempo real",
        "porque": "Baixa latência para sincronização",
        "exemplo": "Jogos de ação, estratégia em tempo real"
    },
    "Colaboração em Tempo Real": {
        "descricao": "Edição colaborativa",
        "porque": "Mudanças aparecem instantaneamente para todos",
        "exemplo": "Google Docs, Figma colaborativo"
    },
    "Trading/Finanças": {
        "descricao": "Cotações de ações em tempo real",
        "porque": "Precisão e velocidade crítica",
        "exemplo": "Plataformas de trading, dashboards financeiros"
    }
}

for caso, info in casos_uso.items():
    print(f"\n{caso}:")
    print(f"  Descrição: {info['descricao']}")
    print(f"  Por quê usar WebSocket: {info['porque']}")
    print(f"  Exemplo: {info['exemplo']}")


# ============================================
# 4. QUANDO USAR HTTP vs WEBSOCKET
# ============================================

print("\n" + "=" * 60)
print("QUANDO USAR HTTP vs WEBSOCKET")
print("=" * 60)

quando_usar = """
Use HTTP/REST quando:
✓ Dados são solicitados sob demanda
✓ Não precisa de atualizações constantes
✓ Stateless é adequado
✓ Simplicidade é prioridade
✓ Exemplos: APIs REST, formulários, páginas web tradicionais

Use WebSocket quando:
✓ Precisa de atualizações em tempo real
✓ Comunicação bidirecional frequente
✓ Baixa latência é importante
✓ Muitas mensagens pequenas
✓ Exemplos: Chat, notificações, dashboards ao vivo
"""

print(quando_usar)


# ============================================
# 5. VANTAGENS E DESVANTAGENS
# ============================================

print("\n" + "=" * 60)
print("VANTAGENS E DESVANTAGENS DO WEBSOCKET")
print("=" * 60)

vantagens_desvantagens = """
VANTAGENS:
✓ Comunicação bidirecional em tempo real
✓ Baixa latência (sem overhead de headers HTTP)
✓ Eficiente para muitas mensagens pequenas
✓ Servidor pode iniciar comunicação
✓ Conexão persistente

DESVANTAGENS:
✗ Mais complexo que HTTP
✗ Requer gerenciamento de estado (conexões abertas)
✗ Mais difícil de escalar horizontalmente
✗ Proxies e load balancers podem complicar
✗ Não funciona bem com alguns firewalls/proxies
✗ Consome mais recursos (múltiplas conexões abertas)
"""

print(vantagens_desvantagens)


# ============================================
# 6. ALTERNATIVAS E COMPLEMENTOS
# ============================================

print("\n" + "=" * 60)
print("ALTERNATIVAS E TÉCNICAS RELACIONADAS")
print("=" * 60)

alternativas = {
    "Server-Sent Events (SSE)": {
        "descricao": "Servidor envia eventos para cliente",
        "direcao": "Apenas servidor → cliente",
        "vantagem": "Mais simples que WebSocket",
        "uso": "Notificações, updates unidirecionais"
    },
    "Long Polling": {
        "descricao": "Cliente faz requisição, servidor mantém aberta até ter dados",
        "direcao": "Cliente → Servidor (request), depois Servidor → Cliente (response)",
        "vantagem": "Funciona sobre HTTP",
        "uso": "Fallback quando WebSocket não disponível"
    },
    "Polling": {
        "descricao": "Cliente faz requisições periódicas",
        "direcao": "Cliente → Servidor repetidamente",
        "vantagem": "Muito simples",
        "uso": "Quando updates não precisam ser instantâneos"
    }
}

for alternativa, info in alternativas.items():
    print(f"\n{alternativa}:")
    print(f"  Descrição: {info['descricao']}")
    print(f"  Direção: {info['direcao']}")
    print(f"  Vantagem: {info['vantagem']}")
    print(f"  Uso: {info['uso']}")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - INTRODUÇÃO A WEBSOCKETS")
print("=" * 60)
print("""
Conceitos aprendidos:

1. HTTP vs WebSocket:
   - HTTP: Stateless, request-response
   - WebSocket: Conexão persistente, bidirecional

2. Quando usar:
   - HTTP: APIs REST, dados sob demanda
   - WebSocket: Tempo real, chat, notificações

3. Casos de uso:
   - Chat em tempo real
   - Notificações push
   - Dashboards ao vivo
   - Colaboração

4. Considerações:
   - Mais complexo que HTTP
   - Requer gerenciamento de conexões
   - Melhor para comunicação frequente

Próximos passos:
- Implementação básica de WebSocket
- Criar exemplo de chat simples
""")

