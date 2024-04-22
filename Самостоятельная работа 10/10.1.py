import time  # Импортируем модуль time для измерения времени выполнения функции


# Создаем декоратор для измерения времени выполнения функции
def calculate_execution_time(func):
    def wrapper():
        # Запоминаем время начала выполнения функции
        start_time = time.time()

        # Выполняем переданную функцию
        func()

        # Вычисляем время выполнения функции
        end_time = time.time()
        execution_time = end_time - start_time

        # Выводим время выполнения функции
        print("Execution time:", execution_time, "seconds")

    return wrapper


# Определяем функцию для вычисления последовательности Фибоначчи
@calculate_execution_time  # Применяем декоратор к функции
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')


# Проверяем, запускается ли функция напрямую (если запускается как скрипт, а не импортируется как модуль)
if __name__ == '__main__':
    fibonacci()  # Вызываем функцию для вычисления последовательности Фибоначчи