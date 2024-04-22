def calculate_triangle_area(a, b, c):
    # Вычисление полупериметра
    s = (a + b + c) / 2
    # Вычисление площади по формуле Герона
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area