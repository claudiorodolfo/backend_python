#15. Potência sem usar a função pow
b = int(input("Digite a base: "))
n = int(input("Digite o expoente: "))
resultado = 1
for _ in range(n):
    resultado *= b
print(f"{b} elevado a {n} é {resultado}")