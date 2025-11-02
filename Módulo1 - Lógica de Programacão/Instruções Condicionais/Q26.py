x = int(input("Digite a coordenada x: "))
y = int(input("Digite a coordenada y: "))

if x > 0 and y > 0: print("1º quadrante")
elif x < 0 and y > 0: print("2º quadrante")
elif x < 0 and y < 0: print("3º quadrante")
elif x > 0 and y < 0: print("4º quadrante")
else: print("Sobre os eixos")