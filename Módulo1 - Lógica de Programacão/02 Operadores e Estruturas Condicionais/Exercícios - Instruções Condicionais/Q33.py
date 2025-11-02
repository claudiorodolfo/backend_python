n1 = int(input("Digite a 1ª nota: "))
n2 = int(input("Digite a 2ª nota: "))
media = (n1+n2)/2
if media >= 70:
    print("Aprovado")
elif media < 30:
    print("Reprovado")
else:
    final = int(input("Digite a nota da prova final: "))
    mediaf = (2*media + final)/3
    if mediaf >= 50: print("Aprovado por Final")
    else: print("Reprovado")