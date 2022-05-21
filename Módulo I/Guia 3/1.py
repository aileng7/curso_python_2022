# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
user_age = int(input("¿Cuál es tu edad?\n"))
legal_age = user_age >= 18
if legal_age:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")
19