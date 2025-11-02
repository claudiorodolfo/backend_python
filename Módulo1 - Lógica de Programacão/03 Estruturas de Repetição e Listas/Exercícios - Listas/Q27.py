# 27. Gere uma lista com os números perfeitos menores que N
N = int(input("Digite N (limite para perfeitos): "))
perfeitos = []
num = 1
while num < N:
    soma_div = 0
    i = 1
    while i < num:
        if num % i == 0:
            soma_div += i
        i += 1
    if soma_div == num and num != 0:
        perfeitos.append(num)
    num += 1
print(f"Números perfeitos menores que {N}:", perfeitos)