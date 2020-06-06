import os

# print("Загружен как: ", __name__)


def fun():
    print("first_fun2.py")


# Виден только если запущен как самостоятельный скрипт!
if __name__ == "__main__":  # если запускается, как сценарий
    print("Запущен как: ", __name__)
    os.system("pause")
    exit()
