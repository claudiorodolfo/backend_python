"""
07 - Implementação Básica de WebSocket
========================================
Exemplo prático de implementação de WebSocket com Flask-SocketIO
"""

# NOTA: Este exemplo requer flask-socketio
# Instale com: pip install flask-socketio

from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

print("=" * 60)
print("IMPLEMENTAÇÃO BÁSICA DE WEBSOCKET")
print("=" * 60)

# ============================================
# 1. INSTALAÇÃO
# ============================================

print("\n" + "=" * 60)
print("INSTALAÇÃO")
print("=" * 60)

instalacao = """
Para usar WebSockets com Flask, instale:

pip install flask-socketio

Flask-SocketIO usa um dos seguintes dependendo do servidor:
- eventlet (recomendado)
- gevent
- gevent-websocket

Para produção com eventlet:
pip install flask-socketio eventlet
"""

print(instalacao)

# ============================================
# 2. APLICAÇÃO BÁSICA
# ============================================

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'
CORS(app)

# Criar instância do SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")


# ============================================
# 3. EVENTOS DE CONEXÃO
# ============================================

@socketio.on('connect')
def handle_connect():
    """Quando cliente conecta"""
    print(f"Cliente conectado: {request.sid}")
    emit('message', {
        'type': 'system',
        'message': 'Você está conectado!'
    })


@socketio.on('disconnect')
def handle_disconnect():
    """Quando cliente desconecta"""
    print(f"Cliente desconectado: {request.sid}")


# ============================================
# 4. COMUNICAÇÃO BIDIRECIONAL SIMPLES
# ============================================

@socketio.on('message')
def handle_message(data):
    """Recebe mensagem do cliente"""
    print(f"Mensagem recebida: {data}")
    
    # Echo: enviar mensagem de volta
    emit('message', {
        'type': 'echo',
        'message': f"Echo: {data.get('message', '')}"
    })


@socketio.on('send_message')
def handle_send_message(data):
    """Recebe e processa mensagem do cliente"""
    mensagem = data.get('message', '')
    usuario = data.get('usuario', 'Anônimo')
    
    # Broadcast para todos os clientes conectados
    socketio.emit('broadcast_message', {
        'usuario': usuario,
        'message': mensagem,
        'timestamp': '2024-01-15 10:30:00'  # Em produção, usar datetime
    })


# ============================================
# 5. SALAS (ROOMS) - GRUPOS DE CONEXÕES
# ============================================

@socketio.on('join_room')
def handle_join_room(data):
    """Cliente entra em uma sala"""
    room = data.get('room', 'default')
    usuario = data.get('usuario', 'Anônimo')
    
    join_room(room)
    print(f"{usuario} entrou na sala: {room}")
    
    # Notificar outros na sala
    socketio.emit('room_message', {
        'type': 'user_joined',
        'usuario': usuario,
        'message': f"{usuario} entrou na sala"
    }, room=room)


@socketio.on('leave_room')
def handle_leave_room(data):
    """Cliente sai de uma sala"""
    room = data.get('room', 'default')
    usuario = data.get('usuario', 'Anônimo')
    
    leave_room(room)
    print(f"{usuario} saiu da sala: {room}")
    
    socketio.emit('room_message', {
        'type': 'user_left',
        'usuario': usuario,
        'message': f"{usuario} saiu da sala"
    }, room=room)


@socketio.on('room_message')
def handle_room_message(data):
    """Mensagem enviada para uma sala específica"""
    room = data.get('room', 'default')
    usuario = data.get('usuario', 'Anônimo')
    mensagem = data.get('message', '')
    
    # Enviar apenas para clientes na sala
    socketio.emit('room_message', {
        'type': 'message',
        'usuario': usuario,
        'message': mensagem
    }, room=room)


# ============================================
# 6. EXEMPLO: CHAT SIMPLES
# ============================================

usuarios_conectados = {}  # {socket_id: username}

@socketio.on('chat_join')
def handle_chat_join(data):
    """Usuário entra no chat"""
    username = data.get('username', 'Anônimo')
    usuarios_conectados[request.sid] = username
    
    # Notificar todos
    socketio.emit('chat_update', {
        'type': 'user_joined',
        'username': username,
        'message': f"{username} entrou no chat",
        'usuarios_online': list(usuarios_conectados.values())
    }, broadcast=True)


@socketio.on('chat_message')
def handle_chat_message(data):
    """Mensagem no chat"""
    username = usuarios_conectados.get(request.sid, 'Anônimo')
    mensagem = data.get('message', '')
    
    # Enviar para todos
    socketio.emit('chat_message', {
        'username': username,
        'message': mensagem,
        'timestamp': '2024-01-15 10:30:00'
    }, broadcast=True)


@socketio.on('chat_leave')
def handle_chat_leave():
    """Usuário sai do chat"""
    username = usuarios_conectados.pop(request.sid, 'Anônimo')
    
    socketio.emit('chat_update', {
        'type': 'user_left',
        'username': username,
        'message': f"{username} saiu do chat",
        'usuarios_online': list(usuarios_conectados.values())
    }, broadcast=True)


# ============================================
# 7. HTML DE TESTE (OPCIONAL)
# ============================================

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Test</title>
    <script src="https://cdn.socket.io/4.5.0/socket.io.min.js"></script>
</head>
<body>
    <h1>Teste de WebSocket</h1>
    <div id="messages"></div>
    <input type="text" id="messageInput" placeholder="Digite uma mensagem">
    <button onclick="sendMessage()">Enviar</button>
    
    <script>
        const socket = io();
        
        socket.on('message', (data) => {
            const div = document.createElement('div');
            div.textContent = data.message;
            document.getElementById('messages').appendChild(div);
        });
        
        function sendMessage() {
            const input = document.getElementById('messageInput');
            socket.emit('message', {message: input.value});
            input.value = '';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Página de teste"""
    return render_template_string(html_template)


# ============================================
# 8. EXEMPLO DE USO COM PYTHON CLIENTE
# ============================================

print("\n" + "=" * 60)
print("EXEMPLO DE CLIENTE PYTHON")
print("=" * 60)

exemplo_cliente = """
# Instalar: pip install python-socketio

import socketio

# Criar cliente
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Conectado ao servidor')

@sio.on('message')
def on_message(data):
    print(f'Mensagem recebida: {data}')

# Conectar
sio.connect('http://localhost:5000')

# Enviar mensagem
sio.emit('message', {'message': 'Olá do cliente Python!'})

# Desconectar
sio.disconnect()
"""

print(exemplo_cliente)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - IMPLEMENTAÇÃO WEBSOCKET")
print("=" * 60)
print("""
Conceitos implementados:

1. Conexão:
   - @socketio.on('connect')
   - @socketio.on('disconnect')

2. Comunicação:
   - emit() - envia mensagem
   - broadcast=True - para todos
   - room= - para sala específica

3. Eventos customizados:
   - @socketio.on('evento_personalizado')
   - Cliente e servidor definem eventos

4. Salas:
   - join_room()
   - leave_room()
   - Mensagens para salas específicas

Próximos passos:
- Criar exercício prático de chat
- Adicionar autenticação
- Implementar em produção
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("1. Instale: pip install flask-socketio eventlet")
    print("2. Execute: python 07_websockets_exemplo.py")
    print("3. Acesse: http://localhost:5000")
    print("=" * 60)
    
    # Descomentar para executar:
    # socketio.run(app, debug=True, port=5000)

