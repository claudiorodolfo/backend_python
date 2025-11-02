# 26. Divisores de um número
n = int(input("Digite um número: "))
divisores = [i for i in range(1, n + 1) if n % i == 0]
print(f"Divisores de {n}: {divisores}")