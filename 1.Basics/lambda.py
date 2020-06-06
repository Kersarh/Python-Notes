import os


def f1():
    return 10 + 20  # Функция без параметров


def f2(x, y):
    return x + y  # Функция с двумя параметрами


def f3(x, y, z):
    return x + y + z  # Функция с тремя параметрами


print(f1())  # Выведет: 30
print(f2(5, 10))  # Выведет: 15
print(f3(5, 10, 30))  # Выведет: 45

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
