import os

t = ("Первый", "Второй", "Третий")
print(t[1])  # Извлекаем второй элемент

# Отсчет идет с 0 а не с 1
t = ((1, 2, 3, 4), (5, 6, 7, 8, 9))
print(t[1][3])

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
