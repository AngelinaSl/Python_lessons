# Задание №8
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

friends_dict = {'Вася':{'рюкзак', 'палатка', 'котелок', 'фонарик'},
             'Коля':{'рюкзак', 'палатка', 'фонарик', 'спички'},
             'Миша':{'рюкзак', 'палатка', 'спички', 'велосипед'}}

# Преобразуем кортежи вещей в множества для удобства работы
friends_sets = {name: set(items) for name, items in friends_dict.items()}

# Вещи, которые взяли все три друга
all_items = set.intersection(*friends_sets.values())

# Вещи, которые уникальны для каждого друга
unique_items = {name: items - set.union(*(s for n, s in friends_sets.items() if n != name))
                for name, items in friends_sets.items()}

# Вещи, которые есть у всех друзей, кроме одного
one_missing_items = {name: (set.union(*(s for n, s in friends_sets.items() if n != name)) - items)
                     for name, items in friends_sets.items()}

print(f'Все друзья: {all_items},\n Уникальные вещи: {unique_items}, \n Взял один: {one_missing_items}')



# absent = []
#
# for curr_name, curr_items in baggage.items():
#     temp_items = set()
#     for other_name, other_items in baggage.items():
#         if other_name == curr_name:
#             continue
#         elif not temp_items:
#             temp_items = set(other_items)
#             continue
#
#         if temp_items != other_items:
#             others = temp_items.intersection(set(other_items))
#             temp_items = others
#
#     absent_items = others - set(curr_items)
#     if absent_items:
#         absent.append((absent_items, curr_name))
#
# for item, name in absent:
#     print(f'{item} нет у {name}, но есть у остальных')