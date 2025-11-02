preco = float(input("Digite o preço de compra: "))
if preco < 20:
    venda = preco * 1.4
else:
    venda = preco * 1.3
print("Preço de venda:", venda)