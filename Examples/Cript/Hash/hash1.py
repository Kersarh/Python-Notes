"""
Хеш-функция детерминистически создает ключ из пароля.
Поскольку хеш являются односторонними, злоумышленник не cможет восстановить пароль из хеша.

Cуществует библиотека Bcrypt, которая позволяет получить сильные ключи.
Созможно использовать в прод коде:
pip install bcrypt

!!! Обратите внимание, что использование метода KDF не останавливает атаки грубой силы/перебора по словарю или использование радужных таблиц, а просто делает методы более сложными в вычислительном отношении.
"""

import bcrypt

# Получаем хеш из пароля
hs = bcrypt.hashpw("MY_PASSWORD".encode(), bcrypt.gensalt())  # gensalt() + соль к хешу
print(hs)


# Проверка пароля
password = "MY_PASSWORD"
valid = bcrypt.checkpw(password.encode(), hs)
print(valid)


# KDF
slt = bcrypt.gensalt()  # Получаем соль
key = bcrypt.kdf(password=b"MY_PASSWORD", salt=slt, desired_key_bytes=32, rounds=100)
print(key)

# Проверка пароля KDF
ps = input("Пароль:").encode()
new_key = bcrypt.kdf(password=ps, salt=slt, desired_key_bytes=32, rounds=100)

if new_key == key:
    print("Верно")
else:
    print("Пароли не совпадают")
