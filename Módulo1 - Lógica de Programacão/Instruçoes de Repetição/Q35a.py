# 35: Dígitos em ordem inversa com laço for

numero = input("Digite um número: ")

# Inicializa uma string vazia para armazenar os dígitos invertidos
invertido = ""

# Itera sobre os caracteres do número de trás para frente
for i in range(len(numero) - 1, -1, -1):
    invertido += numero[i]

# Exibe os dígitos em ordem inversa
print(f"Dígitos em ordem inversa: {invertido}")