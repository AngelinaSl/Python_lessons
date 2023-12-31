# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.


from random import randint
from  sys import argv

__all__ = ['game']


def game(start: int=0, end: int=1000, tries: int=5) -> bool:
    num = randint(start, end)
    for _ in range(tries):
        enter = int(input('Введите число: '))
        if num > enter:
            print('больше')
        elif num < enter:
            print('меньше')
        else:
            break
    return enter == num


if __name__ == '__main__':
    arguments = map(int, argv[1:])
    print(game(*arguments))

# Вызов через терминал:
# python Seminars/Seminar_6/Module_2-3.py 3 7 2