import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", 8001))
# sock.setsockop(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # Широковещательные сообщения всем клиентам
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Переиспользование порта

print("Server UP")
result = sock.recv(1024)
print(result.decode("utf-8"))

sock.close()
print("Server DOWN")
