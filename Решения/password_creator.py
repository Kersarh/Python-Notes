# -*- coding: UTF-8 -*-

import random
import os


def pwgen(length=10):
    """
    Генератор пароля
    """
    keylist = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_@*#$%"""
    password = []

    while len(password) < length:
        a_char = random.choice(keylist)
        password.append(a_char)
    return ''.join(password)

pwd = pwgen(12)
print(pwd)

os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")