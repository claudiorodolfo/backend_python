# 34. Soma dos dígitos pares de um número
# Solicita ao usuário um número
numero = input("Digite um número: ")

# Inicializa a variável para armazenar a soma dos dígitos pares
soma_pares = 0

# Itera sobre cada caractere do número
for digito in numero:
    # Converte o caractere para inteiro
    digito_int = int(digito)
    # Verifica se o dígito é par
    if digito_int % 2 == 0:
        soma_pares += digito_int

# Exibe a soma dos dígitos pares
print(f"Soma dos dígitos pares: {soma_pares}")