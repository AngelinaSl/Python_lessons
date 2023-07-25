# Задание №1
# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

my_list = [1, 2, 3, 4, 5, 1, 2, 2, 3, 4]
"""
Короткое решение
"""
# my_set = list(set(my_list))
# print(f'{my_list},\n{my_set}')

"""
Длинное решение
"""
# my_list_two = []
# for i in range(len(my_list)):
#     eggs = my_list.count(my_list[i])
#     if eggs == 1:
#         my_list_two.append(my_list[i])
#     elif eggs > 1:
#         for j in range(len(my_list_two)):
#             if my_list[i] not in my_list_two:
#                 my_list_two.append(my_list[i])
# print(f'{my_list},\n{my_list_two}')


# for num in my_list:
#     while my_list.count(num) > 1:
#         my_list.remove(num)
#     print(my_list)

my_list2 = []
for num in my_list:
    if num not in my_list2:
        my_list2.append(num)
print(my_list2)
