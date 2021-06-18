"""
Эмулятор броска костей для D&D
"""

import random

# Бросок одной кости
def dise(data):
    s = data.split("d")
    summ = 0
    for i in range(int(s[0])):
        a = random.randint(1, int(s[1]))
        summ += a
    return summ


# Обработка набора
def round(in_data):
    summ = 0
    if in_data == "":
        return
    data = in_data.split(" ")

    for i in data:
        summ += dise(i)
    return summ


while True:
    # Надор данных в формате "2d6 1d8"
    in_data = input("Набор?\n")
    if not in_data:
        break
    s = round(in_data)
    print("Выпало: ", s, "\n")
