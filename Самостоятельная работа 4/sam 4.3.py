import time  # Импортируем модуль time для работы с временем
from datetime import datetime, timedelta  # Импортируем классы datetime и timedelta из модуля datetime для работы с датами и временем

# Устанавливаем время окончания выполнения программы через 5 секунд
end_time = datetime.now() + timedelta(seconds=5)

# Цикл, который будет выполняться в течение 5 секунд
while datetime.now() < end_time:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущее время и форматируем его
    print("Текущее время:", current_time)  # Выводим текущее время
    time.sleep(1)  # Приостанавливаем программу на 1 секунду