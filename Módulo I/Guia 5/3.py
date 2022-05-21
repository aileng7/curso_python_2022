materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for materia in materias:
    score = input(f"¿Cuál es tu nota en {materia}?\n")
    scores.append(score)
for i in range(len(materias)):
    print(f"Tu nota en {materias[i]} es {scores[i]}.")
