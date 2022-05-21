# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# Renta Tipo impositivo
# Menos de $10000 5%
# Entre $10000 y $20000 15%
# Entre $20000 y $35000 20%
# Entre $35000 y $60000 30%
# Más de $60000 45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo
# que le corresponde.

user_gain = int(input("¿Cuál es su renta anual?\n"))
if user_gain < 10000:
    print("Debe tributar el 5%.")
if 10000 <= user_gain < 20000:
    print("Debe tributar el 15%.")
if 20000 <= user_gain < 35000:
    print("Debe tributar el 20%.")
if 35000 <= user_gain < 60000:
    print("Debe tributar el 30%.")
if user_gain > 60000:
    print("Debe tributar el 45%.")
