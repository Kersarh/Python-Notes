# -*- coding: UTF-8 -*-

import os
import subprocess

# Программа
program = "notepad.exe"
process = subprocess.Popen(program)
code = process.wait()  # Ожидание завевершения
print(code)  # 0

# Командная строка
code = subprocess.call(["ping", "yandex.ru"])
print("--------------------------------------------")
# Связь с созданным  процессом
args = ["ping", "google.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
for line in data:
	if line:
		line = line.strip()
		print(line.decode('cp866'))

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
