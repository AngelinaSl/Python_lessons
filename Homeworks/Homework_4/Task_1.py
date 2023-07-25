# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

matrix = [[1, 2, 3], [4, 5, 6]]
transpose_matrix = [list(row) for row in zip(*matrix)]
print(f'{matrix} -> {transpose_matrix}')