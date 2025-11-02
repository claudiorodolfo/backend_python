"""
Serviço para interação do usuário via linha de comando com a entidade Categoria
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria


class CategoriaService:
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
        self.categoriaDao = CategoriaDAO(db)
    
    def exibirMenu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE CATEGORIAS")
        print("="*50)
        print("1. Criar categoria")
        print("2. Listar todas as categorias")
        print("3. Buscar categoria por ID")
        print("4. Buscar categoria por nome")
        print("5. Atualizar categoria")
        print("6. Deletar categoria")
        print("0. Sair")
        print("="*50)
    
    def criarCategoria(self):
        """Solicita dados do usuário e cria uma nova categoria"""
        print("\n--- CRIAR CATEGORIA ---")
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("❌ Erro: O nome da categoria não pode ser vazio!")
            return
        
        try:
            # Verificar se já existe uma categoria com esse nome
            categoriaExistente = self.categoriaDao.buscarPorNome(nome)
            if categoriaExistente:
                print(f"❌ Erro: Já existe uma categoria com o nome '{nome}' (ID: {categoriaExistente.id})")
                return
            
            # Criar nova categoria
            categoria = Categoria(id=None, nome=nome)
            categoriaId = self.categoriaDao.salvar(categoria)
            print(f"✅ Categoria criada com sucesso!")
            print(f"   ID: {categoriaId}")
            print(f"   Nome: {categoria.nome}")
        
        except Exception as e:
            print(f"❌ Erro ao criar categoria: {e}")
    
    def listarCategorias(self):
        """Lista todas as categorias cadastradas"""
        print("\n--- LISTAR TODAS AS CATEGORIAS ---")
        
        try:
            categorias = self.categoriaDao.listarTodas()
            
            if not categorias:
                print("⚠️  Nenhuma categoria cadastrada.")
                return
            
            print(f"\nTotal de categorias: {len(categorias)}")
            print("\n" + "-"*50)
            print(f"{'ID':<5} | {'Nome':<30}")
            print("-"*50)
            
            for categoria in categorias:
                print(f"{categoria.id:<5} | {categoria.nome:<30}")
            
            print("-"*50)
        
        except Exception as e:
            print(f"❌ Erro ao listar categorias: {e}")
    
    def buscarPorId(self):
        """Solicita um ID e busca a categoria correspondente"""
        print("\n--- BUSCAR CATEGORIA POR ID ---")
        
        try:
            idStr = input("Digite o ID da categoria: ").strip()
            categoriaId = int(idStr)
            
            categoria = self.categoriaDao.buscarPorId(categoriaId)
            
            if categoria:
                print("\n✅ Categoria encontrada:")
                print(f"   ID: {categoria.id}")
                print(f"   Nome: {categoria.nome}")
            else:
                print(f"⚠️  Categoria com ID {categoriaId} não encontrada.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar categoria: {e}")
    
    def buscarPorNome(self):
        """Solicita um nome e busca a categoria correspondente"""
        print("\n--- BUSCAR CATEGORIA POR NOME ---")
        
        nome = input("Digite o nome da categoria: ").strip()
        
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        try:
            categoria = self.categoriaDao.buscarPorNome(nome)
            
            if categoria:
                print("\n✅ Categoria encontrada:")
                print(f"   ID: {categoria.id}")
                print(f"   Nome: {categoria.nome}")
            else:
                print(f"⚠️  Categoria '{nome}' não encontrada.")
        
        except Exception as e:
            print(f"❌ Erro ao buscar categoria: {e}")
    
    def atualizarCategoria(self):
        """Solicita dados do usuário e atualiza uma categoria existente"""
        print("\n--- ATUALIZAR CATEGORIA ---")
        
        try:
            idStr = input("Digite o ID da categoria a atualizar: ").strip()
            categoriaId = int(idStr)
            
            # Buscar a categoria existente
            categoria = self.categoriaDao.buscarPorId(categoriaId)
            
            if not categoria:
                print(f"⚠️  Categoria com ID {categoriaId} não encontrada.")
                return
            
            print(f"\nCategoria atual:")
            print(f"   ID: {categoria.id}")
            print(f"   Nome: {categoria.nome}")
            
            novoNome = input("\nDigite o novo nome da categoria (ou Enter para manter): ").strip()
            
            if not novoNome:
                print("⚠️  Operação cancelada. Nome não foi alterado.")
                return
            
            # Verificar se já existe outra categoria com esse nome
            categoriaExistente = self.categoriaDao.buscarPorNome(novoNome)
            if categoriaExistente and categoriaExistente.id != categoriaId:
                print(f"❌ Erro: Já existe outra categoria com o nome '{novoNome}' (ID: {categoriaExistente.id})")
                return
            
            # Atualizar categoria
            categoria.nome = novoNome
            self.categoriaDao.salvar(categoria)
            print(f"\n✅ Categoria atualizada com sucesso!")
            print(f"   ID: {categoria.id}")
            print(f"   Nome: {categoria.nome}")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao atualizar categoria: {e}")
    
    def deletarCategoria(self):
        """Solicita um ID e deleta a categoria correspondente"""
        print("\n--- DELETAR CATEGORIA ---")
        
        try:
            idStr = input("Digite o ID da categoria a deletar: ").strip()
            categoriaId = int(idStr)
            
            # Buscar a categoria existente
            categoria = self.categoriaDao.buscarPorId(categoriaId)
            
            if not categoria:
                print(f"⚠️  Categoria com ID {categoriaId} não encontrada.")
                return
            
            print(f"\nCategoria a ser deletada:")
            print(f"   ID: {categoria.id}")
            print(f"   Nome: {categoria.nome}")
            
            confirmacao = input("\n⚠️  Tem certeza que deseja deletar esta categoria? (s/N): ").strip().lower()
            
            if confirmacao != 's':
                print("❌ Operação cancelada.")
                return
            
            sucesso = self.categoriaDao.deletar(categoria)
            
            if sucesso:
                print(f"\n✅ Categoria deletada com sucesso!")
            else:
                print(f"\n❌ Erro ao deletar categoria.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao deletar categoria: {e}")
    
    def executar(self):
        """Método principal que executa o loop do menu"""
        try:
            while True:
                self.exibirMenu()
                opcao = input("\nEscolha uma opção: ").strip()
                
                if opcao == '0':
                    print("\n👋 Encerrando o sistema...")
                    break
                elif opcao == '1':
                    self.criarCategoria()
                elif opcao == '2':
                    self.listarCategorias()
                elif opcao == '3':
                    self.buscarPorId()
                elif opcao == '4':
                    self.buscarPorNome()
                elif opcao == '5':
                    self.atualizarCategoria()
                elif opcao == '6':
                    self.deletarCategoria()
                else:
                    print("❌ Opção inválida! Tente novamente.")
                
                input("\nPressione Enter para continuar...")
        
        except KeyboardInterrupt:
            print("\n\n👋 Sistema encerrado pelo usuário.")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Função principal para executar o serviço"""
    db = DatabaseConnection('exemplo_bd.db')
    
    try:
        # Conectar ao banco
        db.conectar()
        
        # Garantir que as tabelas existam
        db.criarTabelas()
        
        # Criar e executar o serviço
        service = CategoriaService(db)
        service.executar()
    
    except Exception as e:
        print(f"❌ Erro ao inicializar o sistema: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.fechar()
        print("✓ Conexão com banco de dados encerrada.")


if __name__ == "__main__":
    main()

