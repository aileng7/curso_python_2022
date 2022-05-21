# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
# de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al
# usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede
# entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10.

user_age = int(input("Ingrese su edad.\n"))
free_pass = user_age < 4
bonus_pass = 4 <= user_age <= 18
normal_pass = user_age > 18
if free_pass:
    print("Puede ingresar gratis.")
elif bonus_pass:
    print("El valor de la entrada es de $5.")
elif normal_pass:
    print("El valor de la entrada es de $10.")
