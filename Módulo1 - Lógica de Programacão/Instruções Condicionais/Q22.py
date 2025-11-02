import random

num = random.randint(1,10)
palpite = int(input("Adivinhe o número (1-10): "))
if palpite == num:
    print("Acertou!")
else:
    print("Errou, o número era", num)