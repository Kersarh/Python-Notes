#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

print(
    "Set-cookie: name=value; expires=Wed May 18 03:33:20 2033; path=/cgi-bin/; httponly"
)
# Срок её хранения до мая 2033 года,
# отправляется повторно на сервер только к скриптам,
# которые расположены в /cgi-bin/,
# и передается только http-запросами
# (её нельзя получить из браузера пользователя с помощью javascript).

#print("Set-cookie: name=value")
# Храниться она будет до того момента, когда закроется браузер,
# будет отправляться на сервер для любых документов
# (и для /index.html тоже, в отличие от предыдущего случая).
# Также её можно будет получить средствами javascript
# (поскольку не был установлен флаг httponly).

print("Content-type: text/html\n")
print("Cookies!!!")
