# Exercício 4: Maior e menor elemento em lista
lista = [10, -3, 25, 7, 0, 25]
# inicializar
maior = lista[0]
menor = lista[0]
for x in lista:
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print("Maior:", maior)
print("Menor:", menor)