# 9) Задача: Подсчет суммы цифр введенного пользователем числа

num = input("Введите целое число: ")
sum_digits = 0

try:
    num = int(num)
    for digit in str(num):
        sum_digits += int(digit)

    print(f"Сумма цифр в числе {num} равна: {sum_digits}")

except ValueError:
    print("Ошибка: Введите целое число!")
