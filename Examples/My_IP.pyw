import os
import re
import http.client
import ipaddress
import socket
import tkinter
from tkinter import messagebox


def net_ip():
	# Получаем внешний IP
	conn = http.client.HTTPConnection("eth0.me")
	try:
		conn.request("GET", "")
	except Exception:
		return "Err (not connected)"

	ip_raw = conn.getresponse().read()
	# Декодируем в utf-8 и убираем символ конца строки
	ip = ip_raw.decode('utf-8').rstrip('\n')
	return ip


def local_ip():
	# Получаем локальный IP
	local_ip = socket.gethostbyname(socket.gethostname())
	if local_ip == "192.168.244.1":
		return "Err (192.168.244.1)"
	return local_ip

# list_local_ip = [i for i in socket.getaddrinfo(socket.gethostname(), None)] # Можно получить через генератор списков

def my_list_ip():
	# Получаем ВСЕ локальные IP
    l = []
    ret = ""
    for i in socket.getaddrinfo(socket.gethostname(), None):
        l.append(i[4][0])
    for a in l:
    	ret += a +"\n"
    return ret


if __name__ == "__main__":
	# hide main window
	root = tkinter.Tk()
	root.withdraw()
	msg = "WEB - \n{}\nLOCAL - \n{}".format(net_ip(), my_list_ip())
	while messagebox.askretrycancel("IP", msg):
		pass
