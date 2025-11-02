# 30. Remova elementos repetidos mantendo apenas uma ocorrência de cada (preservando ordem)
lista = [1, 2, 3, 2, 4, 3, 5, 1]
print("Antes:", lista)
nova = []
i = 0
while i < len(lista):
    if lista[i] not in nova:
        nova.append(lista[i])
    i += 1
print("Depois:", nova)