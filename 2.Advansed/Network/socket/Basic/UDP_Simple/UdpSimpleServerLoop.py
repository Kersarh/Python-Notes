import socket

# создаем UDP socket
# AF_INET - ipv4, AF_INET6 - ipv6
# SOCK_DGRAM - Использование UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 8001))
print("Server UP")
while True:
    try:
        # Пытаемся получить данные 1024байта и выводим на экран
        result = sock.recv(1024)
    except Exception:
        print("Server ERROR")
        continue

    print(result.decode("utf-8"))

sock.close()
