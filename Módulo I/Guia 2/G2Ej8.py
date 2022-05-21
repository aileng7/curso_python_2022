# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
# muestre por pantalla el número de euros y el número de céntimos del precio introducido.
price = input("¿Cual es el precio del producto en euros?\n")
print(f"El precio es de {price[0:2]} euros y {price[3:5]} centimos")
