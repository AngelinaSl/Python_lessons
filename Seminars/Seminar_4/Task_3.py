# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def str_to_dict(string: str) -> dict[str, int]:
    result = {}
    start, end = sorted(map(int, string.split()))
    for i in range(start, end + 1):
        result[chr(i)] = i
    return result


print(str_to_dict("2 9"))


