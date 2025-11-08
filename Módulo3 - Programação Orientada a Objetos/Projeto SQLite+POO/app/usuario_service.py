"""
Serviço para interação do usuário via linha de comando com a entidade Usuario
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from dao.usuario_dao import UsuarioDAO
from dao.pessoa_dao import PessoaDAO
from model.usuario import Usuario


class UsuarioService:
    
    def __init__(self, db: DatabaseConnection):
        self.__db = db
        self.__usuarioDao = UsuarioDAO(db)
        self.__pessoaDao = PessoaDAO(db)
    
    def exibirMenu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE USUÁRIOS")
        print("="*50)
        print("1. Criar usuário")
        print("2. Listar todos os usuários")
        print("3. Buscar usuário por ID")
        print("4. Buscar usuário por login")
        print("5. Buscar usuário por pessoa")
        print("6. Atualizar usuário")
        print("7. Deletar usuário")
        print("0. Sair")
        print("="*50)
    
    def listarPessoasDisponiveis(self):
        """Lista todas as pessoas disponíveis para vincular a um usuário"""
        pessoas = self.__pessoaDao.listarTodas()
        if not pessoas:
            print("⚠️  Nenhuma pessoa cadastrada. Cadastre uma pessoa primeiro!")
            return None
        
        print("\nPessoas disponíveis:")
        print("-"*50)
        for p in pessoas:
            # Verificar se já tem usuário
            usuarioExistente = self.__usuarioDao.buscarPorPessoaId(p.id)
            status = " (já tem usuário)" if usuarioExistente else ""
            print(f"  {p.id}. {p.nome} - {p.email}{status}")
        print("-"*50)
        return pessoas
    
    def selecionarPessoa(self):
        """Solicita ao usuário que selecione uma pessoa sem usuário"""
        pessoas = self.listarPessoasDisponiveis()
        if not pessoas:
            return None
        
        try:
            pessoaIdStr = input("Digite o ID da pessoa: ").strip()
            pessoaId = int(pessoaIdStr)
            
            # Verificar se já tem usuário
            usuarioExistente = self.__usuarioDao.buscarPorPessoaId(pessoaId)
            if usuarioExistente:
                print(f"❌ Erro: A pessoa com ID {pessoaId} já possui um usuário!")
                return None
            
            pessoa = self.__pessoaDao.buscarPorId(pessoaId)
            if not pessoa:
                print(f"❌ Erro: Pessoa com ID {pessoaId} não encontrada!")
                return None
            
            return pessoa
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
            return None
    
    def criarUsuario(self):
        """Solicita dados do usuário e cria um novo usuário"""
        print("\n--- CRIAR USUÁRIO ---")
        
        # Selecionar pessoa
        pessoa = self.selecionarPessoa()
        if not pessoa:
            return
        
        login = input("Digite o login: ").strip()
        if not login:
            print("❌ Erro: O login não pode ser vazio!")
            return
        
        # Verificar se já existe um usuário com esse login
        usuarioExistente = self.__usuarioDao.buscarPorLogin(login)
        if usuarioExistente:
            print(f"❌ Erro: Já existe um usuário com o login '{login}' (ID: {usuarioExistente.id})")
            return
        
        senha = input("Digite a senha: ").strip()
        if not senha:
            print("❌ Erro: A senha não pode ser vazia!")
            return
        
        print("Tipos disponíveis: admin, professor, aluno, visitante")
        tipo = input("Digite o tipo: ").strip().lower()
        if not tipo:
            print("❌ Erro: O tipo não pode ser vazio!")
            return
        
        try:
            usuario = Usuario(
                id=None,
                login=login,
                senha=senha,
                tipo=tipo,
                pessoa=pessoa
            )
            
            usuarioId = self.__usuarioDao.salvar(usuario)
            print(f"\n✅ Usuário criado com sucesso!")
            self.exibirDetalhesUsuario(usuario)
        
        except Exception as e:
            print(f"❌ Erro ao criar usuário: {e}")
    
    def exibirDetalhesUsuario(self, usuario: Usuario):
        """Exibe os detalhes completos de um usuário"""
        print(f"\n   ID: {usuario.id}")
        print(f"   Login: {usuario.login}")
        print(f"   Tipo: {usuario.tipo}")
        print(f"   Pessoa: {usuario.pessoa.nome} (ID: {usuario.pessoa.id}, Email: {usuario.pessoa.email})")
    
    def listarUsuarios(self):
        """Lista todos os usuários cadastrados"""
        print("\n--- LISTAR TODOS OS USUÁRIOS ---")
        
        try:
            usuarios = self.__usuarioDao.listarTodos()
            
            if not usuarios:
                print("⚠️  Nenhum usuário cadastrado.")
                return
            
            print(f"\nTotal de usuários: {len(usuarios)}")
            print("\n" + "-"*80)
            print(f"{'ID':<5} | {'Login':<20} | {'Tipo':<15} | {'Pessoa':<30}")
            print("-"*80)
            
            for usuario in usuarios:
                print(f"{usuario.id:<5} | {usuario.login[:19]:<20} | {usuario.tipo[:14]:<15} | {usuario.pessoa.nome[:29]:<30}")
            
            print("-"*80)
        
        except Exception as e:
            print(f"❌ Erro ao listar usuários: {e}")
    
    def buscarPorId(self):
        """Solicita um ID e busca o usuário correspondente"""
        print("\n--- BUSCAR USUÁRIO POR ID ---")
        
        try:
            idStr = input("Digite o ID do usuário: ").strip()
            usuarioId = int(idStr)
            
            usuario = self.__usuarioDao.buscarPorId(usuarioId)
            
            if usuario:
                print("\n✅ Usuário encontrado:")
                self.exibirDetalhesUsuario(usuario)
            else:
                print(f"⚠️  Usuário com ID {usuarioId} não encontrado.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar usuário: {e}")
    
    def buscarPorLogin(self):
        """Solicita um login e busca o usuário correspondente"""
        print("\n--- BUSCAR USUÁRIO POR LOGIN ---")
        
        login = input("Digite o login: ").strip()
        
        if not login:
            print("❌ Erro: O login não pode ser vazio!")
            return
        
        try:
            usuario = self.__usuarioDao.buscarPorLogin(login)
            
            if usuario:
                print("\n✅ Usuário encontrado:")
                self.exibirDetalhesUsuario(usuario)
            else:
                print(f"⚠️  Usuário com login '{login}' não encontrado.")
        
        except Exception as e:
            print(f"❌ Erro ao buscar usuário: {e}")
    
    def buscarPorPessoa(self):
        """Solicita um ID de pessoa e busca o usuário correspondente"""
        print("\n--- BUSCAR USUÁRIO POR PESSOA ---")
        
        try:
            pessoaIdStr = input("Digite o ID da pessoa: ").strip()
            pessoaId = int(pessoaIdStr)
            
            pessoa = self.__pessoaDao.buscarPorId(pessoaId)
            if not pessoa:
                print(f"❌ Erro: Pessoa com ID {pessoaId} não encontrada!")
                return
            
            usuario = self.__usuarioDao.buscarPorPessoaId(pessoaId)
            
            if usuario:
                print("\n✅ Usuário encontrado:")
                self.exibirDetalhesUsuario(usuario)
            else:
                print(f"⚠️  A pessoa '{pessoa.nome}' (ID: {pessoaId}) não possui usuário cadastrado.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar usuário: {e}")
    
    def atualizarUsuario(self):
        """Solicita dados do usuário e atualiza um usuário existente"""
        print("\n--- ATUALIZAR USUÁRIO ---")
        
        try:
            idStr = input("Digite o ID do usuário a atualizar: ").strip()
            usuarioId = int(idStr)
            
            usuario = self.__usuarioDao.buscarPorId(usuarioId)
            
            if not usuario:
                print(f"⚠️  Usuário com ID {usuarioId} não encontrado.")
                return
            
            print(f"\nUsuário atual:")
            self.exibirDetalhesUsuario(usuario)
            
            print("\nDigite os novos dados (ou Enter para manter o valor atual):")
            
            # Login
            novoLogin = input(f"Login [{usuario.login}]: ").strip()
            if novoLogin:
                # Verificar se já existe outro usuário com esse login
                usuarioExistente = self.__usuarioDao.buscarPorLogin(novoLogin)
                if usuarioExistente and usuarioExistente.id != usuarioId:
                    print(f"❌ Erro: Já existe outro usuário com o login '{novoLogin}' (ID: {usuarioExistente.id})")
                    return
                usuario.login = novoLogin
            
            # Senha
            novaSenha = input("Senha (ou Enter para manter): ").strip()
            if novaSenha:
                usuario.senha = novaSenha
            
            # Tipo
            novoTipo = input(f"Tipo [{usuario.tipo}]: ").strip().lower()
            if novoTipo:
                usuario.tipo = novoTipo
            
            self.__usuarioDao.salvar(usuario)
            print(f"\n✅ Usuário atualizado com sucesso!")
            print("\nDados atualizados:")
            self.exibirDetalhesUsuario(usuario)
        
        except ValueError as e:
            print(f"❌ Erro: {e}")
        except Exception as e:
            print(f"❌ Erro ao atualizar usuário: {e}")
    
    def deletarUsuario(self):
        """Solicita um ID e deleta o usuário correspondente"""
        print("\n--- DELETAR USUÁRIO ---")
        
        try:
            idStr = input("Digite o ID do usuário a deletar: ").strip()
            usuarioId = int(idStr)
            
            usuario = self.__usuarioDao.buscarPorId(usuarioId)
            
            if not usuario:
                print(f"⚠️  Usuário com ID {usuarioId} não encontrado.")
                return
            
            print(f"\nUsuário a ser deletado:")
            self.exibirDetalhesUsuario(usuario)
            
            confirmacao = input("\n⚠️  Tem certeza que deseja deletar este usuário? (s/N): ").strip().lower()
            
            if confirmacao != 's':
                print("❌ Operação cancelada.")
                return
            
            sucesso = self.__usuarioDao.deletar(usuario)
            
            if sucesso:
                print(f"\n✅ Usuário deletado com sucesso!")
            else:
                print(f"\n❌ Erro ao deletar usuário.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao deletar usuário: {e}")
    
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
                    self.criarUsuario()
                elif opcao == '2':
                    self.listarUsuarios()
                elif opcao == '3':
                    self.buscarPorId()
                elif opcao == '4':
                    self.buscarPorLogin()
                elif opcao == '5':
                    self.buscarPorPessoa()
                elif opcao == '6':
                    self.atualizarUsuario()
                elif opcao == '7':
                    self.deletarUsuario()
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
        service = UsuarioService(db)
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

