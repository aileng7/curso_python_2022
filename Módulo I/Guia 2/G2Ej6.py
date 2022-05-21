# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después
# muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input("Introducí una frase\n")
vocal = input("Introducí una vocal\n")
print(frase.replace(f"{vocal}", f"{vocal.upper()}"))
