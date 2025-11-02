# Exercício 24 — Substituir sobrenome
def main():
    nome = input("Nome completo: ")
    velho = input("Sobrenome a ser substituído: ")
    novo = input("Novo sobrenome: ")
    resultado = nome.replace(velho, novo)
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()