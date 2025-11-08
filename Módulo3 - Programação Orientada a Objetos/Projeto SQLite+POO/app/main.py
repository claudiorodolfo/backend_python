"""
Sistema principal de gerenciamento com menu unificado
Permite ao usuário escolher entre gerenciar Categorias, Usuários (com Pessoa) ou Disciplinas
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection

# Importar serviços
from categoria_service import CategoriaService
from usuario_service import UsuarioService
from disciplina_service import DisciplinaService


class SistemaPrincipal:
    
    def __init__(self, db: DatabaseConnection):
        self.__db = db
        self.__categoriaService = CategoriaService(db)
        self.__usuarioService = UsuarioService(db)
        self.__disciplinaService = DisciplinaService(db)
    
    def exibirMenuPrincipal(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("     SISTEMA DE GERENCIAMENTO")
        print("="*50)
        print("1. Gerenciar Categorias")
        print("2. Gerenciar Usuários + Pessoa")
        print("3. Gerenciar Disciplinas")
        print("0. Sair")
        print("="*50)
        print("ℹ️  Nota: Ao criar um Usuário, a Pessoa é criada automaticamente!")
        print("="*50)
    
    def executar(self):
        """Método principal que executa o loop do menu"""
        try:
            while True:
                self.exibirMenuPrincipal()
                opcao = input("\nEscolha uma opção: ").strip()
                
                if opcao == '0':
                    print("\n👋 Encerrando o sistema...")
                    break
                elif opcao == '1':
                    print("\n" + "="*50)
                    print("  ENTRANDO NO GERENCIAMENTO DE CATEGORIAS")
                    print("="*50)
                    self.__categoriaService.executar()
                elif opcao == '2':
                    print("\n" + "="*50)
                    print("  ENTRANDO NO GERENCIAMENTO DE USUÁRIOS")
                    print("="*50)
                    self.__usuarioService.executar()
                elif opcao == '3':
                    print("\n" + "="*50)
                    print("  ENTRANDO NO GERENCIAMENTO DE DISCIPLINAS")
                    print("="*50)
                    self.__disciplinaService.executar()
                else:
                    print("❌ Opção inválida! Tente novamente.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário.")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Função principal para executar o sistema"""
    db = DatabaseConnection('exemplo_bd.db')
    
    try:
        # Conectar ao banco
        db.conectar()
        
        # Garantir que as tabelas existam
        db.criarTabelas()
        
        # Criar e executar o sistema principal
        sistema = SistemaPrincipal(db)
        sistema.executar()
    
    except Exception as e:
        print(f"❌ Erro ao inicializar o sistema: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.fechar()
        print("✓ Conexão com banco de dados encerrada.")


if __name__ == "__main__":
    main()

