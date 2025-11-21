"""
Padrão DAO (Data Access Object) - Exemplo de uso
=================================================

Este arquivo demonstra o uso do padrão DAO.
As classes foram separadas em módulos distintos:
- model.py: Classe Usuario
- dao_interface.py: Interface UsuarioDAO
- dao_sqlite.py: Implementação SQLiteUsuarioDAO
- dao_dicionario.py: Implementação DicionarioUsuarioDAO
- dao_arquivo.py: Implementação ArquivoUsuarioDAO
- service.py: Classe UsuarioService
"""

from .model import Usuario
from .dao_interface import UsuarioDAO
from .dao_sqlite import SQLiteUsuarioDAO
from .dao_dicionario import DicionarioUsuarioDAO
from .dao_arquivo import ArquivoUsuarioDAO
from .service import UsuarioService


if __name__ == "__main__":
    print("=" * 60)
    print("DEMONSTRAÇÃO DO PADRÃO DAO")
    print("=" * 60)
    
    # Exemplo 1: Usando DAO SQLite
    print("\n1. Usando DAO SQLite:")
    print("-" * 60)
    daoSqlite = SQLiteUsuarioDAO("exemplo_usuarios.db")
    service = UsuarioService(daoSqlite)
    
    # Criar usuários
    usuario1 = service.cadastrarUsuario("João Silva", "joao@email.com")
    usuario2 = service.cadastrarUsuario("Maria Santos", "maria@email.com")
    print(f"Criado: {usuario1}")
    print(f"Criado: {usuario2}")
    
    # Listar todos
    print("\nTodos os usuários:")
    for usuario in service.listarUsuarios():
        print(f"  - {usuario}")
    
    # Buscar por ID
    usuarioEncontrado = service.obterUsuario(usuario1.id)
    print(f"\nUsuário encontrado: {usuarioEncontrado}")
    
    # Atualizar
    service.atualizarUsuario(usuario1.id, "João Silva Jr", "joao.silva@email.com")
    print(f"\nApós atualização: {service.obterUsuario(usuario1.id)}")
    
    # Exemplo 2: Usando DAO Dicionário (para testes)
    print("\n\n2. Usando DAO Dicionário (para testes):")
    print("-" * 60)
    daoDicionario  = DicionarioUsuarioDAO()
    serviceDicionario = UsuarioService(daoDicionario)
    
    usuario3 = serviceDicionario.cadastrarUsuario("Pedro Costa", "pedro@email.com")
    usuario4 = serviceDicionario.cadastrarUsuario("Ana Lima", "ana@email.com")
    print(f"Criado: {usuario3}")
    print(f"Criado: {usuario4}")
    
    print("\nTodos os usuários (Dicionario):")
    for usuario in serviceDicionario.listarUsuarios():
        print(f"  - {usuario}")
    
    # Exemplo 3: Usando DAO Arquivo (persistência em JSON)
    print("\n\n3. Usando DAO Arquivo (persistência em JSON):")
    print("-" * 60)
    daoArquivo = ArquivoUsuarioDAO("usuarios.txt")
    serviceArquivo = UsuarioService(daoArquivo)
    
    usuario5 = serviceArquivo.cadastrarUsuario("Carlos Oliveira", "carlos@email.com")
    usuario6 = serviceArquivo.cadastrarUsuario("Julia Ferreira", "julia@email.com")
    print(f"Criado: {usuario5}")
    print(f"Criado: {usuario6}")
    
    print("\nTodos os usuários (Arquivo):")
    for usuario in serviceArquivo.listarUsuarios():
        print(f"  - {usuario}")
    
    # Buscar por ID
    usuarioEncontradoArquivo = serviceArquivo.obterUsuario(usuario5.id)
    print(f"\nUsuário encontrado: {usuarioEncontradoArquivo}")
    
    # Atualizar
    serviceArquivo.atualizarUsuario(usuario5.id, "Carlos Oliveira Jr", "carlos.oliveira@email.com")
    print(f"\nApós atualização: {serviceArquivo.obterUsuario(usuario5.id)}")

