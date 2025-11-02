"""
08 - Exercício Prático: Chat com WebSocket
===========================================
Criar um canal de comunicação simples - Chat em tempo real
"""

# REQUISITOS: pip install flask flask-socketio eventlet

from flask import Flask, render_template_string, request
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS
from datetime import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chat-secret-key-123'
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

print("=" * 60)
print("EXERCÍCIO PRÁTICO: CHAT COM WEBSOCKET")
print("=" * 60)

# ============================================
# 1. ARMAZENAMENTO DE DADOS (EM MEMÓRIA)
# ============================================

usuarios = {}  # {socket_id: {"username": "...", "room": "..."}}
mensagens = []  # Histórico de mensagens
salas = {}  # {room_name: {"users": [...], "created_at": "..."}}


# ============================================
# 2. EVENTOS DE CONEXÃO
# ============================================

@socketio.on('connect')
def handle_connect():
    """Quando cliente conecta"""
    print(f"Cliente conectado: {request.sid}")
    emit('connected', {
        'message': 'Conectado ao servidor de chat',
        'socket_id': request.sid
    })


@socketio.on('disconnect')
def handle_disconnect():
    """Quando cliente desconecta"""
    socket_id = request.sid
    
    if socket_id in usuarios:
        usuario = usuarios[socket_id]
        username = usuario['username']
        room = usuario.get('room')
        
        # Remover usuário
        del usuarios[socket_id]
        
        # Se estava em uma sala, notificar
        if room:
            leave_room(room)
            socketio.emit('user_left', {
                'username': username,
                'message': f"{username} saiu",
                'timestamp': datetime.now().strftime('%H:%M:%S')
            }, room=room)
        
        print(f"Cliente desconectado: {username}")


# ============================================
# 3. ENTRAR NO CHAT
# ============================================

