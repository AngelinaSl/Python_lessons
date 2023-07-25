# Задание №5
# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# Нумерация начинается с единицы.

# my_list = list(range(1, 10))
# res = []
#
# for i, v in enumerate(my_list):
#     if v % 2 != 0:
#         res.append(i+1)
# print(my_list)
# print(res)




my_list = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 6]
odd_indices = [index + 1 for index, item in enumerate(my_list) if item % 2 != 0]
print(odd_indices)