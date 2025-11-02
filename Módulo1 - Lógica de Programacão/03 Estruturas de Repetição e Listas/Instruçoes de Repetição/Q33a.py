# 33: Soma dos dígitos de um número

numero = input("Digite um número: ")

soma_digitos = 0
# Itera sobre cada caractere do número
for digito in numero:
    soma_digitos += int(digito)

# Exibe a soma dos dígitos
print(f"A soma dos dígitos de {numero} é: {soma_digitos}")