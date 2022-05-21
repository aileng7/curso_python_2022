# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

number = int(input("Ingrese un numero entero.\n"))
rest_division = number % 2
if rest_division == 0:
    print("El número es par.")
else:
    print("El número es impar.")
