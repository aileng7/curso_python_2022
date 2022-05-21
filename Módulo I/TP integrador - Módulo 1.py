productos = {
    'esponjas': {'stock': 150, 'precio': 70},
    'bolsas de residuos': {'stock': 70, 'precio': 120},
    'fósforos': {'stock': 50, 'precio': 85},
    'detergente': {'stock': 90, 'precio': 25},
    'servilletas': {'stock': 150, 'precio': 33}
}

cantidad = 0
producto = ""
while producto != "fin":
    producto = input("Ingresá el producto que querés vender: ")
    if producto != "fin":
        try:
            cantidad = int(input("Ingresá la cantidad: "))
            try:
                productos[producto]["stock"] = productos[producto]["stock"] + cantidad
            except KeyError:
                print("Ingresá un producto válido o la palabra FIN.")
        except ValueError:
            print("Ingresá una cantidad válida.")
    if producto == "fin":
        precio_venta = ((cantidad * productos[producto]["precio"]) * 1.21)
        print(f"El precio de la venta es: {precio_venta}.")
