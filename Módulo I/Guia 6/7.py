basket = {}
follow = True
while follow:
    item = input('Ingresá un artículo: ')
    price = float(input('Ingresá el precio de ' + item + ': '))
    basket[item] = price
    follow = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
amount = 0
print('Lista de la compra')
for item, price in basket.items():
    print(item, '\t', price)
    amount += price
print('Coste total: ', amount)