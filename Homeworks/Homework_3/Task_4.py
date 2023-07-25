# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.


friends_dict = {
                'Вася': {'backpack', 'tent', 'water', 'first aid kit', 'food'},
                'Коля': {'backpack', 'tent', 'water', 'matches', 'food'},
                'Миша': {'backpack', 'tent', 'water', 'matches'}
                }


friends_name = []
for key in friends_dict.keys():
    friends_name.append(key)
print(friends_name)

overall_things = friends_dict[friends_name[0]]
for friend_index in range(1, len(friends_name)):
    overall_things = overall_things.intersection(friends_dict[friends_name[friend_index]])
print(f'Вещи, которые взяли все три друга: {overall_things}')


unique_things = friends_dict[friends_name[0]]
for friend_index in range(1, len(friends_name)):
    unique_things = unique_things.difference(friends_dict[friends_name[friend_index]])
print(f'Список уникальных вещей: {unique_things}')


for friend_index in range(len(friends_name)):
    if friend_index == len(friends_name) - 1:
        overall_things = friends_dict[friends_name[0]]
    else:
        overall_things = friends_dict[friends_name[friend_index + 1]]
    for num, value in enumerate(friends_dict.values(), start=0):
        if num is not friend_index:
            overall_things = overall_things.intersection(value)
    overall_things = overall_things - friends_dict[friends_name[friend_index]]
    if len(overall_things) != 0:
        print(f'{friends_name[friend_index]} не взял {overall_things}')

