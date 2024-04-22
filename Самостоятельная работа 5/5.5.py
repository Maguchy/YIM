from collections import Counter

def generate_sets(numbers):
    unique_numbers = set(numbers)
    result_set = set()

    for num in unique_numbers:
        count = numbers.count(num)
        if count > 1:
            for i in range(1, count + 1):
                result_set.add(str(num) * i)
        else:
            result_set.add(num)

    return result_set

# Множества для теста
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

# Результаты вывода
result_set_1 = generate_sets(list_1)
result_set_2 = generate_sets(list_2)
result_set_3 = generate_sets(list_3)

# Вывод результатов
print(result_set_1)
print(result_set_2)
print(result_set_3)