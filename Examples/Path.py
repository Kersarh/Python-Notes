import os
import sys

print(sys.path)  # path содержит список путей поиска модулей
print("--------------")
sys.path.append("C:\\folder1")  # Добавляем в конец списка
sys.path.insert(0, "C:\\folder2")  # Добавляем в начало списка
print(sys.path)

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
