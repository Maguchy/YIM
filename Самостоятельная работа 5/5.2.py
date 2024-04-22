# Список результатов бега
running_results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
                   30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

# 1. Три лучшие результаты
top_three_results = sorted(running_results)[:3]

# 2. Три худшие результаты
worst_three_results = sorted(running_results)[-3:]

# 3. Все результаты начиная с 10
results_from_10 = [result for result in running_results if result >= 10]

# Вывод результатов
print(f"Три лучшие результаты: {top_three_results}")
print(f"Три худшие результаты: {worst_three_results}")
print(f"Все результаты начиная с 10: {results_from_10}")