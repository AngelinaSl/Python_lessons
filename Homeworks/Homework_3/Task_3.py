# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

backpack = []
LOAD_CAPACITY = 7
THINGS = {
    "compass": 1,
    "matches": 1,
    "first aid kit": 2,
    "water": 3,
    "clothes": 4,
    "tent": 5
    }


# метод для одного допустимого варианта
def fill_backpack(baggage: dict[str:int], size: int) -> list[str]:
    for key, value in baggage.items():
        if value <= size:
            size -= value
            backpack.append(key)
    return backpack


print(fill_backpack(THINGS, LOAD_CAPACITY))

