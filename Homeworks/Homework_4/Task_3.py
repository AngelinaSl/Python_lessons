# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


COMM_WITHDRAWAL = 1.5
COMM_REFILL = 3
TAX = 10
COMM_MIN = 30
COMM_MAX = 600
SUM_WORK = 50
MAX_ACCOUNT = 5000000
account = 0
count_refill = 0
count_withdrawal = 0
operations_history = []


# Получение суммы денег
def get_money(input_string: str) -> int:
    while True:
        try:
            num = int(input(input_string))
            if num > 0 and num % SUM_WORK == 0:
                return num
            else:
                print('Сумма должна быть положительной и кратной 50')
        except ValueError:
            print('Попробуйте еще раз')


# добавить деньги на счет
def refill_account(num: int, list_history: list) -> None:
    global account
    account += num
    list_history.append(num)


# добавление 3%
def account_proc(list_history: list) -> None:
    global account
    num = account / 100 * COMM_REFILL
    refill_account(num, list_history)


# снятие денег со счета
def take_account(num: int, list_history: list) -> None:
    global account
    account -= num
    list_history.append(-num)


# снятие 10% на роскошь
def take_tax(list_history: list) -> None:
    global account
    if account > MAX_ACCOUNT:
        num = account / 100 * TAX
        take_account(num, list_history)


# подсчет суммы для снятия и 1,5%
def check_money(num: int | float) -> int | float:
    proc = num / 100 * COMM_WITHDRAWAL
    if proc < COMM_MIN:
        num += COMM_MIN
    elif proc > COMM_MAX:
        num += COMM_MAX
    else:
        num += proc
    return num


print('Здравствуйте.Это программа банкомат\n')
while True:
    choice = int(input('Выберите желаемое действие:\n'
                       '1 - Пополнить счет\n'
                       '2 - Снять деньги со счета\n'
                       '3 - История операций\n'
                       '4 - Выход\n'))
    take_tax(operations_history)
    match choice:
        case 1:
            number = get_money('Введите сумму для зачисления на счет:\n')
            refill_account(number, operations_history)
            count_refill += 1
            if count_refill == 3:
                account_proc(operations_history)
                count_refill = 0
            print(f'У вас на счету: {account} рублей')
        case 2:
            number = get_money('Введите сумму для снятия со счета:\n')
            number = check_money(number)
            if number < account:
                take_account(number, operations_history)
                count_withdrawal += 1
                if count_withdrawal == 3:
                    account_proc(operations_history)
                    count_withdrawal = 0
            else:
                print('Недостаточно средств')
            print(f'У вас на счету: {account} рублей')
        case 3:
            print(operations_history)
        case 4:
            print('До свидания')
            print(f'У вас на счету: {account} рублей')
            break
        case _:
            print('Ошибка ввода')
