# 34. Insira elemento em posição específica de lista
lista = ['a', 'b', 'c', 'd']
print("Original:", lista)
pos = int(input("Índice para inserir novo elemento: "))
elem = input("Elemento para inserir: ")
# Usando insert:
lista.insert(pos, elem)
print("Após inserção:", lista)
