import os
from pathlib import Path

# Через pathlib
print(Path.cwd())

# Получить текущую директорию, где запущен скрипт
dr = os.path.abspath(os.curdir)
print("Скрипт запущен из ", dr)
# Где скрипт
dr2 = os.path.abspath(__file__)
print("Скрипт ",dr2)
# Директория скрипта
cur_dir = Path(__file__).resolve().parent
print("Директория скрипта ",cur_dir)

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
