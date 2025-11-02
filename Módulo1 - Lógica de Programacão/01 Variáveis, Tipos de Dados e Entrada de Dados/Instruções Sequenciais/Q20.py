# Exercício 20 — Área de trapézio
def main():
    b_maior = float(input("Base maior: "))
    b_menor = float(input("Base menor: "))
    altura = float(input("Altura: "))
    area = (b_maior + b_menor) * altura / 2
    print(f"Área do trapézio: {area:.2f}")

if __name__ == "__main__":
    main()