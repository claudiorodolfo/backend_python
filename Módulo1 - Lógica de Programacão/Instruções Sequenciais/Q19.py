# Exercício 19 — Hipotenusa de triângulo retângulo
import math

def main():
    c1 = float(input("Cateto 1: "))
    c2 = float(input("Cateto 2: "))
    hip = math.hypot(c1, c2)
    print(f"Hipotenusa: {hip:.2f}")

if __name__ == "__main__":
    main()