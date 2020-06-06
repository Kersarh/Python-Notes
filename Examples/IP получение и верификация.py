import os
import re
import http.client
import ipaddress

# Получаем внешний IP
conn = http.client.HTTPConnection("eth0.me")
conn.request("GET", "")
ip_raw = conn.getresponse().read()
print(ip_raw)
# Декодируем в utf-8 и убираем символ конца строки
ip = ip_raw.decode("utf-8").rstrip("\n")
print(ip)

# Проверяем IP на корректность
ip_y = input(">>> Ваш IP? %s (y/n):" % ip)
if len(ip_y) <= 0:
    ip_y = "Y"
if ip_y not in ["y", "Y"]:
    while True:
        try:
            ip = input("Введите ваш IP:")
            ipaddress.ip_address(ip)
            break
        except Exception as e:
            print(e)
            pass
