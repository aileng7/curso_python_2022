dictionary = {}
words_list = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for index in words_list.split(','):
    key, value = index.split(':')
    dictionary[key] = value
words = input('Introduce una frase en español: ')
for index in words.split():
    if index in dictionary:
        print(dictionary[index], end=' ')
    else:
        print(index, end=' ')
