# 32. Soma de números até um número negativo
soma = 0
while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    soma += num
print(f"Soma dos números digitados: {soma}")