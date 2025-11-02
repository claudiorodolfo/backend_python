# 24. Sequência de Fibonacci até o enésimo termo
n = int(input("Digite o número de termos: "))
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b