""" """
import os
import sys


def pr_name():
    # Проверка текущей OS
    os_name = os.name
    py_name = "python"
    if os_name == "nt":
        py_name = "python"
    elif os_name == "posix":
        py_name = "python3"
    else:
        py_name = "python"

    project_name = input("Введите название проекта: ")
    if len(project_name) <= 0:
        project_name = "new_venv"
        print(">>> Использовано значение по умолчанию!", project_name)
    # Создаем папки и окружение
    try:
        os.mkdir(project_name)
        os.chdir(project_name)
        print(">>> Создается окружение подождите...")
        os.system("%s -m venv venv" % py_name)
        # path_dir = os.path.abspath(os.curdir)
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
    os.chdir(os.path.abspath(os.curdir))
    # Текст файла
    text_f = """# -*- coding: utf-8 -*-
import subprocess
cmd = "cmd /K venv\\Scripts\\\\activate"
subprocess.Popen(cmd, shell=False)
"""
    file = open("start.py", "w", encoding="utf-8")
    file.write(text_f)
    file.close()


while True:
    pr = pr_name()
    if pr == 1:
        continue
    elif pr == 0:
        create_runfile()
        print(">>> Окружение создано в", os.path.abspath(os.curdir))
        break
    else:
        pass

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
