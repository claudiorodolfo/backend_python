import random
escolha = input("Escolha (pedra, papel, tesoura): ").lower()
opcoes = ["pedra","papel","tesoura"]
comp = random.choice(opcoes)
print("Computador escolheu:", comp)
if escolha == comp:
    print("Empate")
elif (escolha == "pedra" and comp == "tesoura") or \
        (escolha == "papel" and comp == "pedra") or \
        (escolha == "tesoura" and comp == "papel"):
    print("Você venceu")
else:
    print("Computador venceu")