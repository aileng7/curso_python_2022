# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al
# usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con
# la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

user_key = "1598ghjk"
key_entered = input("Ingrese su contraseña.\n")
correct_key = str(user_key).upper() == str(key_entered).upper()
if correct_key:
    print("La clave es correcta.")
else:
    print("La clave es incorrecta.")
