# Задание №2
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def list_sim(str_input: str) -> list[str]:
    return [ord(i) for i in sorted(list(str_input.replace(" ", '')), reverse=True)]


def list_sim2(str_input: str) -> map:
    return map(ord,
               sorted(list(str_input.replace(" ", '')),
                      reverse=True))



text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
print(list_sim(text))
print(*list_sim2(text))
