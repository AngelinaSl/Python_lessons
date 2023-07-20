# Задание 9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.,

# Определите размеры сетки
columns = 3
rows = 2

# Итерация по строкам
for i in range(rows):
    # Итерация по столбцам
    for j in range(2, 11):
        line = ""
        # Итерация по таблицам в столбце
        for k in range(columns):
            table_num = k * rows + i + 2
            if table_num > 9:
                break
            line += f"{table_num} x {j} = {table_num * j}   "
        print(line)
    print("------------------------------------------------")
