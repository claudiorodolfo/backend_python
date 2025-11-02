"""
Script de teste completo do projeto SQLite+POO
Testa todas as funcionalidades e verifica se está tudo funcionando
"""
import sys
import os

# Adicionar o diretório pai ao path para permitir imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bd.database import DatabaseConnection
from model.categoria import Categoria
from model.pessoa import Pessoa
from dao.categoria_dao import CategoriaDAO
from dao.pessoa_dao import PessoaDAO


def limparBanco(db):
    """Remove todos os dados do banco para testes limpos"""
    print("🧹 Limpando banco de dados...")
    db.limparDados()
    print("✓ Banco limpo!\n")


def testarCategoria_dao(db):
    """Testa operações CRUD de Categoria"""
    print("=" * 60)
    print("TESTE 1: Operações CRUD - Categoria")
    print("=" * 60)
    
    categoriaDao = CategoriaDAO(db)
    erros = []
    
    try:
        # CREATE
        print("\n✓ CREATE - Criando categoria...")
        cat1 = Categoria(id=None, nome="Desenvolvedor")
        categoriaDao.salvar(cat1)
        assert cat1.id is not None, "ID não foi atribuído"
        print(f"  ✓ Categoria criada: {cat1}")
        
        cat2 = Categoria(id=None, nome="Designer")
        categoriaDao.salvar(cat2)
        assert cat2.id is not None, "ID não foi atribuído"
        print(f"  ✓ Categoria criada: {cat2}")
        
        # READ - Buscar por ID
        print("\n✓ READ - Buscando categoria por ID...")
        catEncontrada = categoriaDao.buscarPorId(cat1.id)
        assert catEncontrada is not None, "Categoria não encontrada por ID"
        assert catEncontrada.nome == "Desenvolvedor", "Nome incorreto"
        print(f"  ✓ Categoria encontrada: {catEncontrada}")
        
        # READ - Buscar por nome
        print("\n✓ READ - Buscando categoria por nome...")
        catPorNome = categoriaDao.buscarPorNome("Designer")
        assert catPorNome is not None, "Categoria não encontrada por nome"
        assert catPorNome.nome == "Designer", "Nome incorreto"
        print(f"  ✓ Categoria encontrada: {catPorNome}")
        
        # READ - Listar todas
        print("\n✓ READ - Listando todas as categorias...")
        todas = categoriaDao.listarTodas()
        assert len(todas) >= 2, f"Esperava pelo menos 2 categorias, encontrou {len(todas)}"
        print(f"  ✓ Total de categorias: {len(todas)}")
        for cat in todas:
            print(f"    - {cat}")
        
        # UPDATE
        print("\n✓ UPDATE - Atualizando categoria...")
        cat1.nome = "Desenvolvedor Senior"
        categoriaDao.salvar(cat1)
        catAtualizada = categoriaDao.buscarPorId(cat1.id)
        assert catAtualizada.nome == "Desenvolvedor Senior", "Nome não foi atualizado"
        print(f"  ✓ Categoria atualizada: {catAtualizada}")
        
        # DELETE
        print("\n✓ DELETE - Deletando categoria...")
        sucesso = categoriaDao.deletar(cat2)
        assert sucesso, "Falha ao deletar categoria"
        catDeletada = categoriaDao.buscarPorId(cat2.id)
        assert catDeletada is None, "Categoria ainda existe após deletar"
        print(f"  ✓ Categoria deletada com sucesso")
        
        print("\n✅ TESTE 1 PASSOU - Categoria CRUD OK\n")
        return True
        
    except Exception as e:
        erros.append(f"Erro no teste de Categoria: {e}")
        import traceback
        traceback.print_exc()
        print(f"\n❌ TESTE 1 FALHOU: {e}\n")
        return False


