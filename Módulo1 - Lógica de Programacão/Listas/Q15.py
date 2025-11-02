# Exercício 15: Preencher lista com N aleatórios e ordenar decrescente
import random

N = int(input("Quantos números aleatórios gerar? "))
lista = []
i = 0
while i < N:
    lista.append(random.randint(0, 100))
    i += 1
print("Gerados:", lista)
lista.sort(reverse=True)
print("Ordenados decrescente:", lista)