# 21. Substitua todas as vogais numa lista de caracteres por '*'
lista = list(input("Digite uma palavra ou sequência de caracteres: "))
vogais = ['a','e','i','o','u','A','E','I','O','U']
i = 0
while i < len(lista):
    if lista[i] in vogais:
        lista[i] = '*'
    i += 1
print("Resultado:", ''.join(lista))