@socketio.on('join_chat')
def handle_join_chat(data):
    """Usuário entra no chat (define username)"""
    username = data.get('username', 'Anônimo')
    socket_id = request.sid
    
    # Verificar se username já existe
    usernames_atuais = [u['username'] for u in usuarios.values()]
    if username in usernames_atuais:
        emit('error', {
            'message': f"Username '{username}' já está em uso"
        })
        return
    
    # Adicionar usuário
    usuarios[socket_id] = {
        'username': username,
        'joined_at': datetime.now().isoformat(),
        'room': None
    }
    
    print(f"Usuário '{username}' entrou no chat")
    
    emit('joined_chat', {
        'username': username,
        'message': f"Bem-vindo ao chat, {username}!",
        'usuarios_online': list(set([u['username'] for u in usuarios.values()]))
    })
    
    # Notificar outros
    socketio.emit('user_joined', {
        'username': username,
        'message': f"{username} entrou no chat",
        'usuarios_online': list(set([u['username'] for u in usuarios.values()])),
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, broadcast=True, include_self=False)


# ============================================
# 4. ENVIAR MENSAGEM
# ============================================

@socketio.on('send_message')
def handle_send_message(data):
    """Envia mensagem no chat"""
    socket_id = request.sid
    
    if socket_id not in usuarios:
        emit('error', {'message': 'Você precisa entrar no chat primeiro'})
        return
    
    usuario = usuarios[socket_id]
    username = usuario['username']
    mensagem_texto = data.get('message', '').strip()
    
    if not mensagem_texto:
        emit('error', {'message': 'Mensagem vazia'})
        return
    
    room = usuario.get('room')
    timestamp = datetime.now().strftime('%H:%M:%S')
    
    # Criar objeto de mensagem
    mensagem = {
        'id': str(uuid.uuid4()),
        'username': username,
        'message': mensagem_texto,
        'room': room or 'global',
        'timestamp': timestamp,
        'created_at': datetime.now().isoformat()
    }
    
    # Adicionar ao histórico
    mensagens.append(mensagem)
    # Limitar histórico (manter últimas 100)
    if len(mensagens) > 100:
        mensagens.pop(0)
    
    # Enviar mensagem
    if room:
        # Enviar para sala específica
        socketio.emit('new_message', mensagem, room=room)
    else:
        # Enviar para todos (chat global)
        socketio.emit('new_message', mensagem, broadcast=True)
    
    print(f"Mensagem de {username}: {mensagem_texto}")


# ============================================
# 5. GERENCIAMENTO DE SALAS
# ============================================

@socketio.on('join_room')
def handle_join_room(data):
    """Usuário entra em uma sala"""
    socket_id = request.sid
    
    if socket_id not in usuarios:
        emit('error', {'message': 'Você precisa entrar no chat primeiro'})
        return
    
    usuario = usuarios[socket_id]
    username = usuario['username']
    room_name = data.get('room', 'default')
    
    # Sair da sala anterior se houver
    if usuario.get('room'):
        leave_room(usuario['room'])
    
    # Entrar na nova sala
    join_room(room_name)
    usuario['room'] = room_name
    
    # Criar sala se não existir
    if room_name not in salas:
        salas[room_name] = {
            'users': [],
            'created_at': datetime.now().isoformat()
        }
    
    if username not in salas[room_name]['users']:
        salas[room_name]['users'].append(username)
    
    print(f"{username} entrou na sala: {room_name}")
    
    emit('room_joined', {
        'room': room_name,
        'message': f"Você entrou na sala '{room_name}'",
        'usuarios_na_sala': salas[room_name]['users']
    })
    
    # Notificar outros na sala
    socketio.emit('user_joined_room', {
        'username': username,
        'room': room_name,
        'message': f"{username} entrou na sala",
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room_name, include_self=False)


@socketio.on('leave_room')
def handle_leave_room():
    """Usuário sai da sala"""
    socket_id = request.sid
    
    if socket_id not in usuarios:
        return
    
    usuario = usuarios[socket_id]
    username = usuario['username']
    room = usuario.get('room')
    
    if room:
        leave_room(room)
        
        if room in salas and username in salas[room]['users']:
            salas[room]['users'].remove(username)
        
        usuario['room'] = None
        
        print(f"{username} saiu da sala: {room}")
        
        emit('room_left', {
            'message': f"Você saiu da sala '{room}'"
        })
        
        socketio.emit('user_left_room', {
            'username': username,
            'room': room,
            'message': f"{username} saiu da sala",
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }, room=room)


@socketio.on('list_rooms')
def handle_list_rooms():
    """Lista todas as salas disponíveis"""
    rooms_info = {
        room: {
            'users': info['users'],
            'user_count': len(info['users'])
        }
        for room, info in salas.items()
    }
    
    emit('rooms_list', {
        'rooms': rooms_info
    })


# ============================================
# 6. OBTER HISTÓRICO DE MENSAGENS
# ============================================

@socketio.on('get_history')
def handle_get_history(data):
    """Retorna histórico de mensagens"""
    room = data.get('room', None)
    limit = data.get('limit', 50)
    
    if room:
        # Mensagens da sala
        room_messages = [m for m in mensagens if m.get('room') == room]
        historico = room_messages[-limit:]
    else:
        # Mensagens globais
        global_messages = [m for m in mensagens if not m.get('room') or m.get('room') == 'global']
        historico = global_messages[-limit:]
    
    emit('history', {
        'messages': historico,
        'total': len(historico)
    })


# ============================================
# 7. INTERFACE HTML DE TESTE
# ============================================

html_chat = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat WebSocket</title>
    <script src="https://cdn.socket.io/4.5.0/socket.io.min.js"></script>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 0 auto; padding: 20px; }
        #chat { border: 1px solid #ccc; height: 400px; overflow-y: auto; padding: 10px; margin-bottom: 10px; }
        #messageInput { width: 70%; padding: 10px; }
        button { padding: 10px 20px; }
        .message { margin: 5px 0; }
        .username { font-weight: bold; color: #007bff; }
        .timestamp { color: #666; font-size: 0.9em; }
        .system { color: #28a745; font-style: italic; }
    </style>
</head>
<body>
    <h1>Chat WebSocket</h1>
    
    <div id="loginForm">
        <input type="text" id="usernameInput" placeholder="Seu nome" />
        <button onclick="joinChat()">Entrar no Chat</button>
    </div>
    
    <div id="chatArea" style="display:none;">
        <div id="chat"></div>
        <input type="text" id="messageInput" placeholder="Digite sua mensagem..." />
        <button onclick="sendMessage()">Enviar</button>
        <button onclick="leaveRoom()">Sair da Sala</button>
    </div>
    
    <div id="rooms">
        <h3>Salas:</h3>
        <input type="text" id="roomInput" placeholder="Nome da sala" />
        <button onclick="joinRoom()">Entrar em Sala</button>
    </div>
    
    <script>
        const socket = io();
        let currentUsername = '';
        
        socket.on('connected', (data) => {
            console.log('Conectado:', data);
        });
        
        socket.on('joined_chat', (data) => {
            currentUsername = data.username;
            document.getElementById('loginForm').style.display = 'none';
            document.getElementById('chatArea').style.display = 'block';
            addMessage('system', data.message);
        });
        
        socket.on('new_message', (data) => {
            addMessage(data.username, data.message, data.timestamp);
        });
        
        socket.on('user_joined', (data) => {
            addMessage('system', data.message);
        });
        
        socket.on('error', (data) => {
            alert(data.message);
        });
        
        function joinChat() {
            const username = document.getElementById('usernameInput').value;
            if (username) {
                socket.emit('join_chat', {username: username});
            }
        }
        
        function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value;
            if (message) {
                socket.emit('send_message', {message: message});
                input.value = '';
            }
        }
        
        function joinRoom() {
            const room = document.getElementById('roomInput').value;
            if (room) {
                socket.emit('join_room', {room: room});
            }
        }
        
        function leaveRoom() {
            socket.emit('leave_room');
        }
        
        function addMessage(username, message, timestamp = '') {
            const chat = document.getElementById('chat');
            const div = document.createElement('div');
            div.className = 'message';
            
            if (username === 'system') {
                div.className += ' system';
                div.textContent = message;
            } else {
                div.innerHTML = `<span class="username">${username}</span> 
                                 <span class="timestamp">${timestamp}</span>: 
                                 ${message}`;
            }
            
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }
        
        document.getElementById('messageInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """Interface do chat"""
    return render_template_string(html_chat)


# ============================================
# RESUMO DO EXERCÍCIO
# ============================================

print("\n" + "=" * 60)
print("RESUMO DO EXERCÍCIO")
print("=" * 60)

print("""
Funcionalidades implementadas:

✓ Conexão/Desconexão de usuários
✓ Entrar no chat com username
✓ Enviar mensagens
✓ Receber mensagens em tempo real
✓ Salas (rooms) para grupos
✓ Histórico de mensagens
✓ Interface HTML de teste

Como usar:

1. Instalar dependências:
   pip install flask flask-socketio eventlet

2. Executar:
   python 08_exercicio_chat.py

3. Acessar:
   http://localhost:5000

4. Testar:
   - Abra múltiplas abas
   - Entre com diferentes usernames
   - Envie mensagens
   - Crie e entre em salas
   - Veja mensagens em tempo real

Melhorias possíveis:
- Autenticação de usuários
- Persistência em banco de dados
- Upload de arquivos/imagens
- Emojis e formatação
- Notificações
- Moderação de mensagens
""")

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("Para executar:")
    print("1. pip install flask flask-socketio eventlet")
    print("2. python 08_exercicio_chat.py")
    print("3. Acesse: http://localhost:5000")
    print("=" * 60)
    
    # Descomentar para executar:
    # socketio.run(app, debug=True, host='0.0.0.0', port=5000)

