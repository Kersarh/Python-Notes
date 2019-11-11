import os
from pathlib import Path

# Через pathlib
print(Path.cwd())

# Получить текущую директорию, где запущен скрипт
dr = os.path.abspath(os.curdir)
print(dr)
# Получить текущую директорию, где расположен скрипт
dr2 = os.path.abspath(__file__)
print(dr2)

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
