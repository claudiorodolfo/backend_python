import asyncio
import websockets

HOST = 'localhost'
PORT = 8765

async def main():
    """Função principal do cliente"""
    print("=" * 60)
    print("Cliente WebSocket - Testando Conexão")
    print("=" * 60)
    
    uri = f"ws://{HOST}:{PORT}"
    print(f"\nConectando ao servidor {uri}...")
    
    try:
        async with websockets.connect(uri) as websocket:
            print("✓ Conexão WebSocket estabelecida!")
            print("✓ Handshake WebSocket concluído com sucesso!")
            
            # Enviar algumas mensagens de teste
            mensagens_teste = [
                "Olá, servidor!",
                "Esta é uma mensagem de teste",
                "WebSocket funcionando!"
            ]
            
            for i, msg in enumerate(mensagens_teste, 1):
                print(f"\n{i}. Enviando mensagem: {msg}")
                await websocket.send(msg)
                
                # Receber resposta
                resposta = await websocket.recv()
                print(f"   Resposta recebida: {resposta}")
            
            print("\n" + "=" * 60)
            print("Teste concluído com sucesso!")
            print("=" * 60)
            
    except websockets.exceptions.InvalidURI:
        print(f"\n✗ Erro: URI inválida: {uri}")
    except websockets.exceptions.ConnectionRefused:
        print(f"\n✗ Erro: Conexão recusada")
        print("Certifique-se de que o servidor está rodando em localhost:8765")
    except websockets.exceptions.InvalidStatusCode as e:
        print(f"\n✗ Erro: Status code inválido: {e}")
    except Exception as e:
        print(f"\n✗ Erro: {e}")
    finally:
        print("\nConexão fechada.")

if __name__ == "__main__":
    asyncio.run(main())
