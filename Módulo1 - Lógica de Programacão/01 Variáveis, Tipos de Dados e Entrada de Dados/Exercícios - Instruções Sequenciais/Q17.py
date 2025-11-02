# Exercício 17 — Volume da esfera
import math

def main():
    raio = float(input("Raio da esfera (m): "))
    volume = (4/3) * math.pi * raio**3
    print(f"Volume da esfera: {volume:.2f} m³")

if __name__ == "__main__":
    main()