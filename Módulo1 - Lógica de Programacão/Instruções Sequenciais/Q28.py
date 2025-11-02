# Exercício 28 — Fahrenheit para Kelvin
def main():
    f = float(input("Temperatura (°F): "))
    k = (f - 32) * 5/9 + 273.15
    print(f"Equivalente em K: {k:.2f}")

if __name__ == "__main__":
    main()