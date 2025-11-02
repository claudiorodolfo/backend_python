# Exercício 27 — Celsius para Fahrenheit
def main():
    c = float(input("Temperatura (°C): "))
    f = (c * 9/5) + 32
    print(f"Equivalente em °F: {f:.2f}")

if __name__ == "__main__":
    main()