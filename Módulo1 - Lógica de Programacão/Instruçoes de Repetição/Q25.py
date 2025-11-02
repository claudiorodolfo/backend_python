# 25. Verificar se um número é de Lucas
n = int(input("Digite um número: "))
a, b = 2, 1
while b < n:
    a, b = b, a + b
if b == n:
    print(f"{n} é um número de Lucas.")
else:
    print(f"{n} não é um número de Lucas.")