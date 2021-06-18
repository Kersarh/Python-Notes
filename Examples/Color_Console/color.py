import os
import colorama

colorama.init()

print(colorama.Fore.RED + "some red text")
print(colorama.Fore.GREEN + "and with a green background")
print(colorama.Style.DIM + "and in dim text")
print(colorama.Style.RESET_ALL)
print("back to normal now")

os.system("pause")
