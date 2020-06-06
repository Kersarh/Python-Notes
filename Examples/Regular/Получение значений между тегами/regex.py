# -*- coding: UTF-8 -*-

# Получение значание между тегами
import os
import re

# Читаем файл в text
f_r = open("reg_read.txt", "r")
text = f_r.read()
f_r.close()

# Задаем регулярное выражение и выполняем поиск
p = re.compile(r"<tag>(.*)</tag>")
m = p.findall(text)
print("m = {}".format(m))

# сохраняем результат в файл
f_w = open("reg_write.txt", "w")
for i in m:
    f_w.write(i + "\n")
f_w.close()

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
