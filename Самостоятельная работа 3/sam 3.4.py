def manipulation_string(sentence):
    # Длина предложения
    print(f"Длина предложения: {len(sentence)}")

    # Перевод в нижний регистр
    lower_sentence = sentence.lower()
    print(f"Предложение в нижнем регистре: {lower_sentence}")

    # Подсчет количества гласных
    vowels = 'aeiou'
    vowel_count = sum(1 for char in lower_sentence if char in vowels)
    print(f"Количество гласных в предложении: {vowel_count}")

    # Замена "ugly" на "beauty"
    replaced_sentence = sentence.replace("ugly", "beauty")
    print(f"Предложение с заменой 'ugly' на 'beauty': {replaced_sentence}")

    # Проверка начала и конца предложения
    starts_with_the = sentence.startswith("The")
    ends_with_end = sentence.endswith("end")
    if starts_with_the:
        print("Предложение начинается с 'The'")
    else:
        print("Предложение не начинается с 'The'")

    if ends_with_end:
        print("Предложение заканчивается на 'end'")
    else:
        print("Предложение не заканчивается на 'end'")


# Проверка на трех предложениях
sentences = [
    "The ugly duckling wanted to find a nice pond to spend his days in peace.",
    "Endless beauty is only found by those who seek it.",
    "There are messages in both attractive and ugly containers."
]

for sentence in sentences:
    print("\n--- Работа с предложением ---")
    manipulation_string(sentence)