# Exercício 3: Peça N, crie lista de 1 a N e imprima invertida
N = int(input("Digite N: "))
lista = []
for i in range(1, N + 1):
    lista.append(i)
print("Original:", lista)
# inverter
lista_invertida = []
for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])
print("Invertida:", lista_invertida)
