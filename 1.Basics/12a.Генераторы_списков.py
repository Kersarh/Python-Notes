"""
Генераторы списков - это способ создания списков
из других итерируемых объектов.
"""

a = [x + 1 for x in range(3)]
print(a)  # [1, 2, 3]
# x+1 - содержит переменную или выражение (В нашем случае x + 1)
# for x in range(5) - объявляется та же самая переменная x,
# а после размещается итерируемый объект range(10).

# Более развернуто можно записать как

a = []
for x in range(3):
    a.append(x + 1)
print(a)  # [1, 2, 3]

# Вложенные генераторы
# Генераторы списков могут быть вложены друг в друга
# в результате чего могут быть получены списки списков

a = [[x + y for x in range(2)] for y in range(2)]
print(a)  # [[0, 1], [1, 2]]

# Можно записать как
a = []
for y in range(2):
    tmp = []
    for x in range(2):
        tmp.append(x + y)
    a.append(tmp)
print(a)  # [[0, 1], [1, 2]]

# Генераторы с условием
# Действие может выполняться с условием if
# которое указывается после цикла for и проверяется на каждой итерации.

a = [x for x in range(5) if x != 3]
print(a)  # [0, 1, 2, 4]

# Можно записать как
a = []
for x in range(5):
    if x != 3:
        a.append(x)
print(a)  # [0, 1, 2, 4]

# c использованием else
a = [x if x != 3 else x + 10 for x in range(5)]
print(a)  # [0, 1, 2, 13, 4]

a = []
for x in range(5):
    if x != 3:
        a.append(x)
    else:
        a.append(x + 10)
print(a)  # [0, 1, 2, 13, 4]
