# Exercício 5: Segundo maior elemento (considerando repetidos)
lista = [5, 3, 9, 9, 2, 8, 9]
# inicializar dois valores usando None ou valores mínimos
primeiro = None
segundo = None
for x in lista:
    # se ainda não definimos “primeiro” ou x é maior que ele
    if primeiro is None or x > primeiro:
        # se primeiro já tinha valor diferente de x, atualizar segundo
        if primeiro is not None and x != primeiro:
            segundo = primeiro
        primeiro = x
    elif x != primeiro and (segundo is None or x > segundo):
        segundo = x
if segundo is None:
    print("Não há segundo maior distinto.")
else:
    print("Segundo maior:", segundo)