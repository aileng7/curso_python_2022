winners_numbers = []
for i in range(6):
    winners_numbers.append(int(input("Ingresá un número ganador: ")))
winners_numbers.sort()
print(f"Los números ganadores son: {winners_numbers}")
