import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8001))
sock.send(b"TEST MSG!")
sock.close()
input("press Enter")
