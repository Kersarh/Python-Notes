# -*- coding: UTF-8 -*-

import zipfile
import os
import datetime

# import sys
# import codecs

# Правка кодировки
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

dt = datetime.datetime.now()  # получаем дату и время!
now_date = dt.date().strftime("%Y-%m-%d")  # Текущая дата
now_time = dt.time().strftime("%H-%M-%S")  # Текущее время
backup_folders = ["D:\\test1", "D:\\test2",
                  "D:\\test3"]  # Список папок для архивации
arch_name = "backup_" + str(now_date) + ".zip"  # имя архива!
ignore_file = ["123.txt"]  # если надо исключить файлы


def mybackup(arch, folder_list, mode):
    """mybackup(arch, folder_list, mode)
            a = arch_name, b = folder, mode = "r" or "w" or "a"
            r = read w = write a = append  """
    # Счетчики
    num = 0
    num_ignore = 0
    # Создание нового архива
    z = zipfile.ZipFile(arch, mode, zipfile.ZIP_DEFLATED, True)
    # Получаем папки из списка папок.
    for add_folder in folder_list:
        # Список всех файлов и папок в директории add_folder
        for root, dirs, files in os.walk(add_folder):
            for file in files:
                if file in ignore_file:  # Исключаем лишние файлы
                    print("Исключен! ", str(file))
                    num_ignore += 1
                    continue
                # Создание относительных путей и запись файлов в архив
                path = os.path.join(root, file)
                z.write(path)  # Все работает!
                print(num, path)
                num += 1
    z.close()
    print("------------------------------")
    print("Добавлено: ", num)
    print("Проигнорировано: ", num_ignore)


print(now_time, now_date)
# функция создаст архив при наличии перезапишет существующий
mybackup(arch_name, backup_folders, "w")

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
