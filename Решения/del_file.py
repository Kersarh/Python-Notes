# -*- coding: UTF-8 -*-

import os

del_file = "D:\\12.txt"

if os.path.exists(del_file):
	# Если файл есть выполняем условие
	os.remove(del_file)
	print("Файл удален! \n", del_file)

else:
	# Если файла нет
	print("Файл отсутствует! \n", del_file)

os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
