#! python
"""venv conda """

import os
import subprocess

conda_dir = "F:\\Program\\Anaconda3"
conda_script = conda_dir + "\\Scripts\\activate.bat"


def venv_create(conda_script, conda_dir):
    print("Conda dir = ", conda_dir)
    env_name = input("Введите название проекта: ")
    if len(env_name) <= 0:
        env_name = "new_venv_conda"
        print(">>> Default name: ", env_name)
        os.mkdir(env_name)
    else:
        os.mkdir(env_name)
    create_runfile(env_name)

    py_ver = input("Python версия(пример = 3.7.2): ")
    if len(py_ver) <= 0:
        py_ver = "3.7.2"
        print(">>> Использовано значение по умолчанию!", py_ver)

    cmd = "cmd /K {conda_script} {conda_dir} && conda create -p {env_name}\\venv_{env_name} --copy --yes python={py_ver} conda".format(
        conda_script=conda_script,
        conda_dir=conda_dir,
        env_name=env_name,
        py_ver=py_ver)
    subprocess.Popen(cmd, shell=False)


def create_runfile(env_name):
    # Текст файла
    text_f = """# -*- coding: utf-8 -*-

# Скрипт для быстрого запуская venv

import subprocess

cmd = "cmd /K venv_{env_name}\\\\Scripts\\\\activate"
subprocess.Popen(cmd, shell=False)
"""
    file = open("{}\\start_venv.py".format(env_name), "w", encoding="utf-8")
    file.write(text_f)
    file.close()


venv_create(conda_script=conda_script, conda_dir=conda_dir)
