# 31. Rotacione os elementos de uma lista para a esquerda por uma posição
lista = [1, 2, 3, 4, 5]
print("Original:", lista)
rot = []
i = 1
while i < len(lista):
    rot.append(lista[i])
    i += 1
rot.append(lista[0])
print("Rotacionada à esquerda:", rot)
