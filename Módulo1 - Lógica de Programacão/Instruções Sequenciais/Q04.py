# Exercício 4 — Média harmônica das três provas
def main():
    nome = input("Informe o nome do aluno: ")
    n1 = float(input("Nota da prova 1: "))
    n2 = float(input("Nota da prova 2: "))
    n3 = float(input("Nota da prova 3: "))
    if n1 == 0 or n2 == 0 or n3 == 0:
        print("Notas não podem ser zero para cálculo da média harmônica.")
    else:
        media_harmonica = 3 / (1/n1 + 1/n2 + 1/n3)
        print(f"Aluno: {nome} — Média harmônica: {media_harmonica}")

if __name__ == "__main__":
    main()