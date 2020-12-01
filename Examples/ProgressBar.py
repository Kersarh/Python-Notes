# -*- coding: UTF-8 -*-
from time import sleep
import os


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[',
          '#' * left,
          ' ' * right,
          ']',
          f' {percent:.0f}%',
          sep='',
          end='',
          flush=True)


for i in range(101):
    progress(i)
    sleep(0.1)

os.system("cls")

# ----------------------------------
from itertools import cycle
from time import sleep

for frame in cycle(r'-\|/-\|/'):
    print('\r', frame, sep='', end='', flush=True)
    sleep(0.1)
