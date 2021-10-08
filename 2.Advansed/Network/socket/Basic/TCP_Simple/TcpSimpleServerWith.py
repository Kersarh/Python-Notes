import socket
import time

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(("", 8001))
    sock.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
    )  # позволяет переиспользовать аддес
    sock.listen(5)  # Сколько клинтов ждет подключения
    sock.setblocking(False)  # Не блокирующий режим,
    # при отсутвии клиента работа продолжается
    # и вызывается исключение нет данных
    # sock.settimeout(5) # Блокирующий режим с таймаутом

    while True:
        try:
            client, addr = sock.accept()
            client.setblocking(False)
        except socket.error:
            print(">>> CLIENT NOT FOUND!")
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
