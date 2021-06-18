import os
import sys

print("Start!")

restart = True
if restart:
    os.execv(sys.executable, [sys.executable] + sys.argv)

print("Stop!")
exit()
