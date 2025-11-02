# 35. Remova elemento de uma posição específica de lista
lista = [100, 200, 300, 400, 500]
print("Original:", lista)
pos = int(input("Índice para remover elemento: "))
# Usando pop ou del
if 0 <= pos < len(lista):
    del lista[pos]
    print("Após remoção:", lista)
else:
    print("Índice inválido")