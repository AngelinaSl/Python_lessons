# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

text_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
              "Nullam ut ex eget libero fermentum tempus. Maecenas nec tristique metus"

words_list = text_string.split()
words_list = sorted(words_list)
max_word_len = max(len(word) for word in words_list) + 1
for i, word in enumerate(words_list, start=1):
    print(f"{i} {word:>{max_word_len - len(str(i))}}")