n = int(input("Digite um número de 1 a 7: "))
if n in [2,3,4,5,6]:
    print("Dia útil")
elif n in [1,7]:
    print("Final de semana")
else:
    print("Número inválido")