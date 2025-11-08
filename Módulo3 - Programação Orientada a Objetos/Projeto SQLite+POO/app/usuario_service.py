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
from dao.categoria_dao import CategoriaDAO
from model.usuario import Usuario
from model.pessoa import Pessoa


class UsuarioService:
    
    def __init__(self, db: DatabaseConnection):
        self.__db = db
        self.__usuarioDao = UsuarioDAO(db)
        self.__pessoaDao = PessoaDAO(db)
        self.__categoriaDao = CategoriaDAO(db)
    
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
    
    def listarCategoriasDisponiveis(self):
        """Lista todas as categorias disponíveis para seleção"""
        categorias = self.__categoriaDao.listarTodas()
        if not categorias:
            print("⚠️  Nenhuma categoria cadastrada. Cadastre uma categoria primeiro!")
            return None
        
        print("\nCategorias disponíveis:")
        print("-"*30)
        for cat in categorias:
            print(f"  {cat.id}. {cat.nome}")
        print("-"*30)
        return categorias
    
    def selecionarCategoria(self):
        """Solicita ao usuário que selecione uma categoria"""
        categorias = self.listarCategoriasDisponiveis()
        if not categorias:
            return None
        
        try:
            categoriaIdStr = input("Digite o ID da categoria: ").strip()
            categoriaId = int(categoriaIdStr)
            
            categoria = self.__categoriaDao.buscarPorId(categoriaId)
            if not categoria:
                print(f"❌ Erro: Categoria com ID {categoriaId} não encontrada!")
                return None
            
            return categoria
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
            return None
    
    def criarUsuario(self):
        """Solicita todos os dados de uma vez e cria pessoa e usuário de forma transparente"""
        print("\n--- CADASTRAR USUÁRIO ---")
        print("Preencha todos os dados:")
        
        # Dados básicos
        nome = input("Nome: ").strip()
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        email = input("Email: ").strip()
        if not email:
            print("❌ Erro: O email não pode ser vazio!")
            return
        
        # Verificar se já existe uma pessoa com esse email
        todasPessoas = self.__pessoaDao.listarTodas()
        for p in todasPessoas:
            if p.email.lower() == email.lower():
                print(f"❌ Erro: Já existe uma pessoa com o email '{email}' (ID: {p.id})")
                return
        
        # Selecionar categoria
        categoria = self.selecionarCategoria()
        if not categoria:
            return
        
        # Campos opcionais
        alturaStr = input("Altura em metros (ex: 1.75, ou Enter para pular): ").strip()
        altura = float(alturaStr) if alturaStr else None
        
        pesoStr = input("Peso em kg (ex: 75.5, ou Enter para pular): ").strip()
        peso = float(pesoStr) if pesoStr else None
        
        dataNascimento = input("Data de nascimento (AAAA-MM-DD, ou Enter para pular): ").strip()
        dataNascimento = dataNascimento if dataNascimento else None
        
        telefone = input("Telefone (ou Enter para pular): ").strip()
        telefone = telefone if telefone else None
        
        ativoStr = input("Pessoa está ativa? (S/n): ").strip().lower()
        ativo = ativoStr != 'n'
        
        # Dados de acesso do usuário
        login = input("Login: ").strip()
        if not login:
            print("❌ Erro: O login não pode ser vazio!")
            return
        
        # Verificar se já existe um usuário com esse login
        usuarioExistente = self.__usuarioDao.buscarPorLogin(login)
        if usuarioExistente:
            print(f"❌ Erro: Já existe um usuário com o login '{login}' (ID: {usuarioExistente.id})")
            return
        
        senha = input("Senha: ").strip()
        if not senha:
            print("❌ Erro: A senha não pode ser vazia!")
            return
        
        print("Tipos disponíveis: admin, professor, aluno, visitante")
        tipo = input("Tipo: ").strip().lower()
        if not tipo:
            print("❌ Erro: O tipo não pode ser vazio!")
            return
        
        try:
            # Criar a pessoa primeiro (transparente para o usuário)
            pessoa = Pessoa(
                id=None,
                nome=nome,
                email=email,
                categoria=categoria,
                altura=altura,
                peso=peso,
                dataNascimento=dataNascimento,
                ativo=ativo,
                telefone=telefone
            )
            
            pessoaId = self.__pessoaDao.salvar(pessoa)
            
            # Criar o usuário vinculado à pessoa (transparente para o usuário)
            usuario = Usuario(
                id=None,
                login=login,
                senha=senha,
                tipo=tipo,
                pessoa=pessoa
            )
            
            usuarioId = self.__usuarioDao.salvar(usuario)
            print(f"\n✅ Usuário cadastrado com sucesso! (ID: {usuarioId})")
            self.exibirDetalhesUsuario(usuario)
        
        except ValueError as e:
            print(f"❌ Erro de validação: {e}")
        except Exception as e:
            print(f"❌ Erro ao criar usuário: {e}")
            import traceback
            traceback.print_exc()
    
    def exibirDetalhesUsuario(self, usuario: Usuario):
        """Exibe os detalhes completos de um usuário e da pessoa associada"""
        print(f"\n📋 DADOS DO USUÁRIO:")
        print(f"   ID: {usuario.id}")
        print(f"   Login: {usuario.login}")
        print(f"   Tipo: {usuario.tipo}")
        print(f"\n👤 DADOS DA PESSOA:")
        print(f"   ID: {usuario.pessoa.id}")
        print(f"   Nome: {usuario.pessoa.nome}")
        print(f"   Email: {usuario.pessoa.email}")
        print(f"   Categoria: {usuario.pessoa.categoria.nome} (ID: {usuario.pessoa.categoria.id})")
        if usuario.pessoa.altura is not None:
            print(f"   Altura: {usuario.pessoa.altura}m")
        if usuario.pessoa.peso is not None:
            print(f"   Peso: {usuario.pessoa.peso}kg")
        if usuario.pessoa.dataNascimento:
            print(f"   Data de nascimento: {usuario.pessoa.dataNascimento}")
        if usuario.pessoa.telefone:
            print(f"   Telefone: {usuario.pessoa.telefone}")
        print(f"   Status: {'✅ Ativa' if usuario.pessoa.ativo else '❌ Inativa'}")
    
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

