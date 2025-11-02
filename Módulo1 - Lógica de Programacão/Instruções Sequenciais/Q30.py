# Exercício 30 — Dilatação linear (barra de cobre)
def main():
    c0 = 90  # metros a 0 °C
    t = float(input("Temperatura atual (°C): "))
    alpha = 1.7e-5
    comprimento = c0 * (1 + alpha * t)
    print(f"Comprimento atual: {comprimento:.4f} m")

if __name__ == "__main__":
    main()