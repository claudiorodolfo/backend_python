# 4. Tabuada de multiplicação de um número dado pelo usuário
num = int(input("Digite o número para tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")