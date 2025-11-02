# Exercício 29 — Coluna de mercúrio para Celsius
def main():
    h = float(input("Altura (cm): "))
    temp = (h - 0.4) * 100 / (20.4 - 0.4)
    print(f"Temperatura equivalente: {temp:.2f} °C")

if __name__ == "__main__":
    main()