import socket

# создаем UDP socket
# AF_INET - ipv4, AF_INET6 - ipv6
# SOCK_DGRAM - Использование UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Send Message...")
message = "NEW MESSAGE!"
# отправляем сообщение на `localhost:8888`
sock.sendto(message.encode(), ("localhost", 8001))
