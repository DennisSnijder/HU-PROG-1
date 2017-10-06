student_grades: dict = {
    'Peter': 7.0,
    'Dennis': 8.2,
    'Henk': 9.4,
    'Richard': 10.0,
    'Ruben': 7.4,
    'Karel': 9.5,
    'Rembrandt': 7.5,
    'Antonie': 6.9,
    'Meino': 4.2,
    'Will': 8.3
}


for name, grade in student_grades.items():
    if grade > 9.0:
        print(name + ': ' + str(grade))
