person = {}
follow = True
while follow:
    key = input('¿Qué dato quieres introducir? ')
    value = input(key + ': ')
    person[key] = value
    print(person)
    follow = input('¿Quieres añadir más información (Si/No)? ') == "Si"