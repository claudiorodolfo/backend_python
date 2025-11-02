# 18. Dadas duas listas do mesmo tamanho, multiplicar elemento a elemento e armazenar em terceira lista.
listaA = [2, 4, 6, 8]
listaB = [1, 3, 5, 7]
resultado = []
i = 0
while i < len(listaA):
    resultado.append(listaA[i] * listaB[i])
    i += 1
print("Lista A:", listaA)
print("Lista B:", listaB)
print("Resultado da multiplicação elemento a elemento:", resultado)