"""
Serviço para interação do usuário via linha de comando com a entidade Disciplina
e gerenciamento do relacionamento N:N com Pessoa
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from dao.disciplina_dao import DisciplinaDAO
from dao.pessoa_dao import PessoaDAO
from model.disciplina import Disciplina


class DisciplinaService:
    
    def __init__(self, db: DatabaseConnection):
        self.__db = db
        self.__disciplinaDao = DisciplinaDAO(db)
        self.__pessoaDao = PessoaDAO(db)
    
    def exibirMenu(self):
        """Exibe o menu principal de opções"""
        print("\n" + "="*50)
        print("  SISTEMA DE GERENCIAMENTO DE DISCIPLINAS")
        print("="*50)
        print("1. Criar disciplina")
        print("2. Listar todas as disciplinas")
        print("3. Buscar disciplina por ID")
        print("4. Buscar disciplina por nome")
        print("5. Atualizar disciplina")
        print("6. Deletar disciplina")
        print("7. Vincular pessoa a disciplina")
        print("8. Desvincular pessoa de disciplina")
        print("9. Listar pessoas de uma disciplina")
        print("10. Listar disciplinas de uma pessoa")
        print("0. Sair")
        print("="*50)
    
    def criarDisciplina(self):
        """Solicita dados do usuário e cria uma nova disciplina"""
        print("\n--- CRIAR DISCIPLINA ---")
        
        nome = input("Digite o nome da disciplina: ").strip()
        if not nome:
            print("❌ Erro: O nome da disciplina não pode ser vazio!")
            return
        
        # Verificar se já existe uma disciplina com esse nome
        disciplinasExistentes = self.__disciplinaDao.buscarPorNome(nome)
        for d in disciplinasExistentes:
            if d.nome.lower() == nome.lower():
                print(f"❌ Erro: Já existe uma disciplina com o nome '{nome}' (ID: {d.id})")
                return
        
        cargaHorariaStr = input("Digite a carga horária (ou Enter para pular): ").strip()
        cargaHoraria = int(cargaHorariaStr) if cargaHorariaStr else None
        
        descricao = input("Digite a descrição (ou Enter para pular): ").strip()
        descricao = descricao if descricao else None
        
        try:
            disciplina = Disciplina(
                id=None,
                nome=nome,
                carga_horaria=cargaHoraria,
                descricao=descricao
            )
            
            disciplinaId = self.__disciplinaDao.salvar(disciplina)
            print(f"\n✅ Disciplina criada com sucesso!")
            self.exibirDetalhesDisciplina(disciplina)
        
        except ValueError as e:
            print(f"❌ Erro de validação: {e}")
        except Exception as e:
            print(f"❌ Erro ao criar disciplina: {e}")
    
    def exibirDetalhesDisciplina(self, disciplina: Disciplina):
        """Exibe os detalhes completos de uma disciplina"""
        print(f"\n   ID: {disciplina.id}")
        print(f"   Nome: {disciplina.nome}")
        if disciplina.carga_horaria is not None:
            print(f"   Carga horária: {disciplina.carga_horaria} horas")
        if disciplina.descricao:
            print(f"   Descrição: {disciplina.descricao}")
    
    def listarDisciplinas(self):
        """Lista todas as disciplinas cadastradas"""
        print("\n--- LISTAR TODAS AS DISCIPLINAS ---")
        
        try:
            disciplinas = self.__disciplinaDao.listarTodas()
            
            if not disciplinas:
                print("⚠️  Nenhuma disciplina cadastrada.")
                return
            
            print(f"\nTotal de disciplinas: {len(disciplinas)}")
            print("\n" + "-"*80)
            print(f"{'ID':<5} | {'Nome':<40} | {'Carga Horária':<15}")
            print("-"*80)
            
            for disciplina in disciplinas:
                cargaHoraria = f"{disciplina.carga_horaria}h" if disciplina.carga_horaria else "N/A"
                print(f"{disciplina.id:<5} | {disciplina.nome[:39]:<40} | {cargaHoraria:<15}")
            
            print("-"*80)
        
        except Exception as e:
            print(f"❌ Erro ao listar disciplinas: {e}")
    
    def buscarPorId(self):
        """Solicita um ID e busca a disciplina correspondente"""
        print("\n--- BUSCAR DISCIPLINA POR ID ---")
        
        try:
            idStr = input("Digite o ID da disciplina: ").strip()
            disciplinaId = int(idStr)
            
            disciplina = self.__disciplinaDao.buscarPorId(disciplinaId)
            
            if disciplina:
                print("\n✅ Disciplina encontrada:")
                self.exibirDetalhesDisciplina(disciplina)
            else:
                print(f"⚠️  Disciplina com ID {disciplinaId} não encontrada.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao buscar disciplina: {e}")
    
    def buscarPorNome(self):
        """Solicita um nome e busca disciplinas correspondentes"""
        print("\n--- BUSCAR DISCIPLINA POR NOME ---")
        
        nome = input("Digite o nome (ou parte do nome) da disciplina: ").strip()
        
        if not nome:
            print("❌ Erro: O nome não pode ser vazio!")
            return
        
        try:
            disciplinas = self.__disciplinaDao.buscarPorNome(nome)
            
            if disciplinas:
                print(f"\n✅ {len(disciplinas)} disciplina(s) encontrada(s):")
                print("\n" + "-"*80)
                for disciplina in disciplinas:
                    cargaHoraria = f"{disciplina.carga_horaria}h" if disciplina.carga_horaria else "N/A"
                    print(f"ID: {disciplina.id} | {disciplina.nome} | Carga: {cargaHoraria}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma disciplina encontrada com o nome contendo '{nome}'.")
        
        except Exception as e:
            print(f"❌ Erro ao buscar disciplina: {e}")
    
    def atualizarDisciplina(self):
        """Solicita dados do usuário e atualiza uma disciplina existente"""
        print("\n--- ATUALIZAR DISCIPLINA ---")
        
        try:
            idStr = input("Digite o ID da disciplina a atualizar: ").strip()
            disciplinaId = int(idStr)
            
            disciplina = self.__disciplinaDao.buscarPorId(disciplinaId)
            
            if not disciplina:
                print(f"⚠️  Disciplina com ID {disciplinaId} não encontrada.")
                return
            
            print(f"\nDisciplina atual:")
            self.exibirDetalhesDisciplina(disciplina)
            
            print("\nDigite os novos dados (ou Enter para manter o valor atual):")
            
            # Nome
            novoNome = input(f"Nome [{disciplina.nome}]: ").strip()
            if novoNome:
                # Verificar se já existe outra disciplina com esse nome
                disciplinasExistentes = self.__disciplinaDao.buscarPorNome(novoNome)
                for d in disciplinasExistentes:
                    if d.id != disciplinaId and d.nome.lower() == novoNome.lower():
                        print(f"❌ Erro: Já existe outra disciplina com o nome '{novoNome}' (ID: {d.id})")
                        return
                disciplina.nome = novoNome
            
            # Carga horária
            cargaStr = input(f"Carga horária [{disciplina.carga_horaria or 'N/A'}] (ou Enter para manter): ").strip()
            if cargaStr:
                disciplina.carga_horaria = int(cargaStr) if cargaStr else None
            
            # Descrição
            descStr = input(f"Descrição [{disciplina.descricao or 'N/A'}] (ou Enter para manter): ").strip()
            if descStr:
                disciplina.descricao = descStr if descStr else None
            
            self.__disciplinaDao.salvar(disciplina)
            print(f"\n✅ Disciplina atualizada com sucesso!")
            print("\nDados atualizados:")
            self.exibirDetalhesDisciplina(disciplina)
        
        except ValueError as e:
            print(f"❌ Erro: {e}")
        except Exception as e:
            print(f"❌ Erro ao atualizar disciplina: {e}")
    
    def deletarDisciplina(self):
        """Solicita um ID e deleta a disciplina correspondente"""
        print("\n--- DELETAR DISCIPLINA ---")
        
        try:
            idStr = input("Digite o ID da disciplina a deletar: ").strip()
            disciplinaId = int(idStr)
            
            disciplina = self.__disciplinaDao.buscarPorId(disciplinaId)
            
            if not disciplina:
                print(f"⚠️  Disciplina com ID {disciplinaId} não encontrada.")
                return
            
            print(f"\nDisciplina a ser deletada:")
            self.exibirDetalhesDisciplina(disciplina)
            
            confirmacao = input("\n⚠️  Tem certeza que deseja deletar esta disciplina? (s/N): ").strip().lower()
            
            if confirmacao != 's':
                print("❌ Operação cancelada.")
                return
            
            sucesso = self.__disciplinaDao.deletar(disciplina)
            
            if sucesso:
                print(f"\n✅ Disciplina deletada com sucesso!")
            else:
                print(f"\n❌ Erro ao deletar disciplina.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao deletar disciplina: {e}")
    
    def vincularPessoa(self):
        """Vincula uma pessoa a uma disciplina"""
        print("\n--- VINCULAR PESSOA A DISCIPLINA ---")
        
        try:
            # Selecionar disciplina
            disciplinas = self.__disciplinaDao.listarTodas()
            if not disciplinas:
                print("⚠️  Nenhuma disciplina cadastrada.")
                return
            
            print("\nDisciplinas disponíveis:")
            for d in disciplinas:
                print(f"  {d.id}. {d.nome}")
            
            disciplinaIdStr = input("\nDigite o ID da disciplina: ").strip()
            disciplinaId = int(disciplinaIdStr)
            disciplina = self.__disciplinaDao.buscarPorId(disciplinaId)
            
            if not disciplina:
                print(f"❌ Erro: Disciplina com ID {disciplinaId} não encontrada!")
                return
            
            # Selecionar pessoa
            pessoas = self.__pessoaDao.listarTodas()
            if not pessoas:
                print("⚠️  Nenhuma pessoa cadastrada.")
                return
            
            print("\nPessoas disponíveis:")
            for p in pessoas:
                print(f"  {p.id}. {p.nome} - {p.email}")
            
            pessoaIdStr = input("\nDigite o ID da pessoa: ").strip()
            pessoaId = int(pessoaIdStr)
            pessoa = self.__pessoaDao.buscarPorId(pessoaId)
            
            if not pessoa:
                print(f"❌ Erro: Pessoa com ID {pessoaId} não encontrada!")
                return
            
            # Verificar se já está vinculado
            disciplinasPessoa = self.__disciplinaDao.buscarDisciplinasPorPessoa(pessoaId)
            if disciplina in disciplinasPessoa:
                print(f"❌ Erro: A pessoa '{pessoa.nome}' já está vinculada à disciplina '{disciplina.nome}'!")
                return
            
            sucesso = self.__disciplinaDao.vincularPessoa(pessoa, disciplina)
            
            if sucesso:
                print(f"\n✅ Pessoa '{pessoa.nome}' vinculada à disciplina '{disciplina.nome}' com sucesso!")
            else:
                print(f"\n❌ Erro: A pessoa já está vinculada a esta disciplina.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao vincular pessoa: {e}")
    
    def desvincularPessoa(self):
        """Remove o vínculo entre uma pessoa e uma disciplina"""
        print("\n--- DESVINCULAR PESSOA DE DISCIPLINA ---")
        
        try:
            # Selecionar disciplina
            disciplinas = self.__disciplinaDao.listarTodas()
            if not disciplinas:
                print("⚠️  Nenhuma disciplina cadastrada.")
                return
            
            print("\nDisciplinas disponíveis:")
            for d in disciplinas:
                print(f"  {d.id}. {d.nome}")
            
            disciplinaIdStr = input("\nDigite o ID da disciplina: ").strip()
            disciplinaId = int(disciplinaIdStr)
            disciplina = self.__disciplinaDao.buscarPorId(disciplinaId)
            
            if not disciplina:
                print(f"❌ Erro: Disciplina com ID {disciplinaId} não encontrada!")
                return
            
            # Listar pessoas vinculadas
            pessoasVinculadas = self.__disciplinaDao.buscarPessoasPorDisciplina(disciplinaId)
            if not pessoasVinculadas:
                print(f"⚠️  Nenhuma pessoa vinculada à disciplina '{disciplina.nome}'.")
                return
            
            print(f"\nPessoas vinculadas à disciplina '{disciplina.nome}':")
            for p in pessoasVinculadas:
                print(f"  {p.id}. {p.nome} - {p.email}")
            
            pessoaIdStr = input("\nDigite o ID da pessoa a desvincular: ").strip()
            pessoaId = int(pessoaIdStr)
            pessoa = self.__pessoaDao.buscarPorId(pessoaId)
            
            if not pessoa:
                print(f"❌ Erro: Pessoa com ID {pessoaId} não encontrada!")
                return
            
            sucesso = self.__disciplinaDao.desvincularPessoa(pessoa, disciplina)
            
            if sucesso:
                print(f"\n✅ Pessoa '{pessoa.nome}' desvinculada da disciplina '{disciplina.nome}' com sucesso!")
            else:
                print(f"\n❌ Erro: A pessoa não está vinculada a esta disciplina.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao desvincular pessoa: {e}")
    
    def listarPessoasDisciplina(self):
        """Lista todas as pessoas vinculadas a uma disciplina"""
        print("\n--- LISTAR PESSOAS DE UMA DISCIPLINA ---")
        
        try:
            disciplinas = self.__disciplinaDao.listarTodas()
            if not disciplinas:
                print("⚠️  Nenhuma disciplina cadastrada.")
                return
            
            print("\nDisciplinas disponíveis:")
            for d in disciplinas:
                print(f"  {d.id}. {d.nome}")
            
            disciplinaIdStr = input("\nDigite o ID da disciplina: ").strip()
            disciplinaId = int(disciplinaIdStr)
            disciplina = self.__disciplinaDao.buscarPorId(disciplinaId)
            
            if not disciplina:
                print(f"❌ Erro: Disciplina com ID {disciplinaId} não encontrada!")
                return
            
            pessoas = self.__disciplinaDao.buscarPessoasPorDisciplina(disciplinaId)
            
            if pessoas:
                print(f"\n✅ {len(pessoas)} pessoa(s) vinculada(s) à disciplina '{disciplina.nome}':")
                print("\n" + "-"*80)
                for pessoa in pessoas:
                    print(f"ID: {pessoa.id} | {pessoa.nome} | {pessoa.email}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma pessoa vinculada à disciplina '{disciplina.nome}'.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao listar pessoas: {e}")
    
    def listarDisciplinasPessoa(self):
        """Lista todas as disciplinas vinculadas a uma pessoa"""
        print("\n--- LISTAR DISCIPLINAS DE UMA PESSOA ---")
        
        try:
            pessoas = self.__pessoaDao.listarTodas()
            if not pessoas:
                print("⚠️  Nenhuma pessoa cadastrada.")
                return
            
            print("\nPessoas disponíveis:")
            for p in pessoas:
                print(f"  {p.id}. {p.nome} - {p.email}")
            
            pessoaIdStr = input("\nDigite o ID da pessoa: ").strip()
            pessoaId = int(pessoaIdStr)
            pessoa = self.__pessoaDao.buscarPorId(pessoaId)
            
            if not pessoa:
                print(f"❌ Erro: Pessoa com ID {pessoaId} não encontrada!")
                return
            
            disciplinas = self.__disciplinaDao.buscarDisciplinasPorPessoa(pessoaId)
            
            if disciplinas:
                print(f"\n✅ {len(disciplinas)} disciplina(s) vinculada(s) à pessoa '{pessoa.nome}':")
                print("\n" + "-"*80)
                for disciplina in disciplinas:
                    cargaHoraria = f"{disciplina.carga_horaria}h" if disciplina.carga_horaria else "N/A"
                    print(f"ID: {disciplina.id} | {disciplina.nome} | Carga: {cargaHoraria}")
                print("-"*80)
            else:
                print(f"⚠️  Nenhuma disciplina vinculada à pessoa '{pessoa.nome}'.")
        
        except ValueError:
            print("❌ Erro: ID deve ser um número inteiro!")
        except Exception as e:
            print(f"❌ Erro ao listar disciplinas: {e}")
    
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
                    self.criarDisciplina()
                elif opcao == '2':
                    self.listarDisciplinas()
                elif opcao == '3':
                    self.buscarPorId()
                elif opcao == '4':
                    self.buscarPorNome()
                elif opcao == '5':
                    self.atualizarDisciplina()
                elif opcao == '6':
                    self.deletarDisciplina()
                elif opcao == '7':
                    self.vincularPessoa()
                elif opcao == '8':
                    self.desvincularPessoa()
                elif opcao == '9':
                    self.listarPessoasDisciplina()
                elif opcao == '10':
                    self.listarDisciplinasPessoa()
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
        service = DisciplinaService(db)
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

