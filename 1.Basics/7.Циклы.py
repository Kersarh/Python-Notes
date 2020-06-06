import os

i = 10

# цикл while пока i > 0 = True
while i > 0:
    i -= 1  # i = i - 1
    print("Верно!", i)
else:  # Необязательное! Выполняется если while = Falsa
    print("error!")

# цикл for
# проходит по списку выводя значения
lst = [1, 2, 3, 4, 5]
for x in lst:
    print("x= ", x)

for a in range(5):
    print("a= ", a)

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
