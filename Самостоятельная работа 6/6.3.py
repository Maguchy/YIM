def count_most_frequent_digits(numbers_str):
    digits_count = {}

    for digit in numbers_str:
        if digit.isdigit():
            digit = int(digit)
            digits_count[digit] = digits_count.get(digit, 0) + 1

    sorted_digits_count = dict(sorted(digits_count.items(), key=lambda x: x[1], reverse=True))
    most_frequent_digits = dict(list(sorted_digits_count.items())[:3])

    return most_frequent_digits


# Тестовая строка
numbers_str = "12345543129874659"

most_frequent_digits = count_most_frequent_digits(numbers_str)
print(most_frequent_digits)