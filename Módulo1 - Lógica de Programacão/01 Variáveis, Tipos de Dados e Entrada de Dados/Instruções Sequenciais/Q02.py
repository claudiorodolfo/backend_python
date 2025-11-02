# Exercício 2 — Média ponderada (peso 40% e 60%)
def main():
    a = float(input("Informe o primeiro valor (peso 40%): "))
    b = float(input("Informe o segundo valor (peso 60%): "))
    media = a * 0.4 + b * 0.6
    print(f"Média ponderada: {media}")

if __name__ == "__main__":
    main()