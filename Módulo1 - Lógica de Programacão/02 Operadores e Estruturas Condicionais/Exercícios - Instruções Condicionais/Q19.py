# 19 - Corrida de atletas sem usar array

nome1 = input("Nome do atleta 1: ")
tempo1 = float(input("Tempo do atleta 1: "))

nome2 = input("Nome do atleta 2: ")
tempo2 = float(input("Tempo do atleta 2: "))

nome3 = input("Nome do atleta 3: ")
tempo3 = float(input("Tempo do atleta 3: "))

# Verifica quem foi o campeão, vice e terceiro
if tempo1 < tempo2 and tempo1 < tempo3:
    campeao = nome1
    if tempo2 < tempo3:
        vice = nome2
        terceiro = nome3
    else:
        vice = nome3
        terceiro = nome2
elif tempo2 < tempo1 and tempo2 < tempo3:
    campeao = nome2
    if tempo1 < tempo3:
        vice = nome1
        terceiro = nome3
    else:
        vice = nome3
        terceiro = nome1
else:
    campeao = nome3
    if tempo1 < tempo2:
        vice = nome1
        terceiro = nome2
    else:
        vice = nome2
        terceiro = nome1

print("Campeão:", campeao)
print("Vice-campeão:", vice)
print("3º lugar:", terceiro)