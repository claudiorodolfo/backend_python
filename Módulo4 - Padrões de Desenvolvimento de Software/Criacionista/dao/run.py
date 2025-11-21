"""
Exemplo de uso do padrão DAO
"""
from .dao_dicionario import DicionarioUsuarioDAO
from .dao_sqlite import SQLiteUsuarioDAO
from .dao_arquivo import ArquivoUsuarioDAO
from .service import UsuarioService
from .model import Usuario

if __name__ == "__main__":
    print("=" * 60)
    print("EXEMPLO PRÁTICO - PADRÃO DAO")
    print("=" * 60)
    
    # Escolha qual implementação usar
    # Para desenvolvimento/testes: use UsuarioDAOMock
    # Para produção: use UsuarioDAOSQLite
    
    # Exemplo com SQLite
    print("\n[Usando SQLite]")
    dao = SQLiteUsuarioDAO("usuarios_exemplo.db")
    service = UsuarioService(dao)
    
    # Criar alguns usuários
    print("\n1. Criando usuários...")
    u1 = service.cadastrarUsuario("Alice", "alice@example.com")
    u2 = service.cadastrarUsuario("Bob", "bob@example.com")
    u3 = service.cadastrarUsuario("Charlie", "charlie@example.com")
    
    print(f"   ✓ {u1}")
    print(f"   ✓ {u2}")
    print(f"   ✓ {u3}")
    
    # Listar todos
    print("\n2. Listando todos os usuários:")
    usuarios = service.listarUsuarios()
    for u in usuarios:
        print(f"   - {u}")
    
    # Buscar por ID
    print(f"\n3. Buscando usuário ID {u2.id}:")
    encontrado = service.obterUsuario(u2.id)
    print(f"   {encontrado}")
    
    # Atualizar
    print(f"\n4. Atualizando usuário ID {u1.id}:")
    service.atualizarUsuario(u1.id, "Alice Silva", "alice.silva@example.com")
    atualizado = service.obterUsuario(u1.id)
    print(f"   {atualizado}")
    
    # Deletar
    print(f"\n5. Deletando usuário ID {u3.id}:")
    service.removerUsuario(u3.id)
    print("   ✓ Usuário deletado")
    
    # Listar novamente
    print("\n6. Usuários restantes:")
    usuarios = service.listarUsuarios()
    for u in usuarios:
        print(f"   - {u}")
    
    print("\n" + "=" * 60)
    print("Exemplo concluído!")
    print("=" * 60)

