import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 8001))
sock.listen(5)  # Сколько клиентов ждет подключения

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        print("ERR")
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.send(b"Done!")
        client.close()
        print("Message: ", result.decode("utf-8"))
