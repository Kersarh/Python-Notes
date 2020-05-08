import ctypes
import os

syslib = ctypes.cdll.msvcrt
syslib.printf(b"system DLL!\n")



lib = ctypes.cdll.LoadLibrary("./NAME.dll")
lib.PrintData()

lib2 = ctypes.CDLL('./NAME.dll')
x = lib2.SumData(5)
print(x)

os.system("pause")
