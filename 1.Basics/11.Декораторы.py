'''
Декоратор — это функция, которая позволяет обернуть другую функцию
для расширения её функциональности без непосредственного изменения кода.
decorator — синтаксический сахар для конструкций вида:
function = my_decorator(my_function)
'''
import time


def bold(fn):  # функция декоратор
    def wrapper():  # Функция обертка
        return "<b>" + fn() + "</b>"

    return wrapper  # Возвращаем функцию обертку


def benchmark(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return fn()

    return wrapper


@benchmark  # Декоратор
@bold
def func():
    return "Hello World"


print(func())
print("---------------")


# Использование с аргументами
def benchmark2(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        print("arg =", return_value)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark2
def func2(text):
    return text


print(func2('HELLO'))
