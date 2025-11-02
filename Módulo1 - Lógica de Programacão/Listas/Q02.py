# Exercício 2: Peça N, crie lista com quadrados de 1 a N e imprima
print("Exercício 2:")
N = int(input("Digite N: "))
lista = []
for i in range(1, N + 1):
    lista.append(i * i)
print("Quadrados de 1 a", N, ":", lista)
print()