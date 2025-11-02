# 11. Média de 10 números informados pelo usuário
soma = 0
for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num
media = soma / 10
print(f"Média: {media}")