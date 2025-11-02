# Exercício 11 — Potenciação usando cmath
import math

def main():
    base = float(input("Informe a base: "))
    expoente = float(input("Informe o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"Resultado de {base}^{expoente}: {resultado.real}")

if __name__ == "__main__":
    main()