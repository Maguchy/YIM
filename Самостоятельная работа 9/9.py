# Класс Tomato
class Tomato:
    # Словарь с возможными стадиями созревания помидора
    states = {'отсутствует': 0, 'цветение': 1, 'зеленый': 2, 'красный': 3}

    def __init__(self, index):
        self._index = index  # Задаем индекс помидора
        self._state = self.states['отсутствует']  # Изначально устанавливаем стадию созревания "отсутствует"

    def grow(self):
        if self._state < 3:  # Увеличиваем стадию созревания, если она меньше максимальной
            self._state += 1

    def is_ripe(self):
        return self._state == 3  # Проверка, что помидор созрел

# Класс TomatoBush
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num+1)]  # Создаем список объектов класса Tomato

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()  # Увеличиваем стадии созревания всех помидоров на кусте

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])  # Проверяем, все ли помидоры созрели

    def give_away_all(self):
        self.tomatoes = []  # Очищаем список помидоров после сбора урожая

# Класс Gardener
class Gardener:
    def __init__(self, name, plant):
        self.name = name  # Имя садовника
        self._plant = plant  # Растение, за которым ухаживает садовник

    def work(self):
        self._plant.grow_all()  # Садовник заботится о растении, увеличивая стадии созревания помидоров

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()  # Если все помидоры созрели, садовник собирает урожай
            return "Урожай собран"
        else:
            return "Пока не все помидоры созрели. Продолжайте ухаживать."  # Иначе продолжаем уходить за растением

    @staticmethod
    def knowledge_base():
        print("Садоводство: ухаживайте за растениями, следите за их состоянием и собирайте урожай.")  # Печать справочной информации

# Тесты
# 1) Справка по садоводству
Gardener.knowledge_base()

# 2) Создание объектов
tomato_bush = TomatoBush(5)  # Создание куста с 5 помидорами
gardener = Gardener("Alice", tomato_bush)  # Создание садовника с именем Alice

# 3) Уход за кустом помидоров
gardener.work()  # Садовник ухаживает за кустом
print("Стадии созревания помидоров на кусте после ухода:", [tomato._state for tomato in tomato_bush.tomatoes])

# 4) Попытка собрать урожай при несозревших помидорах
print(gardener.harvest())

# 5) Продолжение ухода и сбор урожая
gardener.work()  # Садовник продолжает уход за кустом
print("Стадии созревания помидоров на кусте после продолжения ухода:", [tomato._state for tomato in tomato_bush.tomatoes])
print(gardener.harvest())  # Сбор урожая