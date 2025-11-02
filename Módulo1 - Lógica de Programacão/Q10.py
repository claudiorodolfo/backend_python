# Exercício 10: Substitua elementos negativos por zero
lista = [5, -3, 7, -1, 0, -5, 2]
print("Antes:", lista)
i = 0
while i < len(lista):
    if lista[i] < 0:
        lista[i] = 0
    i += 1
print("Depois:", lista)