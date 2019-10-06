#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket
import time

sock = socket.socket()
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# создает TCP/IP сокет (объект), AF_INET (семейство адресов Интернета) говорит, что сокет будет сетевым (бывают еще файловые для взаимодействия процессов на одном ПК, кстати для работы в IPv6 семейство адресов будет AF_INET6), SOCK_STREAM - сокет будет работать через TCP. SOCK_DGRAM через UDP
sock.bind(("", 9090))
sock.listen(5)  # ненужен при UDP

print("Server started\n")
# Ждем подключения

while True:
	conn, addr = sock.accept()
	#conn.settimeout(60)
	#conn.setblocking(0)
	print("connected:", addr)

	while True:
		try:
			data = conn.recv(1024).decode('utf-8')
			print("Получено: ", data)
			if not data:
				print("not data")
				conn.close()
				break
			send_msg = data.upper().encode('utf-8')
			conn.send(send_msg)
			print("Отправлено: ", data.upper())
		except socket.error:
			print("Error")
			err = "ERROR!"
			conn.close()
			break

conn.close()
os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
