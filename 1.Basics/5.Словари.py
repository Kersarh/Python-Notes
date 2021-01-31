'''
Словарь (dict) - неупорядоченная структура данных,
в которой элементы хранятся в виде ключ: значение.
Объявляются словарь в фигурных скобках {}, и доступ к данным осуществляется по ключу.
'''

# Создадим словарь с произвольными значениями.
# где "1" это ключ, а "Первый" значение и тд..
mydic = {1: "Первый", 2: "Второй", "name": "user", "noname": "user"}

# Получение значения по ключу
print(mydic[1])  # Первый
print(mydic["name"])  # user

#Получение ключа по значению
# !!! Значение не уникальны
# таким образом ключей для одного значения модет быть много
dataname = "user"
for k, v in mydic.items():
    if v == dataname:
        print("Значение {} = ключу {}".format(dataname, k))

# Добавление в словарь
mydic["admin"] = True
print(mydic)

# Важно
# Попытка обратиться к значению по ключу, которого нет в словаре, вызовет исключение KeyError.
# Можно воспользоваться try/except или  if.
# Что приводит к излишним загромождениям кода на простой операции.
print(mydic.get(1))  # Первый
print(mydic.get("test", "NOT_DATA"))  # NOT_DATA
print(mydic.get("test"))  # None

# Обьединение словарей
d1 = {'x': 1, 'y': 2, 'z': 3}
d2 = {'a': 4, 'b': 5, 'x': 10}

d = d1.copy()  # Копируем первый словарь
d.update(d2)  # обновляем его из второго словаря
# Python 3.9
# Слияние в d
d = d1 | d2
# Или слияние c поглощением
d1 |= d2

# Вложенные словари
# Как списки или кортежи словарь может быть вложен в словарь:
sumdic = {
    "name": {
        "first": "Иван",
        "second": "Иванов"
    },
    "job": ["Админ", "Программер"]
}
print("Пользователь: ", sumdic["name"]["second"], "\tДолжность: ",
      sumdic["job"][0])
# -----------------------------------------------

# Замена по словарю
# в строке заменим буквы на цифры используя словарь
dic = {"a": 1, "b": 2, "c": 3}

# Вариант 1 с перезаписью
text = "abccbadfg"
for i in dic.keys():
    text = text.replace(i, str(dic[i]))
print(text)
# Здесь мы объявляем словарь dic и строку text, в которой будем делать замену.
# Далее в цикле for проходим по словарю и заменяем буквы на цифры.

# Вариант 2 создавая новую строку
text2 = "abccbadfg"
trlt_txt = ""

for i in text2:
    if i in dic.keys():
        i = dic[i]
        trlt_txt += str(i)
    else:
        pass  # если значения нет в словаре пропускаем!
print(trlt_txt)

# В этом примере, мы также используем словерь словарь "dic" и строку "text2".
# Создадим еще одну строку ret_txt, в которую запишем итоговые данные.
# Для этого в цикле for, добавим вложенное условие if.
# В if мы проверяем соответствует ли буква ключу словаря dic,
# и если да, то добавляем значение в строку ret_txt.
# -----------------------------------------------

# Инициализация с использованием for
d1 = {name: 0 for name in ["test_1", "test_2", "test_3"]}
print(d1)
# -----------------------------------------------

# Отобразить содержимое
for k, v in d1.items():
    print(k, v)
