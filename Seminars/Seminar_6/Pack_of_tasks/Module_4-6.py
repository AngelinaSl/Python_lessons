# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.

# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


from random import randint
from typing import List, Dict

__all__ = ['VAR_DICT', 'game_guess_two', 'all_var']

VAR_DICT: Dict = {1: [1, 2, 3, 4],
                  3: [2, 2, 3, 4]
                  }

_res: Dict = {}


def game_guess_two(riddle_number: int,
                   variants: List[int],
                   number_of_attempts: int) -> int:
    for attempt_number in range(1, number_of_attempts + 1):
        rnd_number: int = randint(0, len(variants) - 1)
        if riddle_number == variants[rnd_number]:
            return attempt_number
    return 0


def all_var():
    for key, value in VAR_DICT.items():
        _res[str(value)] = game_guess_two(riddle_number=key,
                                          variants=value,
                                          number_of_attempts=10)
        print(_res[str(value)])


if __name__ == '__main__':
    all_var()
    print(_res)
