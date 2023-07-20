# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num = 1_034_597_867
HEX_DIV = 16


def convert_to_hexadecimal_number(number, base):
    hexadecimal_numbers = {0: '0',
                           1: '1',
                           2: '2',
                           3: '3',
                           4: '4',
                           5: '5',
                           6: '6',
                           7: '7',
                           8: '8',
                           9: '9',
                           10: 'a',
                           11: 'b',
                           12: 'c',
                           13: 'd',
                           14: 'e',
                           15: 'f'
                           }

    result = ''
    while number > 0:
        result = hexadecimal_numbers[number % base] + result
        number //= base
    return result


print(f'Число в шестнадцатеричном представлении: {convert_to_hexadecimal_number(num, HEX_DIV)}, \n'
      f'проверка: {hex(num)}')


