#! venv\Scripts\python.exe
"""
Конвертер .PNG в .ICO
"""
from PIL import Image
filename = r'logo.png' # Файл для конвертации
img = Image.open(filename)
icon_sizes = [(256,256)] # Размер
img.save('logo.ico', sizes=icon_sizes) # Сохраняем итог
