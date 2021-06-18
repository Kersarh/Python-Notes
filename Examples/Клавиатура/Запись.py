"""
Given text files or text from stdin, simulates keyboard events that type the
text character-by-character.
"""
import keyboard
import fileinput

for line in fileinput.input():  # Получаем ввод с клавиатуры
    keyboard.write(line)
