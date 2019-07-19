import os

# Открываем в режиме записи
f = open('myfile.txt', 'w')
# Записываем
f.write("Привет!")
f.close()  # Закрываем файл

# Открываем в режиме чтения
f = open('myfile.txt', 'r')
# Считываем
text = f.read()
# Закрываем файл
f.close()
print(text)  # Выводим результат


# Менеджер контекста в любом случае закроет файл по окончании
with open("myfile.py", 'w') as wf:
    wf.write("Привет!")

os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
