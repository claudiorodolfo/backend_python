# 7. Imprimir números de 1 a 50 pulando múltiplos de 4 e 5
for i in range(1, 51):
    if i % 4 == 0 or i % 5 == 0:
        continue
    print(i)