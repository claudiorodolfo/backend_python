# Exercício 32 — Tempo até encontro de veículos
def main():
    v1 = float(input("Velocidade do veículo 1 (m/s): "))
    v2 = float(input("Velocidade do veículo 2 (m/s): "))
    d = float(input("Distância entre eles (m): "))
    tempo = d / (v1 + v2)
    print(f"Tempo até encontro: {tempo:.2f} s")

if __name__ == "__main__":
    main()