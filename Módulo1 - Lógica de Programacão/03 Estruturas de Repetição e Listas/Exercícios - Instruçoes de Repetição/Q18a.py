# 18: Soma dos números entre dois valores
inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

soma = 0
for i in range(inicio, fim + 1):
    soma += i

print(f"A soma dos números entre {inicio} e {fim} é: {soma}")