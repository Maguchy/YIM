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