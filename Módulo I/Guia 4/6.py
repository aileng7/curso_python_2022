# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo, de altura el número introducido.


number = int(input("Ingresá un numero entero.\n"))
index = 1
while index <= number:
    print(index * "*")
    index += 1
print("El programa terminó.")
