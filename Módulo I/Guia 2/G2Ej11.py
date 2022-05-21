# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y
# muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos
# enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2
# decimales.

product = input('Ingresá el nombre del producto: ')
price = float(input('Ingresá el precio unitario: '))
count = int(input('Ingresá el número de unidades: '))
total = count * price
print(f'{product}: {count:3d} unidades x ${price:9.2f} = ${total:11.2f}')
