# Exercício 31 — Calorias para autoignição (álcool)
def main():
    massa = float(input("Quantidade de álcool (g): "))
    calor_especifico = 2389  # exemplo
    calor = massa * calor_especifico
    print(f"Calorias necessárias: {calor:.2f} cal")

if __name__ == "__main__":
    main()