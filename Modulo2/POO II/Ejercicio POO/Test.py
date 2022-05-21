from Clase import Persona
from Clase import Domicilio

Domicilio1 = Domicilio()
Domicilio1.insert_street("9 de Julio")
Domicilio1.insert_number("1235")
Domicilio1.insert_city("CABA")
Domicilio1.address()

Persona1 = Persona()
Persona1.insert_name("Fulano")
Persona1.insert_last_name("Gómez")
Persona1.insert_address(Domicilio1)
print(Persona1.full_name())
print(Persona1.address())

Persona2 = Persona()
Persona2.insert_name("Juan")
Persona2.insert_last_name("Pérez")
Persona2.insert_address(Domicilio1)
print(Persona2.full_name())
print(Persona2.address())
