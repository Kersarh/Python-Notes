import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8001))
sock.send(b"TEST MSG!")
result = sock.recv(1024)
sock.close()
print("Message: ", result.decode("utf-8"))
input("press Enter")
