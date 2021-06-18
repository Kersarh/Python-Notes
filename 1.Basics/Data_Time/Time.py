"""
Использование модуля time
"""

import time

# Возвращает вещественное число, представляющее количество секунд,
# прошедшее с начала эпохи (с 1 января 1970 г.):
tm = time.time()
print("time() = ", tm)

# Возвращает объект struct_time, представляющий
# универсальное время (UTC = ГРИНВИЧ).
# Если параметр не указан, то возвращается текущее время.
# Если параметр указан, то время будет соответствующим количеству секунд,
# прошедших с начала эпохи
d = time.gmtime()
d1 = time.gmtime(147060)
print("gmtime() = ", d)
print("gmtime(147060) = ", d1)
# Получить значение конкретного атрибута можно,
# указав его название или индекс внутри объекта:
print(d.tm_mon)
print(d[1])

lt = time.localtime()
lt1 = time.localtime(147060)
print("localtime() = ", lt)
print("localtime(147060) = ", lt1)

# mktime(<Объект struct_time>) — возвращает вещественное число,
# представляющее количество секунд, прошедших с начала эпохи.
# В качестве параметра указывается объект struct_time или
# кортеж из девяти элементов. Если указан-ная дата некорректна,
# возбуждается исключение OverflowError
trp = tuple(time.localtime(1233368623.0))
# >>> (2009, 1, 31, 5, 23, 43, 5, 31, 0)
time.mktime((2009, 1, 31, 5, 23, 43, 5, 31, 0))
# >>> 1233368623.0

# ПРИМЕР
d = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
m = [
    "",
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]
t = time.localtime()  # Получаем текущее время
print(
    "Сегодня:\n%s %s %s %s %02d:%02d:%02d"
    % (d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t[5])
)
# или краткая форма
print("%02d.%02d.%02d" % (t[2], t[1], t[0]))

# Приостановка программы на 5 секунд
print("start")
time.sleep(5)
print("stop")
