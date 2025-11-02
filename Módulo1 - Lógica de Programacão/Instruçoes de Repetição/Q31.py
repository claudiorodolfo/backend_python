# 31. Verificar se um número é palíndromo
n = input("Digite um número: ")
if n == n[::-1]:
    print(f"{n} é um número palíndromo.")
else:
    print(f"{n} não é um número palíndromo.")