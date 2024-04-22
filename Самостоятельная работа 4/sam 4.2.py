import random

def roll_dice():
    # Бросаем игральный кубик
    dice_value = random.randint(1, 6)
    print(f"Вы бросили кубик: {dice_value}")

    # Проверяем результат броска
    if dice_value in [5, 6]:
        print("Вы победили!")
    elif dice_value in [3, 4]:
        print("Бросаем еще раз...")
        roll_dice()  # Рекурсивно вызываем эту же функцию
    else:
        print("Вы проиграли.")

if __name__ == "__main__":
    roll_dice()  # Точка входа: вызываем функцию roll_dice()