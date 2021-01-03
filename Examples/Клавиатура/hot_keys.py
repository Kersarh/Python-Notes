import keyboard

print('Нажмите желаемую комбинацию клавиш')
shortcut = keyboard.read_hotkey()
print('Вы выбрали:', shortcut)


def on_triggered():
    print("Triggered!")


keyboard.add_hotkey(shortcut, on_triggered, suppress = True)
# keyboard.add_hotkey('ctrl+shift', on_triggered)
# suppress = True подавляет другие возможные пересечения.

print("Нажмите ESC для остановки")
keyboard.wait('esc')