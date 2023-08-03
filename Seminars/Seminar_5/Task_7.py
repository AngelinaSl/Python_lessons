# Создайте функцию-генератор.
# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def is_prime(n):
    """Проверяет, является ли число простым."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(N):
    """Генерирует N простых чисел, начиная с числа 2."""
    count, num = 0, 2
    while count < N:
        if is_prime(num):
            yield num
            count += 1
        num += 1

# Вывод первых 10 простых чисел
print(list(generate_primes(20)))