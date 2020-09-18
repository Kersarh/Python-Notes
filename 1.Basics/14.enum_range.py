'''
Функция enumerate(<Объект>) на каждой итерации цикла for
возвращает кор-теж из индекса и значения текущего элемента
'''
arr2 = [1, 2, 3, 4, 5, 6]
for i, elem in enumerate(arr2):
    print("i=", i, "elem=", elem)

print(enumerate(arr2))  # <enumerate object at 0x000001D9B298C600>
'''
range(arg) может быть очень полезной, если вам нужно выполнить действие определенное количество раз.
'''
arr = [1, 2, 3]

# по длине arr
for i in range(len(arr)):
    print(i)
print("---------------")

# range от 1 до 5 выведет 1-4
for i in range(1, 5):
    print(i)
print("---------------")

# range от 10 до 0 с шагом -1 выведет 5-1
for i in range(5, 0, -1):
    print(i)
print("---------------")

# range от 2 до 15 с шагом 3 выведет 2 5 8 11 14
for i in range(2, 15, 3):
    print(i)
print("---------------")
