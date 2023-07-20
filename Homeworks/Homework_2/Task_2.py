import math
import fractions

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6


PURPOSE_NUMERATOR = 0
PURPOSE_DENOMINATOR = 1
LEN_NUM_SPLIT = 2


def get_number() -> list:
    while True:
        try:
            num = input('Введите дробь в формате "a/b": ')
            num_split = num.split('/')
            if len(num_split) == LEN_NUM_SPLIT or \
                    type(int(num_split[0])) == int or \
                    type(int(num_split[1])) == int:
                num_split[0] = int(num_split[0])
                num_split[1] = int(num_split[1])
                return num_split
        except ValueError:
            print('ValueError: Неверный ввод. Попробуйте еще раз.')
        except IndexError:
            print('IndexError: Неверный ввод. Попробуйте еще раз.')


def calculate_amount(first_fraction: list, second_fraction: list):
    numerator_one = first_fraction[0]
    numerator_two = second_fraction[0]
    denominator_one = first_fraction[1]
    denominator_two = second_fraction[1]
    """
    Нахождение НОК(lcm)
    """
    lcm_num = math.lcm(denominator_one, denominator_two)
    numerator_final = ((lcm_num // denominator_one) * numerator_one
                       + (lcm_num // denominator_two) * numerator_two)
    """
    Сокращение дроби
    """
    calc_fraction = get_gcd(numerator_final, lcm_num)
    print(
        f'\n{numerator_one}/{denominator_one} '
        f'+ {numerator_two}/{denominator_two} '
        f'= {calc_fraction[0]}/{calc_fraction[1]}')


def calculate_multiplication(first_fraction: list, second_fraction: list) -> str:
    numerator_one = first_fraction[0]
    numerator_two = second_fraction[0]
    denominator_one = first_fraction[1]
    denominator_two = second_fraction[1]

    numerator_final = numerator_one * numerator_two
    denominator_final = denominator_one * denominator_two

    calc_fraction = get_gcd(numerator_final, denominator_final)
    print(
        f'{numerator_one}/{denominator_one} '
        f'* {numerator_two}/{denominator_two} '
        f'= {calc_fraction[0]}/{calc_fraction[1]}')


"""
сокращение дробей через НОД
"""


def get_gcd(numerator: int, denominator: int) -> list:
    gcd = math.gcd(numerator, denominator)
    numerator = numerator // gcd
    denominator = denominator // gcd
    fraction = [numerator, denominator]
    return fraction


fraction_1 = get_number()
fraction_2 = get_number()
calculate_amount(fraction_1, fraction_2)
print(
    f'Проверка сложения: {fractions.Fraction(fraction_1[0], fraction_1[1]) + fractions.Fraction(fraction_2[0], fraction_2[1])}\n')
calculate_multiplication(fraction_1, fraction_2)
print(
    f'Проверка умножения: {fractions.Fraction(fraction_1[0], fraction_1[1]) * fractions.Fraction(fraction_2[0], fraction_2[1])}\n')
