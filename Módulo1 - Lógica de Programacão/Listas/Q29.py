# 29. Primeiros N termos da sequência de Lucas
N = int(input("Quantos termos de Lucas gerar? "))
lista = []
i = 0
# Lucas começa com 2, 1, ...
aL = 2
bL = 1
while i < N:
    lista.append(aL)
    proxL = aL + bL
    aL = bL
    bL = proxL
    i += 1
print("Sequência de Lucas:", lista)