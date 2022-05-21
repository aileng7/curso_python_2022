user_message = "Ingresá el producto vendido [ESPONJAS/BOLSAS DE RESIDUOS/FÓSFOROS/DETERGENTE/SERVILLETAS] " \
               "o la palabra [FIN] para finalizar la venta: "

products = {
    'esponjas': {'stock': 150, 'precio': 70},
    'bolsas de residuos': {'stock': 70, 'precio': 120},
    'fósforos': {'stock': 50, 'precio': 85},
    'detergente': {'stock': 90, 'precio': 25},
    'servilletas': {'stock': 150, 'precio': 33}
}
name_product = input(user_message)
sold_quantity = 0


def sale_calculation():
    if sold_quantity > 10:
        return ((sold_quantity * products[name_product]['precio'])*0.97)*1.21
    else:
        return (sold_quantity * products[name_product]['precio'])*1.21


while name_product != "fin":
    sold_quantity = int(input(f"Ingresá la cantidad vendida de {name_product}: "))
    products[name_product]['stock'] -= sold_quantity
    sale_value = sale_calculation()
    name_product = input(user_message)

