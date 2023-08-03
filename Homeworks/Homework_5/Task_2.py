# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


def generate_dict(names: list[str], salaries: list[int], bonuses: list[str]) -> dict[str:int]:
    return {name: salary / 100 * float(bonus)
            for name, salary, bonus in zip(names, salaries, map(lambda x: x.replace('%', ''), bonuses))}


list_name = ['Иван', 'Олег', 'Василий', 'Петр']
list_money = [125000, 110000, 118000, 130000]
list_bonus = ['10.22%', '12.3%', '8.5%', '9.85%']
print(generate_dict(list_name, list_money, list_bonus))
