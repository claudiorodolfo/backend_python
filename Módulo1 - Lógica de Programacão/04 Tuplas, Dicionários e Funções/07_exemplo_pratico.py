"""
07 - Exemplo Prático Completo

Este arquivo combina tuplas, dicionários e funções.
"""

print("=" * 70)
print("SISTEMA DE GERENCIAMENTO DE PRODUTOS")
print("=" * 70)

# ============================================
# FUNÇÕES AUXILIARES
# ============================================

def criar_produto(nome, preco, estoque):
    """Cria dicionário de produto"""
    return {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

def calcular_total(produtos):
    """Calcula valor total do estoque"""
    total = 0
    for produto in produtos:
        total += produto["preco"] * produto["estoque"]
    return total

def encontrar_produto(produtos, nome):
    """Encontra produto por nome"""
    for produto in produtos:
        if produto["nome"] == nome:
            return produto
    return None

def exibir_produto(produto):
    """Exibe informações do produto"""
    if produto:
        print(f"  Nome: {produto['nome']}")
        print(f"  Preço: R$ {produto['preco']:.2f}")
        print(f"  Estoque: {produto['estoque']} unidades")
        print(f"  Valor total: R$ {produto['preco'] * produto['estoque']:.2f}")
    else:
        print("  Produto não encontrado")

# ============================================
# USO DAS FUNÇÕES
# ============================================

print("\n=== CADASTRO DE PRODUTOS ===")
produtos = []

# Adicionar produtos usando função
produtos.append(criar_produto("Notebook", 2500.00, 10))
produtos.append(criar_produto("Mouse", 50.00, 50))
produtos.append(criar_produto("Teclado", 150.00, 30))

print("\n=== LISTA DE PRODUTOS ===")
for i, produto in enumerate(produtos, 1):
    print(f"\nProduto {i}:")
    exibir_produto(produto)

print("\n=== BUSCAR PRODUTO ===")
produto_encontrado = encontrar_produto(produtos, "Mouse")
print("Buscando 'Mouse':")
exibir_produto(produto_encontrado)

print("\n=== VALOR TOTAL DO ESTOQUE ===")
valor_total = calcular_total(produtos)
print(f"Valor total: R$ {valor_total:.2f}")

print("\n" + "=" * 70)

