def determine_employee_order(employee_tuple, random_id):
    if random_id not in employee_tuple:
        return ()

    start_index = employee_tuple.index(random_id)
    end_indices = [i for i, x in enumerate(employee_tuple) if x == random_id]

    if len(end_indices) == 1:  # Если элемент встречается только один раз
        return employee_tuple[start_index:]
    else:
        end_index = end_indices[-1]
        return employee_tuple[start_index:end_index + 1]

# Тестовые данные
tests = [
    ((1, 2, 3), 8),
    ((1, 8, 3, 4, 8, 8, 9, 2), 8),
    ((1, 2, 8, 5, 1, 2, 9), 8)
]

# Проверка функции для каждого теста
for test in tests:
    result = determine_employee_order(*test)
    print(result)