# Добавьте в список повторяющиеся элементы и сравните на результаты.

data = ['vvv', 12, 12.01, 'kkk']

for num, element in enumerate(data, start=1):
    if isinstance(element, int):
        elem_type = 'INT'
    elif isinstance(element, str):
        elem_type = 'STR'
    print(f"""{num} {element} {id(element)} {element.__sizeof__()} {hash(element)}""")

