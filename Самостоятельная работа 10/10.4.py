# Создаем класс для нашего декоратора
class CheckPositiveDecorator:
    def __init__(self, func):
        self.func = func  # Сохраняем функцию, к которой применяется декоратор

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)  # Вызываем функцию, к которой применяется декоратор

        if result <= 0:
            print("Ошибка: Результат не является положительным числом")
        else:
            return result

# Пример функции, к которой применим наш декоратор
@CheckPositiveDecorator
def multiply(a, b):
    return a * b

@CheckPositiveDecorator
def power(base, exp):
    return base ** exp

# Тестируем наши функции, где у нас есть положительные и отрицательные результаты
print("Результат умножения:", multiply(5, 6))  # Положительный результат
print("Результат возведения в степень:", power(-2, 3))  # Отрицательный результат