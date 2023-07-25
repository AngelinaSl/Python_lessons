# Задание №1
# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def sort_by_unicode(text: str):
    lst_sorted = sorted(text.split())
    max_word = len(max(lst_sorted, key=len))
    for i, element in enumerate(lst_sorted, start=1):
        print(f'{i} {element:>{max_word}}')









text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
sort_by_unicode(text)