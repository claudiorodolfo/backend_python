#17. Nome em maiúsculo para homens com mais de 21 anos
for _ in range(20):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == 'M' and idade > 21:
        print(nome.upper())