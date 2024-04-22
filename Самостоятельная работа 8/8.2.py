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