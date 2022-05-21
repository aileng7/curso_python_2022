number = int(input("Ingresá un numero entero.\n"))

for index in range(0, number):
    print((number - index), end=" ")
    index += 2

print("El programa terminó.")
