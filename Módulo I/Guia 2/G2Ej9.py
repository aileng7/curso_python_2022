# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y
# muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione
# cuando el día o el mes se introduzcan con un solo carácter.
birthday = input("Indique su fecha de nacimiento en el siguiente formato dd/mm/aaaa\n")
print(f"Su fecha de nacimiento es el dia {birthday[0:2]}, del mes {birthday[3:5]}, del año {birthday[6:]}.")

# sin resolver