"""
Скрипт записывает уникальные строки из new_data_file в test.txt.
Запись данных происходит в начало файла
"""
# Файлы
new_data_file = "base.txt"  # Откуда берутся данные
work_file = "test.txt"  # Куда добавляются

# Читаем new_data_file в список
# .splitlines() разбивает на строки без символа \n
new_data_list = []
with open(new_data_file, "r") as nd:
    new_data_list = nd.read().splitlines()

work_list = []
with open(work_file, "r") as wl:
    work_list = wl.read().splitlines()

# Сортируем списки выбираем недостающие записи
new_list = []
for i in new_data_list:
    if not i in work_list:
        if len(i) == 0:
            continue
        new_list.append(i)

# Отобразить что добавляем
for i in new_list:
    print("Отсутствует ", i)

# Записываем в файл
if new_list:
    print("Добавляем данные в файл")
    # Двойное открытие файла чтобы писать в начало
    # Если нужно писать в конец оставить только второе открытие файла
    # И прописать модификатор доступа a+
    with open(work_file, "r") as wl:
        file = wl.read()
    with open(work_file, "w") as wl:
        wl.write("# --- Начало блока ---\n")
        for i in new_list:
            wl.write(i + "\n")
        wl.write("# --- Конец блока ---\n")
        wl.write(file)
elif not new_list:
    print("Нет новых данных")
else:
    print("Ошибка")
