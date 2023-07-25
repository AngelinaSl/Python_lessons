# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def create_dict_kwargs(**kwargs) -> dict:
    kwargs_dict = {}
    for key, value in kwargs.items():
        if value.__hash__ is not None:
            kwargs_dict[value] = key
        else:
            kwargs_dict[str(value)] = key
    return kwargs_dict


print(create_dict_kwargs(my_int=1, my_f_set=frozenset((1, 2, 3, 6)), my_str='str', my_set={1, 1, 1, 2, 3}))
