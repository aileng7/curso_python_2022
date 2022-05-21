course = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_points = 0
for subject, points in course.items():
    print(subject, 'tiene', points, 'créditos')
    total_points += points
print('Número total de créditos del curso: ', total_points)