salario = float(input("Digite o salário: "))
tempo = int(input("Digite o tempo de serviço em meses: "))
if tempo >= 60:
    salario *= 1.1
print("Salário final:", salario)