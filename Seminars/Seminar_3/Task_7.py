# Задание №7
# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.



user_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
frequency_dict = {}


# # Проходим по каждому символу в строке
# for char in user_input:
#     if char in frequency_dict:
#         frequency_dict[char] += 1
#     else:
#         frequency_dict[char] = 1
# print(frequency_dict)

for char in user_input:
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
print(frequency_dict)