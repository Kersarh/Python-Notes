'''
Использование модуля datetime
'''

import datetime

# timedelta — дата в виде количества дней, секунд и микросекунд.
# Экземпляр этого класса можно складывать с экземплярами классов date и datetime.
# Кро-ме того, результат вычитания двух дат будет экземпляром класса timedelta;
# timedelta([days[, seconds[, microseconds[, milliseconds[, minutes [, hours[, weeks]]]]]]])

# minutes — минуты (одна минута преобразуется в 60 секунд):
datetime.timedelta(minutes=1)
# >>> datetime.timedelta(0, 60)
# hours — часы (один час преобразуется в 3600 секунд):
datetime.timedelta(hours=1)
# >>> datetime.timedelta(0, 3600)

# можно сравнивать умнодать делить и тд.
d1 = datetime.timedelta(days=1, hours=2)
d2 = datetime.timedelta(days=7, minutes=3)
print(d1 + d2)

# Класс date из модуля datetime позволяет производить операции над датами.
# Конструктор класса имеет следующий формат:
# date(<Год>, <Месяц>, <День>)

d = datetime.date(2011, 2, 23)
print(d)

d = datetime.date.today()
print(d)
print(d.strftime("%d.%m.%Y"))
