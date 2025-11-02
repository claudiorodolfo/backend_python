# Exercício 5 — Troca de valores
def main():
    a = input("Informe o valor da variável A: ")
    b = input("Informe o valor da variável B: ")
    print(f"Antes — A: {a}, B: {b}")
    a, b = b, a
    print(f"Depois — A: {a}, B: {b}")

if __name__ == "__main__":
    main()