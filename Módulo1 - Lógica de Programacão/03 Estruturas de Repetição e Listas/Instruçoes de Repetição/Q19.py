#19. Soma dos números ímpares em um intervalo
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
soma = sum(i for i in range(inicio, fim + 1) if i % 2 != 0)
print(f"Soma dos números ímpares entre {inicio} e {fim}: {soma}")