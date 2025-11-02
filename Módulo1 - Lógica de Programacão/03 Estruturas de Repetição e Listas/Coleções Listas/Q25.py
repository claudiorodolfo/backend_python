# 25. Verifique se uma lista é um palíndromo
lista = [1, 2, 3, 2, 1]
palind = True
i = 0
while i < len(lista) // 2:
    if lista[i] != lista[len(lista) - 1 - i]:
        palind = False
        break
    i += 1
print("É palíndromo?" , "Sim" if palind else "Não")