"""
Exemplo de uso das classes ORM para demonstrar operações CRUD
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


def exemploCrudCompleto():   # Criar conexão
    # Caminho do banco de dados relativo ao diretório raiz do projeto
    dbPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exemplo_bd.db')
    db = DatabaseConnection(dbPath)
    
    try:
        db.conectar()
        
        # Criar tabelas se não existirem
        db.criarTabelas()
        
        # Criar instâncias dos DAOs
        pessoaDao = PessoaDAO(db)
        categoriaDao = CategoriaDAO(db)
        
        # ===== CREATE (Criar) =====
        print("=== CREATE - Criando registros ===")
        
        # Criar categorias (verificar se já existem primeiro)
        cat1 = categoriaDao.buscarPorNome("Desenvolvedor")
        if not cat1:
            cat1 = Categoria(id=None, nome="Desenvolvedor")
            categoriaDao.salvar(cat1)
            print(f"Categoria criada: {cat1}")
        else:
            print(f"Categoria já existe: {cat1}")
        
        cat2 = categoriaDao.buscarPorNome("Designer")
        if not cat2:
            cat2 = Categoria(id=None, nome="Designer")
            categoriaDao.salvar(cat2)
            print(f"Categoria criada: {cat2}")
        else:
            print(f"Categoria já existe: {cat2}")
        
        # Criar pessoas (verificar se já existem por email)
        pessoasJoao = pessoaDao.buscarPorNome("João Developer")
        if pessoasJoao and any(p.email == "joao@example.com" for p in pessoasJoao):
            pessoa1 = next(p for p in pessoasJoao if p.email == "joao@example.com")
            print(f"Pessoa já existe: {pessoa1}")
        else:
            pessoa1 = Pessoa(
                id=None,
                nome="João Developer",
                email="joao@example.com",
                categoria=cat1,
                idade=28,
                altura=1.75,
                peso=75.0,
                data_nascimento="1995-05-15",
                ativo=True,
                observacoes="Desenvolvedor Python",
                telefone="11999999999"
            )
            pessoaDao.salvar(pessoa1)
            print(f"Pessoa criada: {pessoa1}")
        
        pessoasMaria = pessoaDao.buscarPorNome("Maria Designer")
        if pessoasMaria and any(p.email == "maria@example.com" for p in pessoasMaria):
            pessoa2 = next(p for p in pessoasMaria if p.email == "maria@example.com")
            print(f"Pessoa já existe: {pessoa2}")
        else:
            pessoa2 = Pessoa(
                id=None,
                nome="Maria Designer",
                email="maria@example.com",
                categoria=cat2,
                idade=25,
                altura=1.65,
                peso=60.0,
                data_nascimento="1998-03-20",
                ativo=True,
                observacoes="Designer UX/UI",
                telefone="11888888888"
            )
            pessoaDao.salvar(pessoa2)
            print(f"Pessoa criada: {pessoa2}")
        print()
        
        # ===== READ (Ler) =====
        print("=== READ - Lendo registros ===")
        
        # Buscar por ID
        categoriaEncontrada = categoriaDao.buscarPorId(cat1.id)
        print(f"Categoria encontrada por ID: {categoriaEncontrada}")
        
        # Buscar por nome
        categoriaPorNome = categoriaDao.buscarPorNome("Designer")
        print(f"Categoria encontrada por nome: {categoriaPorNome}")
        
        # Listar todas
        todasCategorias = categoriaDao.listarTodas()
        print(f"\nTodas as categorias ({len(todasCategorias)}):")
        for cat in todasCategorias:
            print(f"  - {cat}")
        
        # Buscar pessoas por nome
        pessoasEncontradas = pessoaDao.buscarPorNome("João")
        print(f"\nPessoas encontradas com 'João' ({len(pessoasEncontradas)}):")
        for p in pessoasEncontradas:
            print(f"  - {p}")
        
        # Buscar pessoas por categoria
        devs = pessoaDao.buscarPorCategoria(cat1.id)
        print(f"\nPessoas da categoria 'Desenvolvedor' ({len(devs)}):")
        for p in devs:
            categoria = pessoaDao.obterCategoria(p)
            print(f"  - {p.nome} ({categoria.nome if categoria else 'N/A'})")
        
        # ===== UPDATE (Atualizar) =====
        print("\n=== UPDATE - Atualizando registros ===")
        
        # Atualizar categoria (verificar se nome já existe)
        novoNome = "Desenvolvedor Senior"
        catExistente = categoriaDao.buscarPorNome(novoNome)
        if catExistente and catExistente.id != cat1.id:
            print(f"Categoria '{novoNome}' já existe com outro ID. Usando a existente.")
            cat1 = catExistente
        else:
            cat1.nome = novoNome
            categoriaDao.salvar(cat1)
        print(f"Categoria: {cat1}")
        
        # Atualizar pessoa
        pessoa1.idade = 29
        pessoa1.observacoes = "Desenvolvedor Python Senior"
        pessoaDao.salvar(pessoa1)
        print(f"Pessoa atualizada: {pessoa1}")
        
        # Desativar pessoa
        pessoa2.ativo = False
        pessoaDao.salvar(pessoa2)
        print(f"Pessoa desativada: {pessoa2}")
        
        # ===== DELETE (Deletar) =====
        print("\n=== DELETE - Deletando registros ===")
        
        # Deletar pessoa (deve deletar antes de categoria se houver FK)
        pessoa2Deletada = pessoaDao.deletar(pessoa2)
        print(f"Pessoa deletada: {pessoa2Deletada}")
        
        # Verificar se foi deletada
        pessoaVerificada = pessoaDao.buscarPorId(pessoa2.id)
        print(f"Pessoa ainda existe? {pessoaVerificada is not None}")
        
        # ===== Relacionamentos =====
        print("\n=== RELACIONAMENTOS ===")
        
        pessoa1Atualizada = pessoaDao.buscarPorId(pessoa1.id)
        if pessoa1Atualizada:
            categoriaRelacionada = pessoaDao.obterCategoria(pessoa1Atualizada)
            print(f"Pessoa: {pessoa1Atualizada.nome}")
            print(f"Categoria relacionada: {categoriaRelacionada.nome if categoriaRelacionada else 'N/A'}")
        
    except Exception as e:
        print(f"Erro: {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.fechar()
        print("\n✓ Conexão encerrada!")


if __name__ == "__main__":
    exemploCrudCompleto()

