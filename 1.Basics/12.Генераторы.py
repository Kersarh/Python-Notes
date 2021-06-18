"""
Генератор – это функция, которая будучи вызванной в функции next() возвращает
следующий объект согласно алгоритму ее работы.
Вместо ключевого слова return в генераторе используется yield.
Генератор можно использовать для итерации в цикле for,
но нельзя проиндексировать, так как генератор отрабатывает 1 раз.
"""


def gen_func(num):  # Функция генератор
    print("Start generator")
    while num > 0:
        yield num
        num -= 1


val = gen_func(5)  # Вызываем генератор на 5 циклов
print("next(val) =", next(val))  # Первое обращение к генератору

# Итерация продолжится с 4 так как один раз значение генератора было получено
for i in val:
    print(i)
