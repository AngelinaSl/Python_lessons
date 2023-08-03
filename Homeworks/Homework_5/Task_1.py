# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def divide_link(path: str) -> tuple:
    path, name, ext = '\\'.join(path.split('\\')[:-1]), path.split('\\')[-1].split('.')[0], \
                      path.split('\\')[-1].split('.')[1]
    return path, name, ext


link = r'C:\Users\79274\Desktop\GeekBrains\Markdown\image.png'
print(divide_link(link))