# Exercício 15 — Perímetro e área do círculo
import math

def main():
    raio = float(input("Informe o raio do círculo: "))
    perimetro = 2 * math.pi * raio
    area = math.pi * raio**2
    print(f"Perímetro: {perimetro:.2f}")
    print(f"Área: {area:.2f}")

if __name__ == "__main__":
    main()