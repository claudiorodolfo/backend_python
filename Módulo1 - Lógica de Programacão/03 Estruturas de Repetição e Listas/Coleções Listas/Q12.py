# Exercício 12: Verifique se valor está presente
lista = [7, 4, 9, 12, 3]
valor = int(input("Digite um valor para buscar: "))
achou = False
for x in lista:
    if x == valor:
        achou = True
        break
if achou:
    print("Sim, está presente.")
else:
    print("Não, não está presente.")