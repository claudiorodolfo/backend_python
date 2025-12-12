import asyncio
import websockets

HOST = '0.0.0.0'
PORT = 8765

async def handler(websocket, path):
    """Handler para cada conexão WebSocket"""
    client_address = websocket.remote_address
    print(f"Conexão de {client_address}")
    print("Handshake WebSocket concluído!")
    print("Aguardando mensagens... (Ctrl+C para encerrar)")
    
    try:
        async for mensagem in websocket:
            print(f"Mensagem recebida: {mensagem}")
            
            # Enviar echo da mensagem
            resposta = f"Echo: {mensagem}"
            await websocket.send(resposta)
            print(f"Resposta enviada: {resposta}")
            
    except websockets.exceptions.ConnectionClosed:
        print("Conexão fechada pelo cliente")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print("Conexão encerrada")

async def main():
    """Função principal do servidor"""
    print(f"WebSocket ouvindo em {HOST}:{PORT}")
    
    async with websockets.serve(handler, HOST, PORT):
        await asyncio.Future()  # Roda indefinidamente

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
