def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount


def save_expenses_to_file(expenses, filename):
    with open(filename, 'w') as file:
        for category, amount in expenses.items():
            file.write(f"{category}: {amount}\n")


def load_expenses_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            expenses = {}
            for line in lines:
                category, amount = line.strip().split(': ')
                expenses[category] = float(amount)
    except FileNotFoundError:
        expenses = {}

    return expenses


def display_expenses(expenses):
    if not expenses:
        print("Нет информации о расходах.")
    else:
        print("Информация о расходах:")
        for category, amount in expenses.items():
            print(f"{category}: {amount}")


def main():
    filename = "7.2.txt"
    expenses = load_expenses_from_file(filename)

    while True:
        print("\n=== Учет расходов ===")
        print("1. Добавить расход")
        print("2. Вывести информацию о расходах")
        print("3. Сохранить и выйти")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            category = input("Введите категорию расхода: ")
            amount = float(input("Введите сумму расхода: "))
            add_expense(expenses, category, amount)
            print("Расход успешно добавлен.")
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            save_expenses_to_file(expenses, filename)
            print(f"Расходы сохранены в файл {filename}.")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()