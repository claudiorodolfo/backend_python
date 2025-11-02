# 22. Conte quantas vogais há numa lista de caracteres
lista = list(input("Digite uma palavra ou sequência para contar vogais: "))
vogais = ['a','e','i','o','u','A','E','I','O','U']
cont_vogais = 0
i = 0
while i < len(lista):
    if lista[i] in vogais:
        cont_vogais += 1
    i += 1
print("Número de vogais:", cont_vogais)