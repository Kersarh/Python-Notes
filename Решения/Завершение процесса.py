# -*- coding: UTF-8 -*-

import os

pr = "MSOSYNC.EXE"

a = os.system("taskkill /f /im " + pr)
if a == 0:
    print("процесс", pr, "завершен!")
else:
    print("error")

os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
