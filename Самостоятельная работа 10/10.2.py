# Создаем функцию для чтения файла
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:  # Открываем файл для чтения
            content = file.read()  # Читаем содержимое файла

            if not content:  # Проверяем, если файл пустой
                raise Exception("File is empty")  # Вызываем исключение с сообщением "файл пустой"

            print("File content:")
            print(content)  # Выводим содержимое файла
    except FileNotFoundError:  # Обрабатываем исключение, если файл не найден
        print("File not found")
    except Exception as e:  # Обрабатываем другие исключения
        print("Error:", e)  # Выводим сообщение об ошибке


# Попробуем прочитать содержимое пустого файла
print("Reading empty file:")
read_file('empty_file.txt')

# Попробуем прочитать содержимое файла с данными
print("\nReading data file:")
read_file('data_file.txt')