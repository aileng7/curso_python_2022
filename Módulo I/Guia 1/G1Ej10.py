cant_payaso = input("Ingrese la cantidad de payasos vendidos")
cant_muneca = input("Ingrese la cantidad de muñecas vendidas")
peso_payaso = float(cant_payaso) * 0.112
peso_muneca = float(cant_muneca) * 0.075
peso_total = float(peso_muneca + peso_payaso)
print(f"El peso total del paquete a enviar es {peso_total}kg")
