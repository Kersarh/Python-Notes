# -*- coding: UTF-8 -*-

import os

a = os.getenv("APPDATA")
print(a)
w = os.getenv("WINDIR")
print(w)

# Все переменые окружения
# print(os.environ)

# result = os.environ.get('Переменная')
result = os.environ.get('Переменная', 'Если переменной нет')
print(result)

# Создать или изменить
os.environ['MY_DATA'] = "Мои Данные"
print(os.environ['MY_DATA'])


# Через ctypes
def folder_win():
    import ctypes.wintypes
    CSIDL_PERSONAL = 5  # 5 = My Documents

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, 0, buf)
    return buf.value


print(folder_win())

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
