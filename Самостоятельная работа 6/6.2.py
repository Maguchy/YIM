def remove_first_occurrence(tup, element):
    try:
        index = tup.index(element)
        new_tuple = tup[:index] + tup[index+1:]
    except ValueError:
        new_tuple = tup

    return new_tuple

# Тестовые данные
tests = [
    ((1, 2, 3), 1),
    ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
    ((2, 4, 6, 6, 4, 2), 9)
]

# Проверка функции для каждого теста
for test in tests:
    result = remove_first_occurrence(*test)
    print(result)