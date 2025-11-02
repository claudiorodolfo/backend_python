# Exercício 33 — Altura de queda livre
def main():
    t = float(input("Tempo de queda (s): "))
    g = 9.8
    h_cm = (g * t**2 / 2) * 100
    print(f"Altura da queda: {h_cm:.2f} cm")

if __name__ == "__main__":
    main()