name = input("Ingresá tu nombre: ")
age = input("Ingresá tu edad: ")
address = input("Ingresá tu dirección: ")
phone_number = input("Ingresá tu número de teléfono: ")
user_information = {"nombre": name, "edad": age, "dirección": address, "teléfono": phone_number}

print(user_information["nombre"], "tiene", user_information["edad"], "años, vive en", user_information["dirección"],
      "y su numero de teléfono es", user_information["teléfono"])
