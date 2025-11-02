# Exercício 26 — Fahrenheit para Celsius
def main():
    f = float(input("Temperatura (°F): "))
    c = (f - 32) * 5/9
    print(f"Equivalente em °C: {c:.2f}")

if __name__ == "__main__":
    main()