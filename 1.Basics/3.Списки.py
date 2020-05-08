import os

mylist = [1, "два", 3.1]
print("Число элементов в списке = ", len(mylist))
print("Первый элемент", mylist[0])  # Доступ к первому элементу

mylist.append("new")  # Добавляем новый элемент в конец списка
print("Добавлен---->", mylist)
mylist.pop(0)  # Удаляем первый элемент
print("Удалён---->", mylist)
mylist.remove("new")
print("Удалён---->", mylist)
# Вложенные списки
superlist = [[1, 2, 3], [4, 5, 6]]
print(superlist)
print(superlist[1][1])  # Получаем 2 элемент во втором списке

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
