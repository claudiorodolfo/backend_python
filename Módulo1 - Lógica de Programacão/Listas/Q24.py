# 24. Insira um novo elemento em uma posição específica (índice) informados pelo usuário
lista = [10, 20, 30, 40]
print("Lista inicial:", lista)
pos = int(input("Índice para inserir novo elemento: "))
elem = input("Elemento a inserir: ")
# para inserir manualmente, vamos criar nova lista
nova = []
i = 0
while i < pos and i < len(lista):
    nova.append(lista[i])
    i += 1
nova.append(elem)
while i < len(lista):
    nova.append(lista[i])
    i += 1
print("Após inserção:", nova)