# 30. Verificar se um número é perfeito
n = int(input("Digite um número: "))
soma_divisores = sum(i for i in range(1, n) if n % i == 0)
if soma_divisores == n:
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} não é um número perfeito.")