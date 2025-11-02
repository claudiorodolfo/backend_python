# Exercício 8: Multiplique cada elemento por valor específico; mostre antes e depois
lista = [2, 4, 6, 8]
print("Antes:", lista)
fator = int(input("Multiplicar por: "))
i = 0
while i < len(lista):
    lista[i] = lista[i] * fator
    i += 1
print("Depois:", lista)