def fib(n):
    # Инициализация начальных значений для чисел Фибоначчи
    a, b = 1, 1

    # Генератор чисел Фибоначчи
    for _ in range(n):
        yield a
        a, b = b, a + b


# Генерируем числа Фибоначчи до 200
fibonacci_sequence = list(fib(200))

# Выводим последнее число Фибоначчи (индекс 199) в последовательности
print(f"Число Фибоначчи от 200: {fibonacci_sequence[199]}")

# Записываем числа Фибоначчи в файл "fib.txt"
with open('fib.txt', 'w') as file:
    for num in fibonacci_sequence:
        file.write(str(num) + '\n')

print("Числа Фибоначчи записаны в файл 'fib.txt'.")