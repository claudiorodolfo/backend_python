# Exercício 16 — Volume da caixa d'água (cilíndrica) em litros
import math

def main():
    raio = float(input("Raio da base (m): "))
    altura = float(input("Altura da caixa (m): "))
    volume_m3 = math.pi * raio**2 * altura
    volume_litros = volume_m3 * 1000
    print(f"Volume: {volume_litros:.2f} litros")

if __name__ == "__main__":
    main()