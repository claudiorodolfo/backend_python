idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso (kg): "))
if idade >= 12:
    if peso >= 60: print("Dosagem: 40 gotas")
    else: print("Dosagem: 30 gotas")
else:
    gotas = int(peso/2)
    print("Dosagem:", gotas, "gotas")