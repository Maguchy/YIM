def load_banned_words(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        banned_words = file.read().split()
    return set(banned_words)


def censor_text(sentence, banned_words):
    words = sentence.split()
    censored_words = set()

    for banned_word in banned_words:
        for i, word in enumerate(words):
            if word.lower() == banned_word:
                words[i] = "*" * len(word)
                censored_words.add(word)

    censored_sentence = ' '.join(words)
    return censored_sentence, censored_words


def main():
    banned_words = load_banned_words('input1.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"

    censored_sentence, censored_words = censor_text(sentence, banned_words)

    print(f"Предложение для проверки:")
    print(sentence)

    print("\nЗамененное предложение:")
    print(censored_sentence)

    print("\nЗамененные слова:")
    print(', '.join(censored_words))


if __name__ == "__main__":
    main()