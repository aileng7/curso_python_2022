materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
aprobado = []
for materia in materias:
    score = float(input(f"¿Cuál es tu nota en {materia}?\n"))
    if score >= 5:
        aprobado.append(materia)
for materia in aprobado:
    materias.remove (materia)
print(f"Tenés que recursar {materias}")
