# Exercício 9 — Divisão arredondada usando cmath
import math

def main():
    a = int(input("Informe o primeiro número inteiro: "))
    b = int(input("Informe o segundo número inteiro: "))
    resultado = math.round(a / b)
    print(f"Resultado da divisão arredondada ({a} / {b}): {resultado}")

if __name__ == "__main__":
    main()