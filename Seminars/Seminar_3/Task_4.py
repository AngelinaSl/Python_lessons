# Задание №4
# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются кратное двум раз.

my_list = [1, 2, 1, 3, 2, 1, 1]

# for num in my_list:
#     counter = my_list.count(num)
#     if counter > 1 and counter % 2 == 0:
#         for _ in range(counter):
#             my_list.remove(num)
# print(my_list)


for num in my_list:
    while my_list.count(num) % 2 == 0 and num in my_list:
        my_list.remove(num)
        my_list.remove(num)
print(my_list)

