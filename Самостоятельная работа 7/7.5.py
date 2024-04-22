def count_characters(file_name):
    characters_frequency = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char in characters_frequency:
                    characters_frequency[char] += 1
                else:
                    characters_frequency[char] = 1

    return characters_frequency

def main():
    file_name = "input.txt"  # Имя файла для анализа
    characters_frequency = count_characters(file_name)

    print("Частота встречаемости символов в файле:")
    for char, freq in characters_frequency.items():
        print(f"{char}: {freq}")

if __name__ == "__main__":
    main()