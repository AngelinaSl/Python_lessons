# Задание №7
# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

#
# def profit(dict_input:dict[str:int|float])->bool:
#     return all(map(lambda x: sum(x) > 0, dict_company.values()))
#
#
# dict_company = {'компания1': [1000, -2000, 5000, -1000],
#                 'компания2': [300, 5000, 200, 4000],
#                 'компания3': [1000, 1000, -3000]}
#
# print(profit(dict_company))


def calculate_profit(companies):
    all_profitable = True
    result = {}
    for company, transactions in companies.items():
        total = sum(transactions)
        result[company] = total
        if total < 0:
            all_profitable = False
    return result, all_profitable

companies = {
    "Company1": [1000, -500, 200, -300],
    "Company2": [2000, -1000, 500, -500],
    "Company3": [1500, -700, 300, -200, -800,-850]
}

print(calculate_profit(companies))