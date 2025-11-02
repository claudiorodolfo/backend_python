# 29. Soma dos números primos de 1 a 50
soma = 0
for n in range(2, 51):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        soma += n
print(f"Soma dos números primos de 1 a 50: {soma}")