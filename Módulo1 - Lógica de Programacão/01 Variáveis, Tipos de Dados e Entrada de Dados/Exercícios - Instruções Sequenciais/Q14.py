# Exercício 14 — Parte fracionária
import math

def main():
    valor = float(input("Informe um número decimal: "))
    frac = valor - math.trunc(valor)
    print(f"Parte fracionária: {frac:.2f}")

if __name__ == "__main__":
    main()