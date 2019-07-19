import sys
import os
import site

sp = sys.prefix
print("Путь к Python >>", sp)
print("\n")

data = site.getsitepackages()
print("Путь к Python >>", data[0])
print("Путь к пакетам >>", data[1])
print("\n")
os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")