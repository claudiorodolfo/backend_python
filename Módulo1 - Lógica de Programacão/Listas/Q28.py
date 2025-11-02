# 28. Primeiros N termos da sequência de Fibonacci
N = int(input("Quantos termos de Fibonacci gerar? "))
lista = []
i = 0
a = 0
b = 1
while i < N:
    lista.append(a)
    prox = a + b
    a = b
    b = prox
    i += 1
print("Sequência de Fibonacci:", lista)