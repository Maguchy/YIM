from collections import Counter
import re

# Чтение содержимого текстового файла
with open('7.1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Разделение текста на слова с помощью регулярного выражения
words = re.findall(r'\w+', text.lower())

# Подсчет количества слов
word_count = len(words)

# Определение самого часто встречающегося слова
word_freq = Counter(words)
most_common_word, most_common_count = word_freq.most_common(1)[0]

# Вывод информации
print(f"Количество слов в файле: {word_count}")
print(f"Самое часто встречающееся слово: {most_common_word} (встречается {most_common_count} раз)")