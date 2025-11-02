# Exercício 11: Média dos elementos
lista = [3, 6, 9, 12, 15]
soma = 0
i = 0
while i < len(lista):
    soma += lista[i]
    i += 1
media = soma / len(lista)
print("Média:", media)