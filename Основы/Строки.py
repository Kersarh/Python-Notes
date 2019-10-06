import os

str1 = "Это строка"
str2 = "ЭТО ВТОРАЯ СТРОКА"
print(str1.replace('то', 'хо'))  # Замена одной подстроки другой
print(str1.find('то'))  # Поиск смещения подстроки
print(str1.split(' '))  # Разбивает строку по разделителю
print(str1.upper())  # Преобразование в верхний регистр
print(str2.lower())  # Преобразование в нижний регистр

print("te\nst \nte\tst")

# FORMAT
user = "user"
srv = "server"

# F-строки
# или форматные строки f-строки
log_message = f'>> {user} has logged in {srv}.'

log_message = '>> {} has logged in {}.'.format(user, srv)
print(log_message)

print(log_message)

log_message = "test {0} or {1} and {2}".format(10, 20, "str")
print(log_message)

arr_format = [20, 30, "str"]
print("{0} - {1} - {2}".format(*arr_format))

print("{color} - {model}".format(model="BMW", color="red"))

d = {"color": "red", "model": "BMW"}
print("{color} - {model}".format(**d))

os.system('pause' if os.name == 'nt' else
          """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")

# \n — перевод строки
# \r — возврат каретки
# \t — знак табуляции
# \v — вертикальная табуляция
# \a — звонок;
# \b — забой;
# \f — перевод формата;
# \0 — нулевой символ (не является концом строки);
# \" — кавычка;
# \' — апостроф;
# \0xx — восьмеричное значение символа. Например, \074 соответствует символу <;
# \xhh — шестнадцатеричное значение символа. Например, \x6a соответствует символу j;
# \\ — обратный слеш.
# В Unicode-строках можно указать следующие специальные символы:
# \uxxxx — 16-битный символ Unicode. Например, \u043a соответствует русской букве к;
# \Uxxxxxxxx — 32-битный символ Unicode.
