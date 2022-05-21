# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima
# por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

user_name = input("¿Cuál es tu nombre?\n")
int_number = int(input("Elija un número entero\n"))
print((user_name + "\n") * int_number)
