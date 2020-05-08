#! python
import os
import sys
# Подключаем наш архив с модулями
sys.path.insert(0, 'lib.zip')

# Импортируем модуль и вызываем функцию
import mod1
mod1.mod1Func()

# Работает ли байт код? 
print(mod1.__file__)

import mod2
mod2.print_sysinfo()

# Не работает как как не импортировано в __init__.py
# mod2.print_notInit()

os.system("pause")


