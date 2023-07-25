# Задание №6
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

# def sum_numbers(numbers: list[int], index_min: int, index_max: int) -> int:
#     if index_min > index_max:
#         index_min, index_max = index_max, index_min
#     if index_min < 0:
#         index_min = 0
#     if index_max > len(numbers) - 1:
#         index_max = len(numbers) - 1
#     return sum(numbers[index_min: index_max + 1])
#
#
# print(sum_numbers([2, 3, 4, 6], 3, 1))


def sum_between_indices(numbers, idx1, idx2):
    start, end = sorted([idx1, idx2])
    start = max(0, start)
    end = min(len(numbers), end)
    return sum(numbers[start:end])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx1 = -6
idx2 = 6

print(sum_between_indices(numbers, idx1, idx2))