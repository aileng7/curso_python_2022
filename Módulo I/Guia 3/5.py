# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o
# superiores a $1000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos
# mensuales y muestre por pantalla si el usuario tiene que tributar o no.

user_age = int(input("¿Cuál es tu edad?\n"))
user_gain = int(input("¿Cuáles son tus ingresos mensuales?\n"))
pay_tax = user_age >= 16 and user_gain >= 1000
if pay_tax:
    print("Deberás tributar.")
else:
    print("No estás alcanzado por este impuesto.")
