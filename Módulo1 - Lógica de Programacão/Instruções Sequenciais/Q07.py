# Exercício 7 — Arredondando valor de ponto flutuante a 2 casas decimais
def main():
    valor = float(input("Informe um valor decimal: "))
    arredondado = round(valor, 2)
    print(f"Valor arredondado (2 casas decimais): {arredondado:.2f}")

if __name__ == "__main__":
    main()