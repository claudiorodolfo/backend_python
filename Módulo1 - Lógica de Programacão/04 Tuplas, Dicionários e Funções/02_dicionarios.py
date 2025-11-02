"""
02 - Dicionários

Este arquivo demonstra o uso de dicionários em Python.
"""

print("=" * 60)
print("DICIONÁRIOS")
print("=" * 60)

# ============================================
# CRIAR DICIONÁRIOS
# ============================================
print("\n1. CRIAR DICIONÁRIOS:")
print("-" * 60)

# Dicionário vazio
dic_vazio = {}
print(f"Dicionário vazio: {dic_vazio}")

# Dicionário com valores
pessoa = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}
print(f"Dicionário: {pessoa}")

# ============================================
# ACESSAR VALORES
# ============================================
print("\n2. ACESSAR VALORES:")
print("-" * 60)

print(f"pessoa['nome']: {pessoa['nome']}")
print(f"pessoa['idade']: {pessoa['idade']}")

# Método get() (mais seguro)
print(f"\npessoa.get('nome'): {pessoa.get('nome')}")
print(f"pessoa.get('email', 'Não informado'): {pessoa.get('email', 'Não informado')}")

# ============================================
# ADICIONAR E MODIFICAR
# ============================================
print("\n3. ADICIONAR E MODIFICAR:")
print("-" * 60)

print(f"Antes: {pessoa}")

# Modificar
pessoa["idade"] = 26
print(f"Após modificar idade: {pessoa}")

# Adicionar
pessoa["email"] = "joao@email.com"
print(f"Após adicionar email: {pessoa}")

# ============================================
# REMOVER ELEMENTOS
# ============================================
print("\n4. REMOVER ELEMENTOS:")
print("-" * 60)

pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
print(f"Antes: {pessoa}")

# del
del pessoa["cidade"]
print(f"Após del pessoa['cidade']: {pessoa}")

# pop()
pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}
idade = pessoa.pop("idade")
print(f"pessoa.pop('idade'): removeu {idade}")
print(f"Depois: {pessoa}")

# ============================================
# MÉTODOS ÚTEIS
# ============================================
print("\n5. MÉTODOS ÚTEIS:")
print("-" * 60)

pessoa = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

# keys() - chaves
print(f"keys(): {list(pessoa.keys())}")

# values() - valores
print(f"values(): {list(pessoa.values())}")

# items() - pares chave-valor
print(f"items(): {list(pessoa.items())}")

# Iterar sobre dicionário
print("\nIterando sobre dicionário:")
for chave, valor in pessoa.items():
    print(f"  {chave}: {valor}")

# ============================================
# EXEMPLOS PRÁTICOS
# ============================================
print("\n" + "=" * 60)
print("EXEMPLOS PRÁTICOS")
print("=" * 60)

# Exemplo 1: Cadastro de produtos
print("\nExemplo 1: Produtos")
print("-" * 60)
produto = {
    "nome": "Notebook",
    "preco": 2500.00,
    "estoque": 10
}

print(f"Produto: {produto['nome']}")
print(f"Preço: R$ {produto['preco']:.2f}")
print(f"Estoque: {produto['estoque']} unidades")

# Exemplo 2: Múltiplos produtos
print("\nExemplo 2: Lista de dicionários")
print("-" * 60)
produtos = [
    {"nome": "Notebook", "preco": 2500.00},
    {"nome": "Mouse", "preco": 50.00},
    {"nome": "Teclado", "preco": 150.00}
]

for produto in produtos:
    print(f"{produto['nome']}: R$ {produto['preco']:.2f}")

