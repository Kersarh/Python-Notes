import os
import sys
import sys

# import random #импорт всего мудуля random. Вызов random.randint(1, 100)
# from random import randint # Вызов randint(1, 100)
# или импорт *(всех) функций из модуля. Вызов randint(1, 100)
from random import *

f = randint(1, 100)
print(f)

# импорт СВОЕГО модуля!
import fun2

fun2.fun()

# Из вложенной директории
from mod1.func import fun  # Вызов fun()

fun()
# mod1 = имя папки
# first_fun = имя файла
# fun = имя функции или * если ВСЕ

# при правильной настройке __init__.py
import mod1

mod1.func.fun()

# импорт в переменную
obj = __import__("fun2")
obj.fun()

# Импорт из ZIP архива
sys.path.insert(0, 'MyZipMod.zip')
import mymod1

mymod1.func1()
print(mymod1.__file__)

print(">> Директории для поиска модулей <<")
print(*sys.path, sep='\n')


os.system("pause")
