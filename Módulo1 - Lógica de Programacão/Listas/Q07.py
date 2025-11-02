# Exercício 7: Soma dos elementos em posições pares (índices pares)
lista = [10, 11, 12, 13, 14, 15]
soma = 0
# índice 0, 2, 4 ...
indice = 0
while indice < len(lista):
    soma += lista[indice]
    indice += 2
print("Soma índices pares:", soma)