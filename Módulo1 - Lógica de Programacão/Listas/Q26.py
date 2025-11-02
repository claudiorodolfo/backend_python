# 26. Gere uma lista com os N primeiros números primos
print("Exercício 26:")
N = int(input("Quantos primos gerar? "))
primos = []
num = 2
while len(primos) < N:
    # verificar se num é primo
        eh_primo = True
        div = 2
        while div * div <= num:
            if num % div == 0:
                eh_primo = False
                break
            div += 1
        if eh_primo:
            primos.append(num)
        num += 1
print(f"Primeiros {N} primos:", primos)