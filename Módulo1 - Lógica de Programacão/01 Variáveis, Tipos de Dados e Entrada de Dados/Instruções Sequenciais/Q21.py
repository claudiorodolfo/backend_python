# Exercício 21 — Cálculo de IMC
def main():
    nome = input("Nome: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura**2)
    print(f"{nome} — IMC: {imc:.2f}")

if __name__ == "__main__":
    main()