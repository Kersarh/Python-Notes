#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket
import threading
import time

sock = socket.socket()
sock.connect(("localhost", 9090))

print ("Client started\n")

text = "Hello"
while True:
	# Отправляем собщение
    sock.send(text.encode('utf-8'))
    # Получаем ответ и выводим
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    # Набираем новое сообщение
    text = input("Команда: ")
    if not text:
        print("Error! Введите команду!")
        text = "not_data"

sock.close()
os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
