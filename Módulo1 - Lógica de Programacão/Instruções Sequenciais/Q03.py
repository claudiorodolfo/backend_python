# Exercício 3 — Média ponderada com 3 valores (pesos: 4,7,3)
def main():
    a = float(input("Informe o primeiro valor (peso 4): "))
    b = float(input("Informe o segundo valor (peso 7): "))
    c = float(input("Informe o terceiro valor (peso 3): "))
    media = (a * 4 + b * 7 + c * 3) / (4 + 7 + 3)
    print(f"Média ponderada: {media}")

if __name__ == "__main__":
    main()