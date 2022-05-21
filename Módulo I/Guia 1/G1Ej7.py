kg = input("¿Cuál es tu peso?")
mts = input("¿Cuál es tu altura en metros?")
imc = float(kg) / float(mts)
print("Tu índice de masa corporal es " + str(round(imc, 2)))
