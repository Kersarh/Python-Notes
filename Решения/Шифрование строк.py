# -*- coding: UTF-8 -*-

import os
import hashlib

ps = "password"
# Получение ХЕШ пароля
h = hashlib.md5(ps.encode('utf-8'))

# можно также с помощью метода update().
# В этом случае строка присоединяется
# к предыдущему значению
# h = hashlib.md5()
# h.update("password")

# Получить хеш строку позволяют два метода
# h.digest()
# '[\xaaa\xe4\xc9\xb9??\x06\x82%\x0bl\xf83\x1b~\xe6\x8f\xd8'
# h.hexdigest()
# '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
# полученое значение сохраняем в базе для проверки.
p = h.hexdigest()
print("p = ", p, "\n")

# Пароль, введенный пользователем
import getpass  # не хранить пароль в логах консоли
ps_inp = getpass.getpass(prompt="Enter secret password:")

h2 = hashlib.md5(ps_inp.encode('utf-8'))
if p == h2.hexdigest():  # сравнение с хешем в базе
	print("Password is correct!!!")
else:
	print("Wrong password!")

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
