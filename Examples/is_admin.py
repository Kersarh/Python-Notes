import ctypes
import os
import sys


def is_admin():
    """Проверяем права"""
    try:
        # Если админ вернет True
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    # Если админ продолжаем скрипт дальше
    input(" As Admin!!!\n Press Enter!")

else:
    # Перезапускаем скрипт с правами админа
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1
    )
    exit()  # выходим из старой версии скрипта

print("your code...")

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
