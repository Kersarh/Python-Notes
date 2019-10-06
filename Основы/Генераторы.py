import os

# Генераторы - итерируемые объекты, но, в общем случае,
# вы можете их использовать только один раз.
# Это связано с тем, что они не хранят все значения в памяти,
# а генерируют значения "на лету" - по мере запроса.


# Yield - это ключевое слово которое используется так же,
# как и слово return. Функция при этом
# возвращает генератор вместо значения
def generator():
	for i in (1, 2, 3):
		yield i


g = generator()  # создаём генератор
print("g = ", g)

for i in g:
	print(i)

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