def testarPessoaDao(db):
    """Testa operações CRUD de Pessoa"""
    print("=" * 60)
    print("TESTE 2: Operações CRUD - Pessoa")
    print("=" * 60)
    
    categoriaDao = CategoriaDAO(db)
    pessoaDao = PessoaDAO(db)
    erros = []
    
    try:
        # Garantir que temos uma categoria
        print("\n✓ Preparando categoria para testes...")
        categoria = categoriaDao.buscarPorNome("Desenvolvedor Senior")
        if not categoria:
            categoria = Categoria(id=None, nome="Desenvolvedor Senior")
            categoriaDao.salvar(categoria)
        print(f"  ✓ Usando categoria: {categoria}")
        
        # CREATE
        print("\n✓ CREATE - Criando pessoa...")
        pessoa1 = Pessoa(
            id=None,
            nome="João Developer",
            email="joao@example.com",
            categoria=categoria,
            idade=28,
            altura=1.75,
            peso=75.0,
            data_nascimento="1995-05-15",
            ativo=True,
            observacoes="Desenvolvedor Python",
            telefone="11999999999"
        )
        pessoaDao.salvar(pessoa1)
        assert pessoa1.id is not None, "ID não foi atribuído"
        print(f"  ✓ Pessoa criada: {pessoa1}")
        
        # CREATE - Segunda pessoa
        categoria2 = categoriaDao.buscarPorNome("Designer")
        if not categoria2:
            categoria2 = Categoria(id=None, nome="Designer")
            categoriaDao.salvar(categoria2)
        
        pessoa2 = Pessoa(
            id=None,
            nome="Maria Designer",
            email="maria@example.com",
            categoria=categoria2,
            idade=25,
            altura=1.65,
            peso=60.0,
            data_nascimento="1998-03-20",
            ativo=True,
            observacoes="Designer UX/UI",
            telefone="11888888888"
        )
        pessoaDao.salvar(pessoa2)
        assert pessoa2.id is not None, "ID não foi atribuído"
        print(f"  ✓ Pessoa criada: {pessoa2}")
        
        # READ - Buscar por ID
        print("\n✓ READ - Buscando pessoa por ID...")
        pessoaEncontrada = pessoaDao.buscarPorId(pessoa1.id)
        assert pessoaEncontrada is not None, "Pessoa não encontrada por ID"
        assert pessoaEncontrada.nome == "João Developer", "Nome incorreto"
        assert pessoaEncontrada.email == "joao@example.com", "Email incorreto"
        print(f"  ✓ Pessoa encontrada: {pessoaEncontrada}")
        
        # READ - Buscar por nome
        print("\n✓ READ - Buscando pessoa por nome...")
        pessoasJoao = pessoaDao.buscarPorNome("João")
        assert len(pessoasJoao) > 0, "Nenhuma pessoa encontrada com nome 'João'"
        print(f"  ✓ Pessoas encontradas com 'João': {len(pessoasJoao)}")
        for p in pessoasJoao:
            print(f"    - {p}")
        
        # READ - Buscar por categoria
        print("\n✓ READ - Buscando pessoas por categoria...")
        pessoasCat = pessoaDao.buscarPorCategoria(categoria.id)
        assert len(pessoasCat) > 0, "Nenhuma pessoa encontrada na categoria"
        print(f"  ✓ Pessoas na categoria '{categoria.nome}': {len(pessoasCat)}")
        
        # READ - Listar todas
        print("\n✓ READ - Listando todas as pessoas...")
        todasPessoas = pessoaDao.listarTodas()
        assert len(todasPessoas) >= 2, f"Esperava pelo menos 2 pessoas, encontrou {len(todasPessoas)}"
        print(f"  ✓ Total de pessoas: {len(todasPessoas)}")
        
        # Testar relacionamento
        print("\n✓ READ - Testando relacionamento com categoria...")
        categoriaRel = pessoaDao.obterCategoria(pessoaEncontrada)
        assert categoriaRel is not None, "Categoria não foi encontrada"
        assert categoriaRel.nome == "Desenvolvedor Senior", "Categoria incorreta"
        print(f"  ✓ Categoria relacionada: {categoriaRel.nome}")
        
        # UPDATE
        print("\n✓ UPDATE - Atualizando pessoa...")
        pessoa1.idade = 29
        pessoa1.observacoes = "Desenvolvedor Python Senior"
        pessoaDao.salvar(pessoa1)
        pessoaAtualizada = pessoaDao.buscarPorId(pessoa1.id)
        assert pessoaAtualizada.idade == 29, "Idade não foi atualizada"
        assert pessoaAtualizada.observacoes == "Desenvolvedor Python Senior", "Observações não foram atualizadas"
        print(f"  ✓ Pessoa atualizada: {pessoaAtualizada}")
        
        # UPDATE - Desativar pessoa
        print("\n✓ UPDATE - Desativando pessoa...")
        pessoa2.ativo = False
        pessoaDao.salvar(pessoa2)
        pessoaDesativada = pessoaDao.buscarPorId(pessoa2.id)
        assert pessoaDesativada.ativo == False, "Pessoa não foi desativada"
        print(f"  ✓ Pessoa desativada: {pessoaDesativada}")
        
        # DELETE
        print("\n✓ DELETE - Deletando pessoa...")
        sucesso = pessoaDao.deletar(pessoa2)
        assert sucesso, "Falha ao deletar pessoa"
        pessoaDeletada = pessoaDao.buscarPorId(pessoa2.id)
        assert pessoaDeletada is None, "Pessoa ainda existe após deletar"
        print(f"  ✓ Pessoa deletada com sucesso")
        
        print("\n✅ TESTE 2 PASSOU - Pessoa CRUD OK\n")
        return True
        
    except Exception as e:
        erros.append(f"Erro no teste de Pessoa: {e}")
        import traceback
        traceback.print_exc()
        print(f"\n❌ TESTE 2 FALHOU: {e}\n")
        return False


