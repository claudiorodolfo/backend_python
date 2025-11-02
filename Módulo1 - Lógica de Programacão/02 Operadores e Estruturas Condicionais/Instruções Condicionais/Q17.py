valor = float(input("Digite o valor da compra: "))
if valor <= 50: valor *= 0.9
elif valor <= 100: valor *= 0.85
else: valor *= 0.8
print("Valor com desconto:", valor)