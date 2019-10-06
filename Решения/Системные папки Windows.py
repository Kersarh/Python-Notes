# -*- coding: UTF-8 -*-

import os

a = os.getenv('APPDATA')
print(a)
w = os.getenv('WINDIR')
print(w)

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
