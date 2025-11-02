#20. Maior número informado pelo usuário
quantidade = int(input("Quantos números você deseja informar? "))
maior = float('-inf')
for i in range(quantidade):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > maior:
        maior = num
print(f"Maior número informado: {maior}")