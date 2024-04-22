# Тестовые списки с оценками
grades_lists = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]

# Обновление оценок: удаление двоек и замена троек на четверки
updated_grades_lists = []
for grades in grades_lists:
    updated_grades = [4 if grade == 3 else grade for grade in grades if grade != 2]
    updated_grades_lists.append(updated_grades)

# Вывод обновленных массивов
for index, updated_grades in enumerate(updated_grades_lists):
    print(f"Обновленный массив {index + 1}: {updated_grades}")