#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")

# Если куки нет то установить else вывести то что есть
if name is None:
    print("Set-cookie: name=test_cookie_value")
    print("Content-type: text/html\n")
    print("Cookies Install!!!")
else:
    print("Content-type: text/html\n")
    print("Cookies read:")
    print(name.value)
