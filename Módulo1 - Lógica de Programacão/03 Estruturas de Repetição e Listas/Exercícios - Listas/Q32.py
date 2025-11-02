# 32. Busca binária em lista ordenada
lista = [2, 4, 6, 8, 10, 12, 14, 16]
valor = int(input("Valor para buscar (binária): "))
low = 0
high = len(lista) - 1
indice = -1
while low <= high:
    mid = (low + high) // 2
    if lista[mid] == valor:
        indice = mid
        break
    elif lista[mid] < valor:
        low = mid + 1
    else:
        high = mid - 1
print("Índice encontrado:", indice)