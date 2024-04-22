def analyze_text(file_name):
    latin_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_letters = 0
    total_words = 0
    total_lines = 0

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            total_lines += 1
            total_letters += sum(1 for char in line if char in latin_letters)
            total_words += len(line.split())

    return total_letters, total_words, total_lines

def main():
    file_name = "input.txt"
    total_letters, total_words, total_lines = analyze_text(file_name)

    print(f"Количество букв латинского алфавита: {total_letters}")
    print(f"Число слов: {total_words}")
    print(f"Число строк: {total_lines}")

if __name__ == "__main__":
    main()