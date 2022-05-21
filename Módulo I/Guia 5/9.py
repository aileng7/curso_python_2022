word = input("Ingresá una palabra: ")
vocals = ["a", "e", "i", "o", "u"]
for vocal in vocals:
    times = 0
    for letter in word:
        if letter == vocal:
            times += 1
    print(f"La vocal {vocal} aparece {str(times)} veces.")