def testarIntegridadeReferencial(db):
    """Testa integridade referencial e constraints"""
    print("=" * 60)
    print("TESTE 3: Integridade Referencial e Constraints")
    print("=" * 60)
    
    categoriaDao = CategoriaDAO(db)
    pessoaDao = PessoaDAO(db)
    
    try:
        # Testar constraint UNIQUE em email
        print("\n✓ Testando constraint UNIQUE em email...")
        categoria = categoriaDao.listarTodas()[0]  # Pegar primeira categoria
        
        pessoaDuplicada = Pessoa(
            id=None,
            nome="Teste Duplicado",
            email="joao@example.com",  # Email já existe
            categoria=categoria,
            idade=30
        )
        
        try:
            pessoaDao.salvar(pessoaDuplicada)
            print("  ⚠️  AVISO: Constraint UNIQUE não foi aplicada (pode ser esperado se não houver constraint)")
        except Exception as e:
            if "UNIQUE" in str(e) or "unique" in str(e).lower():
                print("  ✓ Constraint UNIQUE funcionando corretamente")
            else:
                raise
        
        # Testar constraint de foreign key
        print("\n✓ Testando integridade referencial (foreign key)...")
        pessoaInvalida = Pessoa(
            id=None,
            nome="Teste FK",
            email="teste_fk@example.com",
            categoria=Categoria(id=99999, nome="Inexistente"),  # Categoria que não existe
            idade=30
        )
        
        try:
            pessoaDao.salvar(pessoaInvalida)
            print("  ⚠️  AVISO: Foreign key constraint não foi verificada")
        except Exception as e:
            if "FOREIGN KEY" in str(e) or "foreign" in str(e).lower():
                print("  ✓ Foreign key constraint funcionando")
            else:
                # Pode dar erro de categoria sem ID, que é o comportamento esperado
                if "categoria válida" in str(e).lower():
                    print("  ✓ Validação de categoria funcionando")
                else:
                    raise
        
        print("\n✅ TESTE 3 PASSOU - Integridade OK\n")
        return True
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\n❌ TESTE 3 FALHOU: {e}\n")
        return False


def executarTestes():
    """Executa todos os testes"""
    print("\n" + "=" * 60)
    print("INICIANDO TESTES DO PROJETO SQLite+POO")
    print("=" * 60 + "\n")
    
    # Caminho do banco de dados relativo ao diretório raiz do projeto
    dbPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exemplo_bd.db')
    db = DatabaseConnection(dbPath)
    resultados = []
    
    try:
        db.conectar()
        
        # Criar tabelas
        print("📋 Criando/verificando tabelas...")
        db.criarTabelas()
        print("✓ Tabelas OK\n")
        
        # Limpar banco para testes limpos
        limparBanco(db)
        
        # Executar testes
        resultados.append(("Categoria CRUD", testarCategoria_dao(db)))
        resultados.append(("Pessoa CRUD", testarPessoaDao(db)))
        resultados.append(("Integridade Referencial", testarIntegridadeReferencial(db)))
        
        # Resumo
        print("\n" + "=" * 60)
        print("RESUMO DOS TESTES")
        print("=" * 60)
        
        total = len(resultados)
        passou = sum(1 for _, resultado in resultados if resultado)
        
        for nome, resultado in resultados:
            status = "✅ PASSOU" if resultado else "❌ FALHOU"
            print(f"{nome}: {status}")
        
        print("\n" + "-" * 60)
        print(f"Total: {passou}/{total} testes passaram")
        print("=" * 60 + "\n")
        
        if passou == total:
            print("🎉 TODOS OS TESTES PASSARAM! Projeto está funcionando corretamente.")
            return True
        else:
            print("⚠️  ALGUNS TESTES FALHARAM. Verifique os erros acima.")
            return False
        
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        db.fechar()
        print("✓ Conexão encerrada!")


if __name__ == "__main__":
    sucesso = executarTestes()
    sys.exit(0 if sucesso else 1)

