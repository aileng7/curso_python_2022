def facturar(neto: float, tasa: float = 21):
    return neto + neto * tasa / 100


print(facturar(1000, 10.5))
print(facturar(1000))
