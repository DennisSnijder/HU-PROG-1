studentGrades = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def get_average_for_student_grades(student_grades: list) -> float:
    return sum(student_grades) / len(student_grades)


def get_average_for_multiple_students(students_grades: list) -> float:
    average_list: list = []

    for student_grades in students_grades:
        average_list.append(
            get_average_for_student_grades(student_grades)
        )

    return get_average_for_student_grades(average_list)

print(get_average_for_student_grades(studentGrades[0]))
print(get_average_for_multiple_students(studentGrades))
