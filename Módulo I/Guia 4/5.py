# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de
# años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

capital = int(input("Ingresá la cantidad de dinero a invertir.\n"))
interest_rate = float(input("Ingresá la tasa de interés anual.\n"))
years = int(input("Ingresá la cantidad de años que dura la inversión.\n"))
interest = capital * (interest_rate / 100)

index = 1
while index <= years:
    print(f"El año {index} el capital obtenido será de ${capital + (interest * index)}.")
    index += 1
print("El programa terminó.")
