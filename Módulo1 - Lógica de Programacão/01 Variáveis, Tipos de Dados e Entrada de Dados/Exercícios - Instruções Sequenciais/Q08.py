# Exercício 8 — Seno e cosseno de um ângulo (graus)
import math

def main():
    graus = float(input("Informe o ângulo em graus: "))
    rad = math.radians(graus)
    seno = math.sin(rad)
    cosseno = math.cos(rad)
    print(f"Seno({graus}°): {seno}\nCosseno({graus}°): {cosseno}")

if __name__ == "__main__":
    main()