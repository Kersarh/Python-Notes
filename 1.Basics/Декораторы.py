def fun_decor(fn):
    def decor():
        print("До выполнения")
        print(fn())
        print("После выполнения")

    return decor


def f_decor(f):
    print("Вызвана функция f_decor()")
    print(f)
    print("Завершена f_decor()")
    return f


@f_decor  # Декораторы
@fun_decor
def test1():
    return "Выполнение test1()"


test1()
