# Exercício 9: Conte elementos pares em lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cont_pares = 0
for x in lista:
    if x % 2 == 0:
        cont_pares += 1
print("Quantidade de pares:", cont_pares)