import keyboard
import time

for i in range(5):
    keyboard.press('a') # Напечатает a
    time.sleep(0.1)
keyboard.release('a')