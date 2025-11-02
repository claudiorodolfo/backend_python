# Exercício 12 — Raiz quadrada usando cmath
import math

def main():
    valor = float(input("Informe um valor: "))
    raiz = math.sqrt(valor)
    print(f"Raiz quadrada: {raiz.real:.2f}")

if __name__ == "__main__":
    main()