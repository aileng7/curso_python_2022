cant_dinero = input("Indique la cantidad de dinero depositada en la caja de ahorros")
int_1 = float(cant_dinero) * 0.04
int_2 = (float(cant_dinero) + float(int_1)) * 0.04
int_3 = (float(cant_dinero) + float(int_1) + float(int_2)) * 0.04
ahorro_1 = round((float(cant_dinero) + int_1), 2)
ahorro_2 = round((float(cant_dinero) + int_2 + int_1), 2)
ahorro_3 = round((float(cant_dinero) + int_3 + int_2 + int_1), 2)
print(f"La cantidad de ahorros el primer año es {ahorro_1}, el segundo año {ahorro_2}, y el tercer año {ahorro_3}.")
