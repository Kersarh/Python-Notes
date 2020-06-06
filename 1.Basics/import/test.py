import os

# import random #импорт всего мудуля random.randint(1, 100)
# from random import randint # можно вызвать как randint(1, 100)
# или импорт всех функций из модуля вызвать как randint(1, 100)
from random import *

f = randint(1, 100)
print(f)

# импорт СВОЕГО модуля!
from test_pack.first_fun import fun

# test_pack = имя папки
# first_fun = имя файла
# fun = имя функции или * если ВСЕ
fun()  # Если через from test_pack.first_fun import fun

# или
import test_pack  # при правильной настройке __init__.py

test_pack.first_fun.fun()

#
obj = __import__("test_pack.first_fun2")
obj.first_fun2.fun()

os.system("pause")
