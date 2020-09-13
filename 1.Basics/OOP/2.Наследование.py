'''
Наследование позволяет создавать новый класс на основе уже существующего класса.
'''


# Родительский класс
class A:
    def prt_a(self):
        print("class A")


# Дочерний класс
class B(A):
    def prt_b(self):
        print("class B")


b = B()
b.prt_a()  # метод наследуемый от класса A
b.prt_b()  # метод определенный в классе B


# Множественно наследование. Класс может наследовать сразу от нескольких классов
class Base1:
    def basemethod(self):
        return "Hello"

    def prnt(self):
        return "Class Base1"


class Base2:
    value = 44

    def prnt(self):
        return "Class Base2"


# Класс наследующий от двух предыдущих
class MyClass(Base1, Base2):
    def __init__(self):
        self.a = 10


obj = MyClass()
print(obj.basemethod())  # Hello
print(obj.value)  # 44
# метод prnt есть в Base1 и Base2.
# Будет выполнен метод первого класса от которого идет наследование
print(obj.prnt())  # Class Base1

# super - позволяет принудительно использовать методы родительского класса в классе дочернем.


# Родительский класс
class A:
    def prt(self):
        return ("class A")


# Дочерний класс
class B(A):
    def prt(self):
        return ("class B")

    def fun(self):
        print(self.prt())  # метод prt класса B
        print(super(B, self).prt())  # метод prt класса A


b = B()
b.fun()
