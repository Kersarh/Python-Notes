import re
import os

pattern = re.compile("(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)")
address = input("inter you email address:")
is_valid = pattern.match(address)
if is_valid:
    print("правильный email:", is_valid.group())
    # объект is_valid содержит 3 метода
    print(
        "методы: start:",
        is_valid.start(),
        "end:",
        is_valid.end(),
        "group:",
        is_valid.group(),
    )
else:
    print("неверный email! введите email...\n")

os.system("pause" if os.name == "nt" else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
