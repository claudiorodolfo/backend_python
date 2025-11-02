# 17. Verifique se duas listas são iguais (mesmos elementos, mesma ordem).
listaA = [1, 2, 3, 4]
listaB = [1, 2, 3, 4]
igual = True
if len(listaA) != len(listaB):
    igual = False
else:
    i = 0
    while i < len(listaA):
        if listaA[i] != listaB[i]:
            igual = False
            break
        i += 1
print("São iguais?" , "Sim" if igual else "Não")