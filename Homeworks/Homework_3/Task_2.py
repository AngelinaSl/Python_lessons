import string

# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.


TOP_POSITIONS = 10
amount = 1
my_dict = dict()
count_for_print = 1
text_string = "Python is a widely-used general-purpose, " \
              "high-level programming language. " \
              "It was initially designed by Guido van Rossum in 1991 " \
              "and developed by Python Software Foundation. " \
              "It was mainly developed for emphasis on code readability, " \
              "and its syntax allows programmers to express concepts in fewer lines of code."

# Разделяем строку по пробелу, удалив все знаки препинания
text_string = (text_string.translate(str.maketrans('', '', string.punctuation))).split(' ')
# считаем количество строк, формируя словарь, где ключ - слово, значение - количество встречаемости слова в тексте
for word in text_string:
    if word not in my_dict.keys():
        my_dict[word] = amount
    else:
        my_dict[word] += 1
# сортируем словарь в порядке убывания
my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

if len(my_dict) <= TOP_POSITIONS:
    TOP_POSITIONS = len(my_dict)
print('ТОП-10 часто встречающихся слов:')
for i in range(TOP_POSITIONS):
    print(f'\t{count_for_print}. {str(list(my_dict)[i]).upper()}')
    count_for_print += 1

