# 12. Média de uma quantidade variável de números
quantidade = int(input("Quantos números você deseja informar? "))
soma = 0
for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num
media = soma / quantidade
print(f"Média: {media}")