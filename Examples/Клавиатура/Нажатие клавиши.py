import keyboard
import time

for i in range(5):
    keyboard.press("a")  # Напечатает a
    time.sleep(0.1)
keyboard.release("a")

# Вариант только для Windows
# import msvcrt
# key = ord(msvcrt.getch())
# if key == 27:
#     print("ESC")
