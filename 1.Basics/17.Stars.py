"""
Использование операторов * и **.
"""
# Распаковка аргументов в функции

list1 = ["test", "test1", "test2"]
# Использование оператора * для распаковки итерируемого объекта
print(*list1)
# Что соответствует
print(list1[0], list1[1], list1[2])
# Но через * нам ненужно знать длину списка

# Оператор ** делает подобную операцию но только с именованными аргументами.
# Позволяет взять словарь с парами ключ-значение и распаковать его
# в именованные аргументы.

date_info = {"year": "2000", "month": "01", "day": "01"}
inf2 = {"todo": "NEW YEAR!"}
data_str = "{year}-{month}-{day}-{todo}".format(**date_info, **inf2)
print(data_str)

# Упаковка аргументов при передачи в функцию
# При определении функции можно использовать * ,
# для указания переменного количества позиционных аргументов


def fun(*data):
    print(data)


# Мы можем передать любое кол-во аргументов
fun("test1", "test2")


# Оператор ** соберёт все переданные именованные аргументы в словарь
def tag2(**attrib):
    print(attrib)


tag2(data="mydata", test="mytest")

# В Python есть специальный синтаксис
# для только именованных (keyword-only) аргументов.
# Такие аргументы нельзя указать позиционно, ТОЛЬКО ПО ИМЕНИ.
# Вызов функции с именованными аргументами выглядит гораздо нагляднее.
# Сразу можно понять, какой аргумент за что отвечает.
# Также при использовании позиционных аргументов
# Вы вынуждены соблюдать их порядок.
# Именованные аргументы можно расположить в произвольном порядке.


# Аргументы dictionary и default идут после *keys,
# Что означает что их можно указать только как именованные аргументы.
def pos_arg(*keys, dictionary, default=True):
    print("keys= ", keys)
    print("dictionary= ", dictionary)
    print("default= ", default)


pos_arg("data1", "data2", dictionary=list1, default=False)  # Вызов по имени

# pos_arg("data1", 'data2', list1, True) # Такой вызов приведет к ошибке


# Одиночная звездочка указывает что функция принимает именованные аргументы!
# Данная функция принимает позиционный аргумент mydata
# И именованный аргумент
def pos_arg2(mydata, *, dictionary):
    print("mydata= ", mydata)
    print("dictionary= ", dictionary)


pos_arg2("Hello World", dictionary=list1)
