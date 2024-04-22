# Функция для складывания 2 и введенного пользователем числа
def add_two_and_input_number():
    try:
        user_input = input("Введите число: ")
        number = float(user_input)  # Преобразуем введенное значение в число

        result = 2 + number
        print(f"Результат сложения 2 и {number} = {result}")

    except ValueError:  # Обрабатываем исключение, если введено нечисловое значение
        print("Неподходящий тип данных. Ожидалось число.")

# Тест с корректным вводом числа
add_two_and_input_number()

# Тест с некорректным вводом (например, строкой)
add_two_and_input_number()