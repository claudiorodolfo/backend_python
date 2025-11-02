"""
Serviço para interação do usuário via linha de comando com a entidade Pessoa
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from dao.pessoa_dao import PessoaDAO
from dao.categoria_dao import CategoriaDAO
from model.pessoa import Pessoa


class PessoaService:
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
        self.pessoaDao = PessoaDAO(db)
        self.categoriaDao = CategoriaDAO(db)
    
    def exibirMenu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE PESSOAS")
        print("="*50)
        print("1. Criar pessoa")
        print("2. Listar todas as pessoas")
        print("3. Buscar pessoa por ID")
        print("4. Buscar pessoa por nome")
        print("5. Buscar pessoas por categoria")
        print("6. Atualizar pessoa")
        print("7. Deletar pessoa")
        print("0. Sair")
        print("="*50)
    
    def listarCategoriasDisponiveis(self):
        """Lista todas as categorias disponíveis para seleção"""
        categorias = self.categoriaDao.listarTodas()
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
            
            categoria = self.categoriaDao.buscarPorId(categoriaId)
            if not categoria:
                print(f"❌ Erro: Categoria com ID {categoriaId} não encontrada!")
                return None
            
            return categoria
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
            return None
    
    def criarPessoa(self):
        """Solicita dados do usuário e cria uma nova pessoa"""
        print("\n--- CRIAR PESSOA ---")
        
        nome = input("Digite o nome: ").strip()
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        email = input("Digite o email: ").strip()
        if not email:
            print("❌ Erro: O email não pode ser vazio!")
            return
        
        # Verificar se já existe uma pessoa com esse email
        pessoasExistentes = self.pessoaDao.buscarPorNome("")  # Buscar todas para verificar email
        todasPessoas = self.pessoaDao.listarTodas()
        for p in todasPessoas:
            if p.email.lower() == email.lower():
                print(f"❌ Erro: Já existe uma pessoa com o email '{email}' (ID: {p.id})")
                return
        
        # Selecionar categoria
        categoria = self.selecionarCategoria()
        if not categoria:
            return
        
        # Campos opcionais
        idadeStr = input("Digite a idade (ou Enter para pular): ").strip()
        idade = int(idadeStr) if idadeStr else None
        
        alturaStr = input("Digite a altura em metros (ex: 1.75, ou Enter para pular): ").strip()
        altura = float(alturaStr) if alturaStr else None
        
        pesoStr = input("Digite o peso em kg (ex: 75.5, ou Enter para pular): ").strip()
        peso = float(pesoStr) if pesoStr else None
        
        dataNascimento = input("Digite a data de nascimento (AAAA-MM-DD, ou Enter para pular): ").strip()
        dataNascimento = dataNascimento if dataNascimento else None
        
        telefone = input("Digite o telefone (ou Enter para pular): ").strip()
        telefone = telefone if telefone else None
        
        observacoes = input("Digite observações (ou Enter para pular): ").strip()
        observacoes = observacoes if observacoes else None
        
        ativoStr = input("Pessoa está ativa? (S/n): ").strip().lower()
        ativo = ativoStr != 'n'
        
        try:
            pessoa = Pessoa(
                id=None,
                nome=nome,
                email=email,
                categoria=categoria,
                idade=idade,
                altura=altura,
                peso=peso,
                data_nascimento=dataNascimento,
                ativo=ativo,
                observacoes=observacoes,
                telefone=telefone
            )
            
            pessoaId = self.pessoaDao.salvar(pessoa)
            print(f"\n✅ Pessoa criada com sucesso!")
            self.exibirDetalhesPessoa(pessoa)
        
        except ValueError as e:
            print(f"❌ Erro de validação: {e}")
        except Exception as e:
            print(f"❌ Erro ao criar pessoa: {e}")
    
    def exibirDetalhesPessoa(self, pessoa: Pessoa):
        """Exibe os detalhes completos de uma pessoa"""
        print(f"\n   ID: {pessoa.id}")
        print(f"   Nome: {pessoa.nome}")
        print(f"   Email: {pessoa.email}")
        print(f"   Categoria: {pessoa.categoria.nome} (ID: {pessoa.categoria.id})")
        if pessoa.idade is not None:
            print(f"   Idade: {pessoa.idade} anos")
        if pessoa.altura is not None:
            print(f"   Altura: {pessoa.altura}m")
        if pessoa.peso is not None:
            print(f"   Peso: {pessoa.peso}kg")
        if pessoa.data_nascimento:
            print(f"   Data de nascimento: {pessoa.data_nascimento}")
        if pessoa.telefone:
            print(f"   Telefone: {pessoa.telefone}")
        print(f"   Status: {'✅ Ativa' if pessoa.ativo else '❌ Inativa'}")
        if pessoa.observacoes:
            print(f"   Observações: {pessoa.observacoes}")
        if pessoa.momento_cadastro:
            print(f"   Cadastrado em: {pessoa.momento_cadastro}")
    
    def listarPessoas(self):
        """Lista todas as pessoas cadastradas"""
        print("\n--- LISTAR TODAS AS PESSOAS ---")
        
        try:
            pessoas = self.pessoaDao.listarTodas()
            
            if not pessoas:
                print("⚠️  Nenhuma pessoa cadastrada.")
                return
            
            print(f"\nTotal de pessoas: {len(pessoas)}")
            print("\n" + "-"*80)
            print(f"{'ID':<5} | {'Nome':<25} | {'Email':<25} | {'Categoria':<15} | {'Status':<8}")
            print("-"*80)
            
            for pessoa in pessoas:
                status = "Ativa" if pessoa.ativo else "Inativa"
                print(f"{pessoa.id:<5} | {pessoa.nome[:24]:<25} | {pessoa.email[:24]:<25} | {pessoa.categoria.nome[:14]:<15} | {status:<8}")
            
            print("-"*80)
        
        except Exception as e:
            print(f"❌ Erro ao listar pessoas: {e}")
    
    def buscarPorId(self):
        """Solicita um ID e busca a pessoa correspondente"""
        print("\n--- BUSCAR PESSOA POR ID ---")
        
        try:
            idStr = input("Digite o ID da pessoa: ").strip()
            pessoaId = int(idStr)
            
            pessoa = self.pessoaDao.buscarPorId(pessoaId)
            
            if pessoa:
                print("\n✅ Pessoa encontrada:")
                self.exibirDetalhesPessoa(pessoa)
            else:
                print(f"⚠️  Pessoa com ID {pessoaId} não encontrada.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar pessoa: {e}")
    
    def buscarPorNome(self):
        """Solicita um nome e busca pessoas correspondentes"""
        print("\n--- BUSCAR PESSOA POR NOME ---")
        
        nome = input("Digite o nome (ou parte do nome) da pessoa: ").strip()
        
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        try:
            pessoas = self.pessoaDao.buscarPorNome(nome)
            
            if pessoas:
                print(f"\n✅ {len(pessoas)} pessoa(s) encontrada(s):")
                print("\n" + "-"*80)
                for pessoa in pessoas:
                    print(f"ID: {pessoa.id} | {pessoa.nome} | {pessoa.email} | {pessoa.categoria.nome}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma pessoa encontrada com o nome contendo '{nome}'.")
        
        except Exception as e:
            print(f"❌ Erro ao buscar pessoa: {e}")
    
    def buscarPorCategoria(self):
        """Lista pessoas de uma categoria específica"""
        print("\n--- BUSCAR PESSOAS POR CATEGORIA ---")
        
        categorias = self.listarCategoriasDisponiveis()
        if not categorias:
            return
        
        try:
            categoriaIdStr = input("Digite o ID da categoria: ").strip()
            categoriaId = int(categoriaIdStr)
            
            categoria = self.categoriaDao.buscarPorId(categoriaId)
            if not categoria:
                print(f"❌ Erro: Categoria com ID {categoriaId} não encontrada!")
                return
            
            pessoas = self.pessoaDao.buscarPorCategoria(categoriaId)
            
            if pessoas:
                print(f"\n✅ {len(pessoas)} pessoa(s) encontrada(s) na categoria '{categoria.nome}':")
                print("\n" + "-"*80)
                for pessoa in pessoas:
                    status = "Ativa" if pessoa.ativo else "Inativa"
                    print(f"ID: {pessoa.id} | {pessoa.nome} | {pessoa.email} | Status: {status}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma pessoa encontrada na categoria '{categoria.nome}'.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar pessoas: {e}")
    
    def atualizarPessoa(self):
        """Solicita dados do usuário e atualiza uma pessoa existente"""
        print("\n--- ATUALIZAR PESSOA ---")
        
        try:
            idStr = input("Digite o ID da pessoa a atualizar: ").strip()
            pessoaId = int(idStr)
            
            pessoa = self.pessoaDao.buscarPorId(pessoaId)
            
            if not pessoa:
                print(f"⚠️  Pessoa com ID {pessoaId} não encontrada.")
                return
            
            print(f"\nPessoa atual:")
            self.exibirDetalhesPessoa(pessoa)
            
            print("\nDigite os novos dados (ou Enter para manter o valor atual):")
            
            # Nome
            novoNome = input(f"Nome [{pessoa.nome}]: ").strip()
            if novoNome:
                pessoa.nome = novoNome
            
            # Email
            novoEmail = input(f"Email [{pessoa.email}]: ").strip()
            if novoEmail:
                # Verificar se já existe outra pessoa com esse email
                todasPessoas = self.pessoaDao.listarTodas()
                for p in todasPessoas:
                    if p.id != pessoaId and p.email.lower() == novoEmail.lower():
                        print(f"❌ Erro: Já existe outra pessoa com o email '{novoEmail}' (ID: {p.id})")
                        return
                pessoa.email = novoEmail
            
            # Categoria
            categoriaStr = input(f"Categoria ID [{pessoa.categoria.id} - {pessoa.categoria.nome}] (ou Enter para manter): ").strip()
            if categoriaStr:
                novaCategoriaId = int(categoriaStr)
                novaCategoria = self.categoriaDao.buscarPorId(novaCategoriaId)
                if not novaCategoria:
                    print(f"❌ Erro: Categoria com ID {novaCategoriaId} não encontrada!")
                    return
                pessoa.categoria = novaCategoria
            
            # Idade
            idadeStr = input(f"Idade [{pessoa.idade or 'N/A'}] (ou Enter para manter): ").strip()
            if idadeStr:
                pessoa.idade = int(idadeStr) if idadeStr else None
            elif not idadeStr and pessoa.idade is not None:
                # Manter o valor atual
                pass
            
            # Altura
            alturaStr = input(f"Altura [{pessoa.altura or 'N/A'}]m (ou Enter para manter): ").strip()
            if alturaStr:
                pessoa.altura = float(alturaStr) if alturaStr else None
            
            # Peso
            pesoStr = input(f"Peso [{pessoa.peso or 'N/A'}]kg (ou Enter para manter): ").strip()
            if pesoStr:
                pessoa.peso = float(pesoStr) if pesoStr else None
            
            # Data de nascimento
            dataStr = input(f"Data de nascimento [{pessoa.data_nascimento or 'N/A'}] (ou Enter para manter): ").strip()
            if dataStr:
                pessoa.data_nascimento = dataStr if dataStr else None
            
            # Telefone
            telefoneStr = input(f"Telefone [{pessoa.telefone or 'N/A'}] (ou Enter para manter): ").strip()
            if telefoneStr:
                pessoa.telefone = telefoneStr if telefoneStr else None
            
            # Observações
            obsStr = input(f"Observações [{pessoa.observacoes or 'N/A'}] (ou Enter para manter): ").strip()
            if obsStr:
                pessoa.observacoes = obsStr if obsStr else None
            
            # Status ativo
            ativoStr = input(f"Status ativo (S/n) [{'S' if pessoa.ativo else 'n'}] (ou Enter para manter): ").strip().lower()
            if ativoStr:
                pessoa.ativo = ativoStr != 'n'
            
            self.pessoaDao.salvar(pessoa)
            print(f"\n✅ Pessoa atualizada com sucesso!")
            print("\nDados atualizados:")
            self.exibirDetalhesPessoa(pessoa)
        
        except ValueError as e:
            print(f"❌ Erro: {e}")
        except Exception as e:
            print(f"❌ Erro ao atualizar pessoa: {e}")
    
    def deletarPessoa(self):
        """Solicita um ID e deleta a pessoa correspondente"""
        print("\n--- DELETAR PESSOA ---")
        
        try:
            idStr = input("Digite o ID da pessoa a deletar: ").strip()
            pessoaId = int(idStr)
            
            pessoa = self.pessoaDao.buscarPorId(pessoaId)
            
            if not pessoa:
                print(f"⚠️  Pessoa com ID {pessoaId} não encontrada.")
                return
            
            print(f"\nPessoa a ser deletada:")
            self.exibirDetalhesPessoa(pessoa)
            
            confirmacao = input("\n⚠️  Tem certeza que deseja deletar esta pessoa? (s/N): ").strip().lower()
            
            if confirmacao != 's':
                print("❌ Operação cancelada.")
                return
            
            sucesso = self.pessoaDao.deletar(pessoa)
            
            if sucesso:
                print(f"\n✅ Pessoa deletada com sucesso!")
            else:
                print(f"\n❌ Erro ao deletar pessoa.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao deletar pessoa: {e}")
    
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
                    self.criarPessoa()
                elif opcao == '2':
                    self.listarPessoas()
                elif opcao == '3':
                    self.buscarPorId()
                elif opcao == '4':
                    self.buscarPorNome()
                elif opcao == '5':
                    self.buscarPorCategoria()
                elif opcao == '6':
                    self.atualizarPessoa()
                elif opcao == '7':
                    self.deletarPessoa()
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
        service = PessoaService(db)
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

