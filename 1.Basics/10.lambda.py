"""
Лямбда-функция — это небольшая анонимная функция.
Она может принимать любое количество аргументов,
но в то же время иметь только одно возвращаемое значение.
Название функции = lambda (входные аргументы) : (возвращаемое значение)
- по такому принципу описывается функция.
"""

f = lambda x: x * x  # ! антипаттерн
v = f(2)
print(v)  # отобразится 4


# Данная запись аналогична
def func1(x):
    return x * x


v = func1(2)
print(v)
