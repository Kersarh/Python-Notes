"""
Подключение DLL файлов.
"""

import ctypes

# Подключение системных файлов
syslib = ctypes.cdll.msvcrt  # msvcrt.dll
syslib.printf(b"system DLL!\n")

# Подключение своих файлов
# Пример 1
lib = ctypes.cdll.LoadLibrary("./NAME.dll")
lib.PrintData()

# Пример 2
lib2 = ctypes.CDLL("./NAME.dll")
x = lib2.SumData(5)
print(x)
"""
Бывает что необходимо получить доступ к функции или атрибуту DLL,
имя которого Python не распознает.
На этот случай имеется функция:
getattr(lib, attr_name)
Данная функция принимает два аргумента:
объект библиотеки и имя атрибута, а возвращает объект атрибута.
"""

lib = ctypes.cdll.LoadLibrary(r"C:\Windows\System32\msvcrt.dll")
num = 10
print_attr = getattr(lib, "printf")
print_attr(b"Print = %d\n", num)

# Использование типов данных С
lib = ctypes.CDLL(r"C:\Windows\System32\msvcrt.dll")

int_var = ctypes.c_int(17)  # тип int из C
lib.printf(b"int_var = %d\n", int_var)

str_ = b"Hello, World\n"
str_pt = ctypes.c_char_p(str_)  # указатель на строку
lib.printf(str_pt)

print("str_pt=", str_pt)  # str_pt - указатель на строку
print("str_pt.value", str_pt.value)  # получить значение через атрибут value
