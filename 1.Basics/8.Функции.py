import os


# Функция (сначала определение потом вызов)
def myfunc(a):
    """ документация myfunc """
    return a


# --------------------------------------
def myfunc2(x, y):
    if x > y:
        return x
    else:
        return y


# Вызов
myfunc("тест")

# получение документации функции
print(myfunc.__doc__)
print(myfunc("print -> myfunc()"))

# присвоить переменной функцию
my_var = myfunc
my_var("my_var")

# --------------------------------------
d = myfunc2(1, 2)
print(d)

# Вызов по ключам
e = myfunc2(y=5, x=10)
print(e)


# --------------------------------------
# передача функции параметром
def fun1(name):
    print("привет " + name() + "!")


def fun2():
    return input("Введите имя: ")


# вызов
fun1(fun2)
# --------------------------------------

# args -список аргументов в порядке их указания при вызове return args


def func1(*args):
    return args


print(func1("dd", 11, 22, "aa"))

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
