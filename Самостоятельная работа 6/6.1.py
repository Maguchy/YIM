numbers_input = input("Введите последовательность чисел, разделенных пробелом: ")
numbers_list = numbers_input.split()
number_tuple = tuple(numbers_list)

print("Список из введенных чисел:", numbers_list)
print("Кортеж из введенных чисел:", number_tuple)