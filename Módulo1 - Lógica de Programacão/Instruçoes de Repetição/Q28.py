# 28. Números primos de 1 a 50
for n in range(2, 51):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        print(n)