# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


my_list = [1, 2, 3, 1, 2, 4, 5]
COUNT = 1
my_list_two = []
for i in my_list:
    eggs = my_list.count(my_list[i])
    if eggs > COUNT and my_list[i] not in my_list_two:
        my_list_two.append(my_list[i])

print(f'{my_list},\n{my_list_two}')

