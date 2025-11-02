# 20. Remova todas as ocorrências de um texto específico em uma lista de strings.
lista = ["gato", "cachorro", "pássaro", "gato", "peixe", "gato"]
texto = input("Texto para remover todas as ocorrências: ")
# vamos construir nova lista sem o texto
nova = []
i = 0
while i < len(lista):
    if lista[i] != texto:
        nova.append(lista[i])
    i += 1
print("Original:", lista)
print("Nova:", nova)