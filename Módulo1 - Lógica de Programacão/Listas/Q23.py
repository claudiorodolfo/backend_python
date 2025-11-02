# 23. A partir de duas listas, crie uma terceira concatenando-as
listaA = [1, 3, 5]
listaB = [2, 4, 6]
concat = []
i = 0
while i < len(listaA):
    concat.append(listaA[i])
    i += 1
i = 0
while i < len(listaB):
    concat.append(listaB[i])
    i += 1
print("Lista A:", listaA)
print("Lista B:", listaB)
print("Concat:", concat)