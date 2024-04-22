from triangle_area_calculator import calculate_triangle_area


def get_triangle_sides_from_user():
    # Получение длин сторон треугольника от пользователя
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c


if __name__ == "__main__":
    # Взаимодействие с пользователем для получения информации о треугольнике
    print("Программа для вычисления площади треугольника по формуле Герона.")
    a, b, c = get_triangle_sides_from_user()

    # Вычисление площади треугольника
    area = calculate_triangle_area(a, b, c)

    # Вывод результата
    print(f"Площадь треугольника: {area}")