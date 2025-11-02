# 22. Verificar se um número é triangular
n = int(input("Digite um número: "))
i = 1
soma = 0
while soma < n:
    soma += i
    i += 1
if soma == n:
    print(f"{n} é um número triangular.")
else:
    print(f"{n} não é um número triangular.")