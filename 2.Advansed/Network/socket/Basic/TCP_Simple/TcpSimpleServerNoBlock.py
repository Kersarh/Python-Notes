import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 8001))
sock.listen(5)  # Сколько клинтов ждет подключения
sock.setblocking(False)  # Не блокирующий режим,
# при отсутвии клиента работа продолжается и вызывается исключение нет данных
# sock.settimeout(5) # Блокирующий режим с таймаутом

while True:
    try:
        client, addr = sock.accept()
    except socket.error:
        print("NO CLIENT")
    except KeyboardInterrupt:
        print("ERR")
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.send(b"Done!")
        client.close()
        print("Message: ", result.decode("utf-8"), addr)
    time.sleep(1)  # Проверять каждую секунду можно УДАЛИТЬ!
