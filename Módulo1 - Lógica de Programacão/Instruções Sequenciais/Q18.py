# Exercício 18 — Equação do segundo grau (raizes)
import math

def main():
    a = float(input("Coeficiente a: "))
    b = float(input("Coeficiente b: "))
    c = float(input("Coeficiente c: "))
    delta = b**2 - 4*a*c
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Raízes: x1 = {x1.real:.2f}, x2 = {x2.real:.2f}")

if __name__ == "__main__":
    main()