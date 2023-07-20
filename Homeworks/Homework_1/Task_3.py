from random import randint

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


INTERVAL_MIN = 0
INTERVAL_MAX = 1000


def check_random(num):
    count = 9
    x = int(input('Угадайте число из диапазона от 0 до 1000: '))
    while count > 0:
        if x > num:
            print('Загаданное число меньше')
            count -= 1
            x = int(input('Введите число: '))
        elif x < num:
            print('Загаданное число больше')
            count -= 1
            x = int(input('Введите число: '))
        else:
            print('Ура! Вы угадали!')
            break
    if count == 0:
        print('Закончились попытки. Загаданное число:', num)


number = randint(INTERVAL_MIN, INTERVAL_MAX)
check_random(number)
