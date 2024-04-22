def palindromes_check(words_list):
    result_list = []

    for word in words_list:
        if word == word[::-1]:
            result_list.append(word)
        else:
            result_list.append(word[::-1])

    return result_list


# Тестовые данные
tests = [
    ["radar", "hello", "level", "python", "kayak"],
    ["madam", "world", "civic", "apple", "deified"],
    ['abba', 'apple', 'tenet', 'banana', 'racecar']
]

# Проверка функции для каждого теста
for test in tests:
    result = palindromes_check(test)
    print(result)