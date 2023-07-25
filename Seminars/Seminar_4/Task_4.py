# Задание №4
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


def sort_number(numbers: list[int]) -> None:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]


lst = [77, 394, 29, 9, 12, 9]
print(lst)
sort_number(lst)
print(lst)