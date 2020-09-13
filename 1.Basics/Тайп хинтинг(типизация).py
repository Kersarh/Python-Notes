'''
>>> 	Warning 	<<<
>>> 	PYTHON 3.9 	<<<

Python динамически типизирован, то есть нам не нужно указывать типы данных в нашем коде.
Но иногда требуется указать ожидаемое значение
'''
'''
В нашей функции мы хотим сложить два одинаковых числа. Но python этого не знает, и соединяет две строки используя “+”, поэтому никакого предупреждения мы не увидим.
'''


def add_num(n):
    return n + n


print(add_num(10))
# Но аргументом может быть текст что может привести к ошибке в программе
print(add_num("TEXT"))


def add_num2(n: int):
    return n + n


print(add_num2(10))
print(add_num2("TEXT"))

# Словарь
mydict = {"one": 1, "two": 2}


def add_dict(n: dict) -> int:
    return sum(n[key] for key in n)


print(add_dict(mydict))
