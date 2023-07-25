# Задание №2
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# Целое положительное число
# Вещественное положительное или отрицательное число
# Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# Строку в верхнем регистре в остальных случаях


atributes = ['qwqw', '1121', ' 12.01', 'anFanf', 'fasgdf.2736516', '-12']

for attr in atributes:
    if attr.lstrip('-').isdigit():
        res = abs(int(attr))
        print(res, type(res))
    elif attr.count('.') == 1:
        if attr.replace('.', '', 1).isdigit():
            res = float(attr)
            print(res, type(res))
    elif attr != attr.lower():
        print(attr.lower())
    else:
        print(attr.upper())
