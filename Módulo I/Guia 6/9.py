tickets = {}
charged = 0
pending = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Ingresá el número de la factura: ')
        price = float(input('Ingresá el coste de la factura: '))
        tickets[key] = price
        pending += price
    if more == 'P':
        key = input('Ingresá el número de la factura a pagar: ')
        price = tickets.pop(key, 0)
        charged += price
        pending -= price
    print('Recaudado:', charged)
    print('Pendiente de cobro: ', pending)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')