# 19. Crie lista de strings, depois inverta a ordem; imprima antes e depois.
lista = ["lua", "sol", "mar", "céu"]
print("Antes:", lista)
invertida = []
i = len(lista) - 1
while i >= 0:
    invertida.append(lista[i])
    i -= 1
print("Depois:", invertida)