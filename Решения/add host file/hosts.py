import os
# Пути к файлам
#windir = os.getenv('WINDIR')
#raw_file = windir + "\\System32\\drivers\\etc\\hosts"
base_file = "base.txt"
raw_file = "test.txt"

# Читаем файлы в списки
b_ls = []
with open(base_file, "r") as bf:
	b_ls = bf.read().splitlines()
	# .splitlines() разбивает на строки без символа \n

r_ls = []
with open(raw_file, "r+") as rf:
	r_ls = rf.read().splitlines()
rf.close()

# Сортируем списки выбираем недостающие записи
ss_ls = []
for i in b_ls:
	if not i in r_ls:
		if len(i) == 0:
			continue
		ss_ls.append(i)

# Отобразить что добавляем
for i in ss_ls:
	print("отсутствует ", i)

# Записываем в файл
if ss_ls:
	print("Add data to file")
	of = open(raw_file, "a+")
	of.write("\n--- open new block ---\n")
	for i in ss_ls:
		of.write(i + "\n")
	of.write("\n--- close new block ---\n")
	of.close()
elif not ss_ls:
	print("Not new data")
else:
	print("error")

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
