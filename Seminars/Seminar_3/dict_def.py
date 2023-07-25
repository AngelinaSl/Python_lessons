def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return 'Division by zero error'

# Словарь функций
operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Вызов функции из словаря
print(operations['add'](5, 3))  # Выводит 8
print(operations['subtract'](5, 3))  # Выводит 2
print(operations['multiply'](5, 3))  # Выводит 15
print(operations['divide'](5, 3))  # Выводит 1.6666666666666667