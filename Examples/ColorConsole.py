#! python
import os
import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))


out_red("Вывод красным цветом")
out_yellow("Текст жёлтого цвета")
out_blue("Синий текст")

print("\033[4m\033[37m\033[44m{}\033[0m".format("Python 3"))

os.system("pause")
