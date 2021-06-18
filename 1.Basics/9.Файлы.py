"""
Работа с файлами в python.
Python есть встроенная функция open() для работы с файлами.
Синтаксис:

f = open(file_name, access_mode)

file_name - имя открываемого файла
access_mode - режим открытия файла.
Он может быть: для чтения, записи и т. д.
По умолчанию используется режим чтения (r), если другое не указано.
"""

# Запись данных в файл
f = open("myfile.txt", "w")  # Открываем файл в режиме записи
f.write("Привет!\n2 строка")  # Записываем в файл
f.close()  # Закрываем файл

# Чтение из файла
f = open("myfile.txt", "r")  # Открываем в режиме чтения
text = f.read()  # Считываем файл в переменную text
f.close()  # Закрываем файл
print(text)  # Выводим результат
# -----------------------------------------------

# Оператор with создает Менеджер контекста,
# который автоматически закрывает файл по окончанию работы.
with open("myfile.txt", mode="w") as f:
    f.write("Привет!")  # Запись в файл
    f.seek(2)  # Перейти к 3-му байту в файле
    f.write("Мир!")


# Чтение файла
with open("myfile.txt", "r") as r:
    print(r.read())
"""
r   Открывает файл только для чтения. Указатель стоит в начале файла.
rb  Открывает файл для чтения в двоичном формате.
    Указатель стоит в начале файла.
r+  Открывает файл для чтения и записи. Указатель стоит в начале файла.
rb+ Открывает файл для чтения и записи в двоичном формате.
    Указатель стоит в начале файла.
w   Открывает файл только для записи. Указатель стоит в начале файла.
    Создает файл с именем имя_файла, если такового не существует.
wb  Открывает файл для записи в двоичном формате.
    Указатель стоит в начале файла.
    Создает файл с именем имя_файла, если такового не существует.
w+  Открывает файл для чтения и записи. Указатель стоит в начале файла.
    Создает файл с именем имя_файла, если такового не существует.
wb+ Открывает файл для чтения и записи в двоичном формате.
    Указатель стоит в начале файла.
    Создает файл с именем имя_файла, если такового не существует.
a   Открывает файл для добавления информации в файл.
    Указатель стоит в конце файла.
    Создает файл с именем имя_файла, если такового не существует.
ab  Открывает файл для добавления в двоичном формате.
    Указатель стоит в конце файла.
    Создает файл с именем имя_файла, если такового не существует.
a+  Открывает файл для добавления и чтения.
    Указатель стоит в конце файла.
    Создает файл с именем имя_файла, если такового не существует.
ab+ Открывает файл для добавления и чтения в двоичном формате.
    Указатель стоит в конце файла.
    Создает файл с именем имя_файла, если такового не существует.
"""
