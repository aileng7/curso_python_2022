coins = {'Euro': '€', 'Dollar': '$', 'Yen': '¥', "Peso Argentino": "$"}
coin = input("Ingresá una divisa: ")
print(coins.get(coin.title(), "La divisa no está."))
