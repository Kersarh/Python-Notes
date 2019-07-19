import os

num1 = 1
num2 = 5

# в одном цикле не должно быть два if заменить на elif

if num1 == 1 and (num2 == 2 or num2 == 5):
    print("block if", num1, num2)

elif num1 == 3 and num2 == 4:
    print("block elif", num1, num2)

else:
    print("block else")

# запись условия в 1 строку.
# вывести Верно! если num1 < num2 иначе вывести Не верно!
print("Верно!") if (num1 < num2) else print("Не верно!")

# если i ЕСТЬ в списке
i = "y"
if i in ["y", "Y"]:
    print('Верно! {} in ["y", "Y"]'.format(i))

# если i НЕТ в списке
if i not in ["n", "N"]:
    print('ОШИБКА! {} NOT ["n", "N"]'.format(i))


# Альтарнатива множественным if - else
def fun1(a):
    print("msg" + a)


def fun2():
    print("msg2")


method = {
    "test": fun1,
    "fun2": fun2,
}

method["test"]("_ttt_")
method["fun2"]()

os.system('pause' if os.name ==
          'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
