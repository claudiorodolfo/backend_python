# 16. Encontre o índice da primeira ocorrência de um elemento específico; se não existir, imprima -1.
lista = [5, 3, 9, 1, 7, 9]
valor = int(input("Valor para achar o índice da primeira ocorrência: "))
indice = -1
i = 0
while i < len(lista):
    if lista[i] == valor:
        indice = i
        break
    i += 1
print("Índice:", indice)