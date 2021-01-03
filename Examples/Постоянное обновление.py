# -*- coding: UTF-8 -*-

import datetime
""" Часы с обновлением в текущей строке """
import time

print("Время:")
while True:
    d = str(datetime.datetime.now())
    print(d[0:20], end="\r")
    time.sleep(1)
