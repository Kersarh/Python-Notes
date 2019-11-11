# -*- coding: utf-8

import os
import shutil  # Подключаем модуль
# Метаданные (права и тд) НЕ копируются!
shutil.copyfile("C:\mouse.txt", "C:\\new-mouse.txt")

# Копирование с сохранением прав
shutil.copy("C:\mouse.txt", "C:\\new-mouse.txt")

# Копирование директории
shutil.copytree(
    "F:\Projects\Python",
    "F:\wer",
)

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
