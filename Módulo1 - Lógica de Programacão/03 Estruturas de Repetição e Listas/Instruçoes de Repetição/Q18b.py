# 18. Soma de números entre dois valores fornecidos pelo usuário
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
soma = sum(range(inicio, fim + 1))
print(f"Soma dos números entre {inicio} e {fim}: {soma}")