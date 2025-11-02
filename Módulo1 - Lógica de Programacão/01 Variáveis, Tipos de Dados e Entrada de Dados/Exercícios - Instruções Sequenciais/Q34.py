# Exercício 34 — Massa gravitacional
def main():
    d = float(input("Distância (m): "))
    m2 = float(input("Massa do outro objeto (kg): "))
    F = float(input("Força gravitacional (N): "))
    G = 6.67408e-11
    m1 = F * d**2 / (G * m2)
    print(f"Massa calculada: {m1:.2e} kg")

if __name__ == "__main__":
    main()