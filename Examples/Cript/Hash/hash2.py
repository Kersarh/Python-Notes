"""
Хеш-функция детерминистически создает ключ из пароля.
Поскольку хеш являются односторонними, злоумышленник не cможет восстановить пароль из хеша.

Обратите внимание, что использование метода PBKDF2 не останавливает атаки грубой силы/перебора по словарю или использование радужных таблиц, а просто делает методы более сложными в вычислительном отношении.
"""

import os
import hashlib

ps = "MY_PASSWORD"

# Получаем хеш из пароля
hs = hashlib.md5(ps.encode())

# Получить хеш строку позволяют два метода
# h.digest()
# '[\xaaa\xe4\xc9\xb9??\x06\x82%\x0bl\xf83\x1b~\xe6\x8f\xd8'
# h.hexdigest()
# '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'
ps = hs.hexdigest()
print(ps, "\n")


# Пароль, введенный пользователем
ps_inp = "MY_PASSWORD"

h2 = hashlib.md5(ps_inp.encode())
ps2 = h2.hexdigest()
if ps == ps2:  # сравнение с хешем в базе
    print("Верно")
else:
    print("Пароли не совпадают")


# KDF
salt = os.urandom(32)  # !Не забываем сохранить соль
password = "MY_PASSWORD"

key = hashlib.pbkdf2_hmac(
    "sha256",  # алгоритм хеширования
    password.encode(),  # пароль в byte
    salt,  # соль
    100000,  # кол-во итераций
    dklen=128,
)  # длинна ключа

# Проверка пароля
new_pass = "MY_PASSWORD"
new_key = hashlib.pbkdf2_hmac(
    "sha256",  # алгоритм хеширования
    new_pass.encode(),  # пароль в byte
    salt,  # соль
    100000,  # кол-во итераций
    dklen=128,
)  # длинна ключа

if new_key == key:  # сравнение с хешем в базе
    print("Верно")
else:
    print("Пароли не совпадают")
