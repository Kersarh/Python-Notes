import keyboard
import time

keyboard.start_recording()  # записываем нажатия
time.sleep(10)  # в течении n секунд
keyboard.replay(events)