import os
if __name__ != "__main__":
    from . import first_fun2
# print("Загружен как: ", __name__)

def fun():
    print("first_fun.py")
    first_fun2.fun()


# Виден только если запущен как самостоятельный скрипт!
if __name__ == "__main__":  # если запускается, как сценарий
    print("Запущен как: ", __name__)
    os.system("pause")
    exit()
