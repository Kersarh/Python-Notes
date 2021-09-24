"""
Получение данных со страниц
"""
import os
from urllib import request

response = request.urlopen("http://yandex.ru")

print("\n------------------\n")
print(response.status)
print("\n------------------\n")
print(response.getcode)
print("\n------------------\n")
print(response.msg)
print("\n------------------\n")
print(response.reason)
print("\n------------------\n")
print(response.headers)
print("\n------------------\n")
print(response.getheaders)
print("\n------------------\n")
print(response.headers.get("Content-Type"))
print("\n------------------\n")
print(response.getheader("Content-Type"))
print("\n------------------\n")

os.system("pause")
