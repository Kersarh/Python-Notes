import sys

sys.path.append("..")
# добавляет в PATH директорию выше
# что позволяет импортировать модули из нее
# вместо .. можно указать любую директорию с пакетом

import mod1.func as mf

mf.fun()

import fun2

fun2.fun()
