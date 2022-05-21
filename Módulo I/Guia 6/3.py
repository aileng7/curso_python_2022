fruits = {"plátano": 1.35, "manzana": 0.8, "pera": 0.85, "naranja": 0.7}
fruit = input("¿Qué fruta necesitas comprar?: ")
kg = float(input("¿Cuántos kilos necesitás?: "))
if fruit in fruits:
    print(kg, "kilos de", fruit, "valen $", fruits[fruit]*kg)
else:
    print("Lo siento, la fruta", fruit, "no está disponible.")
