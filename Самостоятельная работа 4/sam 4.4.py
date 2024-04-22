def calculate_average(*args):
    if len(args) == 0:
        return 0  # Возвращаем 0 в случае отсутствия аргументов

    total = sum(args)  # Вычисляем сумму всех аргументов
    average = total / len(args)  # Вычисляем среднее арифметическое

    return average


if __name__ == "__main__":
    values = [5, 10, 15, 20]  # Пример значений для подсчета среднего

    result = calculate_average(*values)  # Распаковываем список значений и передаем их в функцию
    print(f"Среднее арифметическое: {result}")