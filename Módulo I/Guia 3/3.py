# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es
# cero el programa debe mostrar un error.

number_one = float(input("Ingrese un número.\n"))
number_two = float(input("Ingrese otro número.\n"))
error_result = number_two <= 0
if error_result:
    print("Error - no se puede resolver.")
else:
    result = round((number_one / number_two), 2)
    print(result)
