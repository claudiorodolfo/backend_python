a = float(input("Digite o 1º número: "))
b = float(input("Digite o 2º número: "))
c = float(input("Digite o 3º número: "))
media = (a+b+c)/3
nums = sorted([a,b,c])
mediana = nums[1]
if mediana > media: print("Mediana maior que média")
elif mediana < media: print("Mediana menor que média")
else: print("Iguais")