# 33. Soma dos dígitos de um número
n = input("Digite um número: ")
soma = sum(int(digit) for digit in n)
print(f"Soma dos dígitos: {soma}")