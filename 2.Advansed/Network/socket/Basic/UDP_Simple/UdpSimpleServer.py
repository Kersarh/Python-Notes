import socket

# создаем UDP socket
# AF_INET - ipv4, AF_INET6 - ipv6
# SOCK_DGRAM - Использование UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# наш сервер будет на IP 127.0.0.1 использовать порт 8888
sock.bind(("127.0.0.1", 8001))

print("Server UP")
# Пытаемся получить данные 1024байта и выводим на экран
result = sock.recv(1024)
print(result.decode("utf-8"))

# Закрываем сокет
sock.close()
print("Server DOWN")
