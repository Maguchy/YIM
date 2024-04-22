# 4) Создание строки длиной не менее 16 символов из переменной длиной не более 5 символов
short_string = "Hello"
long_string = short_string.ljust(16, '!')
print(long_string)