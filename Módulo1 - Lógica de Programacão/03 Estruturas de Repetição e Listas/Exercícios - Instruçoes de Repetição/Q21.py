# 21. Menor número informado pelo usuário
quantidade = int(input("Quantos números você deseja informar? "))
menor = float('inf')
for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    if num < menor:
        menor = num
print(f"Menor número informado: {menor}")