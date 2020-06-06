import os
import sys
import subprocess

path_dir = ""


def pr_name():
    global path_dir

    # Проверка текущей OS
    os_name = os.name
    py_name = "python"
    if os_name == "nt":
        py_name = "python"
    elif os_name == "posix":
        py_name = "python3"
    else:
        py_name = "python"

    projekt_name = input("Введите название проекта: ")
    if len(projekt_name) <= 0:
        projekt_name = "new_venv"
        print(">>> Использовано значение по умолчанию!", projekt_name)
    # Создаем папки и окружение
    try:
        os.mkdir(projekt_name)
        os.chdir(projekt_name)
        print(">>> Создается окружение подождите...")
        os.system("%s -m venv venv" % py_name)
        path_dir = os.path.abspath(os.curdir)
    except FileExistsError:
        print(">>> Заданное имя уже существует!")
        return 1
    except:
        print(">>> Скрипт завершен с ошибкой!!!" "")
        print(sys.exc_info())
        return 9
    return 0


def create_runfile():
    # Создаем скрипт запуска
    os.chdir(path_dir)
    # Текст файла
    text_f = """# -*- coding: utf-8 -*-
# ! /usr/bin/env python

# Скрипт для быстрого запуская venv

import subprocess

cmd = "cmd /K venv\Scripts\\\\activate"
subprocess.Popen(cmd, shell=False)
"""
    file = open("start.py", "w", encoding="utf-8")
    file.write(text_f)
    file.close()


pr = pr_name()

while pr == 1:
    pr = pr_name()
else:
    if pr == 0:
        create_runfile()
        print(">>> Окружение создано в", path_dir)
    else:
        pass
input("\nPress any key to continue...")
