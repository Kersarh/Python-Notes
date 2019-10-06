# coding: utf8

import os

arr = [1, 2, 3]

for i in range(len(arr)):
	arr[i] *= 2  # i = i*2
print(arr)  # Результат выполнения: [2, 4, 6]

# range от 1 до 11 выведет 1-10
for i in range(1, 11):
	print(i)
# range от 10 до 0 с шагом -1 выведет 10-1
for i in range(10, 0, -1):
	print(i)
# range от 2 до 15 с шагом 3 выведет 2 5 8 11 14
for i in range(2, 15, 3):
	print(i)

# Функция enumerate(<Объект>) на каждой итерации цикла for
# возвращает кор-теж из индекса и значения текущего элемента
# В качестве примера умножим на 2 каждый элемент списка,
# который содержит четное число
arr2 = [1, 2, 3, 4, 5, 6]
for i, elem in enumerate(arr2):
	if elem % 2 == 0:
		arr2[i] *= 2
print(arr2)

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
