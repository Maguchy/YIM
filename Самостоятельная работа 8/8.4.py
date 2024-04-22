# Создаем класс Robot
class Robot:
    # Конструктор класса
    def __init__(self, name):
        self.name = name

    # Метод для представления робота
    def introduce(self):
        return f"Привет, меня зовут {self.name}!"

# Создаем объект робота
robot1 = Robot("Robbie")

# Вывод приветствия от робота
print(robot1.introduce())
# Расширяем класс Robot с новым атрибутом и методом
class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        return f"Привет, я {self.name}, модель {self.model}!"

    def move(self, direction):
        return f"{self.name} движется {direction}"

# Создаем объект робота с моделью
robot2 = Robot("Bot", "R2")

# Вывод информации о роботе и его действии
print(robot2.introduce())
print(robot2.move("вперед"))
# Создаем подкласс Android, наследующий от класса Robot
class Android(Robot):
    def __init__(self, name, model, serial_number):
        super().__init__(name, model)
        self.serial_number = serial_number

    def info(self):
        return f"{self.name} ({self.model}) - SN: {self.serial_number}"

# Создаем объект Android
android1 = Android("Andy", "A1", "123456")

# Вывод информации об Android
print(android1.info())
# Расширяем класс Robot с инкапсуляцией
class Robot:
    def __init__(self, name, model):
        self._name = name  # Инкапсулированный атрибут
        self._model = model  # Инкапсулированный атрибут

    def introduce(self):
        return f"Привет, я {self._name}, модель {self._model}!"

# Создаем объект робота с инкапсулированными атрибутами
robot3 = Robot("SecureBot", "S1")

# Попытка получить доступ к инкапсулированному атрибуту (должна возникнуть ошибка)
try:
    print(robot3._name)  # Попытка доступа к инкапсулированному атрибуту
except AttributeError as e:
    print("AttributeError occurred:", e)

# Вывод информации о роботе
print(robot3.introduce())