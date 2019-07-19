import os

mydic = {1: "Первый", 2: "Второй"}
print("Возьмём элемент с ключом 1 ------>", mydic[1])

# Более сложная структура
superdic = {'name': {'first': 'Александр',
                     'second': 'Иванов'}, 'job': ['ОИТ', 'ОТК']}
print(superdic['name']['second'], "--->", superdic['job'][0])

# Замена по словарю
dic = {'a': 1, 'b': 2, 'c': 3}

# Вариант 1
text = 'abccba'
for i in dic.keys():
    text = text.replace(i, str(dic[i]))
print(text)

# Вариант 2
text2 = 'abccba'
trlt_txt = ""

for i in text2:
    if i in dic.keys():
        i = dic[i]
        trlt_txt += str(i)
    else:
        pass
print(trlt_txt)


os.system('pause' if os.name ==
          'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")
