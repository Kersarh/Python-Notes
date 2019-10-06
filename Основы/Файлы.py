import os

# Открываем в режиме записи
f = open('myfile.txt', 'w')
# Записываем
f.write("Привет!\n2 строка")
f.close()  # Закрываем файл

# Открываем в режиме чтения
f = open('myfile.txt', 'r')
# Считываем
text = f.read()
# Закрываем файл
f.close()
print(text)  # Выводим результат

# Менеджер контекста в любом случае закроет файл по окончании
with open("myfile.txt", 'w') as wf:
	wf.write("Привет!")

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")

#
# r 	Открывает файл только для чтения. Указатель стоит в начале файла.
# rb 	Открывает файл для чтения в двоичном формате. Указатель стоит в начале файла.
# r+ 	Открывает файл для чтения и записи. Указатель стоит в начале файла.
# rb+ 	Открывает файл для чтения и записи в двоичном формате. Указатель стоит в начале файла.
# w 	Открывает файл только для записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# wb 	Открывает файл для записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# w+ 	Открывает файл для чтения и записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# wb+ 	Открывает файл для чтения и записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# a 	Открывает файл для добавления информации в файл. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# ab 	Открывает файл для добавления в двоичном формате. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# a+ 	Открывает файл для добавления и чтения. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# ab+ 	Открывает файл для добавления и чтения в двоичном формате. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
