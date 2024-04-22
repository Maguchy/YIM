# Создаем класс для нашего собственного исключения
class ValueTooLargeError(Exception):
    def __init__(self, value, max_value):
        self.value = value
        self.max_value = max_value
        super().__init__(f"Значение {value} превышает максимально допустимое значение {max_value}")

# Пример использования исключения в первом фрагменте кода
def calculate_area(length, width, max_area=100):
    area = length * width

    if area > max_area:
        raise ValueTooLargeError(area, max_area)

    return area

try:
    area1 = calculate_area(15, 8)
    print("Площадь равна:", area1)
except ValueTooLargeError as e:
    print("Ошибка:", e)

# Пример использования исключения во втором фрагменте кода
def check_value(value, max_value=10):
    if value > max_value:
        raise ValueTooLargeError(value, max_value)
    print("Значение в пределах допустимого:", value)

try:
    check_value(15, 10)
except ValueTooLargeError as e:
    print("Ошибка:", e)