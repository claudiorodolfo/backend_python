# Exercício 25 — Recomendação nutricional
def main():
    nome = input("Nome: ")
    peso = float(input("Peso (kg): "))
    agua = (50 * peso) / 1000  # litros
    carbo = 6 * peso  # gramas
    prote = 2.5 * peso  # gramas
    print(f"{nome}, ingestão diária recomendada:\n  Água: {agua:.2f} L\n  Carboidratos: {carbo:.2f} g\n  Proteínas: {prote:.2f} g")

if __name__ == "__main__":
    main()